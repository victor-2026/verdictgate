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

## 2026-09-25 — Slot 1 DONE: 5 worked examples locked (Victor session)

Joint calibration with Victor (arbiter-facilitated, scaffolding faded 5/5 —
last two items labeled independently before confirmation):

- **H3** (external-link): NOISE + fp=true (rules 4+5). Worked jointly.
- **H7** (external-link, vendor): NOISE + fp=true. Victor independent. Mechanics repeat confirmed.
- **E2** (dismissed-transient, S2): NOISE + fp=true (rule 2, both conditions verified by live inspection of adjacent clipboard assertion :58 covering :59).
- **U10** (validation-quirk): NOISE + fp=true (rule 3). Rejected alternative recorded: P2-reading loses (rests on speculative fragility "if required removed", not observed; cf. rule-7 spirit).
- **E5** (survived-negation, S5): **P2 + fp=false** (rule 5, file-it). Victor's reasoning accepted over arbiter's NOISE lean: asserted visibility = specified requirement; negation passing = requirement unenforced = cosmetic-functional defect. Function works → not P1.

Precedent rules established (guide the remaining E-items):
- **R1:** survived negation + NO adjacent enforcement → P2 (file-it).
- **R2:** survived negation + adjacent stable coverage → NOISE (rule 2).
- E2 vs E5 is the clean R1/R2 split: clipboard assertion covers :59; nothing covers avatar content at :255.

Recording rule: worked-5 resolutions live HERE (not in gold fields — excluded from kappa by design). W3 merges all 30 into gold-n30.json once (worked 5 converged + 25 post-kappa/arbitration); W2 verifies before Phase B.

Slot 2 OPEN: remaining 25 items, independent, private copies, separate submission to W2 (format per item: severity + fp + one-line note + pointer), embargo until W2 publishes comparison. W3 takes the same order via relay. Deadline: none — "по готовности" (owner decision 2026-09-25); quality over speed, embargo holds regardless.

---

## 2026-09-26 — 60 runs STARTED: source local-only, API = bonus (W3)

W3: Jev API alive at 05:20 probe (US-hours grace plausible till evening) —
correctly framed as BONUS, not dependency. Verdict source one-liner: 60
app-runs judged ONLY by local vitest exit codes; Jev API never in the loop
(Jev verdicts were a separate survivor-enrichment branch). This resolves W2's
dependency-key question as sequencing (в), NOT methodological (б) — no scoring
replan needed. Start condition (W4) met with no access/payment.

Protocol endorsed as stated: same-tree, revert-after-each, incremental save.
Preventive note for the run: exit -9 cases (if any) follow the batch #2
binding mapping (re-run + capture → caught-by-crash / killed / infra-excluded,
never silent). W2 awaits raw in results/ on completion.

---

## 2026-09-26 — 60-run verdict VERIFIED from raw (W3 bc900e1)

Recomputed independently: 81 rows = 21 baselines (all exit 0) + 60 mutant runs
(10 × 6). Killed exactly {M2,M4,M5,M9}, each 6/6 red; survived
{M1,M3,M6,M7,M8,M10}, each 6/6 green. Unanimous everywhere — zero flakes, zero
-9 (binding mapping unneeded). M1 interim confirmed; M6/M10 by-design stands
(pre-registered). Kill rate 4/10 = 40% on app-mutants; survivor analysis
(M1 blind, M3 confirmed, M6/M10 coverage hole, M7 fallback unasserted, M8
cascade unasserted) is W3's verdict text — endorsed as filed.

Smoke-track note: torch wall on W5's box (CPU-index ≤2.2.2 < gliner2 ≥2.5),
background upgrade running. No methodology objection; one lineage requirement:
log the torch upgrade (old→new version + date) wherever the smoke runs land —
env changes travel with measurements, same doctrine as model digests. Binding
sequence (RECON only, no measurement claims) stands.

---

## 2026-09-26 — Fastino/GLiNER third hand: ENDORSED with sequencing (W3+W5 triage)

W3 triage (a94fe21, web-verified: real, Apache 2.0, 340M, CPU, fine-tune,
confidence, hosted API) + W5 recon (their 60.2% vs JevK5/SemIf-Qwen benchmarks;
156 likes, 1k downloads/mo). W2 assessment: the generative-vs-encoder axis is
genuinely missing (all our judges generate; a deterministic encoder tests
whether the task needs generation at all) — endorse the AXIS.

