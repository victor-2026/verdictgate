# VerdictGate

**Mutation Matrix Evaluator — per-risk-tier verdict calculator for AI-QA test suites.**

A green test suite is a claim, not evidence. VerdictGate turns *recorded* mutation results into an audit-ready, per-tier verdict: which risk tiers hold, which have silent survivors, and what to fix first — without executing anything.

The final-gate calculator: evidence in, ship / no-ship per tier out.

- **Static** — no runner integration, no code execution. You recorded what happened; the calculator judges it.
- **Deterministic** — same `results.csv` → byte-identical verdict files, stamped with the scorer version.
- **Per-tier, never blended** — B0 Critical / B1 High / B2 Medium / B3 Low each get their own gate. No single global percentage is computed.
- **Discipline-enforcing** — no-op mutants are rejected at input: refuse pre-seed, never post-hoc.
- **Not an executor** — it never generates or runs mutants. They run (or vendors run); VerdictGate judges. Seeding is out of scope by design.

Requirements: Python 3.10+, standard library only, no dependencies.

## Quick start (30 seconds, no setup)

See a verdict immediately (expected: FAIL, exit 1 — a B0 survivor violates zero-tolerance):

```bash
python3 verdictgate.py examples/payment-critical-fail/results.csv
# B0 FAIL · B1 PASS · B2 NOT EXERCISED · B3 NOT EXERCISED - FAIL (exit 1)
```

Then run your own recorded mutations:

```bash
cp templates/results.csv results.csv
# fill in your recorded mutations (see Input format below)
python3 verdictgate.py results.csv
```

Outputs `results.verdict.md` (evidence pack with RACI sign-off) and `results.verdict.json` (machine-readable, version-stamped).

## Example verdict (real output, `payment-critical-fail`)

| Tier | Seeded | Caught | Survived | Gate |
|---|---|---|---|---|
| B0 Critical | 2 | 1 | 1 | FAIL |
| B1 High | 1 | 1 | 0 | PASS |

Fix first: **B0 · M1 · Payment submits successfully (element_remove) — SURVIVED, no recorded decision.** Sign-off table ships empty (Reviewer of record / Independent Assessor / Engineering owner) — anyone with the same CSV and scorer version reproduces this verdict exactly.

## Input format

| Column | Meaning |
|---|---|
| `mutation_id` | unique id (M1, M2, ...) |
| `behavior` | what the suite claims to verify |
| `operator` | mutation type (`id_change`, `text_change`, `element_remove`, `swap_targets`, ...) |
| `risk_tier` | `B0` Critical · `B1` High · `B2` Medium · `B3` Low |
| `expected` | `Y` = this suite should catch it · `N` = out of scope for this suite · `E` = assessed equivalent (recorded, excluded from the denominator) |
| `suite_result` | `pass` = suite stayed green on the mutant · `fail` = suite went red |
| `observed` | optional: passive observation flag (any text); empty = silent |
| `decision` | optional: `open` / `dismissed` / `fixed` — required for B2 survivors (`dismissed` fires a mandatory signal) |
| `e_reason` / `e_assessor` / `e_basis` | required when `expected=E`: reason ≤280 chars, who assessed, basis enum (`code-review` / `diff-analysis` / `no-observable-path` / `dead-code` / `other`) |
| `observed_by` / `observed_run_ref` / `observed_element` | required when `observed` non-empty: who, which run (opaque ref, never a timestamp), firing element |

Verdict per row: **Caught** (suite went red) · **Observed-only** (green but flagged — reported separately, never inflates the score) · **Survived** (green and silent — the only outcome that fails a gate) · **Equivalent** (assessed: no observable behavior change — recorded, excluded from the denominator, never silent) · **n/a** (expected=N, out of the denominator).

## Verdict rules

| Tier | Hard gate | Score signal |
|---|---|---|
| B0 Critical | 0 survived, always; sign-off additionally requires a confirmatory re-run (two consecutive passing runs) | < 90% → mandatory signed Assessor comment |
| B1 High | 0 survived, always | < 80% → mandatory signed Assessor comment |
| B2 Medium | ≤ 5% survived (N ≥ 20) or max 1 survivor with a recorded decision (N < 20) | < 90% → mandatory signed Assessor comment |
| B3 Low | never blocks; trend vs rolling-3-run baseline | — |

