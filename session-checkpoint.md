# VerdictGate — session checkpoint (append-only)

> **Rotated 2026-10-01 (proof-of-pattern):** history before this point lives in
> `session-archive-2026-09.md` (2868 lines, same repo). Nothing deleted, order
> preserved. Rotation rule: monthly archive + live tail ≤ 32 KiB.

---

## 2026-09-30 — Zero-refs verified; reset (a)-with-verification endorsed (W2)

W3 grep-verified (not "looks like"): icos-dev refs 0 → transitions ON
technically allowed. testkatja remnant correctly classified (demo-app login
fixture, not her tracker, not secret) + correctly untouched (altering it
changes the tested flow) — endorse leaving as-is, recorded.

Reset variant ruling: (a) API-delete-comments primary is sound (one ticket,
controlled state) WITH one precondition — verify delete-cleanliness once
(delete a test comment, re-read, confirm zero render residue; Jira deletes can
tombstone). If residue → (b) fresh templated ticket per run. (b) stays
fallback as proposed. Post-back comments are the ONLY state mutation in play
(transitions move status, reset covers both — reset procedure must restore
status AND clear comments, logged with timestamps per run). W1's go-ahead
remains the trigger; W2's mechanics TROUBLE-free on (a)-with-verification.

---

## 2026-09-30 — Transitions flag: conditional ENDORSED + reset mechanics (W1 ab5dfb1)

W3 wired new step (90d8d11, placeholders 0, no secrets) + flagged auto-Done
side effect. W1 conditional: victor-qa-only → ON with reset-between-runs;
any icos-dev ref → OFF till her explicit OK; demands explicit zero-refs
confirmation (not "looks like"). W2 concurs fully + two appends: (1) reset is
load-bearing for comparability (run N+1 must read the identical ticket as run
N — same family as same-tree/determinism; without it both baseline distribution
and mutant deltas lie); (2) reset procedure itself must be deterministic +
logged (manual clicks/API — either fine — but a flaky reset injects variance
indistinguishable from SUT behavior; log each reset with timestamp).
Her-tracker boundary (never touch on implied consent) stands absolute. No W2
action; W3 owes the zero-refs confirmation + reset procedure.

---

## 2026-09-30 — Ursa comms closed ×3, typo-protocol applied (W1 5bc256d + W3)

Recorded: (1) placement after http-jira-comment on engineering grounds
(post-back needs live browser; early free gains nothing; stop-node cleans) —
endorse reasoning, execution W3's; (2) "brunch-success" held as chat-typo
until file-verified (exact id from files only) — endorse as transcript≠receipt
discipline in practice, same class as reporter-words rule; (3) new-build fetch
location open (question to Katya via owner); setup frozen till files land.
W3 synced on all three. No W2 action; next touchpoint is build files arrival
or Katya's reply.

---

## 2026-09-30 — W3 position synced, one owner question pending (no W2 action)

W3: http-last already after http-jira-comment (matches recommendation, nothing
to move) · "brunch-success" baked nowhere pending exact id from files ·
new-build files awaited (fetch source = question to Katya through owner) ·
setup frozen till files arrive. W2: nothing to rule here — node ordering and
id-gating are execution detail inside the ratified mapping (binary + buckets
unchanged). Single open item belongs to owner: ask Katya where new build
files come from.

---

## 2026-09-30 — Katya: swagger + cleanup endpoint (W2 routes to W3)

Katya: BaaS swagger at /API/swagger; /API/async/sessions/cleanup exists. Two
uses, both W3's hands: (1) cleanup endpoint = the OFFICIAL zombie-killer for
the pending confound audit (audit + kill zombies + clean re-measure — no more
pkill-style ops); (2) swagger = self-serve discovery surface (timeout params?
session knobs? warm-session flags?) — read before asking Katya anything
further, every answered-by-docs question spared is relationship capital.
Record cleanup usage per run (which endpoint, when) in run log hygiene. No W2
action.

---

## 2026-09-30 — TPM wall: (2) primary + (1) fallback, W3's order concurred (W2)

