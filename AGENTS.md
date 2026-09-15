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
- Roadmap: v0.2 configurable thresholds + vendor profiles · v1 importers (Stryker/opro JSON) · v2 GitHub Action posting verdicts to PRs
- Seeding mutants is out of scope by design — this is the verdict layer, not another executor
