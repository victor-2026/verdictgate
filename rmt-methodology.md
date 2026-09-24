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

### Risk-Steering Depth
| Tier | Operator Count | Coverage |
|------|----------------|----------|
| B0 | Full set (6 operators) | 100% |
| B1 | Full set (6 operators) | 100% |
| B2 | Sampled (2 of 3 applicable) | ~66% |
| B3 | Sampled (1 of 1) | 100% |

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
EOF
echo "Created rmt-methodology.md"