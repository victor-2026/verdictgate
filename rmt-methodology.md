# RMT-lite Methodology for VerdictGate

**Owner:** W2 (Product)  
**Version:** 0.1  
**Status:** Draft  
**Date:** 2026-09-22  

---

## Overview

RMT-lite is a lightweight mutation testing methodology adapted from Leonardo Lanni's Reverse Mutation Testing (RMT) for integration into VerdictGate. It focuses on mutating **assertions/verifications** rather than production code, measuring whether tests can detect deliberately broken assertions.

---

## Core Concept

**Traditional MT:** Mutate production code → run tests → measure kill rate  
**RMT-lite:** Mutate **assertions/verifications** → run tests → measure survival of broken assertions

**Key Insight:** The risk lives on the *verification point*, not the mutation operator. The same operator (e.g., `EQ_NEGATION`) has different risk depending on what it verifies:
- `payment.status == PAID` → B0 (Critical)
- `successMessage == "Thank you"` → B3 (Low)

---

## Limitations (Pilot Scope — What RMT-lite Is NOT)

> The tables below describe the **full 6-operator vision**. The pilot implementation
> (`rmt.py`) covers a **2-operator subset**. Read this section first so the vision
> is never mistaken for the engine.

| # | Limitation | Pilot status |
|---|-----------|--------------|
| L1 | Only **2 of 6** operators implemented: `EQ_NEGATION` (toBeVisible/toHaveText/toBeHidden), `COLLECTION_EMPTY` (toHaveLength). `BOOL_NEGATION`, `BOUNDARY_FLIP`, `TYPE_COERCION`, `NULL_INJECTION` are **specified, not built**. | B2 = EQ_NEGATION + COLLECTION_EMPTY; B0/B1 = EQ_NEGATION only; B3 = nothing seeded (trend-only tier) |
| L2 | **Assertion-mutation only, not app-code.** RMT-lite mutates the verification (`expect`), never the system under test. It measures assertion strength, not code coverage. | By design |
| L3 | **Seeder only, no execution.** `rmt.py` emits mutant texts; it does not run suites, record `suite_result`, or write `results.csv`. Execution + recording is the pilot operator's job (W3). | By design |
| L4 | **No sampling yet.** Every applicable operator fires on every assertion (no B2 66% / B3 33% hash sampling). | Planned, gated on W3 pilot volume signal |
| L5 | **No pre-seed relevance filter.** No change-boundary filtering; every file in scope is mutated. | Planned, see Pre-seed Relevance Filter |
| L6 | **Text scanner, not AST.** Balanced-paren matching handles nesting and quoted parens. Chain hops `.soft` / `.element` are unwrapped segment-by-segment to the terminal matcher (rmt 0.1.0+; earlier engines missed `expect.element()` chains — 29 measured on OpenClaw, now covered). Unknown hops, custom matcher wrappers, and `.not` chains (already negated) end the chain with no mutant. | Chain-unwrap implemented; custom wrappers still out of scope |
| L7 | **No-op mutants refused pre-seed.** A mutant identical to the original (e.g. `COLLECTION_EMPTY` on an already-empty `toHaveLength(0)`) is skipped at generation — mirroring the VerdictGate NOOP input rule. | Implemented in `generate_mutants_for_file` |
| L8 | **Runner-agnostic text form only.** Matches `expect(...).matcher(...)` text in Playwright, Vitest + jest-dom, and compat shims. Framework-specific runners (`.browser.test.ts` harnesses, conditional `it.skipIf`) are not interpreted. | By design |

---

## RMT-lite Mutation Operators

