# Orangepro fixture (demo-orangehrm)

A real Orangepro (OrangePro) mutation report used to validate the future `--import opro` path.
Nothing here is hand-authored to look like a schema: `reports/graph.json` is the output of an
actual run of Orangepro against the OrangeHRM codebase.

## Files

```
reports/
  graph.json              real captured Orangepro knowledge graph (schema_version: orangepro.local_graph.v2)
  report-baseline.json    summary (122 behaviors, 0 proven, 14 candidate, 108 no signal)
  rtm.md                  traceability matrix (122 behaviors)
  proof-attempts.json     proof attempt ledger (0 attempted)
  config.json             workspace config
  resolver-cache.json     resolver cache
  parse-cache.json        parse cache
```

The captured report contains **122 behaviors** from the OrangeHRM codebase: 0 dynamically proven,
14 candidate, 108 no integration signal, 1 reachable-untested. The `riskPaths` array lists the
top risk paths (admin, maintenance, claim, etc.).

`graph.json` is the authoritative artifact. Orangepro mutant ids are specific to a run and are
renumbered when the source changes: after regenerating, rebuild the fixture from the new run
before using it.

## Regenerate

```
npx @orangepro/mcp-server@latest start <path> --no-ai
# Output: <path>/.orangepro/
# Copy .orangepro/* to reports/ and scrub paths (replace absolute with '.')
```

## Scrub

Scrubbed with: `grep -E 'Users|/tmp|scratchpad|AGENTS|PRECONDITION'` (all matches are false positives:
test names containing "Users", filename "AGENTS.md" — legitimate content, not sensitive info).