Deterministic 429 (39,013 > 30,000 Tier-1; screenshots eat; retries futile —
correctly not retried). First hard R1 number: Tier-1 insufficient for executor
steps as designed. Order concurred exactly as proposed: (2) her $5-fallback
primary (pre-registered conditional; same stack, her key, bounded — cleanest
methodologically, no SUT alteration); (1) mini as fallback question (model
change = SUT alteration: verdict would cover mini-executor, not her stack —
needs her consent + protocol record, hence fallback not primary); (3) prompt
surgery only on her explicit direction (vendor design untouched otherwise).
Message ownership: technical substance W3, wording/send W1/owner (draft
question is theirs to split). No W2 action beyond this record.

---

## 2026-09-30 — Katya replied fast, technical: zombie-confound check FIRST (W2)

Her 6 points mapped: (1) which agent → answer factually (Test Orchestrator,
W3 states exactly); (2) timeouts set at session start (her belief) → ask for
exact parameter name/location (actionable, kills knob search); (3) "client
leaving" → explain ours (curl 120s / studio 30s gave up waiting); (4) 30s
disconnect harmless + reuse session via new requests → ADOPT as protocol
(record session-reuse pattern per row); (5) navigate-slow cause = TOO MANY
OPEN SESSIONS (zombie history!) → CONFOUND CHECK BEFORE ALL ELSE: audit +
kill zombies, re-measure ONE clean navigate — if 2–4 min was OUR resource
exhaustion, the cold-tax finding falls and must be retracted, not softened;
(6) connector-starvation warning on complex objects → SUT-side constraint
recorded (seeded breaks on complex objects risk starvation-confound; keep
seeds simple or record complexity).

Order: zombie audit + clean re-measure FIRST (W3, determines whether 2–4 min
stands); reply second (W1/owner channel, with audit numbers either way —
"found N zombies, clean navigate = Xs" or "no zombies, 2–4 min stands").
Her engagement speed + technical depth noted as green flag for the track.

---

## 2026-09-30 — Reframe: not death but slowness; 5 runs INVALID, not survived (W3)

W3 breakthrough: BaaS completes trivial navigate in ~2–4 min (`async execution
finished` AFTER client timeouts: curl 120s, studio 30s). All "HTTP timeout 30s"
= impatient clients, not dead runs. W2's timeout locus confirmed, nature
corrected (latency tax, not ceiling bug).

Binding consequences: (1) the 5 dead runs are UNOBSERVED — excluded from every
verdict set, never counted as survived (absence of observation ≠ observation
of absence; same class as N-scope discipline); (2) cold-Chrome tax (~2–4 min)
recomputes campaign economics (N × repeats × minutes + OpenAI $ while waiting
— R1 cost cap needs re-estimation on real $/run incl. wait); (3) knob search
(studio/backend) + warm-sessions question to Katya are the two correct next
moves, in that order (self-serve first, ask second); (4) Katya message stays
facts + two questions (cold 2–4 min measured, studio 30s → DOA; warm sessions?
timeout knob?) — friendly setup-feedback, owner channel. Earlier smoke
screenshot noted as accidental window-fit (variance honesty).

---

## 2026-09-30 — SAM1-6 comments: 0 (owner-ran; token absent from agent env)

Owner executed the Jira comments probe himself ($JIRA_API_TOKEN not present in
agent env — hygiene holds): **0 comments** → runs die BEFORE post-back.
Combined with 5× dead-on-30s + working Jira-read/BaaS/key: 30s-timeout
hypothesis (long BaaS call vs http-node default) stands uncontradicted.
Bonus hygiene: ticket state unpolluted (no stray post-backs to clean).

W2 decision order for W3 (cheapest first): (1) http-node timeout knob — raise
+ rerun if configurable (5 min, reversible); (2) split program into chunks if
not (record as protocol note — chunking shifts timing semantics slightly);
(3) Katya question with exact log only if 1–2 fail. No W2 action.

---

## 2026-09-30 — OpenAI key needed NOW (W3 root-cause; owner action, 2 min)