| Operator ID | Name | Description | Applies To | Risk Tier Default |
|-------------|------|-------------|------------|-------------------|
| **EQ_NEGATION** | Equality Negation | `expect(x).toBe(true)` → `expect(x).toBe(false)` | Boolean assertions, equality checks | B0-B3 (depends on assertion) |
| **BOOL_NEGATION** | Boolean Negation | `expect(x).toBeTruthy()` → `expect(x).toBeFalsy()` | Boolean assertions | B0-B3 |
| **BOUNDARY_FLIP** | Boundary Flip | `expect(x).toBeGreaterThan(10)` → `expect(x).toBeLessThanOrEqual(10)` | Boundary assertions (>, <, >=, <=) | B1-B2 |
| **TYPE_COERCION** | Type Coercion | `expect(x).toBe(5)` → `expect(x).toBe("5")` | Type-sensitive assertions | B1-B2 |
| **NULL_INJECTION** | Null Injection | `expect(obj.prop).toBeDefined()` → `expect(null).toBeDefined()` | Object property assertions | B0-B1 |
| **COLLECTION_EMPTY** | Collection Empty | `expect(arr).toHaveLength(3)` → `expect(arr).toHaveLength(0)` | Array/collection assertions | B2-B3 |

---

## Operator Definitions

### EQ_NEGATION (Equality Negation)
- **Pattern:** `expect(actual).toBe(expected)` → `expect(actual).not.toBe(expected)` OR `expect(actual).toBe(opposite(expected))`
- **Applies to:** `toBe`, `toEqual`, `toStrictEqual`
- **Risk:** Depends on assertion criticality (B0-B3)

### BOOL_NEGATION (Boolean Negation)
- **Pattern:** `expect(value).toBeTruthy()` → `expect(value).toBeFalsy()` / `expect(value).toBe(true)` → `expect(value).toBe(false)`
- **Applies to:** `toBeTruthy`, `toBeFalsy`, `toBeTrue`, `toBeFalse`
- **Risk:** B0-B3 (depends on assertion)

### BOUNDARY_FLIP (Boundary Flip)
- **Pattern:** `expect(x).toBeGreaterThan(10)` → `expect(x).toBeLessThanOrEqual(10)`
- **Applies to:** `toBeGreaterThan`, `toBeLessThan`, `toBeGreaterThanOrEqual`, `toBeLessThanOrEqual`
- **Risk:** B1-B2 (boundary conditions often critical)

### TYPE_COERCION (Type Coercion)
- **Pattern:** `expect(value).toBe(5)` → `expect(value).toBe("5")`
- **Applies to:** Strict equality checks where type matters
- **Risk:** B1-B2 (type confusion often high severity)

### NULL_INJECTION (Null Injection)
- **Pattern:** `expect(obj.prop).toBeDefined()` → `expect(null).toBeDefined()`
- **Applies to:** `toBeDefined`, `toBeUndefined`, `toBeNull`, `toBeTruthy` on objects
- **Risk:** B0-B1 (null handling often critical)

### COLLECTION_EMPTY (Collection Empty)
- **Pattern:** `expect(array).toHaveLength(3)` → `expect(array).toHaveLength(0)`
- **Applies to:** `toHaveLength`, `toContain`, `toContainEqual`
- **Risk:** B2-B3 (empty collections often cosmetic)

---

## Operator Set per Risk Tier

| Risk Tier | Operators (Full Set) | Sampled Subset |
|-----------|---------------------|----------------|
| **B0 Critical** | EQ_NEGATION, BOOL_NEGATION, NULL_INJECTION | All (mandatory) |
| **B1 High** | EQ_NEGATION, BOOL_NEGATION, BOUNDARY_FLIP, TYPE_COERCION, NULL_INJECTION | All (mandatory) |
| **B2 Medium** | BOUNDARY_FLIP, TYPE_COERCION, COLLECTION_EMPTY | Sampled (2 of 3) |
| **B3 Low** | COLLECTION_EMPTY | Sampled (1 of 1) |

---

## Mutation Execution Model

### Per Assertion
Each assertion in the test suite gets mutated by **applicable operators** based on:
1. Assertion type (boolean, equality, boundary, collection, etc.)
2. Risk tier of the verification point (from requirements.csv)
3. Operator applicability matrix

### Mutation Execution
```
For each test case:
  For each assertion in test:
    Determine applicable operators based on assertion type + risk tier
    For each applicable operator:
      Create mutant (mutated assertion)
      Run test with mutant
      Record: killed / survived / observed-only / error
```

