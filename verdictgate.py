#!/usr/bin/env python3
"""VerdictGate - Mutation Matrix Evaluator: per-risk-tier verdict calculator.

Static, deterministic, metadata-only. Reads recorded mutation results (CSV),
applies per-risk-tier gate rules (mirroring the per-risk-tier framework v0.3),
and emits an audit-ready evidence pack: <stem>.verdict.md + <stem>.verdict.json.

Same input -> byte-identical output. Every verdict is stamped with
SCORER_VERSION; any rule change must bump it and update the golden files
in examples/.

Exit codes: 0 = all exercised gates pass, 1 = any gate failed, 2 = input error.
Python stdlib only. MIT license.
"""

import argparse
import csv
import json
import sys
from pathlib import Path

SCORER_VERSION = "0.1.2"

TIER_ORDER = ("B0", "B1", "B2", "B3")
TIER_LABELS = {"B0": "Critical", "B1": "High", "B2": "Medium", "B3": "Low"}
TIER_SCOPE = {
    "B0": "payment, auth, credential, data-integrity paths",
    "B1": "core user journeys, primary CRUD, search, notifications",
    "B2": "secondary flows, edge cases",
    "B3": "cosmetic, copy, layout, non-critical polish",
}

GATE_RULES = {
    "B0": {"survived_tolerance": 0, "score_target": 90, "observed_budget_pct": 10, "confirmatory_rerun": True},
    "B1": {"survived_tolerance": 0, "score_target": 80, "observed_budget_pct": 20, "confirmatory_rerun": False},
    "B2": {"score_target": 90, "small_n_threshold": 20},
    "B3": {"trend_only": True},
}

REQUIRED_COLUMNS = ("mutation_id", "behavior", "operator", "risk_tier", "expected", "suite_result")
NOOP_TOKENS = {"NOOP", "NO-OP"}
VALID_EXPECTED = {"Y", "N", "E"}
VALID_RESULT = {"pass", "fail"}
VALID_DECISIONS = {"open", "dismissed", "fixed"}
KNOWN_COLUMNS = REQUIRED_COLUMNS + ("observed", "decision")


class InputError(Exception):
    pass


def parse_rows(path):
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise InputError(f"cannot read {path}: {exc}")
    numbered = [(i + 1, ln) for i, ln in enumerate(text.splitlines())]
    lines = [(n, ln) for n, ln in numbered if ln.strip() and not ln.lstrip().startswith("#")]
    if not lines:
        raise InputError("empty input")
    reader = csv.DictReader([ln for _, ln in lines])
    fieldnames = reader.fieldnames or []
    missing = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
    if missing:
        raise InputError(f"missing required column(s): {', '.join(missing)}")
    if len(set(fieldnames)) != len(fieldnames):
        raise InputError("duplicate column name(s) in header")
    unknown = [c for c in fieldnames if c not in KNOWN_COLUMNS]
    if unknown:
        raise InputError(f"unknown column(s): {', '.join(unknown)}")
    rows = []
    seen = set()
    for (lineno, _), raw in zip(lines[1:], reader):
        rowno = f"line {lineno}"
        if None in raw:
            raise InputError(f"{rowno}: extra value(s) beyond declared columns")
        mid = (raw.get("mutation_id") or "").strip()
        if not mid:
            raise InputError(f"{rowno}: mutation_id is empty")
        if mid in seen:
            raise InputError(f"{rowno}: duplicate mutation_id '{mid}'")
        seen.add(mid)
        behavior = (raw.get("behavior") or "").strip()
        operator = (raw.get("operator") or "").strip()
        if not behavior or not operator:
            raise InputError(f"{rowno} ({mid}): behavior and operator are required")
        tier = (raw.get("risk_tier") or "").strip().upper()
        if tier not in TIER_ORDER:
            raise InputError(f"{rowno} ({mid}): risk_tier must be one of {', '.join(TIER_ORDER)}")
        expected = (raw.get("expected") or "").strip().upper()
        if expected in NOOP_TOKENS:
            raise InputError(
                f"{rowno} ({mid}): no-op mutant recorded. A mutant that changes nothing "
                "observable is a seeder defect: refuse it PRE-SEED (it stays out of N), "
                "never accept it post-hoc. Remove the row, re-seed, re-run."
            )
        if expected not in VALID_EXPECTED:
            raise InputError(f"{rowno} ({mid}): expected must be Y, N, or E (Equivalent: recorded, excluded from the denominator)")
        result = (raw.get("suite_result") or "").strip().lower()
        if result not in VALID_RESULT:
            raise InputError(f"{rowno} ({mid}): suite_result must be pass or fail")
        decision = (raw.get("decision") or "").strip()
        if decision and decision not in VALID_DECISIONS:
            raise InputError(f"{rowno} ({mid}): decision must be one of open, dismissed, fixed (or empty)")
        if expected == "E" and result == "fail":
            raise InputError(
                f"{rowno} ({mid}): contradictory row: expected=E claims no observable behavior change, "
                "but suite_result=fail means the suite observed it. Re-assess equivalence."
            )
        rows.append(
            {
                "mutation_id": mid,
                "behavior": behavior,
                "operator": operator,
                "risk_tier": tier,
                "expected": expected,
                "suite_result": result,
                "observed": (raw.get("observed") or "").strip(),
                "decision": decision,
            }
        )
    if not rows:
        raise InputError("no result rows found - fill the template before running")
    return rows