Survived count is the hard gate; mutation score is a signal bar — a low score triggers a mandatory signed comment, never a silent auto-fail. Displayed rates are rounded to one decimal; the B2 band gate itself uses exact integer arithmetic. Observed-only has its own budget at survived=0 (B0 ≤ 10%, B1 ≤ 20%): exceeding it is a signal, not a pass. Mass-exclusion signals (0.2.0): any Equivalent rows on B0/B1 fire a review-exclusions signal; mass-E over 5% / mass-observed over 10% of B2 fire review signals. Presence signals are a REVIEW QUEUE ("review the exclusions"), not an alarm — see sweep provenance in AGENTS.md D1.

B0/B1 zero-tolerance is **not** configurable: no decision can pass a zero-tolerance tier. The B2 band is the one disputed knob, so it is CLI-configurable with a strict default (`--b2-band-pct`, default 5; `--b2-small-n-max`, default 1).

## Trust boundaries (read before disputing a vendor report)

The calculator judges what was RECORDED — it cannot verify the recording. Three paths stay human-owned:

- **Scope (N):** marking a mutant out-of-scope removes it from every denominator. Scope truth lives in `requirements.csv` + reviewer sign-off, not in the CSV. Unrestricted N is a known bypass path; a strict cross-check mode is roadmap (v0.2).
- **Tier assignment:** demoting a mutant to a lower tier (e.g. B0 → B2) moves it from zero-tolerance to the 5% band without touching any denominator. Nothing in the CSV proves a tier label — tier truth is a reviewer check against `requirements.csv` risk levels.
- **Run fragmentation:** thresholds apply per file. Splitting 25 B2 mutants into two files of 12+13 dodges the N ≥ 20 band via the small-N floor. One scope = one file = one verdict; multi-file scopes need a run id (roadmap, v0.2).
- **Equivalence (E):** assessed equivalents are recorded and visibly excluded — but the assessment itself is trusted. Mass-E (hard mutants re-labeled E) is the top gaming path; the E-justification guard is roadmap (v0.2).
- **Equivalence (E):** assessed equivalents are recorded with justification (`e_reason`/`e_assessor`/`e_basis`) and visibly excluded — unassessed E is rejected at input. Mass-E fires review signals (any on B0/B1, over 5% on B2).
- **NOT EXERCISED ≠ PASS for release:** a tier with no Y rows exits 0 with the tier marked NOT EXERCISED. For release decisions treat unexercised B0/B1 as a blocker by policy; `--fail-on-unexercised` enforces it (B0/B1 only, display stays NOT EXERCISED).

Reproducibility contract: same CSV + same scorer version + same CLI flags → byte-identical verdict files. The B2 flags used are stamped into every verdict artifact.

## Exit codes

`0` all exercised gates pass · `1` any gate failed · `2` input error (malformed CSV, no-op row, empty input)

## Why not X

| Tool | What it does | Why not that for this job |
|---|---|---|
| [mutgate](https://github.com/JimGalasyn/mutgate) | named mutation contracts, executes each in a sandbox | executes; no per-tier verdicts. Complementary: they run, we judge. |
| mutation-gate | pre-commit gate, runs mutmut on the staged diff | executes, commit-scoped, no tiering |
| Stryker / mutmut / PIT / mutago | generate + execute mutations, report a kill rate | need runner integration; one global score; cannot verdict a vendor run you recorded by hand |
| oracle-gate | tier-based framework for testing AI-built code + conformance checks on evidence packages | a framework to adopt, not a calculator; no per-tier survival verdicts from a results CSV |
| vendor trust scorecards | vendor-side confidence numbers | closed methodology; a single number, not a per-tier gate |
| hand-calculated | a spreadsheet per run | not reproducible, not comparable across runs, no sign-off structure |

## Methodology

Per-risk-tier gating and the mutation matrix come from the field methodology described in [How to Evaluate Any AI-QA Vendor in 5 Scenarios](https://www.linkedin.com/pulse/how-evaluate-any-ai-qa-vendor-5-scenarios-victor-ematin-lqdhe/). `templates/` carries the full and lite methodology for manual runs; `templates/evidence-pack.md` describes what to attach to a PR or release record.

## Status & roadmap

Alpha (0.1.x). MIT.

Roadmap: scorer 0.2.0 shipped (E-justification, observed evidence, mass signals, --fail-on-unexercised). Next: vendor threshold profiles · v1 importers (Stryker / opro JSON as input) · v2 GitHub Action posting verdicts to PRs. (Versioning: `scorer x.y.z` = this calculator; `framework v0.x` = the co-developed methodology — different lines, see AGENTS.md.)

Seeding mutants is out of scope — by design. This is the verdict layer, not another executor.