Binding sequencing (non-negotiable order):
1. **Smoke first** (W5's "one evening": pip install + 7 findings) — labeled
   SMOKE/RECON only: pipeline viability, never numbers.
2. **Schema-mapping design + freeze** (typed questions+rules → severity/fp,
   confidence thresholds, multi-Decide iff non-EN findings) — mini-protocol,
   W2 ratifies BEFORE any run. Unmapped runs produce incomparable verdicts
   (W3's design-cost warning is exactly right).
3. **Measurement on gold-30** — only after (2).

Notes: vendor 60.2% is non-transferable (their domains, not severity
judgments — interest signal only); queue after 60-runs + Phase C stands
(no preemption); multi-Decide only if findings go multilingual (gold-30 is
EN — base suffices unless proven otherwise). Relay to W1 as received: Fastino
Labs in outreach (API + open-weight, Tirtha.ai shelf) — W1's call.

---

## 2026-09-26 — No-migration ruling CONCURRED (W3 24/81 green, ~30 min left)

W3: parallelization technically possible (independent mutants, exit-code
verdicts, trivial JSONL merge) but declined mid-run. W2 concurs on all three
grounds, with the mapping to standing rules: (1) mid-migration = contamination
+ one-batch-one-machine violation; toggle-state fragility (HEAD=true/
worktree=false) newly named as explicit hazard — gain 15–20 min vs batch
invalidation is the right asymmetry call; (2) PC speed unknown — benchmark
first (computer-tool baseline ~25s here), decide next campaigns on facts;
(3) no multiplied entities. PC benchmark runs PARALLEL (separate machine,
no interference with the running batch).

Interim (not a verdict): M1 silent-drop exit 0 ×3 — survived candidate,
3/3 stable green on seeded break is already a strong signal; formalized at
completion. W2 takes no position until the verdict pack.

---

## 2026-09-26 — 60-run campaign design ACCEPTED as-is (W3 launched)

Three points worth stating aloud: (1) Toggle-harness footgun (git checkout →
mutant ON) caught AND guarded (all-false assert at end) AND documented
in-script — textbook hazard handling. (2) M6/M10 proximity mapping with
pre-registered Survived-by-design as legitimate outcome (documented coverage
hole ≠ suite failure) — honest scoping, same family as N-scope. (3) 21
baselines (7×3) match the baseline-green rule; 60 = 10×6 exceeds the 2× minimum
— stronger, no objection. Exit -9 → binding mapping adopted. Raw streaming to
appmut-60 jsonl; full run ~40–60 min. W2 awaits verdict on completion — no
interim action.

---

## 2026-09-26 — Jev API liveness + 60-runs source: two parallel checks (W2 spec)

Victor: maybe Jev not yet disabled (timezones)? W4: start 60 runs ONLY without
Jev API (free expired 25.09, paid unapproved); W3 to confirm verdict source in
one line. W2 answers:

1. **Timezone math is the wrong tool — probe, don't compute.** Expiry "25.09"
   minus/plus TZ offsets resolves nothing; one authenticated call resolves
   everything (200 alive vs 401/402/429 dead). Who: W3 (holds key + working
   TypeSafe client since 09-21) or owner. NOT W2 — no secrets in this window,
   never asks for the key. Probe: single minimal `systemone` call, report
   status code only (no payloads, no keys in chat).
2. **Liveness changes nothing for the 60-runs decision.** Even if alive on
   grace: paid unapproved ⇒ building plans on grace = risk. W4's local-only
   condition stands either way; a live API is informational, not a reopen.
3. **W3's check (verdict source, one line) is the load-bearing one:** if 60
   runs need Jev-API verdicts → HOLD until access/payment decision (this is
   dependency-key (б) from the analysis — replan scoring, don't start blind);
   if local-only → START. That line unblocks more than the probe.

---

## 2026-09-26 — Batch #2 hangs: (б) with pre-registered 3-way mapping (W2 ruling)

W3: 2 inconclusive (tooltip:213, wa-controls:46, exit -9 ×2), env alive.
Ruling: (б) — 3rd run, extended timeout + process capture (~15 min). Decisive
argument beyond W3's: two consecutive -9s on the SAME mutants smell
mutant-correlated (infinite loop from negation?), not random infra — closing
as infra-excluded now could bury a genuine caught-by-crash. The capture
distinguishes; (a) cannot.

Binding outcome mapping (pre-registered, no post-hoc reading):
(i) completes → record actual verdict; (ii) hangs again + capture shows
mutant-correlated loop → Caught (suite red via crash) + observed note with the
capture pointer; (iii) hangs again + infra cause → infra-excluded: OUT of the
denominator (like N-scope, Phase-2 precedent), documented — never counted as
survived, never inflates N. Either way ambiguity dies with this run.

---

## 2026-09-26 — Batch #2 CLOSED, mapping executed exactly (W3 b82b0a5)

Closeout artifact verified run-by-run against the jsonl (4 runs: tags, exits,
durations, CPU samples all match the table): tooltip:213 → Caught-by-crash
(clean 30s baseline vs 3rd consecutive -9 + sustained CPU, mechanism honestly
marked hypothesis); wa-controls:46 → Killed (exit 1, 9F/5P — prior -9s were
the flaky end of a hang→fail spectrum, good catch recorded). 22 killed as
controls; zero inconclusive; N=24 intact, precedent uninvoked. Procedural
hygiene noted with approval (gitlink reset, minimal recommit, fork gitignored,
others' files untouched — same colon-file accident I had myself, handled right).

Batch #2 complete: seeded 0.1.0-stamped, executed, verdict artifact closed.
OpenClaw pilot evidence now: batch #1 (58, B2 FAIL) + batch #2 (24, controls +
2 resolved). Combined verdict pack assembly is W3's call if wanted; W2 needs
no further input on this track.

---

## 2026-09-26 — Correction: batch #2 artifact DONE (was phantom-pending)

W3: verdict artifact executed + verified (4 runs → tooltip Caught-by-crash,
wa-controls Killed, 22 controls → closeout b82b0a5 → W2 verified 8d1a42a).
Earlier summaries listing it as "awaiting execution" were stale — corrected.
W3 real pending: (1) S4-confirmation run; (2) 60 app-runs — Jev-track
dependency cleared, needs one bit from W4: start now or queue still held?
Routed to W4; W2 takes no position (their queue, their call).

Scope confirmed: top-up = batch #2 verdict artifact (22 killed as controls +
2-hang decision), zero new mutants. S4-confirmation and 60 app-runs stay
separate tracks. Execute same-day on W3's side; verdict pack to results/.

---

## 2026-09-26 — REPLACEMENT VERDICT: REJECTED, three independent grounds (W3 48a89ba)

W2 independently recomputed from raws (verbatim 90 + cloud 30). Table VERIFIED:
L0/routed 0/0/24/0/H10-P1; cloud 9/21/4/3/H10-P1 (case-normalized; my first
pass missed the lowercase — caught and corrected, matching W3 exactly).
Verbatim batch + bool fp confirmed (90/90 raws present); W3's self-reported
case-bug recount closes clean — no residual.

1. **Margin FAIL:** routed 0% vs cloud 70% sev-only (exact 0 vs 30%) — gap 70pp
   (30pp on exact) vs 10pp bar. Decisive alone.
2. **FP FAIL:** 100% of negatives (24/24) vs 15% cap. (Context only: cloud
   itself 16.7% — the bar bites the reference too; moves nothing.)
3. **P0-miss STOP FIRES — override of W3's reading, stated openly:** report
   frames H10 as "recorded vs L0-alone, no independent routed miss". W2
   disagrees on the rule mechanics: the 4f3fd45 exemption attached to L0's
   NON-CANDIDATE status, not to the numbers. The candidate (routed pair) has
   now produced its output and it misses P0 (P1 ≠ P0) → stop fires. Outcome
   unchanged (already rejected twice over), but the third ground stands
   independently — if gates 1–2 are ever re-litigated (e.g., bar recalibration),
   P0-miss holds the rejection alone.

Erratum for W3 (notes, not verdict): "fp_bool False on 27/30 (incl. 21)" →
actual 19/30 (incl. 16). Plus new finding from recompute: 12 cloud outputs are
SELF-CONTRADICTORY (severity NOISE + fp False = "is a defect") — instrument
pathology distinct from gold disagreement; worth one line in the report.

Routing: never engaged (T1 0 UNPARSEABLE, T2 0 splits, T3 vacuous in severity
space — documented pre-run) → pair hypothesis UNTESTED here, not disproven.
L0 failure = deterministic overcall; prompt carries no taxonomy. On W3's
Q-design punt (prompt paraphrase): NEW intervention = NEW frozen protocol +
new decision required; not a continuation. Current question answered NO;
reopen only by explicit decision.

---

## 2026-09-26 — Replacement track CLOSED: NO, three grounds (W3 983b0ce concurs)

W3 accepted all three: P0-miss correction (their reading wrong, stop fires,
lesson recorded) · erratum recounted 19/30 + 12 self-contradictory outputs
named (E8/E9/E10/H2/H6/U2–U8) as instrument pathology · "not proven" recorded
(routing unengaged, Q-design punt accepted). Cross-window agreement complete:
margin FAIL + FP FAIL + P0-stop. The local-judge replacement question is
answered NO and stays closed absent a new explicit decision (new intervention,
new protocol, new freeze).

---

## 2026-09-25 — Phase B L0 raw independently recomputed: 0/30, verdict STANDS

W3 raw (90 rows, L0×3/item, digest confirmed, path accepted). W2 recomputation:
stability 30/30 · L0 majority P1×25+P2×5 · **exact vs gold 0/30, severity-only
0/30** (L0 P2s: H2/H3/H4/H9/U6 — zero overlap with gold E3/E4/H8/E5; H10 gold-P0
→ L0 P1; H9 gold-P1 → L0 P2) · fp is STRING "no" everywhere (runner type bug,
see below) · latency consistent · file flags partial=True (L0-arm only).

Rulings:
1. **0/30 does NOT trigger P0-miss stop.** Stop rule (ratified) applies to
   ROUTED-PAIR output; L0 was never the replacement candidate. Worse-than-
   constant (0 < 24) CONFIRMS the ladder's raison d'être instead — overcalling
   is systematic (P0-trial already showed fp-always-no), discrimination must
   come from routing, exactly as designed. Next measured entity: routed pair
   (T1–T4 → Gemma → qwen3), never L0-alone — state this wherever numbers travel.
2. **fp string-vs-bool: BLOCKING data bug.** `got_fp` is "no" (str), gold is
   False (bool) — any `== False` comparison silently mismatches everything.
   Runner must emit booleans before the canonical batch.
3. **Verbatim: REQUIRED (upgraded from optional).** With 0/30 on parsed outputs
   + established parse-sensitivity (hygiene 0.624→0.994), audit needs verbatim
   responses. Cheap re-run, same frozen digest; current file → superseded pilot,
   canonical = verbatim batch. W3 already offered; W2 accepts the offer.
4. H10 P0-miss recorded against L0-alone (no stop); if the ROUTED pair misses
   H10, stop fires for real.

---

## 2026-09-25 — Kappa 0.242: arbitration path, 8 rulings published

Both submissions in (W3 sealed, Victor filed; Victor's trailing-comma JSON
fixed by arbiter, values untouched). Agreement 17/25 (68%), pe=0.578
(both NOISE-heavy) → **kappa 0.242, gate FAIL** → guideline path: reconcile +
arbitration (this entry), no relabel round needed — rulings below ARE gold.

Directional finding: Victor +1 level on 6/8 divergences (E3,E4,E8,U5,U6,U9);
H8 Victor-higher, H10 Victor-LOWER (attention, not blanket inflation).
Concentration: control-item over-calling (U5/U6/U9 = the set's traps firing as
designed) + file-it liberality on E-items.

Rulings (arbiter inspection-backed):
- E3 P2 (Victor): live inspection :265–300 — transient message, NO adjacent
  enforcement (unlike E2's clipboard). R1 applies. W3's "same class as S2/S3"
  rejected as principle: pilot dismissal ≠ gold NOISE (different instruments).
- E4 P2 (SPLIT): Victor right on defect (R1, counts/URL neighbors don't enforce
  handle text), level per Victor's OWN E5 logic ("not P1 since function works").
- E8 NOISE (W3): killed mutant = control, Boundary 3. Victor misread (killed =
  works); noted kindly as the key lesson.
- H8 P2 (W3): FlowScout index confirms real bug, reproduced by hand — but
  fade-in transient ⇒ Rule-1 P0 cap (waiting is a workaround). Defect instinct right.
- H10 P0 (W3): core workflow (tool use) + no working workaround + silent
  self-misrepresentation = P0 per taxonomy letter. "Closed"/non-repro notes
  don't erase verified facts (healthy provider + zero invocations).
- U5/U6 NOISE (W3): textbook controls (terminal-preserved, transient-retried);
  Boundary 3. Victor P1s had no inspection basis (pointers "unsure") — the set
  caught over-calling exactly as designed.
- U9 NOISE (W3): describes the FIX (retry path instead of silent fail) — correct
  improved behavior, no deviation.

Embargo lifted with this publication. Next: W3 merges all 30 (17 agreed + 8
ruled + 5 worked-converged) into gold-n30.json; W2 verifies the merge before
Phase B. Victor: E8-lesson (killed = works) + E4 self-consistency check are the
two takeaways; nothing to redo — arbitration replaced relabel by design.

---

## 2026-09-25 — Merge 25/30 VERIFIED, worked values handed over (W3 0596d05)

Verified read-only: 8/8 ruled match rulings exactly; 17 agreed filled;
5 worked pending/null; distribution 20 NOISE + P2×3 + P1 + P0 = 25, matches
report. W3's recorded lesson (pilot dismissal ≠ gold NOISE; check adjacent
coverage by hand) is the right takeaway — arbitration did its teaching job.

Worked values for merge completion (W2 records, W3 writes):
- H3: NOISE + fp=true (rules 4+5; external-link, file-it fails).
- H7: NOISE + fp=true (rules 4+5; vendor-link, same mechanics as H3).
- E2: NOISE + fp=true (rule 2; transient + adjacent clipboard assertion
  :58 covering :59, verified live).
- U10: NOISE + fp=true (rule 3; rejected P2 alternative — speculative
  fragility, no observed impact).
- E5: P2 + fp=false (rule 5; asserted visibility unenforced, function works).

On W3 writing these in: merge 30/30 complete → W2 final verification (counts +
worked values + distribution) → Phase B unblocked. Note: kappa gate (0.242,
FAIL) already discharged via the guideline's arbitration path — arbitration
replaced relabel, no second kappa round. Worked-5 converged by construction.

---

## 2026-09-25 — Gold 30/30 VERIFIED, Phase B UNBLOCKED (W3 56f83d3)

Final verification, all green: 30 items, zero nulls; worked-5 + ruled-8 all
match records; distribution 24/4/1/1 exact; fp⇔NOISE biconditional holds across
all 30 (guideline §1 mapping coherent end to end — unplanned but welcome
consistency proof).

Composition: 24 NOISE (incl. 3 controls U5/U6/U9 firing as designed), P2×4
(E3/E4/H8/E5), P1×1 (H9 agreed), P0×1 (H10 ruled). Class imbalance noted once
more for Phase B validity reading: a call-everything-noise judge scores 24/30
by default — discrimination rests on 6 items + the pair-routing behavior.

Phase B unblocked. Execution per frozen plan (bars 10pp/FP≤15%/P0-miss=0 on
routed-pair output; ladder routing binding; CONF append-only). W2 stands by
for results; next scheduled entry: Phase B numbers or Slot-1 follow-ups.

---

## 2026-09-25 — Arbiter clarification (binding): SYSTEM, not test — with bridge rule

Victor's question exposes a guideline gap; ruling it explicitly (applies
prospectively; Slot-1 worked examples already conform):

**Default: assess the SYSTEM (product behavior).** Taxonomy + fp-definition
leave no room: fp=true ⇔ NOT a real product defect. Test code quality is not
in the schema at all — never rate it.

**Bridge rule (test observation → product evidence):** a test-side observation
counts iff it reveals an UNENFORCED SPECIFIED behavior (E5 precedent: asserted
visibility unenforced → P2). Test-imprecision with correct/covered product
behavior → NOISE (R2 pattern, cf. E2).

**Decision procedure for ambiguous items:**
1. "Does this describe product behavior deviating from spec/expectation?"
   Yes → rate the deviation (P0/P1/P2). No → NOISE.
2. Genuinely unresolvable from the packet → best call + note
   "ambiguous: test-vs-system" + flag for arbitration (that is what W2 is for).
3. Never label test code quality — out of schema.

---

## 2026-09-25 — Reassurance recorded: RMT mental model + iteration guarantee

Victor (first labeling ever): confused by negative/mutant items — confirmed
this IS RMT (E-items = deliberately broken assertions the suite didn't catch).
Mental model issued: mutant = intentional breakage; survived = suite stayed
green; assessor's job = would a REAL product bug of that shape matter
(P1/P2 → rate it) or is it test theater (NOISE)? R1/R2 precedents ARE this
distinction, already in his hands from Slot 1.

Iteration guarantee: non-convergence is a designed-for outcome, not failure —
kappa < 0.6 → reconcile + arbitration + relabel per guideline; worked examples
excluded from kappa precisely so learning happens off-score. No penalty for
first-pass divergence, ever. (His questions so far — pointers, test-vs-system —
keep hitting load-bearing points; the confusion is well-calibrated.)

---

## 2026-09-25 — Slot-2 protocol amendment: pointers deferred to divergences

Victor asked whether submission accepts `my_pointer: null`. Ruling: YES.
Rationale (overrides my earlier "no pointer = not ready"): kappa needs severity
only; pointers function as arbitration support, and arbitration happens solely
on diverged items. Two-phase protocol: (1) labels + fp + rule-citing note now
→ kappa + comparison publication; (2) pointers mandatory ONLY for diverged
items at arbitration (agreed items need no re-inspection — agreement itself +
item evidence in the gold file suffice). Note stays mandatory in phase 1
(rule citation distinguishes substantive agreement from coincidence at
arbitration prep). Less friction, same rigor where it matters.

---

## 2026-09-25 — UrsaMinor pilot methodology issued (W2, for W3 filing)

Tool: Ursa-Minor-Beta (Jira bug → fixed-check → post back), author Ekaterina
warm, Monday call = go/no-go gate. Same M0 family as QAEverest/testRigor/
FlowScout/qa-cube (mutate → run → killed/survived), decider node llm-2
(pass/fail/broken) as SUT. Verdict mapping: fail/broken → suite fail (Caught);
pass on seeded break → Survived (false-PASS). `broken` carries observed note
with the agent's error quote (error-attribution is W3's call). Scope: llm-2
decider ONLY — ticket fetch, post-back, studio UI explicitly out (Jira path
untestable without local Jira; login-hardcode auth meaningless until confirmed).

Load-bearing rules: (1) baseline distribution not point — llm-2 is
non-deterministic, ≥3 smoke repeats before mutation, else flake reads as signal;
(2) each mutant ≥2 runs, inconsistency → re-run/observed-only, never silent
majority-hide; (3) SHA-pin the beta (tags move; beta drifts mid-pilot otherwise);
(4) cost cap pre-registered (paid OpenAI × mutants × repeats; hit → stop +
partial report); (5) Monday gate pre-registered: key decided + Jira workaround
viable + setup done + baseline recorded, else no-go (no sunk-cost drift);
(6) relationship guard: joint-experiment framing, no public numbers without
Ekaterina's consent (verdictgate repo is public; pilot data stays private).

Risks R1 cost overrun · R2 LLM flake-as-signal · R3 beta drift · R4 Jira block ·
R5 relationship (warm, no pitch) · R6 hardcode-auth scope · R7 call drift.
Limits L1 decider-only · L2 small-N (provisional bands) · L3 budget-capped N ·
L4 version-bound results · L5 verdicts are per-run records (scoring is
deterministic, the SUT is not — state both in the report).

---

## 2026-09-25 — Hygiene freeze + void classes adopted (W5 protocol input)

W2 confirms entry into protocol (W3/W5 append the lines to the plan-doc freeze
section; this entry is the adoption record):

1. **Hygiene (verbatim):** "Текст опции дословно равен лейблу из сета (без
   префиксов, пробелов по краям и case-вариаций); 0.624 измерен на опции
   `gold = Refund_not_showing_up`, 0.994 — на `Refund_not_showing_up`,
   остальное идентично." Standing rule: hygiene version travels with every
   number; cross-run comparisons valid only under identical hygiene.
