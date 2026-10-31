# Orangepro fixture (demo-orangehrm)

A real Orangepro (OrangePro) run artifact used to validate the future `--import opro` path.
Nothing here is hand-authored to look like a schema: `reports/graph.json` is the output of an
actual run of Orangepro against the OrangeHRM codebase.

## Files

```
reports/
  graph.json              real captured Orangepro knowledge graph (schema_version: orangepro.local_graph.v2)
  report-data.json        summary (113 mapped, 110 ranked, 0 proven, 4 linked, 11 unconfirmed, 98 none)
  rtm.md                  traceability matrix (113 behaviors)
  proof-attempts.json     proof attempt ledger (0 attempted)
  config.json             workspace config
```

The captured report contains **113 behaviors** from the OrangeHRM codebase: 0 dynamically proven,
4 linked, 11 unconfirmed, 98 no integration signal, 1 reachable-untested.

`graph.json` is the authoritative artifact. Orangepro mutant ids are specific to a run and are
renumbered when the source changes: after regenerating, rebuild the fixture from the new run
before using it.

## Provenance

- **Tool version:** @orangepro/mcp-server 0.2.58
- **Node version:** v24.15.0
- **Command:** `opro start . --no-ai`
- **Tree hash:** 0ba17497dc4211b2b658d0417f5cec16c2cedb84 (clean worktree, no uncommitted changes)
- **Run date:** 2026-10-31
- **Source:** OrangeHRM-orangepro-compare (clean worktree at 0ba1749)
- **Two runs verified byte-identical** (modulo wall-clock timestamps + scope id)

## Regenerate

```
npx @orangepro/mcp-server@0.2.58 start <path> --no-ai
# Output: <path>/.orangepro/
# Copy .orangepro/{graph,report-data,rtm,proof-attempts,config}.json to reports/
# Scrub paths: replace absolute paths with '.'
# Do NOT commit parse-cache.json, resolver-cache.json, last-start.json, ledger.json
```

## Scrub

Scrubbed with: `grep -E 'Users|/tmp|scratchpad|AGENTS|PRECONDITION'` (all matches are false positives:
test names containing "Users", filename "AGENTS.md" — legitimate content, not sensitive info).
