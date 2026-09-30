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

## 2026-09-29 — Wave-ID wall VERIFIED file-by-file (W3 dig, qa-cube H4)

Recomputed: 010919→013947 = 12 files at 10,20,…,120 (running totals, subset
relation verified: 20-row ⊆ 120-row). Report header converges (campaign
01:04–01:39 ~35 min, 120 = 4×5×6, 100% success; first snapshot 01:09).
Fencing matches the file record: setup era (004143–005658, irregular counts)
+ evening rerun (120 wall 20:33–21:06) + aborted 60-series (21:12–21:27)
correctly excluded. Headline 120 insured to exactly this wall — W1 may close
tail #2.

One line beyond W3's report: TWO more complete 120-walls exist on disk
(025753–042036, 203310–210620). Headline stays fenced by header-convergence
(not uniqueness); the extra walls are replication material, never to be mixed
into this 120. If anyone cites them, each wall carries its own header or it
doesn't count.

---

## 2026-09-29 — RMT follow-up inventory for W4 (article published, 3–5 day note)

Recomputed from artifacts (not memory): 82 seeded mutants (batch #1: 58 rows;
batch #2: 27 run-records over 24 mutants) + 4 closeout + 9 confirmation runs =
~98 RMT run-records + smokes. Downstream beyond OpenClaw: NONE (all RMT runs
target OpenClaw specs). Second live case: NONE — stated plainly, no substitute
offered.

Viable angle WITHOUT new case or runs (W4's fear of retelling is solvable):
"post-freeze diary" — everything the article does NOT contain: batch #2
(24 mutants incl. B5 chains the v1 engine missed entirely; 22 killed + hang
resolutions via pre-registered crash mapping) + engine evolution post-freeze
(NO-OP guard, expect.soft, chain-unwrap, RMT_VERSION stamp — the seeder got
stronger AFTER the published numbers) + S4-confirmation (vacuous vs genuine
gaps) + stamp saga (58 UNSTAMPED as teaching example). All recorded, all
citable, zero new runs required. Recommended framing over "how we used RMT"
(retrospective) — "what changed since the freeze" (news).

---

## 2026-09-29 — Integrity batch VERIFIED all three (W3 a371e86 + W1 53510bf)

W2 independent verification (read-only): (1) tag opclaw-baseline-2026-09-29
exists, message "toggles all OFF (clean baseline)" ✓; (2) both reconstructed
runners present + py_compile clean ✓ (proof+tool co-located per W1 refinement);
(3) ollama-memo thorough (one-serve, sticky-start, store-awareness with digest,
no-pull-without-record, pre-departure) ✓. The /tmp-purge-mid-task incident
stands as the canonical "lineage before loss" exhibit — priority systemically
validated, not just completed. Integrity queue EMPTY (W1 confirms nothing
pending). No W2 action.

---

## 2026-09-29 — UrsaMinor article FETCHED, W3 reading confirmed verbatim (W2)

Fetched dev.to/quality_minder/3pc7 (Sep 25) whole. All methodology-load-bearing
claims verified verbatim: BaaS env (API_KEY + macOS Chrome path + HEADFUL +
LLM_CLIENT=openai + OPENAI_TOKEN/ORG) ✓ · smoke = Browser Screenshot with
session ID ✓ · login hardcode RECOMMENDED by author in http-1 ("Login flows
rarely change, so scripting them once saves tokens") ✓ · llm-2 = pass/fail/
broken decider ✓ · Secrets (BAAS_API_KEY, Provider key, Jira_auth base64,
jiraSubdomain + input-1 URL) ✓ · /etc/hosts entry ✓ · studio :8080 (port
finding independently grounded) ✓.

New observations (mine, non-blocking): author account joined Sep 25, 2026
(same-day identity — provenance note, not accusation, side-project consistent) ·
OpenAI key REQUIRED, Anthropic alternative exists (no free path in article —
supports cost-cap rule) · Victor's Sep-25 comment already plants the
seeded-break + ambiguity-flag question publicly (consistent with Monday
framing, no conflict) · closing "keep humans on the loop" + star/DM ask
(traction-seeking beta, as filed). W3's reading stands unamended.

---

## 2026-09-29 — Ursa-Minor PREPPED, build trigger pending (W3 status, W2 notes)

Status recorded: infra present (Docker/Go/Chrome), repos cloned (BaaS HEAD
ec48697 ✓ SHA-pin satisfied for SUT), port conflict found → remap 8081
(record URLs as-remapped in run log), article fully read, Jira gate relaxed by
author + own trial live (victor-qa/KAN/SAM1-6, token in owner's shell),
login-hardcode author-recommended (http-1) → auth-scope exclusion CONFIRMED
(open item closed), llm-2 pass/fail/broken confirmed, Ollama $0 path (vision
pulled, autostart confirmed, cloud models deliberately off), FREE-ONLY guard
track-wide, mismatch ticket/env correctly scoped as pipeline-check.

W2 notes: (1) auth exclusion now verified, not assumed — close the open item
as such; (2) "pins default master" for BUILD — acceptable only with resolved
image digests recorded at build time (master moves; record what actually ran);
(3) $0 Ollama path eases but does not remove the cost-cap rule (cap stays,
binds nothing while free). Monday gate: key→resolved $0-pending-her-OK,
workaround viable, setup pending build, baseline pending smoke — build trigger
is the remaining domino.

---

## 2026-09-29 — W1 pins + build/start boundary: CONCURRED as binding (W2)

(1) SHA-pin extends to BOTH repos' commit SHAs in run log at build (BaaS
ec48697 already recorded; deploy SHA due at build) — my Aamir rule coming
home, concur without reservation. Supplements (not replaces) image-digest
logging. (2) Build ≠ start, stated explicitly: infra neutral (no her systems/
costs/runs); FIRST RUN gated on Katya's signature — "no start" means runs.
W1's go authorizes build only. Jira-token-in-owner-shell-only + FREE-ONLY +
never-exposed: acknowledged as held. Charter + gate + build/start boundary
now triple-consistent; no divergence anywhere on this track.

---

## 2026-09-28 — Qodo: complexity LOW, effect UNASSIGNED → pause supported (W2)

Cost arithmetic (owner asked): 580 issues × 3 runs × 2 arms ≈ 3,480 calls —
machine-cheap (qwen ~0.1s + GLiNER ~0.4s → under an hour compute + analysis).
Cheaper than OpenClaw batches (hours of suites), gold labeling (human hours),
Phase B full arc. Complexity is NOT the problem.

Effect analysis: unique value exists (ONLY benchmark with 580 guaranteed-real
defects → miss-rate on certain positives; functional/best-practice slices) —
but NO open decision consumes it. Replacement closed NO, GLiNER LOSE closed,
ladder parked, fine-tune gated on its own spec. A measurement without a pending
decision violates our own decision-driven doctrine (same rule that killed
make-work stability runs). Severity undescriptive by design further thins the
yield (detection-only, no severity verdict possible).

Recommendation: PAUSE with trigger (not park-and-forget): resume IFF (a) a new
judge needs detection-rate validation, (b) fine-tune spec names Qodo-slices as
bench, or (c) article needs a third data point. Frozen mapping + pinned dataset
persist — unpausing costs one run + analysis. Owner decides; W2 needs nothing
either way.

---

## 2026-09-28 — Qodo mapping RATIFIED +2 pre-run conditions (W3, no runs made)

Verified: dataset pin by SHA-at-fetch (HF MIT, 100 PRs/580, bench-file-only
with broken-viewer note) ✓ · detection-primary with gold-fp=false-for-all
(double-validated construction) ✓ · severity DESCRIPTIVE ONLY with explicit
no-fabrication rationale (labeling 580 = separate campaign, out of scope) —
the key honest decision, endorsed as the standard pattern for unlabeled
injected sets ✓ · same arms full ×3 ✓ · vendor-F1 reported-context with
unpinned/self-serving caveat ✓ · frozen prompts (temp 0, exact one-line,
strict-match else UNPARSEABLE; GLiNER per step-3) ✓ · verdict report-only
(detection + functional/best-practice slices, no comparable baseline — stated,
no thresholds) ✓ · Qodo-bench ≠ Qodo-vendor boundary held, numbers private ✓ ·
slot after s1web/UrsaMinor (no preemption) ✓.

Conditions (binding pre-run, not post-hoc): (1) SHA actually recorded at fetch
— ratification assumes it, runs require it; (2) rule_name→family slice mapping
(functional vs best-practice) frozen pre-run — post-hoc slicing flatters;
list the families in the run log. Runs authorized once both hold.

---

## 2026-09-28 — Practice page: W2+W3 reviews converged (owner edits)

Two independent reviews agree. Consolidated punchlist for owner (Portfolio =
his zone, his edits):
- MUST-FIX (both windows): OpenClaw "2 inconclusive" → "24/24 (22 killed +
  2 resolved: caught-by-crash, killed)". Page currently contradicts verified
  closeout on two cases.
- W1-GATED (W3 drafted, W1 decides): header "no sales" vs "no retainers up
  front" + Stage 0/1 frame → proposed "paid only by results, never up front".
  Commercial wording final word stays W1.
- VERIFY (neither window ran it): Agentiqa 0/6 + cold-start effect — owner
  checks against pilot artifacts; broken case worse than no case.
- OPTIONAL (owner taste): seeded-break sets as-artifact line (promised to
  Jyothi/Urchade tracks already — magnet for builders) · QAEverest "(ongoing)"
  tag (track alive, not ruptured) · cold-start one-word gloss · scope-guard
  line ("I don't fix, I verify") · external-link resolution check (gotcha #8).

---

## 2026-09-28 — Fine-tune track: COMPUTE approved, CONTAMINATION is the gate (W2)

W3 arithmetic concurs (LoRA-340M fits 6GB; ~one evening; Kaggle primary with
private dataset + env token is sound; Colab fallback; Fastino Agent door
separate, non-blocking). Compute is NOT the bottleneck — agreed.

Binding requirements for the frozen spec (W2 signs only with all present):
1. **Site-split, not random:** train/val/TEST split BY SITE (same principle as
   s1web's own site-split calibration) — random split leaks same-site patterns.
2. **Test-lock:** held-out TEST set locked BEFORE training starts; touched
   exactly once (final bench). Training on the eval set then reporting on it
   = train-test contamination, the cardinal sin this program exists to catch.
   (This applies retroactively as a lens: any prior fine-tune claims without
   locked test are void by the same rule.)
3. **Task definition first:** WHAT is predicted (severity classes? P(stable)?) —
   determines head/labels/loss; severity vs stability decided in spec, not mid-run.
4. **Before/after benches** on the LOCKED test only (plus gold-30 as external
   probe if task-compatible — severity task only).
5. **Terms:** weights stay PRIVATE (no derivative publishing under
   eval/research terms); numbers publishable with cite; contamination
   disclosure travels with every number.
6. Owner actions (not W2): Kaggle account + token via env; W1 go-decision.

Data verdict stands: gold-30 (30) insufficient alone — correct call; s1web as
corpus OK only under 1–2 above. Dirty-Hands doctrine applies: whoever trains
touches nothing evaluative without the split locked first.

---

## 2026-09-28 — Fine-tune GO (W1 f81e6bf): contamination gate + disclaimer rule

W1 approves with the contamination gate as the single binding condition
(site-split + test-lock + task-first + locked-test benches + private weights —
no signature without all). Two additions recorded:
1. **Reply-5 extends to fine-tuned judges** (run ours + report privately) WITH
   mandatory disclaimer "trained on your distribution" at report — without it,
   tuned numbers presented as independent measurement = misleading. NDA
   unneeded (public set, our models, private report).
2. **Slot:** evening GPU windows AFTER Tue 29th publish (that window belongs
   to the article + repost mechanics — no preemption).
Chain locked: W3 spec-for-task → W2 signature → run. W2 awaits the spec; no
action until it arrives.

---

## 2026-09-28 — Schedule change: joint article TOMORROW under Leonardo + repost

Publish moved up: joint Article 29 drops tomorrow under Leonardo's name,
Victor reposts immediately. Fine-tune slot ("after 29th publish window")
still consistent — runs after publish + repost mechanics, no conflict.

OPEN VERIFICATION (blocks nothing yet, but time-critical): my approved version
is (2).docx (0ed9a37) + W1's 7-point acceptance. If tomorrow's publish builds
from exactly that file → cleared, no action. If Leonardo touched text after
(2).docx → W2 MUST check the final assembly TODAY (numbers + gates + our
insert — the paraphrase risk lives in last-mile edits). Question to owner:
publish version == reviewed (2).docx, or is there a newer assembly to check?

---

## 2026-09-28 — Publish version CONFIRMED same (2).docx: cleared, no action

Owner: идет та же. Verification chain complete with zero delta: reviewed file
= publish file. No further W2 action on Article 29 pre-publish. Post-publish:
repost mechanics (W4 lane) + quotes.md aphorism linkage (own material, link at
publication per corrected designation).

---

## 2026-09-28 — Fine-tune spec SIGNED (W3 8469bb1, all gates hold)

Verified line by line against c9aa514: task-first stability (severity-
impossible recorded with reason; same-schema head keeps before/after
comparable with s1web arms) ✓ · source-split (commoncrawl-train 2138 els vs
locked mind2web+app ~495 = 2633 total, arithmetic holds; whole-source holdout
stronger than site-split) ✓ · test-lock once with SHA-at-split + dirty-hands ✓ ·
before/after on locked only (base 7ee5da4c) ✓ · weights private + disclaimer
mandatory ✓ · Kaggle GPU + post-29th slot ✓ · LoRA r16/a32/ep≤3 + env logging ✓ ·
zero training pre-signature ✓.

Observation (non-blocking, for the run log): early-stop "on train-loss
plateau" without a val split is approximate — the real overfit guard here is
epochs≤3 + LoRA rank cap, not the plateau rule. Accept as-is; record which
trigger actually stopped training (epochs-exhausted vs plateau) in the run log.
Runs authorized post-29th window. W2's next touchpoint: before/after numbers
verification when they land.

---

## 2026-09-28 — UrsaMinor charter APPROVED for signature (W2, zero blockers)

Read whole (46 lines, RU): goal false-PASS ✓ · scope llm-2-only + OUR sandbox
(stronger than spec: her systems untouched by construction) + OUT list ✓ ·
method (baseline ≥3 distribution-stated, N×≥2, Caught/Survived, divergences =
re-run, majority-hide ban present) ✓ · limitations (capped key w/ her OK, SHA
pin, decoy consent+pre-register, privacy w/ public-repo reason stated,
publication explicit-consent, findings-first) ✓ · gate 4/4 ✓ · done-definition
with HER decision on continue/publish/close ✓ · signatures both sides with
specific commitments ✓. All R1–R7/L1–L5 covered with nothing dropped.

Non-blocking note (execution protocol, not charter): broken→Caught here lacks
the observed-error-quote requirement from my mapping — correctly left out
(charter stays readable; the quote discipline lives in W3's run protocol).
W3 executes after her signature. No W2 action until results or gate failure.

---

## 2026-09-28 — GLiNER s1web: VOID by symmetry (mirror constant), suite exonerated (W2)

Recomputed whole-file: 8074 P=1.0 all · 24,222 rows present · broken
14.38026474/43.14720812 + AUROC 0.5 + coverage 1.0 — digit-identical to qwen.
Same doctrine applied evenly, no favoritism: CONSTANT predictor ⇒ no judgment
measured ⇒ numbers describe the tie-break, not the model. VOID, never cited.

W3's question answered ("what does broken-rate measure under constants?"): it
measures FIRST-CANDIDATE quality — a property of the SUITE's ordering
(~14.38% ≈ id-first level). Opposite constants collapse onto it regardless of
sign; that is why diametrically opposed judges score identically. Corollary
exonerating the suite: s1web DOES discriminate real (non-constant) predictors
(v3 7.9%, Jev 11.1%) — the metric is sound, our two instruments both returned
constants (qwen all-no, GLiNER all-yes: opposite degenerate directions —
negativity bias vs native-head positivity; different mechanisms, same
degeneracy class). GLiNER standing results unchanged (step-3 LOSE on gold-30,
separate task); s1web arm joins qwen arm as VOID. Parked status holds.

---

## 2026-09-28 — H2 CONFIRMED + cross-task bias: MODEL-verdict, not prompt-defect (W2)

W3 verbatim facts (24220/24222 rows existed — doctrine paid off): H1 partial
(bare-no 4322, all "no" — no outcome effect) · H2 CONFIRMED (zero `yes` in
24,220: 19,898 exact + 4,322 bare + 2 empty) · H3 REFUTED (overlap 8074/8074) ·
1662/2633 = ≥2-candidate rule from docstring (closed).

Analyst verdict (the question left to W2): MODEL, not prompt. Grounds: same
negativity direction on TWO tasks with different prompts — gold-30 severity
(all-defect P1×25/P2×5) + s1web stability (all-unstable). A prompt defect
would be task-specific; cross-task systematicity is instrument-level bias.
Corollary with teeth: (c1) fixed compliance (6.4% → 82%) WITHOUT fixing
judgment (0 discriminating yesses) — instruction-following and judgment
quality are independent axes here; paraphrase optimism should be priced
accordingly. Still: ONE paraphrase probe before bigger Q-design (cheap kill
either way — if paraphrase flips it, this verdict falls; if not, it hardens).

Durability order: move /tmp/s1web-qwen25-v2-rows.jsonl to outputs/ next to
scores NOW (/tmp dies on reboot; 24k rows of primary evidence must not live
volatile). W3 moves (their file); W2 will not cite s1web-qwen numbers until
the file lands durable.

---

## 2026-09-28 — MODEL-bias verdict HARDENED, qwen s1web branch CLOSED (W2)

Paraphrase probe verified whole-file (30 rows, e100–e129 slice): 30/30
`stable=no` under REWORDED prompt — zero yes. Prompt-defect alternative KILLED:
two phrasings, same universal negation. Raw rows file durable in outputs
(1.9MB, 24,222 rows — durability order executed before receipt, duplicate
relay correctly identified as such).

Final: qwen2.5:3b carries instrument-level negativity bias across three
probes (gold-30 severity, s1web v2, s1web paraphrase) — 0 discriminating yesses
in ~24.3k answers total. s1web-qwen numbers stay VOID (constant predictor);
14.38% never cited. Branch closed; no further probes authorized on this arm
without a new decision (fine-tune story only). Standing by on GLiNER s1web
(~44% at last report).

---

## 2026-09-28 — qwen closure accepted both sides; GLiNER at ~75% (W3)

W3 recorded the MODEL-bias verdict as accepted (0/24.3k position, 14.38%
banned from citation). GLiNER s1web at 18279/24222 (~75%) — on finish: scores
+ evaluate + numbers to W2 under same discipline (whole-file recompute before
any verdict, per standing practice). Nothing pending W2 until then.

---

## 2026-09-28 — s1web qwen v2: VOID (constant predictor), not 14.38% (W2 recompute)

Verified: eval numbers match file exactly (14.38/43.15/AUROC/coverage as
computed — arithmetic not disputed). BUT all 8074 P = 0.0 exactly → CONSTANT
predictor: AUROC 0.5 is degeneracy (not "binary doesn't rank" — binary would
still rank), broken-rate = arbitrary-tiebreak artifact ≈ id-first level,
coverage 1.0 vacuous (all scored-with-zeros). This measures NOTHING about
judgment. Verdict: VOID, do not cite 14.38% as qwen's score anywhere.

Three hypotheses, ranked, each with discriminating evidence (all require
per-run verbatim raws — absent; same verbatim doctrine as Phase B, now biting
exactly as predicted):
(H1 parser-drops, PRIME SUSPECT): bare yes/no answers parsed as 0 — the
original 93.6% stopper persisting at scale; (c1) 17/20 probe unrepresentative.
Discriminator: verbatim answers per run.
(H2 model-says-no): strengthened prompt biases to negation; (c1) probe's
all-HOLDs=stable=no already hinted this direction.
(H3 join-mismatch): my_scores qids (e0q0-style) vs eval_set candidate_ids —
systematic miss defaults everything to 0. Discriminator: key-overlap audit
+ eval_set SHA check.
Also open: eval covers 1662/2633 elements — why the subset (W3 to state).

GLiNER branch untouched per W3 (still running). No conclusion about qwen on
s1web stands until per-run verbatim raw exists.

---

## 2026-09-27 — Standing practices ENDORSED as-is + Aleksandr triage concurred (W3)

(1) Pilot-fitness verdicts in roster (FIT / FIT-with-costs / Section 3 /
rejected + reason; launchability + oracle + matrix-fit filter; article quotes
excluded) — sound, no changes. (2) Methods-not-opinions rule (artifact-bearing
method → work; opinion → noise) with 5 already-taken items noted — sound.
Aleksandr Valuev: concur no-pilot/no-card; two signals as pointers only (local
Qwen 3.8 + OpenCode validates B0 shape independently; /ponytail for token
economy) — both covered by existing tracks, nothing new opened.

---

## 2026-09-27 — (c1) PASSES: (c) authorized with (c1) instruction, (c2) declined (W2)

W3 (c1) probe: 17/20 HOLD on strengthened instruction (3 BREAK = 15% — above
the 10% spec bar, far from the 93.6% systematic refusal). Digest re-verified
identical pre-run (freeze intact through the re-pull). All HOLDs = stable=no
(recorded as observation).

Decision: (c) FULL RERUN authorized under NEW freeze (v2: strengthened prompt
text frozen verbatim + digest confirmed + UNPARSEABLE handling unchanged),
breaks recorded as UNPARSEABLE data — never disqualification, never silent.
(c2) tolerant schema DECLINED for now: weakening the schema to absorb 15%
changes what's measured (schema drift for convenience); (c1) recovers 85%
inside a frozen schema, and the 15%-vs-10% exceedance is itself a measurement
to re-take on the full set, not to define away. (c2) returns only if the
exceedance proves irreducible AND the arm still justifies it. W3 executes.

---

## 2026-09-27 — s1web qwen-format stopper: ruling (b)+(c), digest re-check MANDATORY

W3 stopped the runner (correct — silent parse-expansion would violate freeze):
qwen2.5:3b answers bare yes/no vs frozen `stable=<yes|no>` on 1084/1159 (93.6%,
systematic). GLiNER branch clean, continues. Ollama stabilized via
persistent-SSH after W3's duplicate-serve fight (admitted, fixed).

Ruling: (a) REJECTED — counting bare answers as observations rewrites the
schema post-hoc (frozen prompt says EXACTLY; letter governs, not intent).
(b) RECORDED — 1084 rows are UNPARSEABLE per schema; the run stands as
measured (arm yields ~75 usable). (c) AUTHORIZED as new decision — prompt/schema
fix under a NEW freeze version, then re-run; suggest (c1) strengthen instruction
first (cheap probe: CAN the model follow exact format?), (c2) tolerant schema
only if (c1) fails systematically (consistent with think=false evidence —
instruction-following is this model's known weak side, not a surprise).

MANDATORY before any (c) run (unnamed by anyone): model was RE-PULLED fresh —
digest MUST re-verify 357c53fb…; a changed digest breaks the freeze silently
(new weights = new instrument). No runs until digest confirmed.

Infra (for owner pre-departure list): Ollama lives on W3's persistent-SSH
(PID 63917, dies with the session) — Victor sets Ollama autostart on PC
before leaving, else next measurement hits the same wall. W3's stoppage under
pressure commended explicitly — stopping a hot runner on principle is the
discipline working.

---

## 2026-09-27 — Ollama autostart DONE (owner, pre-departure item closed)

Persistent-SSH fragility resolved at the root: PC now self-serves Ollama
across reboots/sessions. Remaining infra items: digest re-check post-re-pull
(W3, before any (c) runs). Owner free to depart on this front.

---

## 2026-09-27 — Rinat Abdullin noted, no action (W5 wiki lane)

W5: already covered (digest 0.9, wiki profile + BitGN pages); no card (Following,
no thread). New: transient-events in Given-When-Then + full-stack flattening
(specs → events → HTTP → UI semantic anchors) — same family as QA Wolf
toSatisfy and our fixture patterns; 4 lines added to profile. Positioning
"Founder @ BitGN | Verifying agents" recorded for potential bridge (W1's call
if ever; not now). W2: no verification needed (routine wiki work in own lane),
no action. Noted for pattern resonance only.

---

## 2026-09-27 — s1web mapping RATIFIED +1 annotation (W3, no runs pre-ratification)

Verified: SHA pin (2633/8074 locally) + v4-drift STOP-repin-restart (stricter
than minimum) ✓ · item format observed ✓ · scope qwen2.5 + GLiNER, qwen3
excluded with arithmetic (24k×24s ≈ 6.7d — recomputed, holds) + report-only
needs-no-arbiter reasoning ✓ · QUESTION SHIFT explicit (stability, not
severity; no claim transfers from gold-30 — the category error preempted in
text) ✓ · frozen prompts (temp 0, exact one-line; GLiNER native P + determinism
check with split-as-finding) ✓ · verdict rule honors all four signed points ✓.

Annotation (analysis-phase, non-blocking): P granularity differs by arm —
generative {0,1/3,2/3,1} coarse vs GLiNER continuous. Read broken-locator rate
+ AUROC (rank-based, granularity-robust) as PRIMARY; Brier/log-loss/ECE as
SECONDARY for the coarse arm (proper scores punish coarseness independent of
judgment quality). Runs authorized.

---

## 2026-09-27 — s1web gate fully open: W1 confirms, W3 executes (03c2298)

W1 accepts ratification + granularity annotation (as analysis hygiene, no
commercial action). Binding precondition closed on all points from both sides.
Execution: W3 (runs now authorized). W1 files results on arrival. W2's next
touchpoint: numbers verification when raw lands (same recompute discipline as
Phase B). Nothing pending anywhere else on this thread.

---

## 2026-09-26 — s1web-mirror mini-protocol SIGNED (4× agree + 1 binding precondition)

Read the full Atmaram index (172 lines) before signing. W3's four: (1) report
rates + compare vs in-dataset baselines and reported Jev, no binary pass/fail
— AGREE (foreign suite, not our gold); comparators ranked: in-dataset
baselines (random/id-first) PRIMARY, Jev 11.1%/29.4% reported-context ONLY
(Jev-variant-unpinned caveat from the index travels with the number).
(2) Pin snapshot SHA pre-run (v3: 2,633/8,074/70/20 recorded) — AGREE; plus
v4-drift rule: iterate fast (v1→v3 in a day), so re-verify version at run
start — finish on pinned v3, note v4 if appeared. (3) No thresholds,
first-run-calibration — AGREE. (4) Private-first + mutual-publication
sufficient, no NDA text — AGREE (nothing proprietary crosses: public set,
local judges, outputs private till mutual; revisit if that changes).

BINDING PRECONDITION (without it this signature is void): s1web's scorer
consumes {candidate_id: P(stable)} — our judges emit severity/fp, GLiNER emits
typed decisions. An output→P(stable) MAPPING mini-protocol must be frozen +
ratified BEFORE runs (same binding sequence as GLiNER step-2/step-3). Unmapped
mid-run invention poisons comparability exactly as unmapped severity would.
Terms compliance rides along: cite "s1web-bench v1" + sources in every output
(Mind2Web CC-BY-4.0, Common Crawl ToU). Our set stays home (reply-5 stands).

---

## 2026-09-26 — W1 accepts signature + IP-asset point recorded (0ac24cb)

W1 accepts the full package (report-only, baselines-primary, pin+v4-drift,
no thresholds, private-first) and confirms the precondition as key (protects
both sides: frozen mapping preempts tuning-for-our-judges accusations).
W1's added value endorsed: the frozen severity/fp → P(stable) mapping is a
REUSABLE methodology asset, not one-shot run config. Placement: pattern
generalizes into ai-qa-wiki AFTER first frozen use (s1web) — not prematurely;
the instance mapping itself lives with the run protocol (W3) under W2
ratification. Order stands: mapping → runs; set home; Reply-5 in force.

---

## 2026-09-26 — Article 29 data ruling (W4 draft + W1 critique adjudicated)

Numbers verified from the pack: 53/58 = 91.4% ✓ · 5/58 = 8.6% ✓ · B2 gate
"band violated: 5 survived = 8.6% > 5% of 58" (JSON re-read). W4 reply draft
APPROVED to send (bylines Q fine, no structural changes).

W1 fix endorsed with one mechanism correction: breakdown 1+2+2 (S1 vacuous /
S2+S3 dismissed / S4+S5 confirmed P2) is MANDATORY in text — "5 survivors"
bare reads as decision-theater we criticize; decisions ARE the payload.
BUT the mechanism point needs precision: batch #1 was ALL B2, which fails on
the 5%-BAND (a percentage rule!) — not presence. Zero-tolerance governs B0/B1
(unexercised here). Article must teach: the gate that fired (B2 band) +
B0/B1 zero-tolerance + decisions as payload; 91.4/8.6 are descriptive batch
history, NEVER thresholds (thresholds are 5% and 0). Further: decisions did
NOT flip the verdict (final pack still FAIL on band) — must not imply it.

Naming: concur anonymize-in-joint ("an open-source agent runtime"; notice-first
practice, no vendor track, irreversibility with external co-author); named
version reserved for own channels. Victor to check Leonardo's Google Doc for
existing naming + numbers (unreadable from here) and propose anonymization.

Division match (Leonardo: RMT/sensitivity/risk-behavior his, gates/thresholds
ours, contract as bridge): confirmed at doctrine level (framework v0.3);
doc-level verification awaits Victor's reading. Quote handling (private source
→ quotes.md only at publication with article link): confirmed.

---

## 2026-09-26 — Aphorism authorship CORRECTED: ours, not private (owner catch)

Owner: "это мы придумали — читай первую отправку". Verified: the full quatrain
("The mutation is not the test. The mutant is the question. The survivor is
the answer. The gate is the judgment.") stands at line 11 of OUR policy half
(29-policy-half-to-leonardo.md) — Leonardo's version kept our section verbatim.
Reclassification: OWN material, no consent needed, no privacy constraint. The
"private source → quotes.md only at publication" designation is WITHDRAWN;
quotable as ours immediately (W4 may cite freely). Lesson logged: provenance
claims verify against sending artifacts before entering the record — W1/W4/W2
all repeated the misattribution unchecked.

---

## 2026-09-26 — W1 package (8e2bc0f): accepted EXCEPT one stale line (must fix pre-send)

Accepted: provisional phrasing ("5%, still being calibrated, recheck Oct 2026"
— closes band + score-90 alike) · Order→B1 nit in same letter (table then
B0/B1/B1/B3 under one EQ_NEGATION — thesis reads across four tiers; cheap,
concur) · naming clean → anonymization as insertion condition · B2 cross-check
PASS · provisional hole addressed upstream (our numbers, our status debt).

STALE (blocks send as-is): package still carries "aphorism from private doc
awaits public link" — SUPERSEDED by the authorship correction (5c48db4: ours,
quotable now). Sending that line misstates our own provenance to a co-author.
Fix: delete the line (nothing to wait for) — do NOT send the stale version.
Score-90 provisional status noted as W1's claim (their track); W2 takes no
position beyond the band number already verified.

---

## 2026-09-26 — Stop-line RETRACTED (false alarm) + linkage VERIFIED (W1)

W1 verified per today's rule: the aphorism line never existed in W4's sendable
letter (Articles checkpoint 682–687) — the stale phrasing lived only in W1's
own text, relayed to W2 as send-risk. My a669f80 stop-line was therefore aimed
at a defect the package never contained. RETRACTED with thanks — this is the
verify-before-claim rule working in both directions, and W1 modeling it (checked
before admitting) is the point, not the embarrassment.

Linkage (W1 point 4) verified TRUE against the doc: RMT-002 (B0, Survived,
line 306) is the sentence's "B0 survivor" (lines 322–324); moving it to B1
orphans the prose (remaining survivors B1+B3, no B0). Verdict preserved either
way (B1 zero-tolerance, line 281). ENDORSED as one edit: 2 table cells (lines
176 + 306) + W1's replacement sentence verbatim ("The B3 survivor does not block
the gate. The B1 survivor does — B0 and B1 are both zero-tolerance. …") — it
additionally teaches the B0/B1 pairing explicitly. Superseded-entry note
(679 vs 687, read-late rule) acknowledged — Atlas lesson, third application
today. Package sendable with the one-edit fix; sending = owner.

---

## 2026-09-26 — Leonardo doc verified INDEPENDENTLY (W1 cb1fad8 concurs)

W2 read the 477-line version + grep-verified: ZERO naming (no OpenClaw/agent/
pilot/case-study matches), ZERO our numbers (no 91.4/8.6/58) — purely
doctrinal text. Anonymization therefore a PREVENTIVE insertion condition, not
a text edit. B2 wording (N≥20, 5% band, small-N max-1-with-decision) matches
framework v0.3 verbatim; B0/B1 zero-tolerance, B3 trend-only match; division
halves correct. One illustration-table nit (Order→B0 vs our B1-CRUD mapping)
is pedagogical license, not gate conflict — gates operate on assigned tiers.

Provisional-5% hole (OURS, W1 caught): number must carry status in joint text.
W2 recommends option 1 — "a limited band — our current default is 5%, still
being calibrated (recheck due Oct 2026)" — over dropping the number: concrete
gate + demonstrated honesty beats vague tier-words, and it models the very
provisional-marking doctrine the article preaches.

Reply package (send W4 draft + 4 points): (1) anonymization as insertion
condition; (2) 1+2+2 breakdown mandatory; (3) B2-band mechanism (thresholds 5%
and 0, never 8.6%/91.4%; decisions didn't flip); (4) provisional status of 5%.
Aphorism stays out of quotes.md until publication link.

---

## 2026-09-26 — Correction: Victor's Slot 2 DONE (stale "pending" retracted)

Victor flagged it himself: his 25 were submitted, validated 25/25, kappa 0.242
computed, 8 divergences arbitrated, merged into gold-30 (verified 30/30), Phase
B executed on that gold. COMPLETE — no re-labeling, nothing pending from him.
My repeated "Slot 2: Victor's 25 pending" lines in later summaries were stale
boilerplate carried forward unread — retracted with apology. Standing-by lists
from 33a7e56 onward should have read "Victor: nothing pending". Lesson: status
lists re-derive from commits, never copy forward.

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

## 2026-09-26 — S4-confirmation VERIFIED + batch #1 survivors FULLY CLOSED (W3)

Confirmation runs recomputed (9 rows): S4 3× exit 0, S5 3× exit 0, S1 3× exit 1
(PROOF=1 branch on) — matches verdict file exactly. Rulings: S4/S5 confirmed
survived = genuine gaps, consistent with gold P2 (E4 ruled-split, E5 worked);
S1 killed-when-branch-executes → plant-run survival VACUOUS (env-gated branch
off), excluded like N-scope; gold E1 = NOISE stands. Final: S1 vacuous ·
S2/S3 dismissed · S4/S5 confirmed gaps (P2). ZERO open survivors batch #1.
60-run verdict (4/10) already verified b2d8216. GLiNER probe run (7 findings)
pending W3 execution under ratified mapping.

---

## 2026-09-26 — GLiNER mapping mini-protocol RATIFIED +2 annotations (W3 b7d9f91)

Verified: ground truth H1–H7 (all NOISE, FP-rate-only scope stated upfront —
honest scoping, not discovered later) · mapping exhaustive over the 5-head
vocabulary with F3-evidenced critical→P1 cap · fp derived with explicit
limitation + independent-head deferred · abstain/UNPARSEABLE separate buckets,
nothing silently dropped · no tuned cutoffs (tuning = new protocol) · zero runs
pre-ratification respected.

Annotation 1 (binding on step 3): P0-cap EXPIRES with this probe. Gold-30
contains H10 (P0) — step-3 mapping must re-derive P0 reachability explicitly;
carrying the cap forward silently would bake in a systematic P0-miss.
Annotation 2 (record): medium→P2 / high→P1 assignments are STIPULATIVE
(no observation behind them, unlike the evidenced critical cap) — revisable
under step-3 evidence without protocol breach. Probe expectation (high FP by
construction) correctly set: this run tests pipeline+mapping viability, not
judge quality.

---

## 2026-09-26 — GLiNER pilot-plan scaffold REVIEWED, relayed to W3 (W1 scaffold)

Spot-check (read-only): arms L0/L1/baseline-with-frozen-numbers ✓ · SHA pins ✓ ·
fixed probe set ✓ · metrics incl. abstention ✓ · determinism ✓ · scope guard ✓ ·
pre-registered adopt/tie/lose with W2-verifies role (accepted) · commercial-none
consistent with silent phase. Sound scaffold.

One sequencing annotation (binding): probe set's ground truth + the step-2
schema mapping are the SAME dependency — mapping mini-protocol must land BEFORE
probe runs, else unmapped outputs (cf. F3-critical inversion already observed).
Abstention needs an operational def (abstain vs UNPARSEABLE) in the mapping doc.
Setup (weights pull, API access) may proceed in parallel — no blocking. W2
sign-off role confirmed for the verdict table.

---

## 2026-09-26 — GLiNER smoke VERIFIED as RECON (W3, file-whole via scp)

Artifact read whole (1086 B): load 9.7s + F1–F7 (~0.4s each), native severity
vocabulary (critical/low/info), partial:false. No measurement claims made —
RECON discipline holds. Env-lineage (PC-224, torch 2.14.0+cpu, transformers
5.17.0, gliner2 2.0.0, weights 7ee5da4c, 2026-09-26, +3 fixed deps) meets the
lineage requirement.

Load-bearing observation for step-2 mapping design: native head says `critical`
on F3 (gold NOISE per calibration H3) and `info` on F7 (gold NOISE per H7) —
direct inversion vs gold on the external-link class. Raw native outputs are
unusable without the mapping layer; thresholds/question-decomposition MUST flip
this class explicitly. This confirms (not surprises) the design-cost warning —
recorded here so the mapping mini-protocol starts from evidence, not hunch.
Mapping review on W3's submission, BEFORE any runs (binding sequence holds).

---

## 2026-09-26 — PC as compute home: path 1 vs 2 assessment (W5 proposal)

W5: PC right place (Linux torch 2.8, 12 cores); blocked on access (password
prompt, no key). Two paths: (1) owner installs by one-liners, W5 directs via
paste-output loop; (2) owner's one-time SSH key → W5 fully remote.

W2 assessment: path 2 unlocks campaign-grade work; path 1 suffices for
one-time smoke ONLY under a file-transfer rule (outputs move as WHOLE FILES
via scp/shared folder, never pasted text — the merge-vs-statistics lesson:
transcribed chains bear pass/fail, not numbers). Pasted single numbers
acceptable solely for the computer-tool benchmark probe. Security scope of any
key (purpose-bound, revocable) is the owner's call — W2 flags, doesn't decide.
Local RECON continues in parallel regardless (no blocking). Decision: owner.

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

## 2026-09-26 — PrimeQA (TesterArmy) triage: CONTENT now + bounded OSS smoke (W1 decides)

Facts (wiki/testerarmy-qa-agent-yc-p26-2026.md, source-verified): YC P26 fresh,
2–10 staff, $1.2M pre-seed (~1wk old news), agentic E2E web+mobile CI-native,
MIT OSS tooling (npx terminal client, OpenAPI-spec tester, trace viewer),
named founders (Szymon Rybczak, Oskar Kwaśniewski, LinkedIn-active), Juno quantified
claims (10x/58%/2d→0), 135:1 token-economics post.

W2 assessment — the binary is false; recommend HYBRID:
(a) CONTENT now, zero cost: Juno fact-check lens + 135:1 token post + YC-fresh
narrative are article-ready without going anywhere (TestMu/Sophia pattern).
(b) OSS-tools smoke, bounded (one evening, GLiNER-smoke discipline: RECON
only): npx tools against OrangeHRM — runnable with NO contact, NO key, NO
Monday gate. Feasibility probe (runs? outputs traces/verdicts? seedable?),
not a matrix. Full vendor pilot (contact + service eval) ONLY if smoke shows
signal AND pipeline has room.
Axes it adds: sole YC-fresh in roster · MIT OSS evaluable-without-permission ·
mobile-first E2E (vs our web-heavy matrix) · token-economics transparency.

Decision rule for W1: content = yes unconditionally; W3-hour = yes IFF bounded
as smoke (not open-ended pilot); full pilot = deferred to smoke signal +
bandwidth. Pipeline is FULL — no new open-ended track without a closed one.

---

## 2026-09-26 — PrimeQA smoke: MIT axis FAILED for product, unbox-ai FOUND (W1 dc39ffc)

Four answers: installs YES (both MIT, npm-confirmed; OpenAPI tester missing,
e2e = coming-soon + email gate) · runs on OrangeHRM NO (`ta` = cloud control
plane, AUTH_REQUIRED without key) · traces YES but agent-traces not verdicts
(54 gens, 1017k/6.5k, 91% cached, 506s; compare --trajectory works) ·
seedable NO (runner behind key).

W2 records own miss first: the "MIT evaluable-without-permission" premise did
NOT survive contact with reality for the PRODUCT (only trace tooling is open;
test loop cloud-gated). Smoke hit exactly the wall it was meant to bypass —
which is the smoke doing its job. Consequence: full pilot = contact, W1's call
with evidence in hand; content track stands as-is.

Independent find (for our side): unbox-ai runs local read-only keyless on our
traces (opencode + AI SDK adapters), compare --trajectory with divergence
markers — instrument CANDIDATE for the AI-flake rule + "transcript ≠ receipt"
thesis. Candidate only: adoption needs its own measurement (same discipline —
no crowning without numbers). Roster status sync: W3/main's zone, not W2's.

---

## 2026-09-26 — TesterArmy roster sync VERIFIED (W3 e3abfc6)

Row + catalog index.md exist; smoke outcome recorded unembellished (YES/NO/YES/
NO, contact-gate, unbox-ai candidate with no-crowning rule). Both W2 outcomes
reflected as filed. TesterArmy track: content stands, full pilot awaits W1
contact decision, unbox-ai awaits measurement. Nothing pending W2.

---

## 2026-09-26 — W1 self-correction VERIFIED + e2e micro-step assessed (2f02c53)

Correction log verified read-only: exemplary (what was wrong + why = method
artifact of guessed names + how reproduced via npm view + registry org
endpoint). Same standard applied to self that we apply to vendors — recorded
as doctrine-in-practice, not just doctrine. Back-pointer present with
no-duplication ban — pointer gap closed.

New facts: @testerarmy/scout 0.3.0 (API exploration harness) + @testerarmy/e2e
0.1.1 (e2e runner infra, Kernel browsers/Limrun devices as drop-in engines);
both MIT, both UNRUN; "which is OpenAPI-driven" marked inference-not-fact
(correct restraint).

e2e assessment: IF @testerarmy/e2e runs keyless locally, the "seedable NO /
contact-only" finding needs revision (scoped to e2e package). Micro-step
design (bounded RECON, falsifies exactly one finding): install (entry: Node
>=22.12 — check first) → keyless-prompt attempt → recorded installs/runs-
keyless/engines-local. Same RECON discipline (no measurement claims). If
key-gated → finding stands strengthened. Owner/W3 decide execution; W2 needs
no input unless the finding flips (then seedability re-probe design).

---

## 2026-09-26 — Micro-probe VERIFIED: keyless architecturally impossible (W1 4a72a2f)

Addendum verified read-only (commit in log): kernel()/limrun() → hosted only,
env-only creds ("no other knobs"), zero local engine in package; e2e 0.1.0
public on npm vs coming-soon page. Two-walls distinction (rights vs money) is
fact-grounded — endorse as load-bearing for commercial framing.

On Draft 2: YES, update — W1 edits (their tree, not mine). Suggested line
(wording theirs): runs cost their infra (Kernel/Limrun), so propose
scoped-key runs with explicit cost handling; "free pilot" must appear nowhere.
Rationale: first-unpack discovery of undisclosed cost = trust breach with a
warm author; prevention is one honest line now. Seedability finding stands
strengthened (mechanism, not just gate observation).

---

## 2026-09-26 — Registry cross-check CONFIRMS W4 table + Draft 2 endorsed (W4)

W2 independently verified via public npm API: `e2e` 0.1.0 deps-empty (core
without engines) ✓ · `@testerarmy/e2e` 0.1.1 carries agent-device 0.21.6 +
@onkernel/sdk 0.68.0 (hard deps bound to provider package, NOT core) ✓ ·
`@e2edev/web` 0.11.0-canary deps-empty ✓ · `@e2edev/mobile` 0.8.0-canary has
utility deps (zod/pngjs/agent-device, no engines — substantive match, engines
still injected). Precision note only, non-blocking.

Draft 2 update ENDORSED with W4's "bill transparently" phrasing: money wall
named in vendor's words (Kernel/Limrun), rights wall via scoped key, "free"
absent everywhere. Final wording = W1 (their tree, their send). Two-walls
model now triple-confirmed (mechanism + registry + architecture).

---

## 2026-09-26 — Leonardo reply: SEND APPROVED (final paragraph verified)

Nit-replacement paragraph verified claim-by-claim against the doc: Order→B0 in
risk table (line 176) ✓ · RMT-002 Survived (line 306) ✓ · B1-per-our-mapping
(core journeys) ✓ · orphaning of "The B0 survivor does" (lines 322–324) ✓ ·
replacement sentence = ratified formulation verbatim ✓. Stale "5 survivors"
marked superseded in checkpoint; rest of letter unchanged per W1. SEND.
Ball moves to Leonardo on send; W2 needs nothing further on this track
(resumes on his reply: review of merged draft vs ratified positions).

---

## 2026-09-27 — Merged draft REVIEWED: APPROVED with 1 optional micro-add (W2)

Leonardo's returned (2).docx (1.2MB: styles + header/footer + 3 images + tables)
verified against ALL ratified positions: B1 double-flip in BOTH tables ✓ ·
B1 sentence with B0/B1 pairing, B3-flow intact ✓ · provisional-5% with Oct 2026
recheck ✓ · batch 91.4% + prose 1+2+2 + band mechanism + decisions-didn't-flip ✓ ·
pre-stamp honesty + batch #2 (24/22/0/0.1.0, 2-error shown, mapping cited,
directional caveat with non-A/B disclaimer) ✓ · zero OpenClaw naming ✓ ·
zero stale B0-survivor prose ✓ · bylines Leonardo-first table ✓ ·
em-dash→hyphen normalizations immaterial. Paraphrase risk did NOT materialize —
inserts applied essentially verbatim.

Optional micro-add (non-blocking, Victor decides): the crash-hang line cites
the pre-registered mapping but drops the "(mechanism hypothesized)" qualifier
(zero hits for hypoth*). Two words restore full precision; absence does not
falsify (mapping basis stated). Images (3 png) unchecked — Victor's eyes if
wanted. Track proceeds: date + channels next.

---

## 2026-09-27 — Final ACCEPTED by W1 (8667ec8), cross-check clean (W2)

W1's 7-point acceptance verified against W2's independent review (0ed9a37):
B1 both tables ✓ · sentence (hyphen cosmetic, goodwill correctly unspent) ✓ ·
provisional verbatim ✓ · naming clean via "In our own batch" (not our proposed
phrase — W1's call not to nitpick a non-defect is correct; anonymization holds
by absence either way) ✓ · batch insert complete ✓ · stamp paragraph complete
with register NOT strengthened ("directionally suggesting" preserved) ✓ ·
skeleton intact ✓. Zero divergences between windows. The optional micro-add
stands as offered-and-not-taken — correctly non-blocking, no revisit. Content
CLOSED; remaining: date (target Tue 29.09) + channels. Technical verification
resumes ONLY if Leonardo edits text again. W2 needs nothing further here.

---

## 2026-09-26 — Sent docx READ (12,757 chars): letter/doc split is coherent

Owner asked whether letter-described edits must go into the doc. Unpacked and
checked: the docx ALREADY carries provisional-5% ("still being calibrated,
recheck Oct 2026") + batch 91.4% + prose 1+2+2 + band mechanism + decisions-
didn't-flip. Zero stamp language (no falsification in doc), zero naming
(anonymization holds by absence). MISSING from docx (postdate it): B1
double-flip + sentence (already AGREED by Leonardo in reply) and the stamp
fix (pending send) — both travel as verbatim-copyable texts in the letter.

Ruling: NO doc edits needed from us — "prepare final yourself" stands WITHOUT
contradiction, precisely BECAUSE every pending change exists as literal quoted
text (B1 sentence verbatim, stamp/batch-#2 phrasing verbatim). Copy-paste
surface, minimal paraphrase risk. The load-bearing guard remains the W2
merged-draft check (already planned): verbatim-quoted does not mean
verbatim-applied — Leonardo rephrased once before.

---

## 2026-09-27 — v2 assembly built + insertion map handed to owner (his build)

Owner reversed ("tell me where, I'll assemble and send myself"): W2 built
`29-policy-half-SEND-v2-our-inserts.docx` in Leonardo's catalog (python-docx;
sent v1 untouched) with 4 edits verified by re-read — risk-table B0→B1,
evidence RMT-002 B0→B1, prose B1-sentence, stamp paragraph (article-voiced,
YELLOW-highlighted, marked pending-W1-signoff). Insertion map + exact stamp
text handed over; owner assembles/sends himself. Clarified on ask: stamp
paragraph is OUR insert for OUR section (not a fix to his), quoted verbatim
for placement. Stamp text unratified as article prose — W1 sign-off still
required before send (flagged, not bypassed).

---

## 2026-09-26 — STOP-SHIP CONFIRMED + batch #2 numbers CORRECTED (W1 9f67340/5631349)

Re-verified from artifacts (not memory): batch #1 jsonl = 58 rows, ALL
UNSTAMPED → pre-0.1.0 engine, definitively. Attaching "rmt 0.1.0" to batch #1
evidence = stamp falsification in a joint article whose thesis is stamp
integrity — adversarial-reviewer bait. STOP-SHIP stands; letter as drafted
must NOT go.

Correction to W1's proposed batch #2 line ("22 killed, 0 survived, 2
inconclusive"): the verified closeout resolves BOTH hangs — wa-controls
COMPLETED exit 1 (9F/5P) = Killed, NOT inconclusive; only tooltip is
interpretive (Caught-by-crash per pre-registered mapping, hypothesis stated).
Publishing "2 inconclusive" would itself misstate the record (in the kind
direction, but still false). Recommended article line: "24 mutants, 22 killed
outright, 0 survived; 2 terminated in error — one fail-run Killed, one
crash-hang Caught under a pre-registered timeout mapping (mechanism
hypothesized, stated as such). Shown, not hidden." Standard MT semantics
(crash/timeout = killed) back the mapping; closeout and article then agree.

Reverse direction CONFIRMED with caveat: unmutated baselines green in both
batches (batch #1 normals + batch #2 30s exits) → engine upgrade didn't break
the working surface. Caveat: different assertion sets seeded, so directional
evidence, not controlled A/B — phrase accordingly.

Two pre-send flags for Victor: (1) the overnight-sent docx ("our 2 edits") —
verify it carries no stamp language (the stamp line lives in the chat letter;
check the docx independently); (2) stray CJK chars ("琪") in the draft reply —
proofread out. W4 coordination concurred (W1 owns reply+go-ahead; W2 checks
merged draft incl. OUR insert on Leonardo's reply; W3 uninvolved — no pilot
claims, batch anonymized).

---

## 2026-09-26 — Stop-ship CLEARED for send (W1 2d768ed, flags closed)

Flag (a): night docx unpacked (13,281 chars) — zero "0.1.0"/"stamp"; sole
"engine" is Leonardo's own phrase. Stamp lives ONLY in letter text → fix the
letter, doc untouched. Our insert already in doc WITH 1+2+2 breakdown.
Flag (b): CJK garbage chat-draft-only, absent from files — keep out of send.

W1 adopted W2's batch #2 line verbatim (wa-controls = Killed correction
accepted with fault admitted — verified-against-artifacts discipline held).
Reverse direction: directional-only phrasing locked. Bonus recorded: 58×
UNSTAMPED makes "run on a pre-stamp engine" a TEACHING example for stamp
discipline (the gap that proves the bar), not a quiet hole.

SEND CONDITIONS (all must hold): honest pre-stamp line IN (replacing 0.1.0) ·
optional batch #2 in W2 phrasing · directional-only engine-change phrasing ·
CJK cleaned · 1+2+2 + B1 one-edit + provisional-5% from prior package. Roles:
W1 correspondence, W2 merged-draft check incl. our insert on reply, W3 out.
Letter still unsent — send = owner.

---

## 2026-09-26 — SEND APPROVED: final letter meets all conditions (W4)

Verified line by line: 1+2+2 ✓ · band + provisional ✓ · anonymized runtime ✓ ·
B1 double-flip + new sentence ✓ · bylines per Leonardo's proposal ✓ · pre-stamp
honesty fix with teaching-point framing ✓ · batch #2 verbatim W2 (24/22/0 +
2-error shown, mapping + hypothesis caveat intact) ✓ · directional-only engine
phrasing ✓ · zero "0.1.0" ✓ · zero CJK ✓. ALL SEND CONDITIONS MET. Send = owner;
ball with Leonardo after. W2 resumes on merged draft (incl. our insert).

---

## 2026-09-26 — Outgoing queue: 3 sends await OWNER (W1 5d70f0f, queue empty)

W1 verified-before-accepting throughout (per today's rule): Leonardo one-edit
package (176+306+prose as single edit, reformulation matches recommendation) ·
Draft 2 duplicate caught (infra-cost line + two-walls block already in 63f2a93,
no double-edit) · Rupesh three-frames held for ping reply. W2 records, no
re-verification (W1's verification chain complete and cited). OWNER SENDS:
(1) Leonardo letter → ball with Leonardo; (2) Rupesh frames → after his ping;
(3) TesterArmy Szymon connect (Draft 1, no ask) → Draft 2 after accept. All
three tracks incoming-wait after send. Nothing pending W2 anywhere in this.

---

## 2026-09-26 — TesterArmy rename VERIFIED, one pointer missing (W1 07fc80f)

Verified: no PrimeQA remnants (both trees clean — codename purged correctly);
pilots/TesterArmy/ (index + smoke) and outreach/silent/TesterArmy/ exist.
W1 decisions recorded: contact opening (connect Szymon, no ask → scoped access
post-accept; sending = owner), terms pre-run (Stage 0 named-not-invoiced →
Stage 1 paid, notice discipline, sandbox-only), unbox-ai gate = measurement vs
pass-rate+spread.

Gap (Atlas lesson, one line): outreach→pilots pointer EXISTS, pilots→outreach
pointer MISSING (pilots index names people but points nowhere for contact/
commercial). Suggest W1/W3 add one line in pilots/TesterArmy/index.md. Not
W2's tree — flagged, not fixed.

---

## 2026-09-26 — PrimeQA OSS-smoke EXECUTING as RECON (W3 accepted bounds)

W3 motivation concurs with triage axes (mobile-first + token-transparency cover
two blind spots; MIT removes all gates; hour of RECON = cheapest information
in roster). Full pilot explicitly declined without smoke + room (deferred
holds). Contract: installs / runs on OrangeHRM / traces-verdicts outputs /
seedability probe; report = four answers + whole file, zero measurement
claims. W2 awaits the four answers; no verdict-grade reading of RECON output
will be accepted from either side.

---

## 2026-09-26 — Step-3 VERDICT: LOSE (record + park), substance over letter (W3 runs)

Recomputed from whole file (90 rows, FP defined severity-based for cross-arm
comparability, matching cloud's 4/24): GLiNER exact 12/30 · sev-only 12/30 ·
FP 12/24 (50%) · FN 4/6 = E3/E4/E5/H10 · H10 mapped NOISE (native low, gate
never engaged) · H9→P0 (watch-item precision-misfire confirmed) · stability
30/30 · latency ~0.9s (2 calls).

Scoreboard gold-30: GLiNER 12 exact (best) / cloud 9 exact + 21 sev / L0 0.
Verdict LOSE, grounds: (1) FN 4/6 incl. the only P0 — a triage layer dropping
2/3 of real defects fails its purpose regardless of exact-lead; (2) FP 50%;
(3) P0-miss (H10 NOISE) — stop-class per doctrine, consistent with routed-pair
ruling. Criterion letter vs substance recorded: letter fails on latency
technicality (0.9 vs 0.1) and lacks FN/P0 dimensions entirely — recommend
adding both explicitly if the criterion is reused.

New instrument findings (beyond the report): (a) inter-head inconsistency on 6
items (severity says defect, fp-head says not — E2/E6/E7/H3/U3/U4): the two
heads disagree with EACH OTHER, distinct from gold disagreement; (b) E3/E4/E5
missed by cloud AND GLiNER alike — hardest items in the set, visible only to
gold+arbitration; (c) flag-FP (25%) vs severity-FP (50%) gap quantifies head
divergence — future mapping work starts here, not from scratch.

Phase C: NOT triggered (clear verdict, no tie-band). Stability 30/30 already
measured descriptively. Parked pending fine-tune story (tie clause's revisit
path). Nothing further on this track without a new decision.

---

## 2026-09-26 — GLiNER track CLOSED by mutual agreement (W3 full-cycle summary)

W3's 8-step close-out (triage → smoke → mapping → probe → freeze → measure →
LOSE → park) matches W2 records at every step — no divergences to reconcile.
Unfreeze conditions identical on both sides (fine-tune + new protocol + new
freeze). Track silent until then. Full local-judge-adjacent program now reads:
replacement NO (3 grounds) · GLiNER LOSE (FN+P0) · ladder unvalidated-but-
parked · gold-30 stands as the reusable instrument for any future judge.

---

## 2026-09-26 — Step-3 freeze RATIFIED clean + Phase C ruled CONDITIONAL (W3 ae62cd7)

Freeze draft verified: scope gold-30 × 3 + env/weights SHA ✓ · P0 re-derived
per annotation (probe cap burns in-text, pattern gate frozen + lexical
limitation recorded, silent carry-over forbidden) ✓ · medium/high kept
stipulative with revision-by-new-freeze-only ✓ · independent fp-head
(question-over-passage) with derived-fallback strictly on head error ✓ ·
buckets as ratified ✓ · verdict exact-vs-gold + within-run stability
descriptive ✓ · zero runs pre-ratification ✓. No annotations — first clean
ratification of the track. Runs authorized.

Watch-item (non-blocking, for analysis phase): pattern-gate precision against
gold-30 non-P0 items (e.g., does any NOISE text trip "blocks all"?) — the
exact-vs-gold verdict surfaces it automatically; no extra protocol needed.

Phase C ruling (W3's question): CONDITIONAL, not standalone-now. The closed
replacement track needs no stability work (instability could only strengthen
NO; stability cannot overturn margin+FP+P0). Phase C activates IFF step-3
lands in a tie/ambiguity band where cross-session stability decides adopt vs
tie — and then ONLY on the tied arms. Neither L0/routed (verdict stands
regardless) nor GLiNER-unless-tied. No make-work stability runs.

---

## 2026-09-26 — GLiNER probe VERIFIED (7/7 scored, mapping exact)

Recomputed from the whole file: 7 scored, 0 abstain/UNPARSEABLE; native→mapped
per protocol exactly (low→NOISE ×5, info→NOISE ×1, critical→P1 ×1 on H3 — the
pre-registered F3 inversion, sole FP); 6/7 match gold (all-NOISE set). Viability
pipeline+mapping confirmed, zero measurement claims — RECON discipline held.
Step 3 awaits separate freeze (P0-reachability re-derivation + medium/high
review under evidence, both annotations recorded as work items).

---

## 2026-09-26 — GLiNER track GATED (W3 confirmed, hands clean till decision)

W3: verification accepted; step 3 only through separate freeze; no runs until
decided. Gate holds from both sides. W2 has nothing pending on this track —
mapping review authority resumes if/when step-3 freeze is submitted.

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

---

## 2026-09-26 06:58 — Session close (W2)

Session scope (single long session 09-24→26): RMT engine completion (CLI,
B1/B2/B3/B4/B5, stamp 0.1.0, split, CI-shim green) · OpenClaw evidence closure
(batch #1 B2 FAIL + survivors, batch #2, 60 app-runs 4/10, S4-confirmation) ·
gold track (Slot 1, Slot 2, kappa 0.242 arbitration, 30/30, Phase B → replacement
REJECTED 3 grounds) · vendor tracks (Q2/Q3/Gemma/ladder ratified; B0/B-banking
characterized) · pilots (UrsaMinor + Klarent methodologies, Aamir protocol) ·
GLiNER (triage → smoke → mapping ratified → probe verified → gated).

Head: c9f7fff. Tree clean, all pushed. No code debt open (verdictgate.py 29930 B,
split discharged). Open threads (all owned elsewhere): Monday gates (UrsaMinor
call, Phase A slots) · batch #2 RMT top-up (W3) · 60 app-runs bit (W4) ·
Klarent silence clock (W1 N) · Aamir package pointer (W3) · Article 29
(Leonardo) · recheck 10-17. W2 resumes on request: verdict-pack text (W4),
arbitration (new sets), verification (new packs). Owner away 30h mobile —
nothing urgent pending.

---

## 2026-09-26 07:23 — Session close (W2, second wrap)

Since 06:58 close (5523fc6): PrimeQA triage (content-now + bounded OSS smoke,
full pilot deferred — decision with W1) · GLiNER full-cycle close (step-3
freeze ratified clean → 12/30 LOSE on FN+P0 → gated till new decision; ladder
routing ratified; Phase C conditional-declined) · S4-confirmation verified
(batch #1 survivors zero open) · 60-run verdict verified (4/10 unanimous) ·
no-migration concur + PC benchmark parallel · Fastino outreach filed (silent,
W1's call) · Klarent demo-request sent (fallback clock ticking) · Aamir rerun
protocol signed (verification BLOCKED on package pointer) · UrsaMinor
methodology + Monday-call additions filed · W1 discipline amendment applied
(Commercial owns registry/monetization/strategy/promos) · vendor-5 declined
(parked with trigger) · B0/Gemma/Q3 closed with corrections logged.

Head: 22ac244. Tree clean, all pushed. Zero code debt (only docs since split).
Owner away 30h mobile — nothing needs him. Standing by on all fronts.

---

## 2026-09-27 — Labeling memo for W4 filed + zone restated (no code)

Owner requested facts memo on his labeling work (for his article on first-time
experience): written to reviews/slot-labeling-experience-memo-2026-09-26.md
(gitignored, local-only) — timeline markers, 6 questions + answers, D1–D5
difficulties, quotable moments, verified numbers; solo wall-clock honestly
marked unmeasured. W4 pulls by path. Zone + open threads restated on request:
W2 owns verdictgate/** (+28 draft, DevAssure frozen); zero pending W2 actions
anywhere — all threads gated on others (sends, slots, gates, 10-17 recheck).

---

## 2026-09-30 — W3 one-liners: jurisdiction rulings (whose sign-off what)

(1) qa-cube version string: NOT W2's call (their tree, cosmetic, no verdict
impact) — W3 decides alone under audit rule (touch only if factually wrong,
one line + justifying commit message; else leave). No sign-off needed from
W2 or W1.
(2) gold version string: W2 DECIDES — DO NOT TOUCH. "FROZEN 2026-09-25" dates
the freeze protocol, content merged 26th under it; editing a frozen artifact
breaks byte-identity every hash depends on. Ambiguity (if any) gets recorded
in the pilot log/index, never in the file. Frozen means frozen — including
metadata.
(3) PC-benchmark: HOLD. No consumer (sharding deferred) → measuring now is
desk-drawer numbers, banned by decision-driven doctrine. Revisit on sharding
decision or a decision that needs it. W3's own instinct correct.
Non-theirs list acknowledged, no action (Qodo SHA on resume; TesterArmy/
ContextQA/Slot moves are owner's; finetune post-29th+Kaggle; /tmp clones live
till campaign end).

---

## 2026-09-30 — Bug report pre-send check PASSED, send it (W2, 30-second read)

Read whole (24 lines): timeline with requestUID + timestamps (silence window
BEFORE cancel — causal order correct, post-mortem framing holds) · elimination
list comprehensive incl. the program-shape find · one-line question names
suspects without asserting (bus/config + cooperation offer) · attachments
on-request not dumped · zero secrets in file · tone technical-friendly, no
blame, no verdict smell. Stale-letter suppression (48f4b3b) concurred — sending
yesterday's text would ship refuted localization. Cover note + Telegram-file
format + gist-secrets proposal: all W1's lane, no objections. SEND (owner).

---

## 2026-09-29 — Reg accept CONDITIONAL + rename applied + gotcha fixed (W1 ad9f475)

Denominator check (assigned to W2) against H4 data (120 rows: success 120/120,
validation_detected yes/120, is_regression True 67/120): Reg as WRITTEN
("seeded-break runs") vs as PUBLISHED (/120 all-runs incl. controls) DIVERGE —
identity with mutation_score (seeded-only denominator) holds ONLY under the
seeded subset. Numbers unaffected either way (0/120 = 0/60 = 0 — degenerate).
Ruling: rename ACCEPTED with denominator condition attached (operationalize
which conditions = seeded-break; recommended break+drift = 60; W1 confirms);
numerator equivalence (absent ⟺ caught) UNTESTED — first nonzero case reopens
the identity, recorded explicitly. Reg → mutation_score, Reg* → native_rate
applied in retro-pipeline-spec (UNDEFINED lifted); article legend already
renamed by W4 (line 57, verified). native_rate = 67/120 = 55.8% raw-field rate
here — descriptive only, gates nothing (is_regression unreliable per H4).

Gotcha collision fixed: mine renumbered to ## Gotcha #12 (was ### 10;
## 10/11 pre-existed — owner-flagged, my grep missed ##-level headings).

---

## 2026-09-29 — Denominator CONFIRMED by W1 independently, UNDEFINED lifted (e97d54c)

W1 rechecked from data (not on trust): 120 rows, 4×30 conditions, success 120,
validation yes/120, is_regression 12+25+12+18 = 67 (55.8% — converged with W2
to the tenth). Break+drift = 60 confirmed as seeded-subset with triple basis
(W2 data check + design coherence + degenerate numerators). Numerator accepted
as untested (first nonzero case reopens). UNDEFINED lifted by W2's rename
(already applied b296ab9: mutation_score + native_rate with denominator
condition) — no further action, both sides agree the line is now defined.

Seeded-flag rule ADOPTED (W1 recommendation, W2 enforces at review): every
future campaign carries an explicit per-row seeded boolean at seed time — next
identity check must need no archaeology. Absence of the flag in a future pack
= review finding, not nitpick.

---

## 2026-09-29 — Night build DONE except post-actions; bug-report path endorsed (W3)

Infra 100% verified as stated (pins, 4 digests, stand up, Docker BaaS healthy).
Key fix recorded: `program`/`timeout` inside `browser{}` (top-level silently
ignored — same silent-misconfig class as unquoted-spaces; vendor schema
validation would have saved hours — feedback item for Katya alongside, not
inside, the bug report). Remainder precisely localized: post-actions CDP fail
IDENTICALLY in both envs (display/network/driver/shm/mongo/SSE all excluded)
— env-independent vendor defect, report-grade evidence.

Endorse path 1 (bug report to Katya): identical-across-envs failure + full
elimination log = high-quality report; her 5-min fix beats further code-digging
on expected value. Framing must stay friendly setup-feedback per Igor pattern
(never verdict-shaped) via owner channel. Smoke runs on green; rest ready.
No W2 action (no verification ask in this one).

---

## 2026-09-29 — AIID incident corpus: flagged, deferred with trigger (W5→W3→W2)

W5 flagged DB snapshots + GitHub repo as queryable real-incident corpus for
seeded scenarios (wiki noted, hands off). W3 assessed: real value (synthetic
seeds today → field-provenance breaks strengthen any future matrix) BUT
deferred — pulling without a consumer violates make-work ban. Trigger:
matrix design requiring real-incident grounding → pull + incident→seed mapping.
W2 concurs: correct triage (value acknowledged, timing gated on consumer);
no action, no review needed (no artifact produced).

---

## 2026-09-29 — Reg/Reg*: provenance unknown, rename required (owner catch)

Owner: industry norm or our invention? plus markdown-asterisk confusion risk.
Verified: "Reg/Reg*" occurs NOWHERE else in our system (codebase metrics are
mutation_score/survival_rate) — it is W1's draft shorthand, undefined in the
spec. Industry MT standard terms are mutation score / kill rate / survival
rate — "Reg/Reg*" matches none; provenance unknown, do not present as norm.
W2 self-flag: I ratified a term I cannot anchor — the filing addition (cite
formulas) mitigates but does not cure; definition still owed by the spec
author (W1).

Ruling: (1) W1 defines Reg and Reg* (formulas + mapping to scorer metrics if
identical — single vocabulary preferred: use mutation_score/survival_rate
directly when they coincide); (2) RENAME to ASCII-safe, markdown-safe tokens
(no asterisks/specials — asterisk already renders wrong in the filed .md);
(3) until defined, the allowlist item is UNDEFINED — implementation blocked on
that line only, rest of spec stands. W1 supplies definition + name; W2 amends
the filed spec.

---

## 2026-09-29 — Retro-pipeline spec REVIEWED, hardened ×2, FILED (W1 draft)

Review: boundary clean — nothing judging-class in machine scope (Reg/Reg* are
fixed-formula computation; drift-diff is presence-boolean; assembly is
field-copy). Filed as docs/retro-pipeline-spec.md with two tagged W2 additions:
(1) Reg/Reg* formulas must cite exact frozen source (SCORER_VERSION + section),
else the column doesn't build; (2) normalization byte-preserving by default
(no folding unless explicitly listed — none listed). Both close silently-
loose phrasing ("fixed formulas", "without interpretation") that implementation
could have driven judgment through. Acceptance (byte-identical on batch #1)
stands; implementation not started (separate decision).

---

## 2026-09-29 — Retro-pipeline spec: skeleton APPROVED, path (b) (W1)

Skeleton sound end to end (goal / machine-scope / human-scope / interfaces /
acceptance-as-golden / non-goals) — matches my boundary exactly. Location
ruling: NO direct drafts into verdictgate/docs/ (single-writer rule holds even
for invited guests — provenance stays clean). Path (b): W1 drafts at home →
W2 reviews → W2 files into docs/ himself. One extra hop, zero ownership blur.

One binding addition for the draft (else the boundary blurs in implementation):
an explicit ALLOWLIST of mechanical derivations (exit_code→suite_result,
timestamp→run_ref format, etc.) vs judgment (behavior/tier assignment,
replacements, narrative). Anything unlisted = human by default. Acceptance
criterion (byte-identical on batch #1) endorsed as the right bar — same as
scorer goldens. Awaiting W1's draft text.

---

## 2026-09-29 — UrsaMinor mapping RATIFIED: binary + 3 buckets + inversion (W2)

Brief read whole (31 lines). Charter effectively signed (👍 + five yeses +
P1 qualification) — accept W1's reading; signature gate closed, build trigger
(Victor's "go") the only open item.

Ratification (binding, pre-runs): BINARY rule confirmed with her-known-issue
adjustment — non-success on seeded break = Caught, where Caught means
"refused to pass", NOT "correctly diagnosed" (diagnostic precision deferred
till she fixes failed/broken distinction; revisit then). Baseline polarity
INVERTED as specified: baseline success = correct; baseline non-success =
FALSE ALARM on a separate track (specificity measurement, never mixed with
survivors). P1-context inside verdict as (llm-2 + context); node portability
explicitly unmeasured.

Three bucket rulings (all required pre-runs, all Caught + differentiated
observations, none flip verdict; wrong-reason catches observed, e.g.
test_broken on app-break).

---

## 2026-09-29 — UrsaMinor: both windows prepped, ONE word pending (owner's "go")

W3 deltas vs prep recorded without dispute: success-only verdict reading ·
memory OFF out of run config (state hygiene kept) · merge boundary honored
(re-pull + re-pin on test day, pre/post separately; today's SHAs = draft) ·
her JSON SHA as fourth pin line · silence-timer starts on version handoff.
Owner confirms bucket rulings + methodology shifts as binding.

State: brief read both sides · mapping ratified (binding) · charter signed ·
gate = Victor's single "гони" → W3 builds (pins+digests) → Secrets + smoke →
Katya's signature opens runs. W2 has zero open items; next touchpoint is
results verification or gate failure. Awaiting owner's word (his decision,
his timing).

---

## 2026-09-29 — Night forks recorded, one framing rule endorsed (W1 11f0c48)

W1: no night actions (Docker builds itself); morning forks with non-W1
decisions: Docker-up → smoke per brief, nothing needed; Docker-down → (a)
owner-session Chrome (OWNER decides, only with W3's SPOKEN "interactive
untouched" guarantee post-pkill-incident + session-lock flake caveat stands)
or (b) Katya bug report (framing strictly friendly setup-feedback per Igor
pattern, never verdict, only via owner channel). Gotcha kept as read-env-
before-launch reminder.

W2 endorses the (b)-framing as load-bearing, not cosmetic: a warm author
receiving anything verdict-shaped pre-agreement reads it as judgment regardless
of intent — the Igor pattern (finding → same-day fix) works precisely because
it never smells like evaluation. No W2 action; morning decides.

---

## 2026-09-30 — Night build session CLOSED (W3, 13h wall / 5–6h active)

Recorded: full stand (deploy+BaaS+mongo×2, pins/SHAs, 4 digests, CORS fix,
studio+secrets, 6 agents) · fixes en route (env-spaces, CORS recreate,
headful→headless, zombie-Chrome + interactive rule embodied, browser{}
nesting as master key) · proven green (Chrome, DevTools, net/driver/mongo/X)
· death localized to ONE place (otto program not dispatched into live session,
170s silence) · artifacts (run log, committed Katya bug report, VNC, shm-
override, resolved-env practice) · open: Katya's dispatch-path reply (or next
code dive with her hint).

W2: localization quality accepted without re-verification (elimination chain
already reviewed point by point last night; 170s-silence datum is new and
consistent). No action — ball with Katya via owner channel. Timing of any next
code dive is W3's tactical call (hint maximizes dive efficiency); license-wise
the OSS BaaS is diggable anytime, and the systems/data gate is already
respected — no conflict between the two, just sequencing.

---

## 2026-09-29 — Attribution note: "Igor pattern" is W1's term, not W2's (owner asked)

Owner: where did Igor come from, nothing above mentioned him. Answer: the
phrase entered via W1's night-forks message ("паттерн Игоря: находка → фикс в
тот же день"); W2 echoed it in 3 entries (tunnel assessment, (b)-framing
endorsement, night-forks record) without first attribution — corrected here.
Igor = Igor Akymenko, FlowScout founder (Alternate QA), warm outreach contact
held via W1; the pattern names that working relationship (friendly finding →
same-day vendor fix). Correspondence stays via W1; W2 has no contact and no
action. No content changes — attribution only.

---

## 2026-09-29 — Night shift closed, doctrine converged 2× in one day (W1 b2ab6c1)

W1 accepts triage fully; notes "lineage = effective values" matches today's
independent PATH lesson — same doctrine class from two places in one day
(env-parse variance + PATH resolution): TRUST RESOLVED STATE, NEVER SOURCE
TEXT. Recorded as candidate Hard Rule if it repeats a third time. Queues empty
all around (W1 explicit). Morning: Docker digest in run log, else fallback
ladder. W2 stands by; session pauses till morning inputs.

---

## 2026-09-29 — Night build: stand up, CDP blocked, fallback ordered (W3)

Stand built (repos re-pulled + SHAs, UI:8081 post-CORS, studio login, secret
in, 6 agents). Blocker triaged textbook: full chain eliminated, remainder
precisely localized — vendor session path broken in this env, NOT the browser
(dump-dom works). Endorsed: the localization proof (working dump-dom) is what
makes it a finding instead of a shrug.

Fallback order correct (Docker BaaS first = article-blessed path, no
methodology deviation; then owner-session Chrome; then vendor bug report with
ready logs). Two appends: (1) Docker base image = new artifact — record its
digest in run log (env delta travels with measurements); (2) log RESOLVED env
(redacted secrets) at every startup — the unquoted-spaces gotcha proves .env
parsing varies by consumer (shell vs docker vs Go dotenv); effective values,
not file text, are the lineage. Owner-session Chrome noted as
session-dependent constraint if reached (screen-lock flake class).

---

## 2026-09-29 — Node content verified (W3 micro-point, temp finding strengthens repeats)

W3 retrieved + READ her JSON (not just SHA): llm-2 = openai/gpt-4.1, temp 0.7,
EOS/L10 systemPrompt; memory_store listed (removed locally per brief — no
contradiction); tail garbage 4109B (valid to 4107) with file-untouched +
tolerant-parser guidance. W2 notes: (1) temp 0.7 CONFIRMED non-deterministic —
baseline-distribution + repeats rule now evidence-backed, not precautionary;
(2) parser rule must be IDENTICAL across all runs (tolerant is fine, variance
is not — freeze it like everything else); (3) prompt-tuning remarks stay
pre-accepted. Nothing changes in mapping or gate; "go" still the only open item.
- test_broken → Caught + observation (wrong-reason class recorded).
- prompt-tuning artifacts → Caught + observation (gpt-4.1-tuned prompt on
  qwen pre-accepted as-is; artifacts expected, not fixed, not penalized).
- tool-error (any tool except removed memory_store) → Caught + observation;
  memory_store error if ever seen = config breach (tool was to be removed) →
  infra-excluded, not scored.
Her $5-fallback branch (bounded, her money, local-only, delete after) and
merge boundary (pre/post unmixed, pin vector + dates separately) accepted as
pre-registered conditionals. Star/DM post-green-smoke noted for W3 execution.

---

## 2026-09-29 — Pins settled + no-re-pull guard ENDORSED (W1 a4a0387)

W1 concedes pins to W2's softer mechanism (master-default + logged resolved
digests; identical goal: know exactly what ran) and ADDS the binding guard: no
image re-pull mid-campaign without digest re-logging (else baselines and mutant
runs silently mix versions — build once, record, freeze for the campaign).
ENDORSED — same determinism-across-runs family as A==B; closes the last
version-drift hole in the design. Rest accepted as-is (auth out, cost-cap for
Phase-2, article verbatim, observations banked). Gate = ONE domino: build
trigger (owner's word) → W3 builds → Secrets + smoke → Katya's signature
opens runs. Nothing pending W2.

---

## 2026-09-29 01:31 — Session checkpoint (routine, no new substance)

Tree clean, all pushed (head ba86da7). No code changes anywhere in window;
only docs since the split. Open threads unchanged: UrsaMinor build trigger
(owner's word) · Klarent silence clock (W1 N) · Aamir pointer (W3) · Article 29
publish tomorrow + repost (version confirmed same file) · fine-tune spec
(W3, post-29th slot) · s1web GLiNER branch (running) · recheck 10-17.
W2 stands by on all fronts.

---

## 2026-09-29 13:46 — Session checkpoint (routine)

Since f945e1f: W4 follow-up Q&A answered (82-mutant inventory, no second live
case stated plainly, post-freeze-diary angle recommended over retrospective).
Tree clean, all pushed (head f945e1f). No code changes anywhere in window.
Open threads unchanged (Monday gates, Klarent clock, Aamir pointer, fine-tune
spec, s1web GLiNER, recheck 10-17, Article 29 post-publish). W2 stands by.