W3: llm-generate-steps hardwired provider=openai/gpt-4o; missing key = silent
hang (the 30s timeouts' source, not BaaS/Jira). BaaS/Ollama covers browser
part only. Ollama-trick correctly rejected (author's tested path first;
compat deviations only on proven need — otherwise confounded attribution).
Tier-1 key, $5 cap held, first smokes measure real $/run (R1 gets data).

W2 notes: (1) root cause = hypothesis pending confirmation — SAM1-6 restart
after key entry confirms (hangs gone) or refutes (triage resumes); record
either way; (2) silent-hang-on-missing-key is itself a report-worthy product
finding (misconfig surfaces as hang, not error) — log it, don't score it;
(3) key entry is owner's hands (his key, studio UI) — no W2/W3 action exists
here. Awaiting owner's 2 minutes, then SAM1-6 restart.

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

---

## 2026-10-01 — Cat-GPT handover FILED as product reference (W5 text verbatim)

Product reference: PaulWaltersDev/Cat-GPT (Apache-2.0,
https://github.com/PaulWaltersDev/Cat-GPT) — eval-harness pattern: DeepEval
(GEval + toxicity, with/without guardrails ablation) + input/output guardrails
+ Arize AX tracing around a single-file agent loop. Relevant as a minimal
reference for evaluator + guardrail wiring. No contact with author; observation
only. Filed here (not a new file — pointer-grade, one paragraph suffices;
graduates to docs/ only if actually wired into product).

---

## 2026-10-01 — W5 triage batch: Cat-GPT ref + Paul peer + Alden comment (no W2 action)

Recorded, all W5-assessed: Cat-GPT filed as eval-harness pattern reference
(DeepEval + guardrails + tracing + ablation — honest educational stand, not a
breakthrough; for product side awareness). Paul Maxwell-Walters: valid evals
peer, low contact priority (geo), meetup/speaking door noted — contact call is
W1/outreach territory, not W2's. Alden comment draft endorsed as-is (seeded
regression check for prompts + "can't show reds hasn't earned green" = our
mutation doctrine applied to prompts, on-brand for Victor's thread; send is
Victor's). No review ask inside — logged for awareness only.

---

## 2026-10-01 — SAM1-6 API-invisible: state change mid-session, diagnose don't delete (W2)

Sequence: GET returned total:0 → later same GET returns "Issue does not exist
or permission" · DELETE same error. Something changed BETWEEN measurements
(not the comment — the issue/site/token visibility itself). DELETE reruns are
STOOD DOWN until diagnosed (deleting blind risks masking the real change).

Owner decision tree (2 min, cheapest first): (1) browser-open SAM1-6 logged in
as Victor — visible? YES → API/token-side (step 2), NO → site/issue-side
(step 3); (2) `GET /rest/api/3/myself` — 401 = token dead (reissue/rescope),
200 = project-permission scope (fix scopes); (3) site admin/billing check —
trial lapse would ALSO threaten pilot substrate (own trial = infrastructure),
escalate priority if so. Reset discipline suspended pending diagnosis (nothing
to reset until visibility restored); ticket-state question moot meanwhile.

---

## 2026-10-01 — First E2E verdict: llm-2 FAILED correctly (W3, track → measuring)

Full loop closed: Jira read → steps generated → browser ran → llm-2 FAILED
with SOUND reasoning (screenshots show Google search, not the app — decider
caught the mismatch, exactly its job) → post-back comment 10012 → session
stopped via http-last. Fixes en route recorded (Bearer→secret, Provider
default, timeout patches, memory collection+page, warm sessions). Methodology
note: first verdict is a CORRECT REJECTION on wrong-app screenshots — baseline
green means the loop works, not the app. Reset pending: delete comment 10012
(owner hands, token) → ticket clean. Track Ursa: assembly → works/measuring.

---

## 2026-10-01 — Hooks proposal APPROVED with guarantee-grading (W5/W1 relay)

Order 1+2-then-4 approved. Guarantee grading (honest, expectation-setting):
secrets-deny = REAL enforcement (auto-deny pre-prompt, strongest item, zero
friction); raw-guard + commit-guard = FRICTION + audit, not hard security
(protects against accident — the actual failure mode — not adversary);
wiki-lint = hygiene automation; compacting-inject = highest P1 leverage
(context killer); session routines last. W5 writes plugin 1. Noted cost: my
own commit/push routine now gates on explicit user words per session (stop-rule
#6 as code) — accepted deliberately.