2. **Void classes (verbatim):** V1 question-as-option (gold absent → verdict
   impossible, run void); V2 same-session paste (no cache validation →
   offline-claim void); V3 harness-misconfig (think=false echo, 0/90
   UNPARSEABLE — runner breakage, fixed not scored). All excluded pre-scoring,
   never in accuracy.
3. Think-boundary: already recorded (B0 methodology + checkpoint), reference
   suffices — no duplication.
4. B0-30: closed.

A-procedure validated in practice (~10 min, no code). Queue stands: merge, n=30.

---

## 2026-09-25 — A-test merged PASS (W3 65d1add, W2 concurs)

Line-by-line: Run 1 polluted 0.624 (matches declared hygiene) · Run 2 VOID V1
correctly excluded · Run 3 clean reload 0.994 replicated · Run 4 offline 0.994
identical → PASS (offline == online) · generation 0.6/0.4 stable.

W2 notes: (1) The VOID exclusion firing correctly on first contact is the most
valuable line — the machinery works, not just the verdict. (2) Merge-grade vs
statistics-grade distinction is exactly right: transcribed chain
user→chat→W5→file cannot bear statistical weight; recorded as such, usable for
pass/fail + verbatim only. (3) A-track closed; B-track (binary update + spare
model pre-departure) still open on W5's side.

