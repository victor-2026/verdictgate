# Window discipline (5 windows, effective 2026-09-22)

Mutation work is cross-cutting; recording is split. One file = one owner.

## Windows and ownership

| Window | Owns (writes) | Must NOT write |
|---|---|---|
| W1 Rupesh Commercial | Rupesh/* (Positions-CV-CL outreach tree) + client×product registry + monetization proposals + per-vendor strategy (stage, next step, owner) + joint promos. Commercial wording/pricing final word stays W1. Other windows feed facts, never negotiate. | verdictgate/**, 28 draft, Aamir/*, OrangeHRM* |
| W2 Product | verdictgate/** + Article 28 draft + DevAssure pilot (frozen, unassigned elsewhere) | Rupesh/*, Aamir/*, OrangeHRM* |
| W3 Pilots | company/pilots/** (all pilots) | Rupesh/*, verdictgate/**, 28 draft bodies |
| W4 Articles | Articles/linkedin-posts/** + Articles/wiki/** + quotes.md (shared bank) | verdictgate/**, pilots/**, outreach/** |
| W5 Career+Wiki | LinkedIn headline/career + post teardowns + Obsidian wiki + person↔company↔wiki links (paths: W5 to specify) | verdictgate/**, article bodies, pilots/** (reads only) |

## Rules

1. One file, one owner. If a file you need belongs to another window, send a text handover — do not edit across the boundary.
2. ai-qa-wiki raw/ + topics: shared inbox, append-only (new files + new topic entries; never rewrite another window's entries). raw/ = evidence inbox: immutable sources behind cited claims (transcripts, article texts, evidence). Link-only refs allowed for pointers without ingest: URL + date + one-line why, filed in the routing note — no raw file required (precedent: JevBench 23.09).
3. Checkpoints: append-only sections with timestamp; never rewrite чужые секции.
4. Handovers between windows are plain text (this chat), not file edits.
5. Atlas provenance: QAEverest-Capability-Atlas.pdf lives in Rupesh catalog (W1); a provenance pointer (not a second copy of the PDF) may be referenced from the qaeverset profile spec in W2. Vendor numbers cross the boundary only as verbatim quotes with source.
6. Compound loop (adopted 2026-09-21 from EveryInc): `brainstorm → plan → work → simplify → review → compound`. Simplify is mandatory before review (dedup, refactor). Review is `review-against-plan` (report-only, Pi reviewer vs `window-discipline` + `per-risk-tier` plan) before merge. Compound via `wiki/` + `session-checkpoints` + `docs/solutions/` per feature.

## Pilot Handover: W5 → W3 (Explicit)

**W5 (Career+Wiki)** discovers pilot leads, gathers source material, writes draft index.md with hypotheses.
**W3 (Pilots)** executes pilot, runs experiments, validates hypotheses, updates index.md with results.

**Flow:**
1. W5 finds lead → creates `company/pilots/<Tool>/index.md` (draft) + `outreach/active/<Author>/index.md`
2. W5 → W3 handover: plain text in this chat with pilot brief + hypotheses
3. W3 executes pilot → runs experiments → updates `company/pilots/<Tool>/index.md` with results
4. W3 → W5 handover: results summary + artifacts for wiki/articles

**Current Pilot Assignments (W3 owns company/pilots/**):**
- **FlowScout** → Igor Akymenko (Founder **Alternate QA**, https://alternateqa.com/) — `company/pilots/FlowScout/`
- **qa-cube** → Vadim Glushonkov (product **qa-cube**, personal project) — `company/pilots/qa-cube/`
- testRigor → Adam Pierce — `company/pilots/testRigor/`
- Agentiqa → — `company/pilots/Agentiqa/`
- DevAssure → — `company/pilots/DevAssure/`
- QAEverest → Rupesh Kabra — `company/pilots/DevQaExpert/` (redirect from Rupesh catalog)
- testMu → — `company/pilots/TestMu/`
- Autonoma → — `company/pilots/Autonoma/`

## Company Clarifications (per outreach/active/)

| Pilot | Product | Company / Author | Company URL |
|-------|---------|------------------|-------------|
| FlowScout | **FlowScout** | **Alternate QA** (Igor Akymenko, Founder) | https://alternateqa.com/ |
| qa-cube | **qa-cube** | Vadim Glushonkov (personal project) | — (works at Fintech Net) |
| testRigor | testRigor | testRigor Inc. | — |
| Agentiqa | Agentiqa | Agentiqa | — |
| DevAssure | DevAssure O2 | DevAssure | — |
| QAEverest | QAEverest | DevQaExpert (Rupesh Kabra) | — |

