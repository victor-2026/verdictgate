# VerdictGate — session checkpoint (append-only)

> **Rotated 2026-10-04 (10th rotation):** history before this point lives in
> `session-archive-2026-09.md` (appended, same repo). Nothing deleted, order
> preserved. Rotation rule: monthly archive + live tail ≤ 32 KiB.

---

## 2026-10-02 — Self-violation: unsigned replies (owner caught, corrected) (W2)

Owner: my last replies carried no handover headers, so nothing was
forwardable (Rule 5 applies to W2's own blocks too — "do as I say" without
"as I do" is how rules die). Standing fix: every forwardable W2 block ships
signed from here on; pure Q&A with owner stays headerless (goes nowhere).
No content lost (substance already in entries above); form repaired going
forward.

---

## 2026-10-02 — Touch #2 exception/ gate split recorded (W1 a643df1 ↔ W2)

W1: exception rationale owned (wrong granularity, pre-scoring catch, zero
picking advantage) + v1-preds never scored for bench. W2: code gate owned
(evaluate.py line-by-line before touch; SHA re-verify; mapping frozen).
Split is clean — rationale exception mine-free, code gate theirs-free. Touch #2
executes after BOTH: W1's exception (done) AND W2's code review (pending
evaluate.py delivery). Awaiting the file; no action until it lands.

---

## 2026-10-02 — Touch #2 APPROVED + evaluate.py review-pending (W2, granularity catch)

W3 caught granularity mismatch PRE-scoring (element-preds vs candidate-truth):
approve touch #2 with reason logged ("v1 granularity mismatch; rerun
per-candidate") — exactly the audited-override case the harness `--reason`
was built for. Conditions binding: same data SHA re-verified at rerun (drift
between touches voids comparability); frozen mapping otherwise unchanged;
ledger records reason verbatim.

evaluate.py: review on arrival, line by line, before ANY run. Pre-registered
review points (not verdicts): gold-qid definition under multiplicity (any-y=1
match vs exact single — must be explicit); confidence source for AUROC (which
output field funds it); multi-y=1 elements handling. Credit where due: catching
this before scoring instead of after is the discipline paying for itself —
garbage verdicts on mismatched granularity were one lazy afternoon away.

---

## 2026-10-02 — W1 routes both open questions to W2; positions stand (W2)

W1 (d4f2c0e): y-truth + formulas are W2's ownership, nothing for W1 to decide.
Positions unchanged from 4d874b2 (no new facts since): (1) y IS truth
(observed survival, oracle-independent) — decided; (2) formulas signed ONLY
against evaluate.py code lines — awaiting W3's paste. Nothing to add, amend,
or re-decide; this entry closes the routing loop (question arrived → owned →
answered → awaiting input).

---

## 2026-10-02 — y IS truth; formulas need evaluate.py lines, not paraphrase (W2)

(1) y=truth CONFIRMED from dataset design (verified 27.09 via Kaggle API):
y=1 = survived all later observations (1,129 changed, 14%); labels observed,
not rule-based; oracle-independence stated in-dataset. y:0.0 = broke. No
ambiguity — use as truth.
(2) Formulas: broken-locator = top-pick-y=0 fraction (lower better); "choice
matters" = y-differing elements; AUROC = P vs y. BUT these are index-level
paraphrases — W2 signs formulas ONLY against evaluate.py code lines (W3
pastes the scoring function; no local copy here, searched). Scoring on
paraphrase risks the same class as transcript-grading. W3: paste function,
then assemble cell. No W2 action beyond this record.

---

## 2026-10-02 — GO: Kaggle kernel + W3 writes runner + file out of /tmp (W1 9d2c186)

W1 approved all three W2 rulings and issued GO: Kaggle eval-kernel; W3 writes
runner (debug non-locked only, first locked contact = bench); locked file out
of /tmp into durable-versioned NOW; touch #1 pre-registered as the bench
(upload ≠ touch — audits must not recount). Debug-location criterion called
out as structural (not personal) dirty-hands solution. SHA chain converges.
Execution: W3. W2 awaits bench numbers (base vs tuned on locked, one touch
each); verdict rule already written (non-regression bar).

---

## 2026-10-02 — Locked-bench readiness rulings: upload≠touch, author-may-write, Kaggle (W2)