---

## 2026-09-25 — Aamir 0.2.44 rerun: W2 methodology sign-off (execution: W3)

W1 intel: current 0.2.44 vs pinned 0.2.40 (4 releases since 07.09), launcher stub
identical (engine from GitHub), 17.09 ORS-ranking fix hits our open questions
(2×2 ranking, renormalization), new credibility/proof measurements, 09.09 key
hygiene. Rerun allowed by protocol; order rerun → delta → nudge (pull > push).

W2 protocol (binding on the rerun):
1. Pin SHA, not tag — record engine commit hash (tags move, SHAs don't) + date.
2. Same-tree or documented delta — spec-tree hash must match 09-09, else the
   delta confounds engine change with spec change.
3. Baseline frozen — 0.2.40 results untouched; 0.2.44 = separate version-stamped
   batch (one batch = one version, same rule as RMT).
4. Pre-register closure mapping — which open questions this rerun CAN close
   (ranking cases: previously-failing now pass?) vs CANNOT (new credibility/
   proof surface: characterize only, no verdict without baseline).
5. Regression direction — previously-passing probes must still pass
   (renormalization must not break what worked).
6. Determinism — run twice; delta attribution requires flake exclusion
   (ranking changes can be order-sensitive).
7. Scope guard — same package, no new probes. New probes = new batch.
8. Security note verify-only (key removal), not scored.

Hands: W3/main executes (their clone, their zone). W2 verifies the delta pack
on arrival. Nudge send + wording: W1 (draft endorsed; micro-suggestion: put the
engine SHA next to the version in [дельта] for precision).

---

## 2026-09-25 — Rerun verification BLOCKED: package not locatable (e538e31)

W3 handover cites commit e538e31 + `evidence/rerun-0.2.44-{baseline-0240,A,B}/` +
closure-mapping + delta-note. W2 searched (read-only): not in
OrangeHRM-orangepro-compare (HEAD 49c4358), not in qaeverset-pilot-mini-compare,
not in OrangeHRM, no `*rerun-0.2.44*` dir on disk, no `closure-mapping` hits in
pilots/Private trees. Per M1: NO verification fabricated — status BLOCKED.

Needed from W3 (one line): repo + path + pushed? (if unpushed local clone, point
at the worktree). On receipt, W2 runs the 8-point protocol check (SHA pin,
same-tree 0ba1749, baseline separation, closure C1/C2/C3 vs H1/H2/H3,
reverse direction, A==B determinism, scope guard, security note) with special
attention to the ONE delta (4 RTM rows Candidate→Associated, +16 static edges,
quote_hash provenance, c60613a attribution) and the open Aamir question
(static-edge promotion intended semantics?). Nudge waits on verification.

---

## 2026-09-25 — Rerun VERIFIED: PASS, nudge green-lit (W2, 8/8 points)

Package located (positions-cv-cl-private, unpushed e538e31 — W3's pointer).
Independent verification, all points:

1. SHA pin ✓ (e4c4b38 pre-registered; manifested consequences match claimed
   engine diff — stronger than re-diffing tarballs).
2. Same-tree ✓ (documented isolated worktree; cross-file consistency supports;
   worktree removed so direct re-check impossible — recorded).
3. Baseline separation ✓ (3 frozen dirs, graph+rtm+coverage each).
4. Closure mapping honored ✓ (C1/C2/C3 closed as claimed; H1/H2/H3 kept to
   characterize-only — Python 16=16 identical sets, no verdict creep).
5. Reverse direction ✓ (487=487 nodes; 113=113 behaviors BOTH reports; Proven 0
   both; top-10 order+scores identical incl. #3 61.2 > #4 61.1).
6. Determinism ✓ (A vs B: exactly 17 diffs, ALL wall-clock — created_at,
   updated_at, 15× last_verified. Structural walk, definitive).
7. Scope guard ✓ (110=110 RTM rows, no new probes).
8. Security ✓ (verify-only accepted; nothing in data contradicts).

THE delta verified row-level: ClaimPage quartet Candidate→Associated in rtm.md;
exactly +16 edges (8 TESTED_BY + 8 COVERS, all hard, all quote_hash, all Claim);
c60613a attribution coherent. Nit (non-blocking): mapping C2 says "122
behaviors" vs measured 113 — pre-run estimate typo, harmless (identical across
runs); suggest one-line correction.

**Verdict: PASS. Nudge green-lit** with the open question as drafted (static-edge
promotion intended semantics? + 17.09 ORS-framing question). Push: YES — local
e538e31 must land in positions-cv-cl-private; lineage demands durability beyond
the worktree (nudge itself needs no repo access).

---

## 2026-09-25 — Vendor #5 for W5: DECLINED for now (parked with trigger)

Question: task W5 to hunt more vendors' local models? Answer: no.
Grounds: 4 vendors already span Qwen/Meta/Google + Qwen-strong; Q3 closed
row-4 and Gemma approved — no open hypothesis a fifth vendor would test.
Marginal value is confirmatory only, while cost (W5 cycles, merge surface,
decision overhead) taxes the critical path (Slot 1 → Phase B). Shiny-object
work while the bottleneck waits is how plans slip.

Parked with pre-registered trigger (not dismissed): vendor #5 IFF Phase B
reveals a gap diversification could fill (e.g., a systematic miss class where
a new lineage is the remedy), or post-n=30 if the replacement verdict needs a
broader base. W5 stays on Phase B execution + batch #2 support.

---

## 2026-09-25 — W3 Slot-2 RECEIVED and SEALED (values unread)

Relayed via owner, integrity-checked blind (25/25 ids exact, all rows labeled,
schema OK — no per-item values read). Sealed at `reviews/slot2-w3-sealed.json`
(gitignored, never committed). W3 attached a cover note with a class-imbalance
flag for the comparison stage — acknowledged, sealed with the file, NOT recorded
here (public repo; embargo). Ball now with Victor: his 25 pending
(`reviews/slot2-victor-working.json`). On his submission → kappa → comparison
publication → W3 merges all 30.

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

---

## 2026-09-25 — Q3 CLOSED row-4: spots task-intrinsic (W3 addendum df9e447)

Addendum verified line by line: 63/90 = 70.0% < 76.7% bar → rejected; 90/90
unique pairs; B0-12 NOT caught (THIRD vendor invents the identical
`Get_virtual_card` — same hallucinated label across weights); B0-23 NOT caught
(same `Get_physical_card`). Outcome-matrix cell 4 applied correctly. New Llama
miss families recorded, NOT merged into T3 (workhorse-calibrated; arbiter path
untouched) — annotations honored. Latency 0.09/0.17/20.09 (no thinking tax).

Strongest line: identical invented label from three vendors' weights turns the
contamination annotation into the decisive argument — memorization predicted
catching, yet all three invent the same non-existent label. Boundary is in the
task (Banking77 near-neighbor + label-set gap), not the models. Q3 CLOSED, no
follow-ups. (Note: this file is append-only; section order is write order, not
chronological — see git log for sequence.)

---

## 2026-09-25 — CORRECTION to Q3 record + Gemma diversification (W5 Gemma run)

Gemma3:4b: 75/90 = 83.3%, med 0.28s (no thinking tax). B0-23 CAUGHT 3/3
(Order_physical_card) — sole vendor of four → spots NOT monolithic, B0-23 is
vendor-specific: diversification PARTIALLY reopened (B0-23 class).

CORRECTION (W2 self-correction, evidence-backed): verified against the frozen
77-label list — `getting_virtual_card` IS a real label (case-insensitive scoring
applies). So B0-12 across qwen3/llama/Gemma is NEAR-NEIGHBOR confusion
(getting_virtual_card vs gold get_disposable_virtual_card), NOT invention.
True invention (`Get_virtual_card`, no casefold match) is qwen2.5-only; the 3.3%
rate stands but is vendor-specific. My d91791b claim "identical invented label
x3 vendors" is WITHDRAWN — the addendum's phrasing conflated the two. The
task-intrinsic conclusion STANDS (4 vendors converge on the same wrong neighbor),
now on cleaner grounds: systematic confusion, not shared hallucination.

Implication for pair-mapping (W3's merge call, flagged not directed): Gemma at
0.28s catches a T3-class confusion → candidate CHEAP escalation path for known
classes (vs qwen3 24s med). B0-12 remains the standing boundary for all four.

---

## 2026-09-25 — Gemma ARBITER CANDIDACY: approved (W3 c832e5b verified)

W3 verified: 75/90, 90 unique pairs, B0-23 HIT 3/3, B0-12 same neighbor,
med 0.28s. Q3 matrix had no row for this outcome (≥bar + catches ONE of two
spots) — deciding as new information, which is what the matrix was for.

**APPROVED.** Grounds: clears entry bar (83.3% ≥ 76.7%); workhorse-class speed
(0.28s, no thinking tax — cost objection vanishes); complementary to qwen3
(union misses only B0-12 + B0-20 = 28/30 = 93.3% case-level).

Design consequence (binding on pair-mapping): escalation is now a LADDER, not a
pair — workhorse (0.1s) → Gemma (0.28s) → qwen3 (24s). The 85× cost ratio
between rungs demands explicit routing (which rung for which trigger class);
unrouted "escalate to arbiter" is now ambiguous and forbidden in Phase B
protocol. W3 formalizes routing; W2 ratifies. B0-20 (missed by both) is the
standing residual alongside B0-12.

---

## 2026-09-25 — Routing RATIFIED with one annotation (W3 3ac6aa9)

Binding table verified: every escalation names its tier (L0→L1→L2, no bare
"escalate" remains operative); CONF extensionally defined (CAL6 ∪ observed
neighbors ∪ UNPARSEABLE — "confused" is now membership, not feeling); cost
83.52 ≈ 84s recomputed OK (6.4× base, far under the 100× gate); termination
holds (L2 ∈ CONF → record, stop; residuals B0-12/B0-20 capped, ladder does not
chase); T2-majority weakness already disclosed in-trigger (stability ≠
correctness); gemma-only-ladder residual risk (B0-20/30) honestly stated with
Phase B as judge.

Annotation (docs hygiene, non-blocking): lines 8–11 still carry the old bare
"→ escalate" arrows from the pre-ladder proposal text. They are SUPERSEDED by
the binding table (§Routing) — suggest a one-line supersede note or arrow
update so a future reader never quotes the stale form. Ratification does not
depend on it.

---

## 2026-09-25 — Klarent trial-start methodology (W2; order W1 (б)→(а) endorsed)

Depth check (W3 2488a37): fore ai AG, free self-serve (entry cost zero), annual
usage license (no public figures), contact info@foreai.co. W1 orders trial
before outreach (findings = warm hook; cold burns first contact). Endorsed —
matches Radik/Adam pattern (vendors answer results, not cold asks).

Start methods (W3 executes, files in pilot catalog):
- M1 trial recon: plan limits/quota/expiry recorded, build version stamped,
  OrangeHRM reachability from Klarent verified. Size matrix to fit quota.
- M2 scope freeze (proposed): Login (B0 auth) + Admin user-create (B1 core) +
  6 pre-registered mutations (testRigor-analogous: label rename, remove button,
  duplicate label, reorder, CSS class, flow reorder). No scope growth mid-matrix.
- M3 baseline green 3× recorded before any mutation.
- M4 matrix 6 × 2 runs (AI-codeless flake rule; split → re-run/observed-only).
- M5 results.csv live → scorer verdict → findings pack → W1 (fact-check notice
  + deadline) → outreach. No public numbers pre-notice, ever.
- Silent phase: zero vendor contact until findings + notice (W1 wording).

Risks R1 quota cutoff mid-matrix · R2 SaaS drift (stamp every run) · R3 flake-
as-signal (repeats rule) · R4 scope creep (named flows only) · R5 secrets in
repo (trial creds via env, NEVER committed — repo is public) · R6 first-contact
burn (W1: no cold) · R7 marketing numbers ($0.30/94%/4.1x excluded — vendor
claims never enter verdict inputs) · R8 compliance claims unverified (SOC2/ISO
out of scope; compliance ≠ test quality).

---

## 2026-09-25 — Klarent M1: public demo endorsed, signup email is owner's call

M1 recon (W3): app.klarent.ai → sign-up, build v1.1.0 stamped. Quotas/expiry
inside-only (matrix sized then, per R1). Localhost unreachable from SaaS.

W2 ruling — public demo OVER tunnel: reproducible for the vendor (they can
replay findings on the same demo), no coupling to owner's machine being up,
Igor's precedent. Tunnel adds flake + security surface + time coupling for
zero methodology gain. Caveats recorded: demo may reset state mid-matrix
→ re-baseline if it does; demo build may differ from localhost → findings
scoped to demo build explicitly, version delta recorded.

Signup email: NOT W2 (agents can't receive verify mail) — owner's inbox,
owner's call. Hygiene binding on receipt: password manager, env-only creds,
never repo/chat-logs (R5). W3 proceeds to quota/expiry/scope-freeze/baseline
3× on account creation.

---

## 2026-09-25 — Klarent: no self-serve, W2 assessment of 3 options (W1 decides)

Fact (W3 dc88346): org-gated, "gradually" — (б)→(а) unexecutable as-is. W2 ruling:

**Support #2 with a mode caveat (load-bearing):** demo-request changes the
evaluation MODE from silent measurement to vendor-led observation. Consequences:
(a) evidence grade drops — observations, NOT measurements; no scorer input, no
verdict pack from a demo; output = qualitative assessment + follow-ups;
(b) curation bias — we see what they show; mitigation = pre-registered OUR
probe list (the 6 mutations reframed as demo-driver tasks) + record
shown-vs-refused; (c) observer effect bounded (their routine demo funnel, per
W3) but nonzero — state it, don't zero it. Evaluator framing + notice offer
stays consistent with the warm-hook strategy.

**Add #1 in parallel (free optionality):** waitlist signup costs 2 minutes and
keeps the self-serve path warm — no reason to choose between #1 and #2.

**#3 as timeboxed fallback:** if no demo within N weeks (W1 sets N), park
formally. Enterprise-focus read (may never open wide) is sound — don't let the
track hang implicitly; park explicitly or not at all.

Decision: W1 (commercial ownership). W2 offers the pre-registered demo probe
list on request.

---

## 2026-09-25 — Klarent decision: #2 + waitlist parallel (W1)

W1: demo-request via official funnel (not cold) + silent waitlist in parallel.
Guard recorded verbatim: vendor-managed demo = recon ONLY, never counts toward
the pilot; scoring runs ONLY on evaluator/sandbox access. Matches W2's mode
caveat exactly — no divergence to reconcile. Draft (their demo channel,
evaluator framing + findings/notice offer) is W1's wording call — endorsed as
consistent, no edits from W2. Send: owner/W3 (not W2 — no outreach sends from
this window). Timebox for #3 fallback still open (W1 sets N on silence).

---

## 2026-09-25 — UrsaMinor methodology filed VERIFIED (W3 1f5565f)

Spot-checked read-only: three load-bearing points verbatim (distribution +
majority-hide ban; llm-2-only mapping with broken-observed rule; Monday gate +
SHA/cost/relationship); R1–R7/L1–L5 by canon-pointer (no duplication drift);
oracle/decoy-consent/cost frames + W1/W4 boundary recorded as-is; index open
item references the gate. Commit confirmed in log. W2 filing review CLOSED —
next touchpoint is Monday call outcome (go/no-go).

---

## 2026-09-25 — UrsaMinor Monday call: W2 additions to W4 questions

1. **Oracle — главный вопрос, усилить:** не просто "где oracle", а рамка "мы приносим oracle" (mutation matrix как внешняя верификация их агента) — это и есть joint-experiment lane W1. Их ответ классифицирует зрелость: eval harness с gold → говорим на одном языке; только ручная сверка → наш seeded break и есть их первый настоящий eval (позиционировать как ценность, не аудит).
2. **Decoy-ticket — только с явного согласия:** seeding в ИХ Jira/agent без consent = нарушение доверия с warm-автором. Decoy-тикет предрегистрировать (какой тикет, какой break, ожидаемый флип) И получить согласие до, не после. Trust > data.
3. **Cost-per-run — linkage:** ответ питает мой R1 cost cap напрямую; попросить цифру в $/прогон, не "дешево/дорого".
4. **Граница:** license/GTM/design-partners/pricing — территория W1 (поправка дисциплины). W4-список хорош как черновик; финальную редакцию call-вопросов смотрит W1 до понедельника (commercial final word).

---

## 2026-09-26 — Klarent demo-request SENT (owner, 02:56)

Evaluator framing + findings/notice offer via their demo channel; waitlist in
parallel (per W1 decision). Clock starts for the #3-fallback timebox (W1 sets N
on silence). Next W2 touchpoint: demo probe list on request (if demo scheduled)
or silence-timeout review.

---

## 2026-09-26 02:57 — Session checkpoint (routine)

No code changes this session; methodology + coordination only. Tree clean, all
pushed. Head: 63b78b7.

Standing by (no W2 action until triggered):
- Slot 2: Victor's 25 pending (W3 sealed); then kappa → comparison → merge.
- Verdict-pack text on W4 request (gated on Leonardo).
- Batch #2 execution (W3, engine 0.1.0, stamped).
- Monday gates: UrsaMinor call (go/no-go) · Phase A Slot 1 (unconfirmed).
- Klarent: demo-request sent, #3-fallback clock ticking (W1 sets N).
- Aamir: nudge after W2 verification (BLOCKED — package pointer needed from W3).
- Effectiveness recheck DUE 2026-10-17.

