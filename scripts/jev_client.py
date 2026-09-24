#!/usr/bin/env python3
import os
import json
import requests
import subprocess
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class JEVResponse:
    severity: str
    is_fp: bool
    confidence: float
    reasoning: str = ""

class JEVClient:
    def __init__(self, api_key=None, base_url="https://api.typesafe.ai"):
        self.api_key = api_key or os.getenv("TYPE_SAFE_API_KEY")
        if not self.api_key:
            raise ValueError("TYPE_SAFE_API_KEY not set")
        self.base_url = "https://api.typesafe.ai"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _build_payload(self, finding_text, context=""):
        state = finding_text if not context else f"Context: {context}\n\nFinding:\n{finding_text}"
        
        return {
            "state": state,
            "model": "jev-latest",
            "questions": {
                "severity": {"type": "choice", "instructions": "Classify the severity of this test finding for pi-review triage.", "criteria": {
                    "P0": "Critical production risk (security, data loss, payment failure, auth bypass)",
                    "P1": "High business risk (core user journeys broken, data corruption)",
                    "P2": "Medium risk (edge cases, UI issues, performance degradation)",
                    "noise": "Not a real issue (flaky test, env problem, test bug, not product bug)"
                }},
                "is_fp": {
                    "type": "noul",
                    "instructions": "Is this finding a false positive? True if the test failed due to test flaw/artifact, not a real product bug.",
                    "criteria": {
                        "true": "Test failed due to test artifact, flaky locator, test bug, env issue - not a real product bug",
                        "false": "Test correctly caught a real product bug/defect"
                    }
                },
                "confidence": {
                    "type": "score",
                    "instructions": "How confident are you in this classification?",
                    "criteria": ["Very uncertain (0.0-0.3)", "Somewhat confident (0.3-0.7)", "Highly confident (0.7-1.0)"]
                }
            }
        }
    
    def classify_finding(self, finding_text, context=""):
        payload = self._build_payload(finding_text, context)
        
        try:
            response = self.session.post(
                "https://api.typesafe.ai/v1/systemone",
                json=payload,
                timeout=30
            )
            if response.status_code == 200:
                return self._parse_response(response.json())
            else:
                return JEVResponse(
                    severity="P2", is_fp=False, confidence=0.0, 
                    reasoning="API error " + str(response.status_code) + ": " + response.text
                )
        except requests.exceptions.RequestException as e:
            return self._fallback_classify(finding_text)
    
    def _parse_response(self, data):
        try:
            answers = data.get("answers", {})
            
            severity_ans = answers.get("severity", {})
            severity = severity_ans.get("choice", "P2")
            
            is_fp_ans = answers.get("is_fp", {})
            fp_prob = is_fp_ans.get("noul", 0.0)
            is_fp = fp_prob > 0.5
            
            conf_ans = answers.get("confidence", {})
            confidence = float(conf_ans.get("score", 0.5))
            if confidence > 2.0:
                confidence = confidence / 2.0
            
            sev_ans = answers.get("severity", {})
            probs = sev_ans.get("probabilities", {})
            reasoning = "Severity probs: " + str(probs)
            
            return JEVResponse(
                severity=severity,
                is_fp=is_fp,
                confidence=confidence,
                reasoning=reasoning
            )
        except Exception as e:
            return JEVResponse(
                severity="P2", is_fp=False, confidence=0.0,
                reasoning="parse failed: " + str(e)
            )
    
    def _fallback_classify(self, text):
        try:
            result = subprocess.run(
                ["pi", "--provider", "openrouter", "--model", "openrouter/free", "--print", 'Classify test finding. Return JSON: {"severity":"P0|P1|P2|noise","is_fp":bool,"confidence":0.0-1.0}}. Finding: ' + text[:2000]],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                parsed = json.loads(result.stdout.strip())
                return JEVResponse(
                    severity=parsed.get("severity", "P2"),
                    is_fp=parsed.get("is_fp", False),
                    confidence=float(parsed.get("confidence", 0.5)),
                    reasoning="fallback via pi/openrouter"
                )
        except Exception:
            pass
        return JEVResponse(severity="P2", is_fp=False, confidence=0.0, reasoning="fallback failed")

def main():
    import sys
    text = sys.stdin.read() if not sys.stdin.isatty() else " ".join(sys.argv[1:])
    api_key = os.getenv("TYPE_SAFE_API_KEY")
    if not api_key:
        print(json.dumps({"error": "TYPE_SAFE_API_KEY not set"}, ensure_ascii=False))
        sys.exit(1)
    client = JEVClient()
    result = client.classify_finding(text)
    print(json.dumps({
        "severity": result.severity,
        "is_fp": result.is_fp,
        "confidence": result.confidence,
        "reasoning": result.reasoning
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()