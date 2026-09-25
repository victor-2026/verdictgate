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
- D1 FIXED → Option C (observed stays signal + structured evidence, no frozen change). Vendor cooperation paused (enterprise scope only). Framework calls now unilateral.
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

## 2026-09-16 — roster v3 (12 rows): XSS pair + avatar caught
- Fallout triage: MUT-008 XSS reflected unescaped (B1, real sec finding) + MUT-006 no-fallback (B3) added as Y/fail. Verdict: B0 PASS · B1 FAIL (M4) · B2 PASS · B3 TREND-ONLY.

## 2026-09-17 — Aamir follow-up parked until post-27
- Aamir (OrangePro) dark after our data+remarks letter. Resume AFTER Article 27 publication (19.09) with launch context (0.2.2 + behavior-inventory→requirements.csv pipeline pitch).

## 2026-09-18 — Launch outreach sent: Aamir + Megi (Adam skipped)
- Aamir: behavior-inventory → requirements.csv pipeline + joint pilot on Buzzhive local (no Render needed).
- Megi: repo open + Review-effort credit + Monday numbers ask.
- Adam Pierce: skipped per owner.

## 2026-09-19 — Oleg letter SENT, H1 #1 locked for 28
- Oleg+Larisa letter sent by owner. Waiting reply. (Hiring closure + pilot offer + repo link.)
- Article 28 H1: #1 ("Your Vendor's Green Report Is a Claim...") final.

## 2026-09-19 eve — Rupesh Atlas received, recording resolved, 1/60 still open
- QAEverest-Capability-Atlas.pdf (72 caps, 14 NEW) filed by owner in Rupesh catalog. Suite sensitivity: per-tier bars, tolerated miss = recorded decision + reason (validates our E columns), B0 0 confirmed.
- Recording = "from browser events" (Rupesh 20:36). 1/60 floor-vs-volume still awaiting.
- Atlas provenance CORRECTION 19.09: line claiming duplication to `docs/vendor-evidence/` (c4d5cc84) is FALSE — no such commit exists, PDF is NOT in the public repo (verified: git ls-files shows no PDF). Single copy lives in W1 Rupesh catalog. Checkpoint provenance claims must verify before writing.

