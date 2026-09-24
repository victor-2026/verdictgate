# RMT Evidence Contract Specification

**Version:** 0.1
**Status:** Draft
**Owner:** W2 (Product)
**Date:** 2026-09-22

---

## Purpose

The Evidence Contract defines the standardized format for mutation testing results to flow from any mutation source (RMT-lite, traditional MT, vendor tools) into VerdictGate. It ensures **source-agnostic** mutation evidence that VerdictGate can consume without knowing the mutation engine.

## Contract Principles

1. **Source-agnostic** - Works with RMT-lite, traditional MT, vendor tools, manual entry
2. **Immutable** - Once written, rows are append-only; corrections via new rows
3. **Self-describing** - Each row contains all context needed for verdict
3. **Deterministic** - Same input -> same verdict, byte-identical output
4. **Extensible** - New columns via versioned schema evolution

---

## Schema

### Required Columns

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `mutation_id` | string | YES | Unique identifier (M1, M2, ...) |
| `behavior` | string | YES | Human-readable behavior description |
| `operator` | string | YES | Mutation operator ID (EQ_NEGATION, BOOL_NEGATION, etc.) |
| `risk_tier` | enum | YES | Risk tier: B0, B1, B2, B3 |
| `expected` | enum | YES | Y (should catch) / N (out of scope) / E (equivalent) |
| `suite_result` | enum | YES | pass / fail (anything else is an input error) |
| `observed` | string | Optional | Free-text observation notes |
| `decision` | enum | Conditional* | open / dismissed / fixed (required for B2 survivors) |
| `e_reason` | string | Conditional** | Required if expected=E (<=280 chars) |
| `e_assessor` | string | Conditional** | Required if expected=E |
| `e_basis` | enum | Conditional** | code-review | diff-analysis | no-observable-path | dead-code | other |
| `observed_by` | string | Conditional*** | Required if `observed` non-empty |
| `observed_run_ref` | string | Conditional*** | Run reference (opaque ref, never a live timestamp) |
| `observed_element` | string | Conditional*** | Specific element that fired the observation |

---

### Conditional Rules

* **`decision` required** when `risk_tier=B2` AND `suite_result=pass` (survived)
* **`e_reason`, `e_assessor`, `e_basis`** required when `expected=E`
* **`observed_by`, `observed_run_ref`, `observed_element`** required when `observed` non-empty

---

## Verdict Mapping

| `expected` | `suite_result` | `observed` | Verdict | Notes |
|------------|----------------|------------|---------|-------|
| Y | fail | - | **Caught** | Test caught the mutant |
| Y | pass | empty | **Survived** | Silent failure - gate concern |
| Y | pass | non-empty | **Observed-only** | Green with anomaly flagged |
| N | any | any | **n/a** | Out of scope (not in denominator) |
| E | pass | any | **Equivalent** | Excluded from denominator |

---

## CSV Schema (Input to VerdictGate)

```csv
mutation_id,behavior,operator,risk_tier,expected,suite_result,observed,decision,e_reason,e_assessor,e_basis,observed_by,observed_run_ref,observed_element
M1,Payment submits,EQ_NEGATION,B0,Y,pass,,open,,,,,,
M2,Login rejects wrong pwd,EQ_NEGATION,B0,Y,fail,,,,,,,
M3,Username placeholder,COLLECTION_EMPTY,B1,Y,pass,two identical username inputs,,,,,reviewer,run-042,username input #2
```

### Column Definitions

| Column | Type | Required | Notes |
|--------|------|----------|-------|
| `mutation_id` | string | YES | Unique per mutation (M1, M2, ...) |
| `behavior` | string | YES | Human-readable behavior description |
| `operator` | string | YES | Mutation operator (EQ_NEGATION, BOOL_NEGATION, etc.) |
| `risk_tier` | enum | YES | B0, B1, B2, B3 |
| `expected` | enum | YES | Y = this suite should catch it, N = out of scope for this suite, E = assessed equivalent (no observable behavior change) |
| `suite_result` | enum | YES | pass = suite stayed green on the mutant, fail = suite went red |
| `observed` | string | Optional | Passive observation flag (any text); empty = silent |
| `decision` | enum | Conditional | open | dismissed | fixed -- required for B2 survivors (`dismissed` fires mandatory signal) |
| `e_reason` / `e_assessor` / `e_basis` | string | Conditional | REQUIRED when expected=E: one-line reason (<=280 chars), who assessed, on what basis (code-review | diff-analysis | no-observable-path | dead-code | other). Unassessed E is rejected -- equivalence must be justified, not asserted. |
| `observed_by` / `observed_run_ref` / `observed_element` | string | Conditional | REQUIRED when `observed` non-empty: who noted it, which run (opaque ref, never a live timestamp), and the specific element that fired |

No-op rule: a NOOP / NO-OP row means the seeder ADMITS nothing was changed. That is a process violation: refuse pre-seed (it stays out of N), never accept it post-hoc. Contrast with E (above): assessed, recorded, excluded.

Run: `python3 -m verdictgate verdict results.csv`
Outputs: `<stem>.verdict.md` + `<stem>.verdict.json` (scorer version stamped).

