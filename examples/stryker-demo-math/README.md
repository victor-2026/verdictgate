# Stryker fixture (demo-math)

A real StrykerJS mutation report used to validate the future `--import stryker` path.
Nothing here is hand-authored to look like a schema: `reports/report.json` is the output of an
actual run of StrykerJS against `src/math.js`, with `projectRoot` normalised to `.` for portability.

## Files

```
src/math.js            source under mutation (mirrors examples/demo-math behaviors)
test/math.test.js      Vitest suite (7 tests) that catches the mutants
stryker.config.json    vitest runner, mutate src/**, jsonReporter -> reports/report.json
package.json           pinned tool versions (StrykerJS 8.7.1, vitest 2.1.9)
reports/report.json    real captured report (schemaVersion 1.0)
```

## Regenerate

```
npm install
npx vitest run     # 7/7 pass
npx stryker run    # writes reports/report.json
```

The framework/version that produced the report is recorded in `report.json` under `framework`.

## Report schema (as verified from this real artifact)

- top level: `files`, `schemaVersion` (1.0), `thresholds`, `testFiles`, `projectRoot`, `config`, `framework`
- `files[<path>].mutants[]`: `id`, `mutatorName`, `replacement`, `status`, `statusReason`,
  `static`, `testsCompleted`, `killedBy[]`, `coveredBy[]`, `location{start,end}`
- `files[<path>].source`: original source text
- `testFiles[<path>].tests[]`: `id`, `name`
- `thresholds`: `high`, `low`, `break` (the vendor's own bar)
- `framework`: `name`, `version` (provenance stamp)

`mutatorName` values seen in this fixture: `ArithmeticOperator`, `BlockStatement`,
`ConditionalExpression`, `EqualityOperator`. `status` values in the wider Stryker vocabulary:
`Killed`, `Survived`, `Timeout`, `NoCoverage`, `RuntimeError`, `Ignored`, `Pending`.

## Status mapping (DRAFT — awaits the importer spec; not implemented yet)

| Stryker status | VerdictGate class | Notes |
|---|---|---|
| `Killed` | Caught | suite observed and rejected the mutant |
| `Timeout` | Caught | hanging mutant is still caught |
| `Survived` | Survived | executed, not caught |
| `NoCoverage` | **unexercised** (NOT Survived) | never executed by any test; mapping it to Survived would inflate survival rate and conflate "not executed" with "executed and survived" |
| `RuntimeError` | excluded, recorded | legitimate "does not count", not an input error |
| `Pending` | excluded, recorded | not run |
| `Ignored` | excluded, recorded | explicitly ignored |

`--no-coverage-as-survived` (default off) is the only intended escape hatch for treating
`NoCoverage` as `Survived`, and it must be explicit.

Tier assignment (B0-B3) is a separate open decision: Stryker has no risk tiers. The existing
`requirements.csv` sidecar (behavior -> tier verbatim keys) is the likely mechanism; the importer
should not invent tiering.