def row_verdict(row):
    if row["expected"] == "E":
        return "Equivalent"
    if row["expected"] == "N":
        return "n/a"
    if row["suite_result"] == "fail":
        return "Caught"
    if row["observed"]:
        return "Observed-only"
    return "Survived"


def pct(part, whole):
    return round(part * 100 / whole, 1) if whole else 0.0


def build_verdict(rows, b2_band_pct, b2_small_n_max):
    enriched = []
    for r in rows:
        e = dict(r)
        e["verdict"] = row_verdict(r)
        enriched.append(e)

    tiers = {}
    any_fail = False
    for tier in TIER_ORDER:
        t_rows = [e for e in enriched if e["risk_tier"] == tier]
        seeded = [e for e in t_rows if e["verdict"] not in ("n/a", "Equivalent")]
        caught = [e for e in seeded if e["verdict"] == "Caught"]
        observed = [e for e in seeded if e["verdict"] == "Observed-only"]
        survivors = [e for e in seeded if e["verdict"] == "Survived"]
        d = {
            "label": TIER_LABELS[tier],
            "scope": TIER_SCOPE[tier],
            "seeded": len(seeded),
            "caught": len(caught),
            "observed_only": len(observed),
            "survived": len(survivors),
            "equivalent": len([e for e in t_rows if e["verdict"] == "Equivalent"]),
            "mutation_score": pct(len(caught), len(seeded)),
            "survival_rate": pct(len(survivors), len(seeded)),
            "gate": None,
            "gate_detail": "",
            "signals": [],
            "survivors": [
                {
                    "mutation_id": s["mutation_id"],
                    "behavior": s["behavior"],
                    "operator": s["operator"],
                    "decision": s["decision"] or None,
                }
                for s in survivors
            ],
            "not_expected": [e["mutation_id"] for e in t_rows if e["verdict"] == "n/a"],
        }
        if d["seeded"] == 0:
            d["gate"] = "NOT EXERCISED"
            d["gate_detail"] = "no seeded mutants (expected=Y) in this tier"
        elif tier == "B3":
            d["gate"] = "TREND-ONLY"
            d["gate_detail"] = "never blocks; alerts on regression vs rolling-3-run baseline"
            if d["survived"]:
                d["signals"].append(
                    f"{d['survived']} survivor(s) recorded - trend-only alert; compare against the rolling-3-run baseline"
                )
        else:
            rule = GATE_RULES[tier]
            ok = True
            if tier in ("B0", "B1"):
                if d["survived"] > 0:
                    ok = False
                    d["gate_detail"] = f"zero-tolerance violated: {d['survived']} survivor(s) in {tier}"
                else:
                    d["gate_detail"] = f"zero-tolerance held (survived 0 of {d['seeded']})"
                if rule["confirmatory_rerun"]:
                    d["signals"].append(
                        "B0 sign-off additionally requires a confirmatory re-run (two consecutive passing runs)"
                    )
                if d["mutation_score"] < rule["score_target"]:
                    d["signals"].append(
                        f"mutation score {d['mutation_score']}% below target {rule['score_target']}% - mandatory signed Assessor comment"
                    )
                obs_rate = pct(d["observed_only"], d["seeded"])
                if d["survived"] == 0 and obs_rate > rule["observed_budget_pct"]:
                    d["signals"].append(
                        f"observed-only {obs_rate}% exceeds budget {rule['observed_budget_pct']}% at survived=0 - signed comment required"
                    )
            elif tier == "B2":
                threshold = GATE_RULES["B2"]["small_n_threshold"]
                if d["seeded"] >= threshold:
                    if d["survived"] * 100 > b2_band_pct * d["seeded"]:
                        ok = False
                        d["gate_detail"] = (
                            f"band violated: {d['survived']} survivor(s) = {d['survival_rate']}% > {b2_band_pct}% of {d['seeded']} seeded"
                        )
                    else:
                        d["gate_detail"] = f"band held ({d['survival_rate']}% <= {b2_band_pct}%)"
                else:
                    if d["survived"] > b2_small_n_max:
                        ok = False
                        d["gate_detail"] = (
                            f"small-N floor violated: {d['survived']} survivor(s) > max {b2_small_n_max} at N={d['seeded']} (< {threshold})"
                        )
                    else:
                        d["gate_detail"] = f"small-N floor held (max {b2_small_n_max} at N={d['seeded']} < {threshold})"
                missing_decision = [s for s in survivors if not s["decision"]]
                # Declared B2 rule (mirrors README + framework v0.3): every recorded
                # survivor carries an enumerated decision (open/dismissed/fixed).
                # Boundary-locked in selfcheck (b2a-b2f matrix).
                if missing_decision:
                    ok = False
                    ids = ", ".join(s["mutation_id"] for s in missing_decision)
                    d["gate_detail"] += f"; survivor(s) without recorded decision: {ids}"
                if d["mutation_score"] < GATE_RULES["B2"]["score_target"]:
                    d["signals"].append(
                        f"mutation score {d['mutation_score']}% below target {GATE_RULES['B2']['score_target']}% - mandatory signed Assessor comment"
                    )
            d["gate"] = "PASS" if ok else "FAIL"
            if not ok:
                any_fail = True
        tiers[tier] = d

    fix_first = []
    for tier in TIER_ORDER:
        for s in tiers[tier]["survivors"]:
            dec = s["decision"] or "NO RECORDED DECISION"
            fix_first.append(
                f"{tier} · {s['mutation_id']} · {s['behavior']} ({s['operator']}) - SURVIVED, decision: {dec}"
            )

    not_expected_rows = [
        {"mutation_id": e["mutation_id"], "risk_tier": e["risk_tier"], "reason": "expected=N"}
        for e in enriched
        if e["verdict"] == "n/a"
    ]

    equivalent_rows = [
        {"mutation_id": e["mutation_id"], "risk_tier": e["risk_tier"], "reason": "expected=E (no observable behavior change)"}
        for e in enriched
        if e["verdict"] == "Equivalent"
    ]

    totals = {
        "rows": len(enriched),
        "seeded": sum(tiers[t]["seeded"] for t in TIER_ORDER),
        "caught": sum(tiers[t]["caught"] for t in TIER_ORDER),
        "observed_only": sum(tiers[t]["observed_only"] for t in TIER_ORDER),
        "survived": sum(tiers[t]["survived"] for t in TIER_ORDER),
        "equivalent": sum(tiers[t]["equivalent"] for t in TIER_ORDER),
    }

    verdict = {
        "scorer_version": SCORER_VERSION,
        "deterministic": True,
        "b2_band_pct": b2_band_pct,
        "b2_small_n_max": b2_small_n_max,
        "totals": totals,
        "note": "gates and scores are per-tier by design; no global percentage is computed",
        "tiers": tiers,
        "fix_first": fix_first,
        "not_expected_rows": not_expected_rows,
        "equivalent_rows": equivalent_rows,
        "gate_summary": "FAIL" if any_fail else "PASS",
        "exit_code": 1 if any_fail else 0,
    }
    return verdict