Dataset verified as stated (mind2web 245 + app 250 = 495; full pin bfdf20…
matched). Rulings:
(1) Upload ≠ touch: moving locked bytes to private Kaggle dataset involves NO
model contact and NO verdicts — test-lock counts measurement touches, not
storage moves. Bench run = touch #1. Stated explicitly so future audits don't
miscount.
(2) W3 MAY write the runner (no writer≠evaluator split needed): the operative
rule is DEBUG-LOCATION, not authorship — runner debugged on NON-locked data
only (train split / smoke fixtures); first locked contact = the bench run.
Debugging on locked = tuning to test (voids bench); authorship alone voids
nothing.
(3) Kaggle recommended (speed; terms covered by private dataset; free tier =
no cost decision needed). CPU path allowed but wasteful for identical result.
(4) Locked file must LEAVE /tmp for durable versioned storage NOW (with SHA
ea675b59… logged) — /tmp volatility + the purge lesson make this non-optional;
re-extraction on demand is drift risk, not a backup strategy. No W2 action
beyond this record; W3 executes.

---

## 2026-10-02 — Success bar APPROVED, bench fully pre-registered (W1 9376a35)

Non-regression bar adopted verbatim (tuned ≤ base → PASS; delta = signal;
severity N/A; report-only waiver REJECTED — numbers-without-verdict is the
same machine-without-verdicts disease). Bench now complete on paper: script +
data/SHA (W3 side) + format + bar, all pre-registered, zero post-hoc surface.
Execution: W3 runs locked before/after (one touch each arm). W2 awaits numbers;
verdict rule already written (PASS iff bar holds). Nothing pending anywhere
on this thread.

---

## 2026-10-02 — Locked-bench handover ASSEMBLED (W2 → W3 via owner) (W2)

Pristine confirmed (Required in place, stand clean) — prior flag closed.
(1) SCRIPT: verdictgate/scripts/locked-run.py @ 854cd57 (pushed, public —
fetch anywhere; usage: --data --data-sha --tag --model-id --out ledger --reason
-- <command>). (2) DATA + SHA: NOT in W2's reach (bounded search: no
eval_set.json, no locked files on this machine) — W3 side holds both (ran the
branches, made the split); W3 supplies path + locked-subset SHA from run env.
Full-set SHA bfdf20… covers eval_set only, not the subset. No data invented
here. (3) FORMAT base-vs-best: two locked-run invocations (tag `base`
model-id fastino/GLiNER2.5-Decide@7ee5da4c; tag `tuned-best` model-id +adapter
BEST dev-loss 6.9470) → evaluate.py both outputs → report broken-locator +
AUROC-secondary. SUCCESS BAR STILL OPEN (recommend now, pre-run): tuned ≤ base
broken-rate = non-regression minimum to claim anything; delta reported either
way; H10-analog P0 check N/A (s1web labels carry no severity). Without a
pre-registered bar the bench produces numbers, not a verdict — W1 decides the
bar or explicitly waives verdict in favor of report-only.

---

## 2026-10-04 — Rook target: OrangeHRM local ONLY, 3 preconditions (W2 ruling) (W2)

Triage by expendability (agent WRITES — target must survive it): UrsaMinor
stand OUT (frozen till Monday, no debate); qaeverset-pilot-mini OUT (static
page, no backend — nothing meaningful to write/break; also another track's
instrument); local OrangeHRM (up 4d, db healthy) SOLE candidate.

Three preconditions, all binding before Rook touches it: (1) D3-seed REVERT
verified pristine first (seed still/might-be active from earlier flag — run on
seeded ground voids everything); (2) snapshot/restore protocol (container
recreate = pristine baseline; snapshot before, restore between runs); (3) EXCLUSIVE
window or explicit coordination (OrangeHRM is shared env — Grafana/other tracks;
concurrent use cross-contaminates baselines). W1/owner decide allocation;
W3 executes prep. No W2 action beyond this ruling.

---

## 2026-10-04 — Rook target: NO suitable target, W2 recommendation WITHDRAWN (W2)

W1 vetoed all three incl. W2's OrangeHRM pick (9ad0438) — correctly, on grounds
beyond technical triage: (a) UrsaMinor not just frozen but HERS (adversarial
writes = breach + relationship risk); (b) OrangeHRM pristine = HER repro until
Monday (not free substrate as W2 assumed); (c) qaeverset-mini = paused RUPESH
track instrument (vendor contamination — angle W2 missed entirely; logged as
standing lesson: cross-track instrument reuse needs contamination check, not
just writability). Prior triage entry above SUPERSEDED in recommendation (kept
for audit trail). Load-bearing insight (W1): Rook needs an AGENT target,
candidates are APPS — category mismatch, not shortlist problem. Paths: W3
estimates toy writer-agent stub (hours?) or pilot waits. Direction: owner's.

