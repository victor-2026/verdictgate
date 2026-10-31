# OrangePro fixture (OrangeHRM demo)

Captured output from a real OrangePro run on the OrangeHRM demo snapshot. The JSON payloads
are generated artifacts with only machine-local paths normalized; no report schema was
hand-authored.

## Contents and evidence

- `reports/report-data.json`: tool `0.2.58`, analyzer `orangepro.analyzer.v10` (:8-9); counts are
  113 mapped, 110 ranked, 0 proven, 4 linked, 11 unconfirmed, and 98 with no signal (:26-39).
- `reports/graph.json`: graph schema `orangepro.local_graph.v3` (:2); 485 nodes and 440 edges.
- `reports/rtm.md`: 113 denominator behaviors and status distribution (:7-15).
- `reports/proof-attempts.json`: schema v2, 5 attempts, 0 proven (:2, :22-25). Attempts are
  recorded as unrunnable because the test runner was unsupported; this is not proof evidence.
  Its `git_dirty: true` records OrangePro-generated output files; the pre-run Git status was clean.
- `reports/config.json`: local-only output; uploads disabled and source snippets excluded (:4-7).

## Provenance

- Source pin: `0ba17497dc4211b2b658d0417f5cec16c2cedb84`.
- Fixture tree: derived commit `d88b80e70998d7223b92eb0d6e43dc8d7e0fff2f`, whose only source changes
  remove the two documentation files before analysis. Tree hash: `2e58aa0158cfd4807a5c3e21e65c8dbf6db26e01`.
- OrangePro shim: `@orangepro/mcp-server` 0.2.58; engine: `@orangepro/orangepro-mcp` 0.2.58.
- Node: v24.15.0.
- Command, run twice in the same worktree: `node @orangepro/mcp-server@0.2.58/bin/mcp-server.js
  start --no-ai --fresh --json .` (shim and engine both pinned to 0.2.58).
- Pre-run status gate printed `CLEAN-OK` for each run. OrangePro-generated `.orangepro/` files
  were removed between runs before checking cleanliness again.
- Surface gate: pin and derived runs both report 113 mapped / 110 ranked and 113 RTM behaviors.
- Repeatability: report-data, RTM, config, and proof-attempt payloads match after removing wall-clock fields;
  graph payload matches after removing generated/verification timestamps.
- Scope: output files only; parser and resolver caches, runtime ledger, and generated HTML are omitted.

`SHA256SUMS` records hashes of the final scrubbed fixture files.
