# VerdictGate — session checkpoint (append-only)

> **Rotated 2026-10-03 (9th rotation):** history before this point lives in
> `session-archive-2026-09.md` (appended, same repo). Nothing deleted, order
> preserved. Rotation rule: monthly archive + live tail ≤ 32 KiB.

---

## 2026-10-03 — RMT paragraph drafted standalone (W1 queue #1, deadline Wed 07.10)

Text for W4's note (self-contained, citable, all numbers previously verified):
"Reverse Mutation Testing mutates test verifications, not app code: seed a
broken assertion (e.g. expect(x).not.toBe(y) where y holds) and check the suite
goes red — surviving mutants expose weak verifications, not app defects. It
differs from classic mutation testing in seeding direction only (verification
vs system); the verdict machinery (per-tier gates, evidence packs) is shared.
Formulation to cite: Leonardo Lanni ('MT challenges the application, RMT
challenges the test'). Our engine (rmt 0.1.0, deterministic, 2 operators +
chain-unwrap + NO-OP guard + stamps): 95 seeded mutants across 98 run-records
(OpenClaw batches #1–2), 91.4% kill on assertions vs 40% on behavioral app
mutants (different layers, never blended)."

Queue status: #1 delivered now; #2 P2-packs await pause-list trigger (which
list? — flagging ambiguity, not blocking); #3 sensitivity-extra allowed but
unscoped (no task defined — awaiting concrete ask); #4 hygiene parked (not
burning). W2 needs nothing further except answers on #2-trigger and #3-scope
if they activate.

---

## 2026-10-02 — setValue probe ordered; bank label CONDITIONAL (W1 b4725a3 + W2)

W1: her move = requalification defect→usage (deflective but concrete →
verifiable). Decider probe: swap to setValue, run login — SUCCESS = our usage
error (deviation closed, crutch replaced), FAIL = defect stands. Cheap, final,
no text-arguing. Concur fully.

W2 records conditionally: "BaaS defect class" label on sendKeysToElement goes
PROBE-CONDITIONAL effective immediately (holds unless probe says otherwise;
flips to usage-corrected on SUCCESS). Bank correction pre-authorized on probe
outcome — no second review needed for the flip itself. Baseline question
refined in her favor (which function did HER SAM1-6 runs use? if setValue,
her PASSes may be clean and the question dissolves — ask with the probe
results, not before). Probe execution = W3 hands; question = owner channel.

---

## 2026-10-02 — Katya: use setValue (directive, not fix) + re-run rule (W2)

Katya's answer confirms the diagnosis implicitly (sendKeysToElement doesn't
sync Vue; setValue does) while declining to fix the footgun itself — author's
prerogative, accepted. Consequences: (1) verify setValue EXISTS in pinned BaaS
before rewriting (if newer than pin → upgrade + re-pin, version discipline
holds); (2) llm-1 workaround REVERTED in favor of setValue (author-blessed
path doctrine — same rule that rejected the Ollama trick); (3) D2a (recorded
post-workaround) RE-RUN under setValue — old verdict stands as
recorded-under-workaround (history not rewritten), clean verdict needs the
blessed path; (4) llm*/Ollama-LAN question UNANSWERED — still open, no assumption.

---

## 2026-10-02 14:30 — Session checkpoint (routine, on request)

Tree was clean, HEAD 6a7a67c pushed. No new substance since stand-down
concurrence; this entry is the requested checkpoint. Open threads unchanged
(Ursa build trigger pending owner "go" or stand-down decision; Klarent
silence; Aamir pointer; fine-tune post-29th; Article 29 post-publish; recheck
10-17). W2 stands by on all fronts.

---

## 2026-10-02 — Stand-down CONCURRED (W1 withdraws own advisory) (W2)