---

## 2026-10-03 — P2 packs BUILT (S4 + S5 single-row, D2b pattern) (W2)

reviews/openclaw-s4-pack + reviews/openclaw-s5-pack (local-only): one row
each (EQ_NEGATION, B2 provisional-default, Y/pass/open, 3× confirmation
noted in behavior). Both B2 PASS (small-N floor, max 1 at N=1) + score-0%
signal + fix-first, tiers unverified-marked. Gold severity (P2) deliberately
NOT conflated into risk_tier (different axes — severity vs likelihood tier).
Ready as issue bodies (repro + evidence per W3's closeout/confirmation files);
external sends (issues + letter) are owner's buttons, one by one. W2 done;
nothing further pending here.

---

## 2026-10-04 01:49 — Session checkpoint (routine, on request)

Tree was clean, HEAD 0f9e040 pushed. No new substance; standing by on all
fronts (Ursa build/Katya reply, Klarent silence, Aamir pointer, Article 29
post-publish mechanics, recheck 10-17, Victor's sends). Live file under cap
post-rotations.

---

## 2026-10-03 — Sensitivity-extra accepted as reported-extra (W2, light touch) (W2)

Runlog verified (not just relayed): FINAL 11.72% (58/495 — arithmetic holds),
AUROC 0.5000 flat (chance; final lost all ranking — consistent with post-
plateau drift), FAIL stands on both checkpoints, best-choice validated.
Deliberately LIGHTER touch than bench numbers: this extra changes no verdict
(FAIL stands either way; best-choice was already decided on dev-loss grounds),
so full recompute-from-raw is disproportionate — arithmetic + protocol-conformance
check suffices, recorded as such. If anyone contests the 11.72, raw preds get
the full recompute treatment on demand. No W2 action beyond this record.

---

## 2026-10-03 — Touch #3 fully authorized both sides; lock mechanics stand (W1)

W1: reason approved (ephemeral working = structural cause like granularity;
frozen pipeline + fixed weights = nothing to tune toward); variant B needs no
approval (saved preds = zero touches). W2's conditions (recompute-free,
conditional-regeneration, pre-registered bar) all met or exceeded. Touch #3
may proceed under locked-run.py mechanics (SHA gate + reasoned ledger) whenever
W3 executes; variant B (recompute) free at all times. Informational-only stands
(FAIL unchanged either way). No W2 action; lock mechanics already shipped.

---

## 2026-10-03 — Touch #3: conditional approve + recompute-is-not-touch (W2)

W3 stopped correctly (touch discipline working — asked instead of running).
Rulings: (1) Deterministic RECOMPUTE (evaluate.py over saved preds + locked
gold) is NOT a touch at all — no model contact, no new information into any
model, frozen code. Proceed freely, no approval needed, ever. (2) Touch #3
(regeneration) APPROVED conditionally: only if saved preds are truly
unavailable (verify bench-2026-10-02/pred2-*.jsonl first — 1444 rows each were
verified present); reason logged ("ephemeral working loss"); same frozen
mapping; ledger records reason verbatim. Order: check durable copies FIRST
(variant B costs zero touches); regenerate only on confirmed absence.
W1's exception-rationale role acknowledged for the record; code-gate side
needs nothing new (evaluate.py already reviewed).

---

## 2026-10-03 — Paul sketch SENT, ball with Paul (W1 63f2db1 + owner send)

Paul final (concession + capex/opex + regress-terminator, no open questions)
sent by owner; Jason/Bas comment stands (Mo absorbed, zero actions); §10
without looping stands. Rest of W5's announcement parsed by owning windows.
Paul track: awaiting his reply — ball with him. No W2 action (ethics inserts
already in sent text per prior ruling; nothing further until reply).

---

## 2026-10-03 — 5→10 gap: Perplexity right, my check missed arithmetic (W2)

W4 relayed Perplexity catch: batch one had 5 survivors, bench items E1–E10
(ten) — where do the second five come from? Verified composition: E1–E5 =
batch-#1 survivors; E6–E7 = batch-#2 infra-timeouts (tooltip, wa-controls);
E8–E10 = batch-#2 killed reps (preview chips, chat-PR, tab-card). My earlier
"E1–E10 correct" covered DIRECTION (RMT outputs → bench) but never the COUNT
— conceded openly, arithmetic gap real. Worse: draft line 17 ("Ten of the
survivors...") misstates it (only five were survivors). Recommended fix for
W4 (their edit): rephrase to "Five survivors from batch one, plus five hard
cases from batch two — two timeouts and three representative kills — became
bench items E1 through E10..." Perplexity credit recorded: external review
caught what four windows missed.

---

## 2026-10-03 — Draft clarification applied (owner order, W4 to commit) (W2)

Owner: line 15 must state mutants went into TEST code, else reads as app
mutants (against the article's own thesis). Applied one clause in W4's file:
"fifty-eight seeded breaks in test code (never the app)". NOT committed —
Articles tree belongs to W4 (commit/push theirs on review). Change is
additive-clarifying (no numbers/facts altered); revert cost zero.

---

## 2026-10-03 — Leo-RMT draft fact-check: PASS, no corrections (W2 → W4) (W2)

Draft read whole (51 lines + metadata): paragraph = faithful abridgment of
b330adb (example + gate-detail dropped, nothing contradicted) ✓ · usage
numbers all within eadb249 (58/24/53/5, 1+2+2, 22+resolved, guards trio,
91.4-vs-40 with never-blended disclaimer) ✓ · E1–E10 as RMT-outputs-turned-
bench correct ✓ · boundaries section accurate (consent ping required, naming
default-closed with swap points marked, no-MT-comparisons holds — line 13 is
method distinction, not results comparison) ✓. Repost metrics (182/3/1)
not mine to verify (W4/owner lane — stated, not endorsed). No corrections;
draft factually cleared from W2 side. Remaining gates: W1 agreement + consent
ping sent + R1 — none W2's.

---

## 2026-10-03 — D-series pack ASSEMBLED in advance (W1 trigger, W2 built) (W2)

reviews/ursaminor-d-full/ (7 rows, local-only): D1/D2b/D3/D4 seeded (Y),
D2a/D5/D6 as N-controls (correct-behavior/negative-control must NEVER read as
gaps — N, not Y; key semantic preserved from design). Result: B2 FAIL
(small-N floor: 2 survivors > max 1 at N=4) + fix-first D2b/D3 (decisions open)
+ score signal. Build note: unquoted commas in behavior broke parse on first
attempt (strict CSV rejected extra values — parser doing its job); fixed with
quoting, pack clean. Tiers B2 provisional-default throughout (marked).
Held for delivery ON REQUEST (W1 trigger); D2b single-row pack stands as
history, this supersedes it for series reporting.

---

## 2026-10-03 — Bench thread FULLY CLOSED all sides (W3 numbers + W1 d00b786)

W3: FAIL numbers submitted (8.08/8.69, AUROC pair), package pushed. W1: relay
stale, closed by fact — 167eefc predates bench (review-PASSED stands via
a66cde9); "awaiting numbers" superseded by W2's own 394c003 (bit-for-bit
recount + double reading + explicit park). W2 concurs: zero open items.
Locked-bench arc complete end to end (exception → gate → touch → numbers →
independent verify → FAIL → park). Nothing pending W2 anywhere in this thread.

---

## 2026-10-03 — Touch #2 executed + bench closed by fact (W3, for W1 relay)

W3: review passed, touch #2 done (pred2-base/best, 1444 qids each), verdict
FAIL recorded + pushed (bench package 61b6931). Matches W2's verified numbers
exactly (40/43 of 495, +3 els, bar fails). Challenge closed by fact (measured
rows), not by process (authorizations). Full chain complete: exception → gate →
touch → numbers → verdict → push. Nothing pending W2 on this thread.

---

## 2026-10-03 — evaluate.py review: ALREADY DONE, touch #2 fully green (W2)

W1's "review pending" is stale: s1web-evaluate.py (104 lines) + runner-v2
(99 lines, both Oct-2 23:18) were read whole and PASSED days ago (a66cde9:
SHA gate, lenient multi-y, confidence source, RENDER frozen, missing=exit-2,
per-candidate granularity, smoke-first, pinned base, deterministic tie-break
+ 5 non-blocking annotations). Touch #2: W1's exception (done) + W2's code
gate (done long ago) = BOTH conditions met. No review outstanding anywhere;
W3 executes touch #2 whenever ready. Standing by for bench numbers.

---

## 2026-10-03 — Harness already delivered; W1's "awaits harness" is stale (W2)

Verified: scripts/locked-run.py committed 854cd57 (Oct 2), smoke-tested 4/4,
pushed, usage handed to W3 with docs. Tree clean. If bench still waits, the
blocker is NOT the harness — candidates: file transfer to PC, touch #2
execution itself, or stale status. Sent back for re-diagnosis (name the actual
blocker, not the delivered artifact). W2 queue remains empty; standing by.

---

## 2026-10-03 — PC off 24h: PC-dependent paused, nothing broken (W5)

Owner away, PC off: KAN-2, Clef pilot, BaaS/GLiNER paused (stop, not breakage).
Queued for return: Clef Flash 10-min pilot (pull + one gate call). Грётц
(Governance as Code): within pre-agreed rules, no action (like at discretion).
Nothing pending W2.

---

## 2026-10-03 — Disclosure rule: her-removed, ours-counted (owner)

Cost line: removed for Katya's version, counted internally. Recorded as
standing practice (not one-off): external reports sanitized per consent/
no-disclosure rules; internal ledger keeps full numbers always. The two
versions must never be confused — sanitized-for-her ≠ redacted-for-us.

---

## 2026-10-03 — Matrix report cleaned, ready to send (W3; send = owner)

Cost line removed (was present in W3's working copy — my read of the shared
file showed none, so either already-cleaned here or lived in W3's local
version; either way resolved, no conflict to adjudicate). Rotation without
joint tail; stand verified. Report ready for Katya; W3's commit awaits owner's
word (their repo, their rule). Sending to Katya = owner. No W2 action.

---

## 2026-10-03 — Matrix report VERIFIED row by row; cost line already absent (W2)

Read whole (31 lines): D1 CAUGHT / D2a SUCCESS (+6 INVALID setup noted) /
D2b SURVIVED (+nav confound noted) / D4 CAUGHT / D3 SURVIVED (+4 INVALID) /
D5 SUCCESS / D6 PASS — all match W2 records exactly (D2b refinement, D5 7s
norm, D6 control all as ruled). Vendor findings 1–4 with dispositions,
incl. NEW item 4 (secrets:null → literals workaround) not previously in W2
records — logged, no objection. Stand PRISTINE confirmed (D3 seed reverted —
revert flag executed). Prompts set as ruled.

Cost scrub: NO $ figure exists in this file (Costs = Kaggle quota only, no
dollars) — nothing to scrub here; if $1.53 lives in another doc, point W2 at
it, else the scrub item is already satisfied. W1 package text consistent with
file on all checkable claims. No W2 action beyond this record.

---

## 2026-10-03 — Note 1 fact-check: 4× PASS + 1 question (W2 → W4) (W2)

Draft read whole (51 lines + metadata): (1) units labeled everywhere, no bare
95/98 ✓; (2) crash narrative within closeout:11 bounds, hypothesis caveat
present verbatim ✓; (3) B5 scope clean, no engine-feature mixing ✓;
(4) Mapping Limit / lifecycle / appmut correctly absent (Notes 2–3) ✓.
Hook/CTA/author-line left to W4 (format lane, not facts).

ONE QUESTION (not silence): line 15 "Friday's 120-run campaign" — weekday vs
campaign identity mismatch on its face (qa-cube H4 ran Thu 24.09; appmut is 81
rows; no 120-run Friday on my record). Confirm which 120 and which Friday, or
rephrase dateless ("last week's 120-run campaign"). Nothing else blocks;
all other lines verified against closeout/jsonl/rmt.py records.

---

## 2026-10-03 — Matrix CLOSED exemplarily, D6 negative control holds (W1 a024e66)

Recorded: D6 PASS (cosmetics unflagged — no oversensitivity) completes the
full class spread + control. Matrix reads: correct-behavior (D2a SUCCESS, D6
PASS) + catches (D1, D4 CAUGHT) + genuine gaps (D2b, D3 SURVIVED) — calibrated
at BOTH ends (neither fail-everything nor blind). Report: 14h/40 runs/4
findings/$1.53+2.5h T4; stand pristine (freeze-rule met); anchor "39/$1.53"
kept as measured (40th run +~$0.04 post-ledger). W2 concurs: closure complete,
no methodology gaps open on this matrix. Nothing pending W2.

---

## 2026-10-03 — RMT-note facts DELIVERED (W2 → W4, Rule-7 paths+lines) (W2)

(1) RMT one paragraph: Reverse Mutation Testing mutates test VERIFICATIONS
(assertions), not app code — measures whether tests detect deliberately broken
assertions (rmt.py: find_assertions + apply_mutation; rmt-methodology.md).
Differs from classic MT in seeding DIRECTION (system vs verification). Cite:
Leonardo's formulation ("MT challenges the application, RMT challenges the
test" — his doc) + our operator/tier docs for mechanics.
(2) Where used: OpenClaw batches #1 (58) + #2 (24 chains) — pilots/OpenClaw/
results/; E1–E10 gold items ARE RMT outputs (survived negations repurposed as
judge-bench items — pilots/Jev/gold-n30.json); B2-band/batch numbers as in
29th. PUBLIC-NAMING FLAG: joint article anonymized SUT ("open-source agent
runtime") — naming OpenClaw in the new note is a NEW decision (W1/owner), NOT
covered by prior practice; default closed unless explicitly opened.
(3) What's good (numbers only, no MT-comparison — we ran NO classic-MT control,
so "what MT didn't see" is UNLICENSED; state RMT findings absolutely):
batch #1 53/58 killed, 5 survivors adjudicated 1+2+2 (S4/S5 genuine P2 gaps
suites didn't catch); batch #2 22 killed + 2 resolved (incl. caught-by-crash
class); engine guards (NO-OP/soft/chains/stamp) evolved from measured gaps.
(4) Consent RECOMMENDATION (W1/owner decide): 24.09 consent covered name+numbers
IN 29th; new note = new publication → new explicit ping (cheap, kills scope-
creep ambiguity). Draft ping on request. (5) 29th metrics: not W2's (W4/owner
LinkedIn stats lane).

