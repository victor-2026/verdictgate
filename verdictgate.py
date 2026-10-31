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

SCORER_VERSION = "0.3.0"

TIER_ORDER = ("B0", "B1", "B2", "B3")
TIER_LABELS = {"B0": "Critical", "B1": "High", "B2": "Medium", "B3": "Low"}
TIER_SCOPE = {
    "B0": "payment, auth, credential, data-integrity paths",
    "B1": "core user journeys, primary CRUD, search, notifications",
    "B2": "secondary flows, edge cases",
    "B3": "cosmetic, copy, layout, non-critical polish",
}

GATE_RULES = {
    "B0": {"survived_tolerance": 0, "score_target": 90, "observed_budget_pct": 10, "confirmatory_rerun": True,
           "mass_e_pct": None, "mass_observed_pct": None},  # None = presence-based signal (sweep-v1)
    "B1": {"survived_tolerance": 0, "score_target": 80, "observed_budget_pct": 20, "confirmatory_rerun": False,
           "mass_e_pct": None, "mass_observed_pct": None},  # None = presence-based signal (sweep-v1)
    "B2": {"score_target": 90, "small_n_threshold": 20,
           "mass_e_pct": 5, "mass_observed_pct": 10},  # provisional, provenance sweep-v1 synthetic
    "B3": {"trend_only": True},
}
# mass_e_pct / mass_observed_pct are D1 Option C SIGNALS — presence/rate only, never gate.
# Do not wire into `ok` without a new explicit decision (see AGENTS.md D1).

REQUIRED_COLUMNS = ("mutation_id", "behavior", "operator", "risk_tier", "expected", "suite_result")
NOOP_TOKENS = {"NOOP", "NO-OP"}
VALID_EXPECTED = {"Y", "N", "E"}
VALID_RESULT = {"pass", "fail"}
VALID_DECISIONS = {"open", "dismissed", "fixed"}
VALID_E_BASIS = {"code-review", "diff-analysis", "no-observable-path", "dead-code", "other"}
E_REASON_MAX_LEN = 280
KNOWN_COLUMNS = REQUIRED_COLUMNS + ("observed", "decision", "e_reason", "e_assessor",
                                     "e_basis", "observed_by", "observed_run_ref",
                                     "observed_element")

class InputError(Exception):
    pass

PROFILE_KNOWN_KEYS = {"name", "version", "score_target", "observed_budget_pct",
                      "mass_e_pct", "mass_observed_pct", "small_n_threshold",
                      "b2_band_pct", "b2_small_n_max", "provisional"}


