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

- **D1 — Observed-budget promotion (Perplexity P1.2): DECIDED 2026-09-16 → Option C. IMPLEMENTED in scorer 0.2.0** (structured observed evidence required at parse; mass-observed presence B0/B1 + 10% B2 as review-queue signals; budget stays signal). CLOSED.
  - C (fixed): budget stays signal; observed rows require structured evidence (who/when/run-ref + names mutated element per framework L71); calculator checks presence, Assessor verifies substance; mass-observed rate fires its own signal. No frozen-semantics change, no external dependency.
  - Rejected A (status quo leaves zero-tolerance evadable) and B (gate promotion needs framework v0.4).
  - Rupesh status (corrected 2026-09-16): NOT silent — DECLINED to continue; resumes only with an enterprise customer on that customer's money. No cross-check expected; framework decisions are unilateral from here. His index/correspondence needs sync (Positions-CV-CL side).
  - Sweep v1 update (2026-09-16, `reviews/sweep-phase1-flip-points-2026-09-16.md`): measured flip rates 5–17.6% — ALL Pi-proposed % thresholds (E 15/20/25, obs 25/35/40) miss. Structural cause: zero-tolerance flips when the LAST survivor is relabeled (rate unbounded below) → B0/B1 get PRESENCE-based signals (any E>0 / observed>0 at survived==0), % only for B2 (provisional: mass-E 5%, mass-obs 10%, provenance "sweep-v1 synthetic"). Pi thresholds REJECTED, do not implement.
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
- Repo PUBLIC since 2026-09-18 (opened with Article 27 publication)
- Roadmap: scorer 0.2.2 SHIPPED (--requirements tier-laundering guard). Effectiveness recheck DUE 2026-10-17 (Schaper ceremony: provisional mass thresholds recalibrated against accumulated Step-7 volume; regressions become own issues). Next: vendor profiles · v1 importers (Stryker/opro JSON) · v2 GitHub Action posting verdicts to PRs
- Phase 2 (APPROVED 2026-09-16): honest-run distributions on Buzzhive local (own substrate) — 6–8 mutants × admin flows incl. 1–2 genuine equivalents + 1 observed case. Goal: E/observed base rates + presence-signal noise-floor test (does presence fire on every honest run?). Multi-app deferred to v0.3+.
- Versioning rule: `scorer x.y.z` (SCORER_VERSION, this calculator) and `framework v0.x` (per-risk-tier methodology, Rupesh dir) are DIFFERENT lines. Never write a bare `v0.x` — always qualify. Framework v0.3 is frozen; its next would be framework v0.4, not scorer 0.4.
- Seeding mutants is out of scope by design — this is the verdict layer, not another executor