### Output per Mutation
| Field | Description |
|-------|-------------|
| `mutation_id` | Unique identifier (e.g., `M1`, `M2`) |
| `behavior` | Human-readable behavior description |
| `operator` | Operator ID (EQ_NEGATION, BOOL_NEGATION, etc.) |
| `risk_tier` | B0, B1, B2, B3 |
| `expected` | Y (expected to catch) / N (out of scope) |
| `suite_result` | pass / fail / error |
| `observed` | Optional: passive observation notes |
| `decision` | open / dismissed / fixed (required for B2 survivors) |
| `e_reason` | If expected=E: reason for equivalence |
| `e_assessor` | Who assessed equivalence |
| `e_basis` | Basis: code-review / diff-analysis / no-observable-path / dead-code / other |

---

## Integration Points with VerdictGate

### Input to VerdictGate
RMT-lite produces standard `results.csv` format compatible with VerdictGate:
```csv
mutation_id,behavior,operator,risk_tier,expected,suite_result,observed,decision,e_reason,e_assessor,e_basis,observed_by,observed_run_ref,observed_element
M1,Payment submits,EQ_NEGATION,B0,Y,pass,,,
M2,Login rejects wrong pwd,BOOL_NEGATION,B0,Y,fail,,,
...
```

### Pre-seed Relevance Filter
Before mutation, filter out verification points outside the change boundary:
- Drop verification points not in changed files/modules
- Only mutate assertions in changed code paths
- Reduces noise, focuses on relevant mutations

### Risk-Steering Depth (vision; pilot subset in § Limitations L1/L4)
| Tier | Operator Count | Coverage |
|------|----------------|----------|
| B0 | Full set (6 operators) | 100% |
| B1 | Full set (6 operators) | 100% |
| B2 | Sampled (2 of 3 applicable) | ~66% |
| B3 | Sampled (1 of 1) | 100% |

Pilot actual: B0/B1 = EQ_NEGATION only; B2 = EQ_NEGATION + COLLECTION_EMPTY, unsampled; B3 = nothing seeded.

---

## Evidence Contract (RMT Output → VerdictGate Input)

Each RMT mutant produces a row in the Evidence Contract:

| Field | Source | Description |
|-------|--------|-------------|
| `mutation_id` | RMT | Unique ID (M1, M2, ...) |
| `behavior` | Test case | Human-readable behavior |
| `operator` | RMT | Operator ID (EQ_NEGATION, etc.) |
| `risk_tier` | Requirements | B0/B1/B2/B3 |
| `expected` | RMT | Y/N/E |
| `suite_result` | Test run | pass/fail |
| `observed` | RMT | Optional observation notes |
| `decision` | VerdictGate | open/dismissed/fixed (for survivors) |

---

## Integration Points

### VerdictGate Pipeline
```
Code Change → RMT Mutation → Test Run → Evidence Contract → VerdictGate → Verdict
```

### VerdictGate Input
RMT produces standard `results.csv` that VerdictGate consumes directly:
- No format conversion needed
- Same columns as traditional MT
- Additional `operator` column for diagnostics

### Pre-seed Relevance Filter
Before mutation, filter verification points:
```python
def is_relevant(verification_point, change_boundary):
    return verification_point.file in change_boundary.files
```
Only mutate assertions within changed files/modules.

---

## Implementation Checklist

- [ ] Define 6 mutation operators (EQ_NEGATION, BOOL_NEGATION, BOUNDARY_FLIP, TYPE_COERCION, NULL_INJECTION, COLLECTION_EMPTY)
- [ ] Implement operator applicability matrix (assertion type → applicable operators)
- [ ] Implement mutation engine (AST-based or regex-based)
- [ ] Integrate with VerdictGate `results.csv` output
- [ ] Add pre-seed relevance filter
- [ ] Implement risk-steering operator selection per tier
- [ ] Add RMT output to VerdictGate evidence pack
- [ ] Document operator semantics and applicability

---

## References

- Leonardo Lanni (RMT author) — architecture discussion 2026-09-21
- VerdictGate per-risk-tier framework v0.3
- TypeSafe Jev primitives (Choice, Noul, Score) — analogous typed outputs
- TypeSafe Jev cookbooks (self-consistency, parallel questions)

---

*End of RMT-lite Methodology v0.1*