---

## 2026-10-03 03:28 — Session checkpoint (routine, on request)

Tree was clean, HEAD 5599720 pushed. No new substance; standing by on all
fronts (Ursa build/Katya reply, Klarent silence, Aamir pointer, fine-tune
post-29th runs, s1web GLiNER done/VOID, recheck 10-17, Article 29 post-publish,
Victor's sends). Live file under cap post-rotations.

---

## 2026-10-02 — Kaggle explained + post-bank piece delivered (W2 → W4) (W2)

Explainer (concurs with W1 7db5616 on all points): WHY = free GPU (T4x2, $0;
local CPU = hours) + privacy (private kernel/dataset, locked never exposed) +
reproducibility (pins + Save-version; session ephemerality solved by
procedure). DONE = tune complete (2000 steps, early stop, best 6.9470@500) +
bundle intact + SHAs converged both hands + log pulled + bench FAIL honest
(±3 noise). PLANS = none open (bench done; sensitivity-on-final allowed as
extra). PROSPECTS = platform + frozen protocol ready for next training
(any model, same pins/privacy/saves); free-tier limits known-managed. Story
for Leo stands: free hardware + honest negative result.

W2's post-bank piece (as tasked): parked-rationale line — "Tuned 340M changed
nothing measurable on locked test (±3 els noise over N=495 both directions
possible) — parked explicitly, not failed forward; the question stays open
for fine-tune stories with locked tests, the answer stays closed for this
one." Terms framing (privacy on shared infra): "Public dataset under
eval/research terms → private kernel + private dataset + private weights; only
aggregate numbers leave the perimeter, with cite; shared infra never sees more
than it must." W3's run-facts piece is theirs to deliver; W4 assembles.

---

## 2026-10-02 — rmt.py lines CONFIRMED + §3 narrative consistent (W2, W3 review)

On W3's partial (engine lines outside their scope — correctly delegated, not
assumed): rmt.py lines :160/:32/:92/:113/:23/:171 re-confirmed present and
correct in W2's checkout (already verified digit-for-digit in eba3d66; this
entry closes W3's open half). §3 narrative verified for consistency: 10
toggles ×6 + 21 baselines = 81 ✓ · M2/M4/M5/M9 killed ✓ · survivor classes
(honest holes M6/M10, blind M1/M3/M7/M8) ✓ · 40%-vs-91% layers explanation
matches W2's "different instruments" ruling ✓. No new claims beyond verified
numbers; insert as-is. W2's skeleton obligations complete (sections 2 + 4
inputs + line confirmations); remaining: W1 (§§6–7), owner (format).

