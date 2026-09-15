# VerdictGate — AGENTS.md

Mutation Matrix Evaluator: per-risk-tier verdict calculator for AI-QA test suites.
Static, deterministic, metadata-only. Python stdlib. MIT.

## Boundaries

| Area | AI can | AI ask | AI cannot |
|---|---|---|---|
| `verdictgate.py` | ✅ edit | | |
| `templates/` | ✅ edit | | |
| `examples/*/results.csv` | ✅ edit | | |
| `examples/*/expected.verdict.json` | | ✅ ask | golden files — change only together with a SCORER_VERSION bump |
| `.github/workflows/` | ✅ edit | | |
| `README.md` | ✅ edit | | |
| `AGENTS.md` | ✅ edit | | |
| `LICENSE` | | | ❌ never |

## Architecture

```
results.csv (recorded mutations) → verdictgate.py → <stem>.verdict.md + <stem>.verdict.json
                                    ├─ parse & validate (no-op rows rejected pre-seed)
                                    ├─ per-tier aggregates (Caught / Observed-only / Survived)
                                    ├─ gate rules (GATE_RULES mirrors per-risk-tier framework v0.3)
                                    └─ evidence pack (RACI sign-off, fix-first, version stamp)
```

## Sources of Truth

1. AGENTS.md (this file)
2. Per-risk-tier framework v0.3 (frozen) — gate rules in `verdictgate.py` must mirror it
3. `templates/mutation-matrix-{lite,full}.md` — the methodology
4. Product PRD — `ai-qa-wiki/outputs/product-concept-mutation-verifier-mvp.md`

## Open decisions (need human approve, framework-adjacent)

- **D1 — Observed-budget promotion (Perplexity P1.2): DECIDED 2026-09-16 → Option C.**
  - C (fixed): budget stays signal; observed rows require structured evidence (who/when/run-ref + names mutated element per framework L71); calculator checks presence, Assessor verifies substance; mass-observed rate fires its own signal. No frozen-semantics change, no external dependency.
  - Rejected A (status quo leaves zero-tolerance evadable) and B (gate promotion needs framework v0.4).
  - Rupesh status (corrected 2026-09-16): NOT silent — DECLINED to continue; resumes only with an enterprise customer on that customer's money. No cross-check expected; framework decisions are unilateral from here. His index/correspondence needs sync (Positions-CV-CL side).
  - Calculator MUST NOT implement B without a new explicit decision.

## Hard Rules

- **Determinism:** same input → byte-identical output. No timestamps, no randomness, no absolute paths in verdicts.
- **Version stamp:** any change to GATE_RULES or verdict logic bumps SCORER_VERSION and updates both golden files (lesson: scorer 0.2.34 → 0.2.40 silently shifted rankings).
- **Exit-code contract:** 0 = pass, 1 = gate fail, 2 = input error. CI and the future GitHub Action depend on it.
- **Zero-tolerance is not configurable:** B0/B1 survived=0 always. Only the disputed B2 band is CLI-configurable.
- **No-op discipline:** `NOOP` / `NO-OP` rows (seeder admits nothing changed) are rejected at input — refuse pre-seed, never post-hoc. `E` rows are the opposite case: ASSESSED equivalent, RECORDED as Equivalent verdicts, visibly excluded from the denominator (v0.1.1+).

## Anti-Patterns

1. No secrets — no tokens, no test credentials in examples
2. No dated facts in README/templates — "as of last update", not fixed dates
3. No model-specific instructions — must work with any LLM
4. ≤ 32 KiB per file — split when exceeded

## Conventions

- Commits: `feat:`, `fix:`, `docs:`, `chore:`
- Repo starts private; public opening is gated on Article 27 publication
- Roadmap: scorer 0.2.0 input-trust hardening (Perplexity review 2026-09-15) — E-justification guard + mass-E signal · observed-flag control (structured evidence; budget→gate promotion DECISION needed, see D1) · NOT EXERCISED policy + --fail-on-unexercised · decision enum + CLI ranges + thresholds stamp (shipped in 0.1.2) · vendor profiles · v1 importers (Stryker/opro JSON) · v2 GitHub Action posting verdicts to PRs
- Versioning rule: `scorer x.y.z` (SCORER_VERSION, this calculator) and `framework v0.x` (per-risk-tier methodology, Rupesh dir) are DIFFERENT lines. Never write a bare `v0.x` — always qualify. Framework v0.3 is frozen; its next would be framework v0.4, not scorer 0.4.
- Seeding mutants is out of scope by design — this is the verdict layer, not another executor
