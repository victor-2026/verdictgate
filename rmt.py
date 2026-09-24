"""RMT-lite mutation engine for VerdictGate (W4 implementation, 2026-09-24).

Mutates Playwright assertions (not app code). Balanced-paren scanner —
no regex nesting traps. Pilot scope: toBeVisible / toHaveText / toHaveLength.
Standalone: `python3 rmt.py FILE --tier B2 --format summary|json`.
Importable: `from rmt import generate_mutants_for_file`.
CLI integration into verdictgate.py left to W2 (no existing files touched).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Matcher -> (operator, mutator of the full call text)
MATCHERS = ("toBeVisible", "toHaveText", "toHaveLength", "toBeHidden")

OPERATOR_SETS = {
    "B0": ["EQ_NEGATION"],
    "B1": ["EQ_NEGATION"],
    "B2": ["EQ_NEGATION", "COLLECTION_EMPTY"],  # Pilot scope
    "B3": [],
}

# matcher -> operator (only what the pilot implements)
MATCHER_OPERATOR = {
    "toBeVisible": "EQ_NEGATION",
    "toHaveText": "EQ_NEGATION",
    "toHaveLength": "COLLECTION_EMPTY",
    "toBeHidden": "EQ_NEGATION",
}


def balanced_span(text: str, open_idx: int) -> int | None:
    """Return index just past the paren matching text[open_idx] == '('.

    Skips over single/double-quoted and template strings. None if unbalanced.
    """
    depth = 0
    i = open_idx
    n = len(text)
    quote = None
    while i < n:
        ch = text[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in ("'", '"', "`"):
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return None


def find_assertions(content: str) -> list:
    """Yield (expect_start, call_end, matcher) for each expect(...).matcher(...) call."""
    out = []
    for m in re.finditer(r"expect\(", content):
        close = balanced_span(content, m.end() - 1)
        if close is None:
            continue
        rest = content[close:]
        mm = re.match(r"\.(\w+)\(", rest)
        if not mm:
            continue
        matcher = mm.group(1)
        if matcher not in MATCHER_OPERATOR:
            continue
        arg_close = balanced_span(content, close + len(mm.group(0)) - 1)
        if arg_close is None:
            continue
        out.append((m.start(), arg_close, matcher))
    return out


def apply_mutation(call: str, operator: str) -> str:
    """Return mutated assertion text."""
    if operator == "EQ_NEGATION":
        if re.search(r"\.not\.(toBeVisible|toHaveText|toBeHidden)\(", call):
            return call  # already negated — do not double-mutate
        return re.sub(
            r"\.(toBeVisible|toHaveText|toBeHidden)\(",
            r".not.\1(",
            call,
            count=1,
        )
    if operator == "COLLECTION_EMPTY":
        return re.sub(r"\.toHaveLength\(\d+\)", ".toHaveLength(0)", call, count=1)
    raise ValueError(f"unknown operator: {operator}")


def get_applicable_operators(assertion_text: str, tier: str) -> list:
    """Operators applicable to one assertion string at tier."""
    allowed = OPERATOR_SETS.get(tier, [])
    found = []
    for _start, _end, matcher in find_assertions(assertion_text):
        op = MATCHER_OPERATOR[matcher]
        if op in allowed and op not in found:
            found.append(op)
    return found


def generate_mutants_for_file(file_path: str, tier: str = "B2") -> list:
    """Generate mutants for all assertions in a test file."""
    content = Path(file_path).read_text(encoding="utf-8")
    mutants = []
    for start, end, matcher in find_assertions(content):
        original = content[start:end]
        for op in get_applicable_operators(original, tier):
            line = content.count("\n", 0, start) + 1
            mutants.append(
                {
                    "operator": op,
                    "original": original,
                    "mutated": apply_mutation(original, op),
                    "file": file_path,
                    "line": line,
                    "tier": tier,
                }
            )
    return mutants


def main(argv: list | None = None) -> int:
    ap = argparse.ArgumentParser(prog="rmt")
    ap.add_argument("input", help="test file to mutate")
    ap.add_argument("--tier", default="B2", choices=["B0", "B1", "B2", "B3"])
    ap.add_argument("--format", default="summary", choices=["summary", "json"])
    args = ap.parse_args(argv)
    mutants = generate_mutants_for_file(args.input, args.tier)
    if args.format == "json":
        print(json.dumps(mutants, indent=2, ensure_ascii=False))
    else:
        print(f"{len(mutants)} mutants @ {args.tier} from {args.input}")
        for mu in mutants:
            print(f"- L{mu['line']} [{mu['operator']}]")
            print(f"    - {mu['original']}")
            print(f"    + {mu['mutated']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
