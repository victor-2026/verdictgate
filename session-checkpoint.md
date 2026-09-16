# VerdictGate — session checkpoint (append-only)

## 2026-09-15/16 — Input-trust hardening 0.1.1→0.1.3 + external reviews

**External reviews (2):**
- Perplexity round 1 → `reviews/perplexity-2026-09-15.md` (gitignored, local-only; links cleaned). 20+ findings triaged: P0.1 downgraded (behavior matched README → boundary tests, not defect); observed-abuse confirmed as top gaming path.
- Pi adversarial (Sonnet, $0.68 total day spend): NEW finds — P0 tier-reassignment laundering, P1 decision-theater/cosmetic-signals, P2 multi-file fragmentation, parser bugs. First run timed out at 10 min ($0.56, no output); resume same session ($0.12) recovered everything. Lesson: 20 min + background for agentic reviews.
- Perplexity round 2 bundle ready (`/tmp/verdictgate-review-bundle-0.1.2.md` + prompt) — free tier closed for the day, send tomorrow.

**Shipped (pushed b2f1a00):**
- 0.1.1: E as recorded Equivalent (was: rejected); NOOP stays exit-2; noop-row example re-cut on NOOP token.
- 0.1.2: CLI ranges, decision enum, E+fail contradiction, strict CSV, thresholds stamp, B2 boundary matrix (6 cases), README Trust boundaries.
- 0.1.3: newline-safe CSV parse (physical line numbers), decision case-fold, small-n-max cap 0–19, tier-laundering + fragmentation documented.
- Self-caught: deleted `--json` flag + flipped small-n-max default 1→5 via sloppy edit — both restored before commit (default is 1, README right).

**Decisions (AGENTS.md Open decisions):**
- D1 FIXED → Option C (observed stays signal + structured evidence, no frozen change). Rupesh corrected: DECLINED (resumes only on enterprise-customer money), not silent. Framework calls now unilateral.
- Version lines disambiguated: `scorer x.y.z` vs `framework v0.x` (commit 4272f1d, UNPUSHED).

**Roadmap v0.2 (scorer 0.2.0):** E-justification guard + mass signals · observed structured evidence · NOT EXERCISED policy + flag · vendor profiles · importers · GH Action.

**Pending:** push 4272f1d · Perplexity round 2 send · Megi numbers (calibrate Full Step 6, not blocking).

## 2026-09-16 — Sweep Phase 1 kills Pi thresholds; Render suspended, local only
- Render Hobby suspended (5GB out, reset ~Oct 1). No pay decision. CI schedule paused (d80bd4b, OrangeHRM). Docker unpaused by user; local OrangeHRM 200 OK.
- Sweep v1 (`/tmp/sweep.py`, synthetic, verdictgate 0.1.3): all Pi mass-% thresholds MISS all measured flips (5–17.6% vs 15–40%). Structural cause: zero-tolerance flips on LAST-survivor relabel → B0/B1 presence-based signals, % only B2 (5%/10% provisional, provenance sweep-v1). Results: `reviews/sweep-phase1-flip-points-2026-09-16.md`. D1 + roadmap updated (Pi numbers REJECTED).
- Harness bug caught: verdict written next to /dev/stdin → OSError → all-exits-1. Detection rule recorded: zero flips on designed-to-flip baseline = harness bug.
- OpenRouter evening: Pi r1 $0.56 (timeout) + resume $0.12 + r2 design ~$0.15 = ~$0.83 day. Guard blocks paid till reset/raise.
- Next: Perplexity round 2 (bundle 0.1.3 + prompt v2 ready) · Megi numbers · 0.2.0 implement (needs threshold sign-off — sweep provides it).

## 2026-09-16 — Phase 2 approved: honest-run distributions on Buzzhive
- Question driving it: do presence-based B0/B1 signals fire on every honest run (noise-floor test)? Decides presence-vs-% viability.
- Substrate: Buzzhive local (own code, real mutants, fast) — NOT OrangeHRM (vendor image, nothing to seed into). Batch: 6–8 mutants x admin flows incl. 1–2 genuine equivalents + 1 observed case → E/observed base rates.
- Multi-app deferred to v0.3+ (thresholds are gate-design choices, diminishing returns now).

## 2026-09-16 — Phase 2 batch executed (Buzzhive)
- Batch: 10 rows (1 Y-caught DBMUT-001, 7 N resilience/defense, 2 E controls). Verdict: B1 PASS, rest NOT EXERCISED, exit 0. E-path verified on real runs.
- Key methodology finding: N-scope load-bearing (7/10 defense greens would pervert a kill-rate gate). Defense-verification ≠ regression-detection.
- Debts: DBMUT-008 broken (schema drift, sandbox side) · distributions need volume (Phase 2b) · no natural observed case yet.
- Files: `reviews/phase2-batch-2026-09-16.csv`, `reviews/phase2-batch-results-2026-09-16.md`; spec in sandbox (uncommitted).

## 2026-09-16 — Phase 2b executed: 17-row honest roster, B1 FAIL on genuine survivor
- New specs: phase2b-roster (E3/E4/O1/O2/D1-D3). Blank-mock caught by probe: `**/api/posts*` never matches `/api/posts/feed` (`*` vs `/`) — fixed to `**/api/posts**` in phase2* files. 12 existing-suite occurrences still blank (sandbox debt flagged, not touched).
- D1 invalidated then re-run valid (probe discipline). D2/D3 genuine red. M4 genuine Survived (stale feed on 500).
- Verdict: B0 PASS · B1 FAIL (M4 + score 50%) · B2 PASS (score signal 33%) · exit 1. All rows correct.
- Noise-floor answer: presence signals would fire routinely on honest mixes → design as REVIEW QUEUE (wording!), not alarm. Review cost ~10 min / 6 flags.
- Files: `reviews/phase2b-roster-2026-09-16.csv`, `reviews/phase2b-roster-results-2026-09-16.md`.

## 2026-09-16 — 0.2.0 validated live on Phase 2b roster v2 (9 rows, exit 1)
- Split-brain: :3000 nginx proxies /api past local postgres (proxy 4 vs local 6).
  DB rows out of CSV; db-spec edits reverted; MUT greens out (blank family).
- All 0.2.0 mechanics fired correctly first try: E-justification accepted,
  presence signals (B0/B1), mass-E 25%, mass-obs 66.7%, observed review-queue
  section with attribution, dismissed path untouched. B1 FAIL is genuine (M4).

## 2026-09-16 — B2 band validated live (5.0% PASS / 10.0% FAIL) + M4 confirmed
- 20-row B2 batch (phase2b-band.spec, API-mock self-contained): file A exit 0, file B exit 1. Exact-edge `>` semantics hold.
- M4 staleness probe: IDENTICAL content + 0 error banners on posts-500. Genuine product bug (sandbox).
- B2 5% band: mechanics validated. mass 5%/10%: fired live, values provisional pending volume.
- Lesson: detection batches with --retries=0 (default retries=2 hung one file 30 min).