---

## 2026-10-02 — Section 2 CONFIRMED (W2 → W4): count + units as ruled (W2)

Skeleton section 2 verified against W2 records: B5 scope/numbers ✓ · engine
one-liners with EXACT rmt.py lines (:160, :32/92/113, :23/:171 — match my
re-verification digit for digit) ✓ · chains scope-split honored ✓ ·
S4/S5/S1 with refs ✓ · stamp saga CORRECTED form present (batch1 UNSTAMPED,
closeout stamped :5, confirmation unstamped — never "both carry") ✓ · count
"95 seeded mutants across 98 run-records" with units labeled + arithmetic
(58+24+4+9 / 58+27+4+9, delta 3) ✓ · ledger CERTIFIED entries consistent.
Zero deviations from rulings. W2's section-2 part is DONE; remaining skeleton
needs are W3's (engine §§2,4 confirm + scope), W1's (§§6–7), owner's (format).

---

## 2026-10-02 — evaluate.py + runner-v2 REVIEWED line by line: APPROVED (W2)

Both files read whole (104 + 99 lines). Pre-registered points all hold:
gold multi-y lenient rule + multi_y_rate ✓ · confidence source (native p,
s-transform documented) ✓ · SHA gate hardcoded + refuse ✓ · RENDER_V frozen
marker ✓ · missing-pred hard exit 2 ✓ · per-candidate granularity (v1 flaw
fixed) ✓ · smoke-first with touch banner (debug-location rule in code) ✓ ·
pinned base under adapter (no base drift) ✓ · deterministic argmax tie-break
(first-max) ✓.