def render_md(verdict, input_name):
    t = verdict["tiers"]
    lines = []
    lines.append(f"# Verdict - {input_name}")
    lines.append("")
    lines.append(
        f"verdictgate v{SCORER_VERSION} · deterministic: same input → same verdict · gates are per-tier, never blended"
    )
    lines.append(f"config: B2 band {verdict['b2_band_pct']}% at N>=20, B2 small-N max {verdict['b2_small_n_max']} survivor(s)")
    lines.append("")
    lines.append("## Per-tier results")
    lines.append("")
    lines.append("| Tier | Seeded | Caught | Observed-only | Survived | Mutation score | Survival rate | Gate |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for tier in TIER_ORDER:
        d = t[tier]
        lines.append(
            f"| {tier} {d['label']} | {d['seeded']} | {d['caught']} | {d['observed_only']} | {d['survived']} "
            f"| {d['mutation_score']}% | {d['survival_rate']}% | {d['gate']} |"
        )
    lines.append("")
    lines.append("## Gate verdicts")
    lines.append("")
    for tier in TIER_ORDER:
        d = t[tier]
        lines.append(f"**{tier} {d['label']} - {d['gate']}** ({d['gate_detail']})")
        for sig in d["signals"]:
            lines.append(f"- Signal: {sig}")
        lines.append("")
    lines.append("## Fix first")
    lines.append("")
    if verdict["fix_first"]:
        for i, item in enumerate(verdict["fix_first"], start=1):
            lines.append(f"{i}. **{item}**")
    else:
        lines.append("None - no survivors recorded.")
    lines.append("")
    if verdict["not_expected_rows"]:
        lines.append("## Not expected (out of scope)")
        lines.append("")
        for r in verdict["not_expected_rows"]:
            lines.append(f"- {r['mutation_id']} ({r['risk_tier']}) - {r['reason']}")
        lines.append("")
    if verdict["equivalent_rows"]:
        lines.append("## Equivalent (recorded, excluded from the denominator)")
        lines.append("")
        for r in verdict["equivalent_rows"]:
            lines.append(f"- {r['mutation_id']} ({r['risk_tier']}) - {r['reason']}")
        lines.append("")
    signal_count = sum(len(t[tier]["signals"]) for tier in TIER_ORDER)
    assessor_note = "signed comment required - signals fired" if signal_count else "none required - no signals fired"
    lines.append("## Sign-off (evidence pack)")
    lines.append("")
    lines.append("| Role | Name | Decision | Date |")
    lines.append("|---|---|---|---|")
    lines.append("| Reviewer of record | | | |")
    lines.append(f"| Independent Assessor | | {assessor_note} | |")
    lines.append("| Engineering owner | | | |")
    lines.append("")
    lines.append(
        "Attach: this file, the .json twin, the raw results.csv, and run logs/screenshots for every "
        "seeded mutant (lineage, not belief). Anyone with the same CSV and scorer version "
        f"reproduces this verdict exactly."
    )
    lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(
        prog="verdictgate",
        description="Mutation Matrix Evaluator: per-risk-tier verdict calculator (static, deterministic).",
    )
    ap.add_argument("results", help="recorded mutation results CSV")
    ap.add_argument("--out-dir", default=None, help="output directory (default: alongside the input)")
    ap.add_argument("--b2-band-pct", type=int, default=5, help="B2 survived band in percent at N>=20 (default: 5)")
    ap.add_argument("--b2-small-n-max", type=int, default=1, help="B2 max survivors below the small-N threshold (default: 1)")
    ap.add_argument("--json", action="store_true", help="print verdict JSON to stdout, write no files")
    ap.add_argument("--md", action="store_true", help="print verdict markdown to stdout, write no files")
    args = ap.parse_args()
    if not 0 <= args.b2_band_pct <= 100:
        ap.error("--b2-band-pct must be 0..100")
    if args.b2_small_n_max < 0:
        ap.error("--b2-small-n-max must be >= 0")

    try:
        rows = parse_rows(args.results)
    except InputError as exc:
        print(f"verdictgate: input error: {exc}", file=sys.stderr)
        return 2

    verdict = build_verdict(rows, args.b2_band_pct, args.b2_small_n_max)
    input_name = Path(args.results).name
    md_text = render_md(verdict, input_name)
    json_text = json.dumps(verdict, indent=2, ensure_ascii=False) + "\n"

    if args.json:
        print(json_text, end="")
        return verdict["exit_code"]
    if args.md:
        print(md_text, end="")
        return verdict["exit_code"]

    out_dir = Path(args.out_dir) if args.out_dir else Path(args.results).parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(args.results).stem
    (out_dir / f"{stem}.verdict.md").write_text(md_text, encoding="utf-8")
    (out_dir / f"{stem}.verdict.json").write_text(json_text, encoding="utf-8")

    summary = " · ".join(f"{tier} {verdict['tiers'][tier]['gate']}" for tier in TIER_ORDER)
    print(f"{summary} - {verdict['gate_summary']} (exit {verdict['exit_code']})", file=sys.stderr)
    print(f"evidence pack: {out_dir / (stem + '.verdict.md')}", file=sys.stderr)
    return verdict["exit_code"]


if __name__ == "__main__":
    sys.exit(main())