def load_profile(name_or_path):
    """Return (profile_dict, sha256_hex, resolved_name) or (None, None, None) if no profile."""
    if not name_or_path:
        return None, None, None
    # resolve path
    p = Path(name_or_path)
    if not p.is_absolute() and ("/" in name_or_path or name_or_path.endswith(".json")):
        p = Path(name_or_path)
    if not p.exists():
        # NAME -> profiles/<name>.json relative to this file
        candidate = Path(__file__).resolve().parent / "profiles" / (name_or_path if name_or_path.endswith(".json") else name_or_path + ".json")
        if candidate.exists():
            p = candidate
    if not p.exists():
        raise InputError(f"profile not found: {name_or_path}")
    try:
        raw = p.read_bytes()
        data = json.loads(raw.decode("utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InputError(f"profile parse error: {exc}")
    if not isinstance(data, dict):
        raise InputError("profile must be a JSON object")
    unknown = set(data) - PROFILE_KNOWN_KEYS
    if unknown:
        raise InputError(f"profile: unknown keys {sorted(unknown)}")
    # validate ranges
    for key in ("score_target", "observed_budget_pct", "mass_e_pct", "mass_observed_pct"):
        if key in data and data[key] is not None:
            v = data[key]
            if not isinstance(v, dict):
                raise InputError(f"profile.{key} must be an object")
            for tier, val in v.items():
                if tier not in TIER_ORDER:
                    raise InputError(f"profile.{key}: unknown tier {tier}")
                if not isinstance(val, int) or isinstance(val, bool) or not (0 <= val <= 100):
                    raise InputError(f"profile.{key}.{tier} must be int 0..100")
    if "small_n_threshold" in data and data["small_n_threshold"] is not None:
        v = data["small_n_threshold"]
        if not isinstance(v, int) or isinstance(v, bool) or not (1 <= v <= 100):
            raise InputError("profile.small_n_threshold must be int 1..100")
    for key in ("b2_band_pct",):
        if key in data and data[key] is not None:
            v = data[key]
            if not isinstance(v, int) or isinstance(v, bool) or not (0 <= v <= 100):
                raise InputError(f"profile.{key} must be int 0..100")
    if "b2_small_n_max" in data and data["b2_small_n_max"] is not None:
        v = data["b2_small_n_max"]
        if not isinstance(v, int) or isinstance(v, bool) or not (0 <= v <= 19):
            raise InputError("profile.b2_small_n_max must be int 0..19")
    if "version" in data and data["version"] is not None:
        if not isinstance(data["version"], int) or isinstance(data["version"], bool):
            raise InputError("profile.version must be int")
    if "provisional" in data and data["provisional"] is not None:
        if not isinstance(data["provisional"], bool):
            raise InputError("profile.provisional must be bool")
    import hashlib
    sha = hashlib.sha256(raw).hexdigest()
    resolved_name = data.get("name") if isinstance(data.get("name"), str) else p.stem
    return data, sha, resolved_name


def apply_profile(profile, rules_base):
    """Return (rules_merged, profile_b2_band_default, profile_b2_small_n_default)."""
    import copy
    rules = copy.deepcopy(rules_base)
    if not profile:
        return rules, None, None
    # score_target / observed_budget_pct per tier
    for key, rule_key in (("score_target", "score_target"), ("observed_budget_pct", "observed_budget_pct")):
        if profile.get(key):
            for tier, val in profile[key].items():
                if tier in rules and rule_key in rules[tier]:
                    rules[tier][rule_key] = val
    # mass_e_pct / mass_observed_pct
    for key in ("mass_e_pct", "mass_observed_pct"):
        if profile.get(key):
            for tier, val in profile[key].items():
                if tier in rules and key in rules[tier]:
                    rules[tier][key] = val
    # small_n_threshold (B2)
    if profile.get("small_n_threshold") is not None:
        rules["B2"]["small_n_threshold"] = profile["small_n_threshold"]
    b2_band_default = profile.get("b2_band_pct", None)
    b2_small_n_default = profile.get("b2_small_n_max", None)
    return rules, b2_band_default, b2_small_n_default


def parse_requirements(path):
    """behavior_name -> risk_tier map. Verbatim keys: the linkage rule."""
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise InputError(f"cannot read requirements {path}: {exc}")
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.lstrip().startswith("#")]
    if not lines:
        raise InputError("empty requirements file")
    reader = csv.DictReader(lines)
    fieldnames = reader.fieldnames or []
    for col in ("behavior_name", "risk_tier"):
        if col not in fieldnames:
            raise InputError(f"requirements missing required column: {col}")
    mapping = {}
    for idx, raw in enumerate(reader, start=2):
        name = (raw.get("behavior_name") or "").strip()
        tier = (raw.get("risk_tier") or "").strip().upper()
        if not name:
            raise InputError(f"requirements line {idx}: behavior_name is empty")
        if name in mapping:
            raise InputError(f"requirements line {idx}: duplicate behavior_name '{name}'")
        if tier not in TIER_ORDER:
            raise InputError(
                f"requirements line {idx} ('{name}'): risk_tier must be one of {', '.join(TIER_ORDER)}"
            )
        mapping[name] = tier
    if not mapping:
        raise InputError("no requirement rows found")
    return mapping


def cross_check_tiers(rows, requirements):
    for r in rows:
        declared = requirements.get(r["behavior"])
        if declared is None:
            raise InputError(
                f"{r['mutation_id']}: behavior '{r['behavior']}' matches no requirements.csv "
                "behavior_name (verbatim linkage rule) — add it or fix the spelling"
            )
        if declared != r["risk_tier"]:
            raise InputError(
                f"{r['mutation_id']}: risk_tier {r['risk_tier']} does not match requirements "
                f"tier {declared} for behavior '{r['behavior']}' (tier laundering refused)"
            )


def parse_rows(path):
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise InputError(f"cannot read {path}: {exc}")
    phys = text.splitlines()
    hdr_idx = next(
        (i for i, ln in enumerate(phys) if ln.strip() and not ln.lstrip().startswith("#")),
        None,
    )
    if hdr_idx is None:
        raise InputError("empty input")
    # Single csv pass over all lines: quoted multiline fields stay intact
    # (pre-filtering text would silently mangle an embedded '#' or blank line).
    reader = csv.DictReader(phys[hdr_idx:])
    fieldnames = reader.fieldnames or []
    missing = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
    if missing:
        raise InputError(f"missing required column(s): {', '.join(missing)}")
    if len(set(fieldnames)) != len(fieldnames):
        raise InputError("duplicate column name(s) in header")
    if "" in fieldnames:
        raise InputError("empty column name in header (trailing comma?)")
    unknown = [c for c in fieldnames if c not in KNOWN_COLUMNS]
    if unknown:
        raise InputError(f"unknown column(s): {', '.join(unknown)}")
    rows = []
    seen = set()
    consumed = hdr_idx  # physical lines consumed before the current record
    for raw in reader:
        end = hdr_idx + reader.line_num
        start = consumed + 1
        while start <= end and (
            not phys[start - 1].strip() or phys[start - 1].lstrip().startswith("#")
        ):
            start += 1
        consumed = end
        if start > end or phys[start - 1].lstrip().startswith("#"):
            continue  # comment-only span
        vals = [v for v in raw.values() if v is not None]
        if all(v.strip() == "" for v in vals):
            continue  # whitespace-only row
        rowno = f"line {start}" if start == end else f"lines {start}-{end}"
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
        decision = (raw.get("decision") or "").strip().lower()
        if decision and decision not in VALID_DECISIONS:
            raise InputError(f"{rowno} ({mid}): decision must be one of open, dismissed, fixed (or empty)")
        if expected == "E" and result == "fail":
            raise InputError(
                f"{rowno} ({mid}): contradictory row: expected=E claims no observable behavior change, "
                "but suite_result=fail means the suite observed it. Re-assess equivalence."
            )
        e_reason = (raw.get("e_reason") or "").strip()
        e_assessor = (raw.get("e_assessor") or "").strip()
        e_basis = (raw.get("e_basis") or "").strip().lower()
        obs_by = (raw.get("observed_by") or "").strip()
        obs_ref = (raw.get("observed_run_ref") or "").strip()
        obs_el = (raw.get("observed_element") or "").strip()
        if expected == "E":
            if not e_reason or not e_assessor or not e_basis:
                raise InputError(
                    f"{rowno} ({mid}): expected=E requires e_reason, e_assessor, and e_basis "
                    "(assessed equivalence must be justified, not asserted)"
                )
            if e_basis not in VALID_E_BASIS:
                raise InputError(
                    f"{rowno} ({mid}): e_basis must be one of {', '.join(sorted(VALID_E_BASIS))}"
                )
            if len(e_reason) > E_REASON_MAX_LEN:
                raise InputError(
                    f"{rowno} ({mid}): e_reason over {E_REASON_MAX_LEN} chars - shorten it, "
                    "detail belongs in the evidence pack, not the cell"
                )
        elif e_reason or e_assessor or e_basis:
            raise InputError(
                f"{rowno} ({mid}): e_reason/e_assessor/e_basis are only valid when expected=E"
            )
        observed = (raw.get("observed") or "").strip()
        if observed:
            if not obs_by or not obs_ref or not obs_el:
                raise InputError(
                    f"{rowno} ({mid}): observed requires observed_by, observed_run_ref, and "
                    "observed_element (a passive-observation claim needs attribution, a run "
                    "reference, and the specific element that fired)"
                )
        elif obs_by or obs_ref or obs_el:
            raise InputError(
                f"{rowno} ({mid}): observed_by/observed_run_ref/observed_element are only valid "
                "when observed is non-empty"
            )
        rows.append(
            {
                "mutation_id": mid,
                "behavior": behavior,
                "operator": operator,
                "risk_tier": tier,
                "expected": expected,
                "suite_result": result,
                "observed": observed,
                "decision": decision,
                "e_reason": e_reason,
                "e_assessor": e_assessor,
                "e_basis": e_basis,
                "observed_by": obs_by,
                "observed_run_ref": obs_ref,
                "observed_element": obs_el,
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


def build_verdict(rows, b2_band_pct, b2_small_n_max, fail_on_unexercised=False,
                  rules=None, profile_name=None, profile_sha=None):
    if rules is None:
        rules = GATE_RULES
    enriched = []
    for r in rows:
        e = dict(r)
        e["verdict"] = row_verdict(r)
        enriched.append(e)

    tiers = {}
    any_fail = False
    fix_first = []
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
            if fail_on_unexercised and tier in ("B0", "B1"):
                d["gate_detail"] += "; --fail-on-unexercised treats this as a release blocker"
                any_fail = True
                fix_first.append(
                    f"{tier} · NOT EXERCISED - no seeded mutants recorded; "
                    "--fail-on-unexercised treats this as a release blocker"
                )
        elif tier == "B3":
            d["gate"] = "TREND-ONLY"
            d["gate_detail"] = "never blocks; alerts on regression vs rolling-3-run baseline"
            if d["survived"]:
                d["signals"].append(
                    f"{d['survived']} survivor(s) recorded - trend-only alert; compare against the rolling-3-run baseline"
                )
            e3 = len([e for e in t_rows if e["verdict"] == "Equivalent"])
            if e3 or d["observed_only"]:
                d["signals"].append(
                    f"informational: {e3} equivalent + {d['observed_only']} observed-only in {tier} (trend-only tier)"
                )
        else:
            rule = rules[tier]
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
                equiv_here = [e for e in t_rows if e["verdict"] == "Equivalent"]
                if equiv_here:
                    d["signals"].append(
                        f"{len(equiv_here)} equivalent row(s) recorded in {tier} - review exclusions "
                        "(e_reason/e_basis), not counted in gates"
                    )
                if d["observed_only"]:
                    d["signals"].append(
                        f"{d['observed_only']} observed-only row(s) in {tier} - review observed_element "
                        "evidence (presence review, not budget)"
                    )
            elif tier == "B2":
                threshold = rules["B2"]["small_n_threshold"]
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
                if any(s["decision"] == "dismissed" for s in survivors):
                    d["signals"].append(
                        "B2 survivor(s) dismissed without fix - mandatory signed Assessor comment "
                        "confirming dismissal rationale is documented outside this CSV"
                    )
                e_count = len([e for e in t_rows if e["verdict"] == "Equivalent"])
                e_rate = pct(e_count, d["seeded"] + e_count)
                if e_rate > rule["mass_e_pct"]:
                    d["signals"].append(
                        f"mass-equivalent {e_rate}% of originally-recorded mutants ({e_count} of "
                        f"{d['seeded'] + e_count}) marked E in {tier} - mandatory signed Assessor comment, "
                        "review e_reason/e_basis distribution"
                    )
                obs_rate_all = pct(d["observed_only"], d["seeded"])
                if obs_rate_all > rule["mass_observed_pct"]:
                    d["signals"].append(
                        f"mass-observed {obs_rate_all}% of seeded mutants in {tier} rely on observed-only "
                        f"evidence ({d['observed_only']} of {d['seeded']}) - review observed_element "
                        "distribution for genuine passive coverage vs blanket-flagging"
                    )
                if d["mutation_score"] < rules["B2"]["score_target"]:
                    d["signals"].append(
                        f"mutation score {d['mutation_score']}% below target {rules['B2']['score_target']}% - mandatory signed Assessor comment"
                    )
            d["gate"] = "PASS" if ok else "FAIL"
            if not ok:
                any_fail = True
        tiers[tier] = d

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
        {"mutation_id": e["mutation_id"], "risk_tier": e["risk_tier"],
         "reason": "expected=E (no observable behavior change)",
         "e_basis": e["e_basis"], "e_reason": e["e_reason"]}
        for e in enriched
        if e["verdict"] == "Equivalent"
    ]

    observed_rows = [
        {"mutation_id": e["mutation_id"], "risk_tier": e["risk_tier"],
         "observed_element": e["observed_element"], "observed_by": e["observed_by"],
         "observed_run_ref": e["observed_run_ref"],
         "context": "observed-only" if e["verdict"] == "Observed-only" else "on-caught-row"}
        for e in enriched
        if e["observed"] and e["verdict"] in ("Observed-only", "Caught")
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
        "profile": {"name": profile_name, "sha256": profile_sha},
        "b2_band_pct": b2_band_pct,
        "b2_small_n_max": b2_small_n_max,
        "totals": totals,
        "note": "gates and scores are per-tier by design; no global percentage is computed",
        "tiers": tiers,
        "fix_first": fix_first,
        "not_expected_rows": not_expected_rows,
        "equivalent_rows": equivalent_rows,
        "observed_rows": observed_rows,
        "unexercised_policy_applied": fail_on_unexercised,
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
    lines.append(f"config: B2 band {verdict['b2_band_pct']}% at N>=20, B2 small-N max {verdict['b2_small_n_max']} survivor(s), fail-on-unexercised={'on' if verdict['unexercised_policy_applied'] else 'off'}, requirements-cross-check={'on' if verdict.get('requirements_checked') else 'off — tiers unverified'}, profile={verdict.get('profile', {}).get('name') or 'none'}")
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
            lines.append(f"- {r['mutation_id']} ({r['risk_tier']}) - {r['reason']} [{r['e_basis']}]")
        lines.append("")
    if verdict["observed_rows"]:
        lines.append("## Observed-only (green with noted anomaly — review queue, not alarm)")
        lines.append("")
        for r in verdict["observed_rows"]:
            tag = "" if r["context"] == "observed-only" else " [on Caught row — note, not verdict]"
            lines.append(f"- {r['mutation_id']} ({r['risk_tier']}) - element: {r['observed_element']} "
                         f"(by {r['observed_by']}, ref {r['observed_run_ref']}){tag}")
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
    subparsers = ap.add_subparsers(dest="command", help="subcommands")

    # Main verdict command (default)
    verdict_parser = subparsers.add_parser("verdict", help="Run verdict on mutation results CSV")
    verdict_parser.add_argument("results", help="recorded mutation results CSV")
    verdict_parser.add_argument("--out-dir", default=None, help="output directory (default: alongside the input)")
    verdict_parser.add_argument("--b2-band-pct", type=int, default=None, help="B2 survived band in percent at N>=20 (default: 5 or profile)")
    verdict_parser.add_argument("--b2-small-n-max", type=int, default=None, help="B2 max survivors below the small-N threshold (default: 1 or profile)")
    verdict_parser.add_argument("--fail-on-unexercised", action="store_true",
                                help="treat unexercised B0/B1 tiers as release blockers (default: off)")
    verdict_parser.add_argument("--requirements", default=None, metavar="REQUIREMENTS_CSV",
                                help="cross-check behavior tiers against requirements.csv (tier-laundering guard; default: off, tiers unverified)")
    verdict_parser.add_argument("--profile", default=None, metavar="NAME_OR_PATH",
                                help="named threshold bundle (profiles/<name>.json) or path to a custom profile JSON")
    verdict_parser.add_argument("--json", action="store_true", help="print verdict JSON to stdout, write no files")
    verdict_parser.add_argument("--md", action="store_true", help="print verdict markdown to stdout, write no files")

    # RMT subcommand
    rmt_parser = subparsers.add_parser("rmt", help="RMT-lite mutation generation")
    rmt_parser.add_argument("input", help="input test file or directory")
    rmt_parser.add_argument("--tier", default="B2", choices=["B0", "B1", "B2", "B3"], help="risk tier for mutation depth (B3 yields no mutants by design: trend-only tier, nothing seeded)")
    rmt_parser.add_argument("--format", choices=["json", "summary", "csv"], default="summary", help="output format (stdout)")
    rmt_parser.add_argument("--exclude", default="node_modules", help="comma-separated directories to exclude from recursive scan")

    # Backward-compat shim (pre-subcommand CLI, broke in 08b158b): a bare
    # `verdictgate.py results.csv ...` must still route to `verdict`.
    # argparse rejects an unknown subcommand at parse time, so the old
    # post-parse default never fires — insert before parsing instead.
    if (
        len(sys.argv) > 1
        and sys.argv[1] not in ("verdict", "rmt", "-h", "--help")
        and not sys.argv[1].startswith("-")
    ):
        sys.argv.insert(1, "verdict")

    args = ap.parse_args()

    if not hasattr(args, 'command') or args.command is None:
        # No-arg invocation: default to verdict (then fails on missing results).
        args.command = "verdict"

    if args.command == "verdict":
        # load profile (if any)
        try:
            profile, profile_sha, profile_name = load_profile(args.profile)
        except InputError as exc:
            print(f"verdictgate: input error: {exc}", file=sys.stderr)
            return 2
        rules, prof_band_default, prof_small_default = apply_profile(profile, GATE_RULES)

        # resolve b2_band_pct with precedence CLI > profile > default
        if args.b2_band_pct is None:
            args.b2_band_pct = prof_band_default if prof_band_default is not None else 5
        if args.b2_small_n_max is None:
            args.b2_small_n_max = prof_small_default if prof_small_default is not None else 1

        if not 0 <= args.b2_band_pct <= 100:
            ap.error("--b2-band-pct must be 0..100")
        small_n_cap = rules["B2"]["small_n_threshold"] - 1
        if not 0 <= args.b2_small_n_max <= small_n_cap:
            ap.error(f"--b2-small-n-max must be 0..{small_n_cap} (at the small-N threshold the floor is vacuous)")

        try:
            rows = parse_rows(args.results)
            if args.requirements:
                cross_check_tiers(rows, parse_requirements(args.requirements))
        except InputError as exc:
            print(f"verdictgate: input error: {exc}", file=sys.stderr)
            return 2

        verdict = build_verdict(rows, args.b2_band_pct, args.b2_small_n_max, args.fail_on_unexercised,
                               rules=rules, profile_name=profile_name, profile_sha=profile_sha)
        verdict["requirements_checked"] = bool(args.requirements)
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

    # RMT subcommand (single implementation lives in rmt.py — see PRECONDITION in AGENTS.md)
    elif args.command == "rmt":
        from rmt import run_rmt
        return run_rmt(args)
    else:
        ap.error(f"Unknown command: {args.command}")


if __name__ == "__main__":
    sys.exit(main())