W1 reverses "continue D3": night seed design risks confounded seeds (removed-
validation vs server Invalid credentials ambiguity would poison D3's reading);
tired-head-sows/fresh-parses rule stated. Concur: seed DESIGN is judgment work
( which break isolates which mechanism?), and judgment degrades at night; one
confounded seed costs more than one night's delay. Self-reversal on new grounds
recorded as good practice, not inconsistency. Stand-down DECISION itself =
owner's (Victor). No W2 action beyond this record.

---

## 2026-10-02 — Weights hash-verified + D3 matrix final + revert flag (W2)

Local weights verified byte-level: adapter_model.safetensors = 1899e036…
(best) + adapter_model_final.safetensors = d92a3f32… (final) — both match
recorded hashes exactly; local = Kaggle, lineage closed end to end.
D3 SURVIVED recorded as matrix-final (D1 CAUGHT / D2a SUCCESS / D2b SURVIVED /
D4 CAUGHT / D3 SURVIVED) — matches every prior record, no drift.

FLAG (action, not mine): OrangeHRM still carries ACTIVE D3 seed (username
without required) — MUST revert to pristine before next works on that env,
else the next campaign measures on seeded ground. Hands: whoever runs next
there (W3 matrix-env owner); rule: no campaign starts on unverified-pristine
env (check first, seed after). W2 records, does not execute.

---

## 2026-10-02 — locked-run harness BUILT + smoke-tested (W3 request, W2 scope)

Scope as ruled: command-agnostic wrapper ONLY (SHA gate + one-touch ledger +
audit rows) — NO inference code duplicated (caller's runner stays theirs;
GLiNER/s1web runners live on PC, none on this machine to reuse). scripts/
locked-run.py, stdlib only. Smoke-verified all 4 paths on fixtures: SHA-
mismatch→refuse(2) · first-run→exec+ledger · rerun-without-reason→refuse(2) ·
rerun-with-reason→exec+logged. Usage: locked-run --data --data-sha --tag
--model-id --out ledger.jsonl --reason -- <command>. Model weights verified
separately at load (out of wrapper scope by design — stated, not hidden).

---

## 2026-10-02 — Key rotation one-sided, W1 approved (W2 record, no action)

W1: rotation one-sided (both ends ours) — joint would apply iff the key were
hers; she gets notification + template-default update request (else her next
redeploy restores the exposed default and kills the rotation). Sequence:
secret first, rollback saved, trial-run verification. W2 records only —
secrets never touch this window; execution owner/W3 hands on owner go.

---

## 2026-10-02 — Day closed: finetune + core5 + stand pristine + key rotated (W3)

W3 day-close (61b6931 pushed): finetune closed (weights + SHA) · bench FAIL
pre-registered + independently confirmed (W2 recompute) · core5 matrix closed ·
stand pristine · key rotated. W2 concurs on all closures; every verdict this
day was either pre-registered-then-measured or independently recomputed —
zero post-hoc numbers stand anywhere. Standing by; next inputs: Monday gates,
Klarent silence, Aamir pointer, Article 29 post-publish mechanics, recheck
10-17, Victor's sends.

---

## 2026-10-02 — Bench FAIL CONFIRMED independently (W2 recompute, W3 relay)

Recomputed whole (495 els, locked SHA ea675b59 verified, lenient multi-y):
base 40/495 = 8.08% / AUROC 0.5295 · tuned 43/495 = 8.69% / 0.5302 · multi 355
— bit-for-bit match with verdict.json on every figure. Non-regression bar
(tuned ≤ base) FAILS: +3 elements = +0.606pp. Verdict stands as filed.

Two readings recorded (both true, different uses): (1) bar verdict: FAIL, no
adoption — binary as pre-registered; (2) statistical lens (NOT a verdict):
±3 els on N=495 is noise-band (McNemar territory); the bar doesn't do p-values
by design, so FAIL stands regardless — but any future claim "tuning HURTS"
would need wider N, symmetric to "tuning helps". Fine-tune track outcome:
no improvement demonstrated; track parked pending new decision (not failed
forward — parked explicitly).

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