5 annotations (analysis/reporting precision, none blocking execution):
(a) multi_y counter mixes zero-gold + multi-gold — split it (zero-gold
always-broken logic itself correct); (b) duplicate qids collapse silently —
one assert recommended; (c) render scope excludes classes/ancestors/siblings —
FINE for base-vs-tuned (identical inputs) but breaks comparability with
qwen-s1web numbers (fuller rendering): record scope, never cross-compare;
(d) classify fallbacks ("no",1.0) need a shape counter; (e) adapter file SHA
into rows/log. Touch #2 may proceed: W1's exception (done) + W2's code gate
(now PASSED) — both conditions met, execution authorized.

---

## 2026-10-02 — RMT-note facts DELIVERED as handover (W2 → W4) (W2)

Recounted from artifacts (not memory): 58 + 27 + 4 + 9 = 98 rows (82 seeded
mutants + 16 run-records); appmut 81 rows separate. Engine lines re-verified
in current rmt.py (docstring 6-8, RMT_VERSION:23, CHAIN_HOPS:32,
find_assertions:79/92, chain-unwrap:113, NO-OP guard:160, stamp in dict:171).
Handover text handed to W4 below; numbers stand as previously ruled (no
re-verdicts inside — pure facts delivery).

---

## 2026-10-02 — 95-vs-98 resolved as UNITS + one stamp imprecision caught (W2)