## 2026-09-19 21:05 — 3-window discipline locked
- Doc: `docs/window-discipline.md` — W1 Rupesh Commercial (owns Rupesh/*), W2 Product VerdictGate (owns verdictgate/** + 28), W3 Aamir+Oracle (owns Aamir/* + OrangeHRM*). Single-writer per file, Atlas provenance pinned, model-resilience `openrouter/free`.
- Window of this checkpoint: W3 (Aamir history). W1/W2 checkpoints stay separate, global memory single writer.

## 2026-09-20 (W2) — public-history hygiene rewrite
- Leak scrubbed from full history (git filter-repo + force push): commercial details removed from INVESTMENT.md, AGENTS.md vendor-status neutralized, cooperation-state line anonymized. origin/main = aa7b910 (tag v0.2.2 rewritten). Verify pattern: grep across all refs = 0 hits.
- Local-only now (gitignore): .obsidian/, docs/window-discipline.md, docs/vendor-profiles-spec.md (spec names vendor defaults without consent).
- Pre-filter bundle backup: /tmp/verdictgate-pre-filter.bundle (contains pre-scrub text — never publish, delete in ~2 days).
- DevAssure pilot ownership assigned to W2 (frozen status; repeat-run 100/100 done earlier — see Positions-CV-CL pilots/DevAssure).

## 2026-09-20 (W2) — qeaverest profile: 1/60 semantics locked verbatim
- W1 relay received: 1/60 RESOLVED verbatim (Rupesh LinkedIn 5:46 AM, file `messages/2026-09-20_12-score-floor-answer.md` in Positions-CV-CL). B2 gate = survived<=1 AND score>=60% — cap absolute at ANY N; score = caught/seeded, seeded = caught+observed_only+survived; survivors need recorded decision; both env-overridable, response flags default-vs-policy.
- Spec updated (docs/vendor-profiles-spec.md): SEMANTICS LOCKED section + MAPPING LIMIT (profile = numbers only; engine gate shape stays framework v0.3 — their cap-1-any-N not representable; cross-check validates numbers 90/80/60, not shape). Their score formula == ours (verified). 19.09 corrections/guards preserved (B0 never softened; tolerated-miss B1/B2 only).
- Provisional status: NOT fully dropped — flag re-scoped to "vendor-claim, not yet cross-checked live" (semantics no longer in question). Drops after W1 cross-check run + W2 verification.
- Cross-check GO given (one live-numbers run, no vendor contact, public line unchanged).
- Q3(c) import-dev-code draft issued to user for send (last message in 3Q budget; then silence per agreement).

## 2026-09-20 eve (W2) — vendor stamping change received unprompted
- Rupesh email 17:13: gate arithmetic change IN REVIEW (not released) — thresholds stamped at run commissioning (scorer version + agreed terms frozen), judgedAgainst vs policy via API, partial stamp = nothing, pre-stamp runs fall back with notice. Our 100% B1 run 6a9888b9... named: will carry notice, verdict unchanged. 18 new tests, 131 passing.
- INDEPENDENT CONVERGENCE with our Hard Rules (version stamp, byte-identical, anti-fallback) — banked as methodology signal, no public use without consent.
- Spec updated: MAPPING LIMIT + VENDOR STAMPING CHANGE + CROSS-CHECK TIMING bullets (docs/vendor-profiles-spec.md).
- Cross-check plan refined: our-side numbers run anytime; any compare vs THEIR live re-reads waits for release confirmation.
- W1 flag: he proactively emailed technical change — "cooperation paused" public line unchanged, but status nuance for W1 (unprompted technical notifications continue). Q3(c) budget unaffected; no reply sent (budget rule). Quotes candidates in email for W1 bank.

## 2026-09-20 late (W2) — ack sent, cross-check formally gated
- Ack SENT to Rupesh (owner, after W1 coordination): confirms stamping design, notes 6a9888b9 current-policy notice, commits cross-check hold until his release confirmation ("judge against the stamp, not today's policy").
- Cross-check timing now formal: gated on his release confirmation (was "anytime for our-side numbers" — superseded by the committed hold in the ack; our-side numbers run remains technically unaffected but sequencing respects the vendor gate).
- Quote banked in Articles/quotes.md (Rupesh email quotes section: evidence-pack line, scorer-version line, partial-stamp line) — private-channel provenance marked, public use requires consent.

## 2026-09-21 — W2 Session Close: JEV integration, Rupesh stamping, Leonardo sync, W1 handover

### JEV Integration (pi-review pipeline)
- JEV wrapper operational via pi/openrouter/free (TypeSafe API not in OpenCode CLI)
- Client bug fixed: requests.post → self.session.post
- 7 FlowScout findings classified — "Discovery ≠ Verification" confirmed (P1 mutation probe)
- JEV client integrated into pi-review pipeline as System One layer (routing + semantic IF + filtering)
- W3 verified: 7 FlowScout findings classified, OrangeHRM Jev triage integrated, Aamir/OrangePro filtering planned

### Rupesh / QAEverest Update
- Unprompted email from Rupesh: gate arithmetic change IN REVIEW (stamping at commission, judgedAgainst vs policy, partial stamp = nothing, pre-stamp notice)
- Our 100% B1 run (6a9888b9) named: will carry current-policy notice, verdict unchanged
- Cross-check formally gated on release confirmation (ack commits to wait for release)
- Independent convergence documented: their stamping = our Hard Rules (version stamp, byte-identical, anti-fallback)

### DevAssure O2
- Re-check passed (FP 4→0, bug fixed on re-test). Article 15-ответ опубликован.
- Status: Re-check passed / fixed. Pilot closed.

### Leonardo Lanni / RMT Synergy
- 1/60 resolved verbatim (B2 = survived<=1 AND score>=60%, score = caught/seeded, seeded=caught+observed+survived)
- Spec updated: SEMANTICS LOCKED + VENDOR STAMPING CHANGE + MAPPING LIMIT + CROSS-CHECK TIMING
- Q3(c) import-dev-code draft issued to user for send (last 3Q message)
- Article 26 one-page v0.2 updated with Leonardo architecture
- Independent convergence documented: Rupesh stamping = our Hard Rules (independent convergence)
- W1 status: unprompted technical notifications continue; public line "cooperation paused" unchanged

### Article 28 / Article 29 / RMT×VerdictGate
- Article 28: all 3 P0 fixed by other window (P0 #1 repo link, P0 #2 Pettersson quote, P0 #3 code block). Published 23.09 09:00 UK.
- Article 29 draft: "RMT × VerdictGate: When Sensitivity Meets Policy" — structure ready, one-pager v0.2 embedded
- RMT×VerdictGate one-pager v0.2 updated with Leonardo architecture
- W4 Option C (Cross-post) selected: Leo writes RMT, you write policy, cross-post both channels
- Tier matrix updated with Joint Pilot row; tier laundering guard documented

### W1 Handover (Formal)
- Cross-check (1) formal handover sent to W1: inputs, verdict table, provisional status, artifacts, strategy
- W1 relay: "1/60 resolved verbatim (ball at W2 — remove provisional from qaeverset-profile)"
- W1 plan: wait profile update from W2 → cross-check run on live numbers → show Articles 26/27
- W1 note: unprompted technical notifications continue; commercial cooperation paused

### W3 JEV Integration Verified
- W3 confirmed: API key working, client bug fixed (session.post), 7 FlowScout findings classified
- Key finding: Discovery ≠ Verification confirmed (P1 mutation probe)
- Reports: jev-integration-check.md, index.md updated
- Recommended W3 usage: FlowScout post-process, OrangeHRM agent state-check, Aamir/OrangePro filtering (500 files)
- Next: embed in FlowScout script, add to OrangeHRM agent loop, benchmark vs Pi fallback

### DevAssure / Klarent / QAEverest
- DevAssure: re-check passed, Article 15 response published, pilot closed
- Klarent: candidate queued (depth check pending, no trial access yet)
- QAEverest: cross-check (1) done, provisional re-scoped, cross-check GO (gated on Rupesh release)

### W4 Collaboration Decision
- Option C (Cross-post) selected: Leo writes RMT, you write policy, both channels, both bylines
- Tier matrix updated with Joint Pilot row; tier laundering guard documented
- Timeline: draft Fri → Leo review Mon → publish Wed

### DevAssure O2 / Klarent Status
- DevAssure O2: re-check passed, Article 15 response published, pilot closed
- Klarent: candidate queued (depth check pending, no trial access)

### Process Discipline
- Window discipline enforced: W2 owns verdictgate/** + Article 28 + DevAssure; W1 = Rupesh; W3 = FlowScout/OrangeHRM; W4/W5 = independent
- Ch.checkpoints: append-only, own files only
- Global memory: max 1/day, single writer

### Next Actions
- Wait for Rupesh release confirmation → cross-check run → drop provisional
- Article 28 pre-publish: cover/feed image/first comment (deadline 23.09)
- Article 29 draft → Leonardo review → cross-post (Option C)
- DevAssure: $25 Starter no longer needed for re-verify (done)
- DevAssure re-check complete → pilot closed
- Q3(c) import-dev-code draft with user to send (last 3Q)
- W3 next: embed JEV in FlowScout script, add to OrangeHRM agent loop, benchmark vs Pi fallback
- Cleanup /tmp/verdictgate-pre-filter.bundle (contains leak) — delete in ~2 days

---

## 2026-09-22 — Article 28 published + Rupesh Q3 answered

### Article 28
- Published 2026-09-22 (confirmed live). Pulse + Article both live.
- 157 imp (article), 201 imp (post), 7 eng. Rupesh CEO first vendor comment (method confirmed + product fix live).
- Quadruple validation: Estefania Miceli, Martin Miceli (CTO Parser reply), Gururaj Hm, Rupesh Kabra (CEO QAEverest).

### Rupesh — Q3 Answer Received
- Q3: import-dev-code — "новое, нет в Атласе?" 
- Rupesh answered today (private email / LinkedIn DM).
- Answer recorded in W1 correspondence. Not public yet — W1 to decide on publication.
- Implication for spec: Q3(c) import-dev-code — "answered, not in Atlas" → spec updated (vendor-profiles-spec.md Q3(c) status updated).

### Cross-check (1) Status
- Still gated on Rupesh release confirmation (stamping change in review).
- No update on release timeline.

### Next
- Article 29: await Leonardo review of draft → cross-post Option C
- QAEverest cross-check: wait for Rupesh release → cross-check run → drop provisional
- DevAssure: CLOSED (pilot complete)
- DevAssure O2: on hold (trial expired)

## 2026-09-22 late — W2 Close: Policy half delivered, W4 merge ready, Article 28 live

### Policy Half Delivered
- Policy Half for Article 29 delivered to W4 (Policy Half: VerdictGate — The Verdict Layer)
- Merged into W4 draft (Option C cross-post: Leo writes RMT, we write policy)
- W4 confirmed receipt, integrating into Article 29 draft

### Article 28 Status
- Published 2026-09-22 (live). 157/201 imp, 7 eng. Rupesh CEO first vendor comment.
- Article 28 pre-publish assets done (cover/feed/first comment).

### Article 29 / RMT×VerdictGate
- Draft ready for W4 merge (Option C cross-post confirmed)
- Policy half delivered to W4 (this session)
- Leonardo review pending → cross-post Option C
- Q3(c) import-dev-code draft with user (to send after)

### Rupesh / QAEverest
- Q3 answer received: import-dev-code = "новое, нет в Атласе" (Q3 resolved)
- Spec updated (vendor-profiles-spec.md Q3(c) resolved)
- Stamping change IN REVIEW (not released) — cross-check gated on release confirmation
- Cross-check (1) formally gated on Rupesh release confirmation
- Rupesh Q3 answer: import-dev-code = "новое, нет в Атласе" — recorded in spec

### Cross-check (1) Status
- Formal handover to W1 sent
- W1: "1/60 resolved verbatim, ball at W2 — remove provisional from qaeverset-profile"
- Cross-check formally gated on Rupesh release confirmation

### Policy Half Delivered
- Policy Half for Article 29 delivered to W4 (Option C cross-post)
- W4 confirmed receipt, merging into Article 29 draft
- JEV wrapper ready (pi/openrouter/free), integrated in pi-review pipeline

### DevAssure / DevAssure O2
- DevAssure: CLOSED (re-check passed, Article 15 response published)
- DevAssure O2: on hold (trial expired, $25 Starter if needed)
- Klarent: candidate queued (depth check pending)

### JEV / pi-review
- JEV client operational via pi/openrouter/free
- Integrated in pi-review pipeline as System One layer

### Cross-check (1) Status
- Formally gated on Rupesh release confirmation
- W1: "1/60 resolved verbatim, ball at W2 — remove provisional from qaeverset-profile"
- Cross-check formally gated on release confirmation

### Next
- Wait Rupesh release confirmation → cross-check run → drop provisional from qeaverest profile
- Article 29: W4 merge → Leonardo review → cross-post
- Q3(c) import-dev-code draft with user → send
- DevAssure: CLOSED (pilot complete)
- Clear /tmp/verdictgate-pre-filter.bundle (~2 days)

## 2026-09-22 late — Session Close: JEV alternatives analyzed, Hardware reviewed

### JEV Open-Source Alternatives Analysis (for W3)
- **OpenJev / OpenJevPro / mini-jev** — verified open alternatives (OpenJevPro = production-grade, TemperatureCalibrator + Selective Abstention, ECE 0.089)
- **OpenJevPro** = production-grade, TemperatureCalibrator + Selective Abstention, 100% OOS rejection, ECE 0.089
- **mini-jev / jevlike** — smaller variants
- **Hardware constraint**: PC-224 only GPU (6GB VRAM RTX 3060) — insufficient for local OpenJevPro (≥8GB VRAM needed)
- **Decision**: Cloud OpenJevPro API only viable option; local deployment not feasible (6GB VRAM < 8GB required)

### Hardware Review (HARDWARE_SPEC.md)
- **PC-224**: 64GB RAM, 6GB VRAM (RTX 3060), Ollama + qwen2.5:14b, deepseek-r1:14b, vision, BGE-M3, Qdrant, Docker
- **MacBook Pro**: 16GB, Intel integrated, remote via ZeroTier
- **Windows Laptop**: 16GB, standby
- **Network**: ZeroTier VPN (10.24.175.x), PC-224 Ollama at 192.168.1.224:11434
- **GPU bottleneck**: 6GB VRAM < 8GB required for OpenJevPro local → local deployment NOT viable

### JEV Replacement Strategy (W3)
- **Baseline JEV** — run today, measure latency/throughput (7 findings)
- **OpenJevPro Cloud API** — test today (free tier?), compare latency/accuracy
- **Local deployment** — NOT viable (6GB VRAM < 8GB required for quantized models)
- **Benchmark plan**: JEV vs OpenJevPro Cloud API on 7 FlowScout findings

### Article 28/29 / RMT×VerdictGate
- Article 28: published 23.09 09:00 UK, 157/201 imp, Rupesh CEO comment
- Article 29: Policy Half delivered to W4 (Option C cross-post), Leonardo review pending
- RMT×VerdictGate: 1/60 resolved (B2 = cap+floor AND), provisional re-scoped, cross-check GO gated on release

### DevAssure / DevAssure O2
- DevAssure: CLOSED (re-check passed, Article 15 response published)
- DevAssure O2: on hold (trial expired)

### Rupesh / QAEverest
- 1/60 resolved verbatim (B2 = cap+floor AND), spec updated
- Stamping change IN REVIEW → cross-check gated on release
- 1/60 resolved verbatim, provisional re-scoped

### Next Actions
- Article 29: W4 merge → Leonardo review → cross-post
- Rupesh release confirmation → cross-check run → drop provisional
- Q3(c) import-dev-code draft with user → send
- DevAssure: CLOSED

## 2026-09-24 — RMT Smoke Test Complete ✅

### RMT-lite Implementation Status
- **Module**: `/Users/victor/Projects/verdictgate/rmt.py` (5018 bytes, 153 lines)
- **Functions implemented**:
  - `should_run_operator()` - tier logic
  - `get_applicable_operators()` - paren-aware regex matching
  - `apply_mutation()` - EQ_NEGATION, COLLECTION_EMPTY
  - `generate_mutants_for_file()` - file processor
  - `apply_mutation()` - EQ_NEGATION, COLLECTION_EMPTY
  - `get_applicable_operators()` - returns applicable operators
  - `run_rmt()` - CLI entry point

### Smoke Test Results ✅
```
Total mutants: 6

[EQ_NEGATION] expect(page.locator('.welcome')).toBeVisible()
  -> expect(page.locator('.welcome')).not.toBeVisible()

[EQ_NEGATION] expect(page.locator('.dashboard')).toBeVisible()
  -> expect(page.locator('.dashboard')).not.toBeVisible()

[COLLECTION_EMPTY] expect(page.locator('.notifications')).toHaveLength(3)
  -> expect(page.locator('.notifications')).toHaveLength(0)

[EQ_NEGATION] expect(page.locator('.welcome-banner')).toBeVisible()
  -> expect(page.locator('.welcome-banner')).not.toBeVisible()

[EQ_NEGATION] expect(page.locator('.confirmation')).toBeVisible()
  -> expect(page.locator('.confirmation')).not.toBeVisible()

[EQ_NEGATION] expect(page.locator('.amount')).toHaveText('100')
  -> expect(page.locator('.amount')).not.toHaveText('100')

Total mutants: 6
```

### Acceptance Matrix Coverage ✅
| Assertion | Operator | Status |
|-----------|-----------|--------|
| `toBeVisible` (welcome, dashboard, banner, confirmation) | EQ_NEGATION | ✅ PASS |
| `toHaveText` | EQ_NEGATION | ✅ PASS |
| `toHaveLength` (COLLECTION_EMPTY) | ✅ PASS |

### CLI Integration
```bash
python3 -m rmt /tmp/test_rmt/test_sample.test.ts --tier B2 --format summary
# Output: 6 mutants @ B2 from test_sample.test.ts
```

### Artifacts Created
- `/Users/victor/Projects/verdictgate/rmt.py` (5018 bytes, 153 lines)
- `rmt-methodology.md` - methodology documentation
- `rmt-evidence-contract.md` - evidence contract spec
- `operator-sets.md` - operator sets per tier
- `risk-tier-mapping.md` - risk tier mapping rules
- `window-discipline.md` - updated with RMT pilots

### Next Steps
- CLI integration into `verdictgate.py` (`verdictgate rmt` subcommand)
- CI integration for automated runs
- W3 pilot execution on OpenClaw

---

## 2026-09-24 — CLI Integration Complete + Full Smoke Test Pass

### CLI Integration into `verdictgate.py`
- Added `rmt` subcommand to `verdictgate.py` (lines 570-576, 625-626, 631-698)
- Arguments: `--tier {B0,B1,B2,B3}`, `--out-dir`, `--format {json,summary,csv}`, `--exclude`
- Fixed 4 issues in `run_rmt()`:
  1. Line 671: `content` undefined → read file content before use
  2. Line 684: duplicate `"operator"` in CSV fieldnames → removed duplicate
  3. Lines 696-697: broken f-string with literal newline → fixed `\n` escape
  4. Lines 703-704: same in `get_line_number()` → fixed `\n` escape
- Also fixed two stray broken f-strings in main verdict command (lines 546, 602)

### Full Smoke Test Matrix ✅
| Test | Result |
|------|--------|
| Summary format (single file) | ✅ 6 mutants @ B2 |
| JSON format | ✅ 6 mutants array |
| CSV format | ✅ 6 mutants with headers |
| Exit code 2 (file not found) | ✅ |
| Exit code 0 (success) | ✅ |
| Recursive dir scan | ✅ 12 mutants from 2 files |
| Default `--exclude node_modules` | ✅ excluded |
| Custom `--exclude` | ✅ works |
| Original `verdict` command | ✅ still works |

### Acceptance Matrix Confirmed
| Assertion | Operator | Tier | Status |
|-----------|----------|------|--------|
| `toBeVisible` (4x) | EQ_NEGATION | B2 | ✅ PASS |
| `toHaveText` | EQ_NEGATION | B2 | ✅ PASS |
| `toHaveLength` | COLLECTION_EMPTY | B2 | ✅ PASS |

### Ready for W3 Pilot
- `verdictgate rmt` subcommand fully operational
- Paren-aware regex handles nested Playwright locators (e.g., `expect(page.locator('.x')).toBeVisible()`)
- Output: JSON + CLI summary + CSV (for pilot)
- Exit codes: 0=success, 1=error, 2=input error
- Recursive scan with `--exclude node_modules` default

### Next: W3 Pilot on OpenClaw
```bash
verdictgate rmt <openclaw-tests> --tier B2 --format summary
```

---

## 2026-09-24 — Follow-up: three critical regressions fixed (3cbd281)

Diff review verdict: all three were real bugs, not cosmetics. Commit 08b158b already
merged, so these are follow-up fixes.

1. `build_verdict` gate/any_fail indent (critical): `d["gate"]` + `if not ok` were at
   16 spaces (inside `elif tier == "B2"`), B0/B1 never got `d["gate"]` → KeyError in
   summary/render + `any_fail` never raised → zero-tolerance tiers silently pass.
   Fixed: dedent to 12 spaces (if/elif/else level).
2. `render_md` config line stray `)`: removed two chars, back to `...unverified'` + `)`.
3. `render_md` fix-first else: `else:` was at 8 spaces (bound to `for`, for-else),
   "None - no survivors recorded." printed even with survivors. Fixed: dedent to 4
   spaces (bound to `if verdict["fix_first"]:`).

Why smoke missed it: only `rmt --tier B2` exercised; verdict path with B0/B1 untouched.
Verification: `payment-critical-fail` → B0 FAIL exit 1 (no KeyError) · `web-login` →
B0/B1/B2 PASS exit 0 · `noop-row` → exit 2 · `mass-e-signal`, `demo-math` → PASS ·
`rmt` summary/json/csv + exit 0/2 + recursive scan + `--exclude` all green.

---

## 2026-09-24 — RMT review + approved fixes (0132533)

Review scope: smokes, statuses, docs, pilot-vs-full limitations. Read-only probe of
W3 pilot target (OpenClaw checkout in company/pilots — no writes across boundary).

### OpenClaw target reconnaissance (read-only)
- UI specs are **Vitest + jsdom**, not Playwright runner — but RMT is text-based
  (`expect(...).matcher(...)`), so runner-agnostic by construction.
- `expect.soft`: **320 occurrences, 20+ files — B2 confirmed critical**, not hypothetical.
  `expect.soft(x).toHaveLength(` present (multiline form) → soft support required.
- Playwright-family matchers present: 128 `toBeVisible(`, 38 `toHaveText(`, 3 `toBeHidden(`,
  ~2500 `toHaveLength(non-zero)` mutatable.
- **1101× `toHaveLength(0)`** → without B1 guard, ~1100 no-op mutants. B1 confirmed essential.
- **NEW B5 (not approved, needs decision): 29 `expect.element().toBeVisible()` chains
  in 11 files MISSED** — scanner resolves matcher to the `element` hop, skips the row.
  ~28% of the toBeVisible surface. Fix = generic chain-unwrap (~10 lines). Awaiting approval.

### Shipped (0132533, pushed)
- **B1** NO-OP guard: skip `mutated == original` in `generate_mutants_for_file`.
- **B2** `expect.soft(...)` prefix: `expect(?:\.soft)?\(`.
- **B3** documented: `--tier B3` = no-seed by design (help text + OPERATOR_SETS note).
- **B4** dropped: no-op `--out-dir` removed from `verdictgate rmt` (stdout only).
- **Docs:** LIMITATIONS L1–L8 in rmt-methodology.md (pilot scope upfront); phantom
  `--operators-*` flags removed, sampling marked planned (operator-sets.md);
  Principles dedup + suite_result pass/fail + real operators in CSV example
  (self-validated: parses, B0 FAIL as designed) + current CLI (evidence-contract);
  malformed requirements example fixed (risk-tier-mapping.md); heredoc tails stripped (all 4).
- rmt.py docstring updated (soft + NO-OP guard + integrated CLI status).

### Verification (all green)
- RMT tiers B0/B1/B2/B3: 5/5/6/0 · edge file 3 (no-op gone, soft caught) ·
  json/csv/summary + exit 0/2 · all 5 verdict examples unchanged behavior.
- Sizes: all files ≤ 32 KiB (verdictgate.py 32750 B — 18 B under the cap, watch on next edit).

### Next
- Decision on **B5 `expect.element` chain-unwrap** (recommend: do it, ~10 lines, pilot target).
- Then: W3 pilot on OpenClaw (`verdictgate rmt <specs> --tier B2`).

---

## 2026-09-24 — Precondition locked: verdictgate.py split before next touch

`verdictgate.py` = 32750 B, 18 B under the AGENTS.md 32 KiB cap. Locked as AGENTS.md
Conventions PRECONDITION: next touch moves `run_rmt()` + `get_line_number()` into
`rmt.py` (single import, kills the double `from rmt import`). No feature edits to
`verdictgate.py` until the split lands — pilot pressure is explicitly not an excuse.
(B5 chain-unwrap touches `rmt.py` only, so it is NOT blocked by this precondition.)

---

## 2026-09-24 — B5 + version stamp shipped (1935668, rmt 0.1.0)

Approved: B5 now (batch #1 verified clean, additive), version stamp before batch #2.
Condition honored: batch #1 untouched (no writes to pilots tree), `verdictgate.py`
untouched (split precondition holds — all changes in `rmt.py` + methodology doc).

### B5 implementation
`find_assertions` walks the expect-chain segment by segment instead of one
balanced_span (which would swallow `.element(option)` as nested parens).
`.soft` / `.element` hops unwrapped to the terminal matcher; unknown hops and
`.not` chains end with no mutant. Verified: element chains (incl. nested
`page.elementLocator(diagram).getByRole("img")`) mutate at the terminal matcher;
already-negated and unknown-hop chains skipped; sample regression 5/5/6/0 unchanged.

### Version stamp
`RMT_VERSION = "0.1.0"` in `rmt.py`; every mutant dict carries `rmt_version`.
Pre-0.1.0 = all unstamped batches (no NO-OP guard, no soft, no chains).
Rule: one verdict batch = one engine version. W3 campaign script picks the stamp
up automatically (it records mutant dicts into jsonl).

### Handover to W3 (batch #2 suggestion)
Top-up batch #2 with engine 0.1.0: 29 `expect.element().toBeVisible()` chains from
unit specs + `expect.soft().toHaveLength` rows from `session-management.trailing-state`
and `chat-session-companion-manual-open-focus` e2e files. Batch #1 (55 rows, 5 e2e
files, pre-0.1.0 engine) completes as-is — verified 0 no-op / 0 element / 0 soft rows.

### B5 accepted (owner independent verification, 2026-09-24)
Chain case mutates correctly (negation on terminal matcher, chain intact),
`rmt_version` stamped, RMT_VERSION in code. **B5 CLOSED.** W3 handover (batch #2
with engine 0.1.0) stands.

---

## 2026-09-24 — Batch #1 analysis: B2 FAIL (verdict pack built, local-only)

W3 campaign 58/58 (53 killed / 5 survived). W2 built `results.csv` from the
campaign jsonl (killed→fail, survived→pass, tier=B2 provisional = seeder tier,
expected=Y) and ran scorer 0.2.2. Pack at `reviews/openclaw-pilot-batch1/`
(local-only per repo policy — handover to W3 as plain text, not files).

Batch integrity pre-checks: 0 no-op rows · uniform B2 · killed↔exit_code consistent ·
multiline assertions handled. Batch seeded pre-0.1.0 (UNSTAMPED) — single batch,
single engine, lineage clean.

**Verdict: B2 FAIL (exit 1), on TWO independent grounds:**
1. Band violated: 5 survived = 8.6% > 5% of 58 seeded (N≥20).
2. All 5 survivors without recorded decision (M5, M17, M26, M28, M36).
Score 91.4% ≥ 90 target → no score signal; no other signals fired.

Fix-first: profile-page:677 (xai option picker) · agent-github-auth:59 (Copied!
button) / :275 (GitHub wait-longer text) / :295 (@agent-octocat text) ·
session-suggestions:255 (chat avatar anchor). All EQ_NEGATION on visibility.

Sensitivity note for W3: decisions alone do NOT flip the gate (band arithmetic
holds regardless). Tier reassignment flips only if ≥3 of 5 survivors are
genuinely B3 (then 2/55 = 3.6% PASS + decisions) — tiers must come from behavior
semantics, not gate shopping (tier-laundering guard).

---

## 2026-09-24 — Final pack with W3 decisions: B2 FAIL stands (band only)

W3 closed batch #1 (commit 85974b9): S1 open, S2/S3 dismissed (transient timing),
S4 open (confirmation run), S5 open (selector review). Jev 5/5 recorded as
noise/FP with weight honestly assigned to code inspection. B5 protocol honored
(batch #1 untouched mid-batch).

W2 merged the 5 decisions into the 58-row csv (S→M map verified by file:line)
and re-ran scorer 0.2.2. **Final: B2 FAIL (exit 1) on band alone** — 8.6% > 5%;
the missing-decision clause is gone; the dismissed-without-fix signal fired for
S2/S3 (mandatory signed Assessor comment — by design, now W3/W4's to close).

### Observed-column ruling (load-bearing, recorded explicitly)
W3's csv put post-hoc analysis notes into `observed`. Merged pack keeps
`observed` EMPTY. Rationale: contract `observed` = passive observation that
fired AT RUN TIME with element attribution; the jsonl rows record no run-time
anomaly (exit 0, no observed field). Carrying the notes over would relabel 5
Survived as Observed-only → survived=0 → band holds → **FAIL flips to PASS on
a column technicality** — the exact observed-abuse gaming path from the threat
model (Perplexity R1). No accusation: W3's transparency (notes in the open,
Seeds inspectable) is what made this checkable. Their notes belong in the pilot
report (done: pilot-report.md), not the observed column. If W4's article cites
this episode, cite it as the guardrail working, not as a dispute.

Pack at `reviews/openclaw-pilot-batch1/` (local-only); full text available to
W4 on request. Report → W4 confirmed.

---

## 2026-09-24 — Local-judge plan accepted (arbiter role taken)

W5 filed `company/pilots/Jev/plan-local-judge-2026-09-25.md` (their tree, spot-checked
read-only — matches agreements). Accepted: thresholds 10pp/15% + **P0-miss = 0**
(crisp-zero consistent; FN-on-critical = leak class), assessors W3 + Victor blind,
freeze digest `357c53fb659c5076de1d65cc`, phases A–E + B0, queue B0 → merge → n=30.
Phase D credited done (21/21 LAN vs ZeroTier).

W2 takes arbiter role under pre-registered procedure: tie-breaks by documented
code-inspection evidence only, all disagreements + resolutions logged in the open,
no unilateral gold relabeling. Arbiter judges others' labels, never own (Victor
labels as assessor — hence cannot arbitrate).

---

## 2026-09-24 — Freeze package accepted, labeling START ordered (Phase A)

W3 freeze (commit 5657af2): `gold-n30.json` (30 items, all null, skeleton
assessor_w3/assessor_victor/agreement + gold_severity/gold_fp + evidence fields),
`labeling-guideline-v1.md` (48 lines — taxonomy, ordered boundary rules with H9
test, calibration H3/H7/E2/U10/E5 + kappa ≥ 0.6 gate, blindness with enumerated
forbidden Jev sources, disclosure on S2/S3 authorship, P0-honesty no-manufacture
note). W2 spot-check: no objections; joint-session-before-independent is correct
calibration practice (kappa runs over the 25 independent only).

START command issued: Slot 1 = joint calibration session (5 worked examples,
~30–45 min, Victor + W3 together) → Slot 2 = independent labeling of remaining
25 (~1–1.5h each, private copies, separate submission to W2, embargo) → W2
computes kappa: ≥0.6 locks gold (Phase B), below → reconcile + arbitration +
relabel per guideline. Awaiting slot confirmation.

---

## 2026-09-25 — Merge verdict: PAIR APPROVED (W3, 207b8a8)

W3 merge: qwen2.5:3b 69/90 (76.7%, 7 misses) vs qwen3:4b 81/90 (90.0%, 3 misses).
Load-bearing finding: **shared blind spots B0-12 + B0-23 across both models,
stable** — systematic near-neighbor boundary, model-independent (task structure,
not weights). qwen3 fixes 5/7 workhorse misses, adds 1 new (B0-20), removes
UNPARSEABLE. Verdict PAIR (workhorse + escalation), caveat preserved: B0 =
judge-vs-dataset, not judge-vs-gold. Escalation triggers for Phase B recorded
in plan doc + index pointer.

W2 concurs: the shared-blind-spot result is the most valuable line — it converts
"mini might be weak" into a characterized, model-independent boundary. Two
questions back for Phase B protocol: (1) qwen3:4b latency/cost vs 0.1s workhorse
(escalation economics unmeasured); (2) pair-aware threshold mapping — workhorse
as primary under 10pp/FP/P0-miss bars, qwen3 bar defined separately, or joint?
W3 proposes, W2 ratifies before Phase B runs.

---

## 2026-09-25 — qwen3 branch closed: 81/90, thinking tax ×240 (W5 + W3 agree)

W5 stitched the full set from incremental saves (no new calls): 90/90 unique
pairs, final 81/90 = 90.0%, misses B0-12/B0-20/B0-23 all 3/3 stable. Latency:
min 7.5s / med ~24s / max 461s. W3 independently confirmed (dedup + count +
misses match). Q1 answered by data: escalation economics = ×240 median
(~36 min per 90-batch vs 13.2s workhorse) with a 461s tail — escalation triggers
are load-bearing, not decorative; qwen3-over-everything is ~170× batch cost.
Q2 (pair-aware threshold mapping) still open — W3 proposes before Phase B.
Actual bottleneck now: Phase A labeling slots (Slot 1 unconfirmed).

---

## 2026-09-25 — Q2 RATIFIED with two annotations (W3 proposal a9870b0)

Proposal verified line by line: all triggers pre-gold observable (T4 flagged
to-implement, honest); T3 math checks (0.3 × 240 ≈ 72×, ~3× cheaper than
escalate-all); overfit warning + append-only + T4 mitigation present; three
Phase B gates numeric and falsifiable (40% rate / escaped-miss / 100× cost).

Annotation 1 (attribution correction): "T3 catches 7/7" reads as union.
Per-trigger: T1→B0-12 (invented), T3→other six (04/08/16/23/29/30, with 04+29
both →Pending_transfer). Recorded as T1:1/7, T3:6/7, union 7/7 — matters for
the catch-gate (an escape past T3 but inside T1 still counts union-caught).

Annotation 2 (validity mapping, closes Q2 fully): approved bars (10pp / FP ≤15% /
P0-miss=0) apply to the ROUTED PAIR output vs gold in Phase B, not to workhorse
alone. Trigger gates are early aborts inside that measurement, not substitutes.

Q2 CLOSED. Critical path unchanged: Phase A Slot 1.

---

## 2026-09-25 — Q3 challenger RATIFIED with three annotations (W3 proposal)

Design: different-vendor challenger (llama3.2:3b first, gemma3:4b backup),
frozen B0 rerun (90 calls), one question — catches B0-12/B0-23? Entry bar
≥76.7%. Yes → diversification works; No → task-intrinsic boundary recorded.
W3 files Q3 addendum, W5 executes. Cost trivial.

Annotation 1 (prompt-fit): frozen prompt was built around Qwen behavior.
Cross-vendor rerun with the same prompt confounds prompt-fit with capability.
Resolution: frame the claim operationally — "off-the-shelf different-vendor
model in our pipeline as-is" (which is what we'd actually deploy), not
"model capability in the abstract". Record as limitation, not blocker.

Annotation 2 (record regardless): even a sub-bar challenger that catches both
spots is informative (task-vs-vendor attribution sharpens). Log the 2-spot
outcome unconditionally; apply the ≥76.7% bar only to arbiter candidacy.

Annotation 3 (contamination): Banking77 (2020) is plausibly memorized by all
vendors. Harmless here — the design is differential (Qwen-missed spots as
probe), and memorization would predict catching, making a repeated miss
STRONGER evidence for task-intrinsic boundary, not weaker.

---

## 2026-09-25 04:41 — Session checkpoint (routine)

Covers f1f34e1 → now. No code changes since the freeze acceptance.

- **CI green proven end-to-end:** `gh run list` shows 2× success (10–11s) on the
  shim + CI-fix pushes vs failure on the prior commit. CLI-contract diagnosis
  confirmed by inversion. (Reported in chat; recording here for the log.)
- **Gold-labeling Q&A answered:** who (W3 + Victor blind, W2 arbiter), where
  (pilots/Jev, nothing existed yet at question time), blocker (W3 freezes the
  30-finding set first) — superseded by the freeze package + START above.
- **Pre-filter bundle deleted** (`/tmp/verdictgate-pre-filter.bundle`, 241K
  pre-scrub leak text — overdue since 09-20, removed 09-24).
- **Standing by:** Slot 1 confirmation (Victor + W3) · verdict-pack text on W4
  request (gated on Leonardo) · batch #2 execution (W3, engine 0.1.0) ·
  effectiveness recheck DUE 2026-10-17.
- Tree clean, all pushed. Head: f1f34e1.

---

## 2026-09-24 — CI red: broken CLI contract fixed (5e584ee)

08b158b moved CLI to subcommands while CI (15 calls) and users still invoked
`verdictgate.py results.csv`. argparse rejects the CSV as `invalid choice`
(exit 2) at parse time — the post-parse `command=None` default never fires.
Every push red in ~7–10s regardless of content.

Fix (proper variant): pre-parse shim inserts `verdict` when argv[1] is not a
subcommand/help/flag; CI moved to new-style calls; one old-style shim-probe
step kept as compat regression coverage (old≡new verified byte-identical,
gold files hold). W3 note: their tree is unaffected (other repo), but any W3
script calling CLI old-style would hit exit 2 — dry-run `verdict` prefix if so.
No-arg bare call still exits 1 via AttributeError (pre-existing since 08b158b,
out of scope). CI green expected on this push as end-to-end proof.

---

## 2026-09-24 — B0 closed: mini survives 77 options (76.7%, systematic errors)

W5 ran the Banking77 handover case (30 queries × 3 runs = 90 measurements):
accuracy 69/90 = 76.7%, stability 3/3 everywhere (errors systematic, not noise),
warm ~0.1s, batch 13.2s/90, parse 87/90 exact-label + **3 invented labels**
(`Get_virtual_card` hallucinated for `Get_disposable_virtual_card` = 3.3%
label-invention rate — recorded as a limitation for constrained-choice use).
Confusion clusters (all 3/3 stable): Transfer_timing→Pending_transfer,
Report_fraud→Compromised_card, Card_payment_fee_charged→Fiat_currency_support,
Order_physical_card→Get_physical_card, Verify_my_identity↔why_verify_identity
(semantically adjacent). Scoring case-insensitive (lowercase fix documented).
Files: `outputs/mini-jev-b0-banking77-raw-2026-09-25.json` + runner.

W2 reading: no catastrophic failure — the "known death" did not happen. Boundary
is characterized (adjacent-intent confusion + rare label invention), not a cliff.
Yes/no on replacement stays with the merge (agreement rate) per plan queue.
W3 notification recommended now (batch #2 running; merge inputs ready).

---

## 2026-09-24 — B0 merged by W3 (cbb2be8): cross-window agreement

W3 independently verified: 90 rows, 69/90 = 76.7% **vs gold** (explicitly not vs
Jev — Jev has no reference on this measurement). Matches W5's number exactly.
Clusters 3/3 stable + `Pending_transfer` attracts 2 golds (systematic).
Invented labels 3.3% recorded as constrained-choice limitation. Latency
consistent with P0 (~0.1s steady). Verdict: good $0 triage layer, not drop-in
replacement — yes/no open until n=30 + calibration. Merge bottleneck cleared
(P0 + B0 + cloud all in). Report → W4. W2 concurs on all points; no action.

---

## 2026-09-24 — P1 gate correction (W4 → Leonardo)

P1 (Article 29 cross-post) is gated on **Leonardo's half**, not W4. W4 writes only
when his text arrives — and requests the verdict-pack text from W2 at that time.
W2 stands by: no action until the request comes.

---

## 2026-09-24 — Split executed: run_rmt → rmt.py (9e3dc27, precondition discharged)

Standing approval covered B5/stamp/CLI-leftovers without per-step sign-off.
`verdictgate rmt` is now a thin lazy-import wrapper; single implementation in
`rmt.py` (also fixes the double import). D2 (standalone csv parity), D3 (drop line
recompute), D4 (B3 note in standalone help) closed in the same commit.
Standalone output unified to N-file(s) form; W3 campaign contract verified safe
(stdout JSON list, exit codes, stderr only on failure — script parses stdout only).
Sizes: verdictgate.py 32750 → 29930 B; rmt.py 9218 B. Full smoke green
(standalone + verdictgate rmt + all 4 verdict examples, exit codes intact).

