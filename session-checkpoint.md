# VerdictGate — session checkpoint (append-only)

> **Rotated 2026-10-03 (8th rotation):** history before this point lives in
> `session-archive-2026-09.md` (appended, same repo). Nothing deleted, order
> preserved. Rotation rule: monthly archive + live tail ≤ 32 KiB.

---

## 2026-10-01 — Decoy-set send BLOCKED on target ambiguity (W1 05ea02a, concurred)

W1: decoy-set file complete (D1–D6 + rules) but "Target: public demo env (URL
in run config)" is ambiguous across three distinct things (local container /
our deploy / foreign read-only demo) — and seeding foreign is never allowed.
W3 must pin the EXACT URL in-file; then send = file + silence-rule +
explicit-yes ask.

W2 concurs as binding: authorization referencing a target by indirection
("URL in run config") is not authorization — indirection is where
seeding-into-foreign happens. Rule: decoy authorization names the target
EXACTLY (literal URL in the authorized file) or it does not authorize.
No W2 action beyond this record; send gated on W3's URL pin.

---

## 2026-10-01 — Commit stands; approval procedure SIMPLIFICATION ordered (owner)

Owner: keep e310a0a (content routine, no harm) — but the self-approved marker
exposed procedure friction: per-commit "давай" rounds on routine log entries
cost more than the accidents they prevent. Approval procedure goes for rework
(owner's track — simplification design, not W2's): goal = keep the protection
(unasked content commits) while dropping the per-entry toll (e.g., session-
scoped standing approval for checkpoint-only commits, hook distinguishes docs
vs code paths). Until reworked: W2 asks "давай" literally every time.

---

## 2026-10-01 — Decoy-env finding ENDORSED + snapshot rule added (W3 plan)

Finding sound: google.com (foreign, nothing to break) + public demo (foreign
read-only) correctly excluded; local OrangeHRM (own container) the ONLY
seedable env — triage by elimination, no objection. Plan endorsed as structured
(owner sends decoy set + silence rule from file; W3 preps matrix-env + KAN
tickets per decoy; seed→runs→verdicts on her yes).

Two appends: (1) snapshot/restore PROTOCOL required on matrix-env (state
snapshot before seeding + restore between mutants — else seeded breaks pollute
each other across runs; same input-identity family as SAM1-6 reset rule);
(2) "silence rule" must be explicit in the sent text (what exactly stays
silent: her team not watching/adapting mid-pilot + findings private till
report — ambiguity here breeds the exact trust breach decoy-consent guards
against). Send = owner; prep = W3. No W2 action beyond this record.

---

## 2026-10-01 — Baseline: 1 PASS / 2 non-success on identical inputs (W3)

Distribution vindicated live: temp-0.7 variance shows 1×PASS + 2×non-success
(broken/failed) on SAME inputs — exactly why ≥3 not one. Per ratified mapping
these two go to the FALSE-ALARM track (specificity), never into survivors.
Tokens 3 runs: in 13,889 / out 814 ≈ $0.01–0.05 total — R1 calm with real data
(caps untouched). Caution for mutant phase: baseline itself 1/3 green means
verdicts must read against the distribution (a mutant "failing" where baseline
also fails is weak evidence) — W3's verdict pack must carry this context, else
mutant verdicts overclaim.

SAM1-6 status check relayed to owner (token his): pass-branch auto-transition
may have moved it to Done — check + revert if so (or W3 records as site-effect
in reset protocol). Awaiting owner's one-liner.

---

## 2026-10-01 — Ticket To Do VERIFIED (W3 checked post-revert); approval routing

W3 verified SAM1-6 back at To Do via API after revert — status item CLOSED
(verification predates this entry). Baseline entry (distribution vindicated,
false-alarm track, R1 calm, mutant-phase caution) stands as written, commit
pending owner "давай" (commit-guard: no self-approval).

Approval routing (load-bearing): commit approvals are PER-AGENT-SESSION by
design — W2 cannot proxy-approve W3's commit nor vice versa, else the guard is
theater. W3's pending commit needs Victor's explicit words in W3's own channel;
mine needs them here. Two separate "давай", no shortcuts.

---

## 2026-10-01 — Reset-(a) VALIDATED end to end, token saga closed (W3)

W3: total 0, all 13 history comments deleted, NO tombstone (delete-cleanliness
precondition verified in practice, not just once) → ticket pristine. Reset-(a)
(API-delete) works like clockwork including the tombstone question. Token saga
closed: death diagnosed → renewed → verified working (comments listed AND
deleted through the new token). Standing rules confirmed by use: recorded
expiry pending (still owed — next lapse must be predictable), reset logged per
run from here on. No W2 action; track back to measuring.

---

## 2026-10-01 — URL pin ACCEPTED (re-recorded; lost in push-timeout turn)

W3 pinned exact target URL (host.docker.internal:8080/…/login, verified 200
from BaaS container); W3 pushed 84f7094. Rule satisfied: authorization names
target literally. Send package complete (file + silence + explicit-yes);
sending to Katya = owner. Note: this acceptance was written once before and
lost to the push-timeout turn — re-recorded here; working-tree-only content
is volatile until pushed (same lesson as incremental saves).

---

## 2026-10-02 — Katya reply: misconfig was OURS, revert + minimal fix (W2 record)

(1) setValue directive stands (unchanged). (2) Ollama dead = OUR misconfig,
not her bug: 3 lines (LLM_Client + URL + API-key, single client) were never
properly uncommented/filled on our side — her "should work" + "don't waste
time" closes it as setup error. Prior "environment coupling" note SUPERSEDED
by this (coupling claim was built on broken config — retract the defectward
half, keep the portability note as untested). (3) "Верните как было": W3 must
diff current BaaS env/config vs pristine, find the divergence, revert, record
what it was — unknown-divergence-resolved-by-revert, no investigation beyond
identification. (4) Deprioritized by vendor herself — minimal fix path: uncomment
3 lines → retest once → move on. Tone (:))) = engaged, not annoyed; reply
briefly with found-and-fixed, zero defensiveness (owner channel).

---

## 2026-10-02 — Owner decision: probe decides, setValueN next after KAN-5 (Victor)

Owner concurs: no text-arguing; on KAN-5 completion → llm-1 to setValueN →
login probe. Outcome requalifies BOTH W2's bank (defect-confirmed vs
usage-corrected) AND the her-SAM1-6 question (ask what her PASSes ran on, with
probe results in hand — combined ask, single round trip). Sequence locked:
KAN-5 finishes untouched → swap → probe → requalify → ask. No W2 action;
standing by for probe numbers.

---

## 2026-10-02 — setValueN identified; KAN-5 untouched mid-run (W3, concurred)

setValueN (deterministic) distinguished from dead llmSetValue — precise catch,
no confusion between them. KAN-5 finishes as-is under workaround (mid-run
changes contaminate; recorded-under-workaround stands). Next iteration to
setValueN per probe order. One binding caveat: setValueN's event-sync is
ASSUMED ("видимо") — the probe VERIFIES it (login SUCCESS); switched ≠ fixed
until measured. If SUCCESS → vendor-native path, crutch removed, bank flips to
usage-corrected. If FAIL → back to analysis (assumption falsified, new cause
sought). Ollama point correctly sequenced after (one variable at a time). No W2
action.

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