W3's facts verified with two corrections: (1) 95 vs 98 = MUTANTS vs ROWS
(58 + 24 + 4 + 9 mutants = 95; 58 + 27 + 4 + 9 rows = 98; delta 3 = error-rerun
rows). Both correct — article must LABEL UNITS ("95 seeded mutants across 98
run-records"), never bare "95/98". (2) "Оба вердикт-пака несут 0.1.0" is LOOSE:
closeout carries it (line 5, correct — same engine as seeding); confirmation
carries NO stamp line at all (correct by omission — pre-0.1.0 seeds, nothing
claimed). No falsification anywhere, but the summary sentence must be tightened
to "closeout stamped, confirmation unstamped" before it travels further —
same error class we blocked a letter over. Engine-scope split (W3's point 2)
concurred exactly as drawn (stamp: shared record; NO-OP/soft: W2 delivered
with lines; chains: finding W3 / implementation W2). Meat A concurred (prior
ruling stands).

---

## 2026-10-04 — Concurrent-rotation incident closed, no loss (W2 post-mortem)

During the P2-packs commit, a concurrent rotation moved ~159 lines live→archive
between W2's read and commit — first seen as unexplained -159 deletions.
Verified by presence matrix (P2 live×1; sensitivity/RMT-paragraph/touch#3/
locked-run live×0 + archive×1 each): every entry exists EXACTLY ONCE across
both files; live 26.8K under cap; no duplication, no loss. Rotation itself was
correct and needed. Lesson extends commit-immediately rule: in shared-repo
multi-writer reality, re-read tail + presence-matrix BEFORE committing, and
verify AFTER — reads alone go stale mid-turn. No further action.

---

## 2026-10-04 — Handover hardening consensus complete (W1 de68297 ↔ W2) (W2)

W1 accepts all three tightenings (branch-from-tag, contamination vector named,
tree-clean-at-handover). Consensus is now bilateral and complete: no open
methodology questions on the Rook→OpenClaw handover. Remaining items are pure
execution (W3: branch + tree-clean check + runs) and owner decisions. W2 has
nothing pending on this track.

---

## 2026-10-04 — Agent-target shortlist: OpenClaw first, rest gated (W1 86cc177) (W2)

Concurred in full: closed agents (Cursor/Windsurf/Copilot/Codex) lean veto —
Rook derives scenarios FROM code, no code = no derivation (black-box-mode
question left open as the single cheap resolver); open ones (Cline, OpenCode)
second wave with MANDATORY sandbox (blast radius = repos: file writes + shell
— unsandboxed agent-testing is how you lose a repo); OpenClaw first (ready
today, reset proven, zero blockers). "Don't swap ready for unknown" endorsed
as sequencing discipline. No W2 action.

---

## 2026-10-04 — OpenClaw as Rook target: CONCURRED with teeth (W1 f2a811e) (W2)

Real agent runtime (stream/computer-tool/oauth = Rook's exact domain) +
local + resettable (expendable workflow PROVEN: RMT batches + 60 runs with
reverts) + no freeze/vendor/pause entanglements — best candidate by elimination
AND by fit (only agent in-house). W1's two conditions endorsed as load-bearing,
not hygiene: (a) SEPARATE worktree/branch from RMT-mutated state (RMT seeds
+M-files live in that tree — running Rook on seeded ground voids everything;
branch FROM baseline tag opclaw-baseline-2026-09-29); (b) reset procedure
before first run, logged. W2 addition: verify tree-clean (git status + toggles
off) AT handover moment, not from memory — the tree has hosted 100+ mutated
runs since the tag. No W2 action beyond this record; prep W3 hands.

---

## 2026-10-05 — Routine: discipline move shipped, ledger rows banked, Notes 2–3 checked (W2)

Discipline: quotes.md + digest management W4→W5 in table (`docs/window-discipline.md:12-13`, `23526e6`, pushed). Ledger: 3 Kravchenko rows + 4 qualifiers entered in `ai-qa-wiki/outputs/verdict-economics-ledger.md:20-22` as W5-provided/unverified-by-W2, short link `lnkd.in/p/e3dTH79v` (`cccbde4`, unpushed — push not ordered). Reviews: Notes 2–3 fact-check delivered (Note 2 PASS + N>=20 prose nit, vendor side to W1; Note 3 PASS + Kanaris quotes confirm in W5 bank). D2b: no VOID class in scorer — ruling-now/versioned-implementation-after-split stands, W1 concurred. `verdictgate.py` untouched (split precondition stands).

---

## 2026-10-05 — Routine-2: escape PASS, hygiene CLEAN, D3 design approved, letter unblocked (W2)

Escape draft: re-fact-check PASS (b0a3a1 paragraph per W3 fact-pack, redactions honored) + scale fix one-full-one-partial. Hygiene CLEAN: b0a257 zero hits repo-wide; 4889d6 already dispositioned 10-02 INVALID-wrong-target (`archive:3476-3489`); both CSVs D-rows only. Generated-D3: CONDITIONAL (Confounded rerun hole) → hole closed → FINAL approval verdict-part (W1 approval still gates execution). KAN-10 confound concur + prompt-pin; W1 HOLD (getSecret/finding-#4) concur; b0a3a1 INVALID concur; guards-are-claims rule bilateral. Letter: S4/S5 packs verified issue-ready (local-only, disk paths given), добро to draft (S1 absent, honest line endorsed); avatar probe relayed (45th complete, pins c6001b88/6f92edf0/661af842, unverified-by-W2).

---

## 2026-10-05 — Routine-3: triage in, memory-datum banked, draft re-verified (W2)

Triage (W1→W2): finish accepted, generated-D3 parked with design, escape-fun-fact → escape note (consent Monday), D-series/taxonomy unchanged — concur all. Memory datum banked: persisted escape program in run memory (6ac42686, from_memory replay), non-baselines demolished, New-Chat evidenced; flagged as new draft material for W1/W4. Escape re-read (61 lines): navigateStatus-by-name + third-variant fix + memory paragraph all per record, redactions hold; 1 micro-note (cover TODO vs DONE). 4-nodes-gpt-4.1 relay banked (generate-steps vs llm-1 attribution, Ollama exonerated); monoculture-correlated-blindness concur, diverse-judges-as-dissent noted. Angle-B draft: not my round, S1-absent consistent with my добро.