---

## VerdictGate Output (Evidence Pack)

### 1. `results.verdict.md` -- human-readable evidence pack
- Per-tier tables with gates, signals, survivors
- Fix-first list with RACI sign-off
- Observed-only rows (review queue, not alarm)

### 2. `results.verdict.json` -- machine-readable, version-stamped
```json
{
  "scorer_version": "0.2.2",
  "deterministic": true,
  "b2_band_pct": 5,
  "b2_small_n_max": 1,
  "totals": { "rows": 7, "seeded": 4, "caught": 2, "observed_only": 1, "survived": 2, "equivalent": 0 },
  "note": "gates and scores are per-tier by design; no global percentage is computed",
  "tiers": {
    "B0": { "label": "Critical", "scope": "payment, auth, credential, data-integrity paths", "seeded": 2, "caught": 2, "observed_only": 0, "survived": 0, "equivalent": 0, "mutation_score": 100.0, "survival_rate": 0.0, "gate": "PASS", "gate_detail": "zero-tolerance held (survived 0 of 2)", "signals": ["B0 sign-off additionally requires a confirmatory re-run (two consecutive passing runs)"], "survivors": [], "not_expected": [] },
    "B1": { "label": "High", "scope": "core user journeys, primary CRUD, search, notifications", "seeded": 2, "caught": 1, "observed_only": 1, "survived": 0, "equivalent": 0, "mutation_score": 50.0, "survival_rate": 0.0, "gate": "PASS", "gate_detail": "zero-tolerance held (survived 0 of 2)", "signals": ["mutation score 50.0% below target 80% - mandatory signed Assessor comment", "observed-only 50.0% exceeds budget 20% at survived=0 - signed comment required", "1 observed-only row(s) in B1 - review observed_element evidence (presence review, not budget)"], "survivors": [], "not_expected": [] },
    "B2": { "label": "Medium", "scope": "secondary flows, edge cases", "seeded": 2, "caught": 1, "observed_only": 0, "survived": 1, "equivalent": 0, "mutation_score": 50.0, "survival_rate": 50.0, "gate": "PASS", "gate_detail": "small-N floor held (max 1 at N=2 < 20)", "signals": ["mutation score 50.0% below target 90% - mandatory signed Assessor comment"], "survivors": [{"mutation_id": "M6", "behavior": "Forgotten password link", "operator": "element_remove", "decision": "open"}], "not_expected": [] },
    "B3": { "label": "Low", "scope": "cosmetic, copy, layout, non-critical polish", "seeded": 1, "caught": 0, "observed_only": 0, "survived": 1, "equivalent": 0, "mutation_score": 0.0, "survival_rate": 100.0, "gate": "TREND-ONLY", "gate_detail": "never blocks; alerts on regression vs rolling-3-run baseline", "signals": ["1 survivor(s) recorded - trend-only alert; compare against the rolling-3-run baseline"], "survivors": [{"mutation_id": "M9", "behavior": "Welcome banner copy", "operator": "text_change", "decision": null}], "not_expected": ["M7", "M8"] },
  "fix_first": ["B2 · M6 · Forgotten password link (element_remove) - SURVIVED, decision: open", "B3 · M9 · Welcome banner copy (text_change) - SURVIVED, decision: NO RECORDED DECISION"],
  "not_expected_rows": [{"mutation_id": "M7", "risk_tier": "B3", "reason": "expected=N"}, {"mutation_id": "M8", "risk_tier": "B3", "reason": "expected=N"}],
  "equivalent_rows": [],
  "observed_rows": [{"mutation_id": "M4", "risk_tier": "B1", "observed_element": "username input #2", "observed_by": "reviewer", "observed_run_ref": "run-042", "context": "observed-only"}],
  "unexercised_policy_applied": false,
  "gate_summary": "PASS",
  "exit_code": 0,
  "requirements_checked": false
}
```

---

## Integrity Rules

1. **Determinism** -- Same input -> byte-identical output. No timestamps, no randomness, no absolute paths in verdicts.
2. **Version stamp** -- Any change to GATE_RULES or verdict logic bumps SCORER_VERSION and updates both golden files (lesson: scorer 0.2.34 -> 0.2.40 silently shifted rankings).
3. **Exit-code contract:** 0 = pass, 1 = gate failed, 2 = input error. CI and the future GitHub Action depend on it.
4. **Zero-tolerance is not configurable:** B0/B1 survived=0 always. Only the disputed B2 band is CLI-configurable.
5. **No-op discipline:** `NOOP` / `NO-OP` rows (seeder admits nothing changed) are rejected at input -- refuse pre-seed, never post-hoc. `E` rows are the opposite case: ASSESSED equivalent, RECORDED as Equivalent verdicts, visibly excluded from the denominator (v0.1.1+).

---

## Anti-Patterns

1. No secrets -- no tokens, no test credentials in examples
2. No dated facts -- avoid "as of 2026-09-22"; use relative time
3. No model-specific instructions -- rules must work with any AI model
3. Size <= 32 KiB -- must fit in one context window

---

## Versioning

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-09-22 | Initial draft |

---

*End of Evidence Contract Specification v0.1*