# Operator Sets per Risk Tier

**Version:** 0.1  
**Status:** Draft  
**Owner:** W2 (Product)  
**Date:** 2026-09-22  

---

## Purpose

Defines which mutation operators are applied at each risk tier. The operator set determines **mutation depth** — how aggressively we shake each verification point.

---

## Core Principle

> **Risk steers mutation depth.** Critical tiers get exhaustive mutation; lower tiers get sampled subsets.

---

## Operator Catalog

| Operator ID | Name | Description | Applies To |
|-------------|------|-------------|------------|
| **EQ_NEGATION** | Equality Negation | `expect(x).toBe(true)` → `expect(x).toBe(false)` | Boolean assertions, equality checks |
| **BOOL_NEGATION** | Boolean Negation | `expect(x).toBeTruthy()` → `expect(x).toBeFalsy()` | Boolean assertions |
| **BOUNDARY_FLIP** | Boundary Flip | `expect(x).toBeGreaterThan(10)` → `expect(x).toBeLessThanOrEqual(10)` | Boundary assertions (>, <, >=, <=) |
| **TYPE_COERCION** | Type Coercion | `expect(x).toBe(5)` → `expect(x).toBe("5")` | Type-sensitive assertions |
| **NULL_INJECTION** | Null Injection | `expect(obj.prop).toBeDefined()` → `expect(null).toBeDefined()` | Object property assertions |
| **COLLECTION_EMPTY** | Collection Empty | `expect(arr).toHaveLength(3)` → `expect(arr).toHaveLength(0)` | Array/collection assertions |

---

## Operator Sets per Tier

### B0 Critical — Full Set (Mandatory)

| Operator | Included | Rationale |
|----------|----------|-----------|
| **EQ_NEGATION** | ✅ Mandatory | Critical assertions must detect negation |
| **BOOL_NEGATION** | ✅ Mandatory | Auth/payment logic often boolean |
| **NULL_INJECTION** | ✅ Mandatory | Credential/data integrity often null-sensitive |
| **BOUNDARY_FLIP** | Optional | If boundary assertions exist |
| **TYPE_COERCION** | Optional | If type-sensitive assertions exist |
| **COLLECTION_EMPTY** | Optional | If collection assertions exist |

**Rule:** All applicable operators **must run** for B0. No sampling.

---

### B1 High — Full Set (Mandatory)

| Operator | Included | Rationale |
|----------|----------|-----------|
| **EQ_NEGATION** | ✅ Mandatory | Core journey assertions |
| **BOOL_NEGATION** | ✅ Mandatory | Auth/permission checks |
| **NULL_INJECTION** | ✅ Mandatory | Core CRUD often checks existence |
| **BOUNDARY_FLIP** | ✅ Mandatory | Boundary conditions critical |
| **TYPE_COERCION** | Optional | If type-sensitive assertions |
| **COLLECTION_EMPTY** | Optional | If collection assertions exist |

**Rule:** All applicable operators **must run** for B1. No sampling.

---

### B2 Medium — Band + Small-N Floor

| Operator | Included | Sampling |
|----------|----------|----------|
| **BOUNDARY_FLIP** | ✅ Always | Boundary conditions common in edge cases |
| **TYPE_COERCION** | ✅ Always | Type coercion common in edge cases |
| **COLLECTION_EMPTY** | ✅ Sampled | 50% of collection assertions |
| **EQ_NEGATION** | Sampled | 50% of equality assertions |
| **BOOL_NEGATION** | Sampled | 50% of boolean assertions |
| **NULL_INJECTION** | Sampled | 50% of null checks |

**Gate Rules:**
- N ≥ 20: Band ≤ 5% survivors
- N < 20: Small-N floor max 1 survivor
- Every B2 survivor requires explicit `decision` (open/dismissed/fixed)

**Pilot actual:** EQ_NEGATION + COLLECTION_EMPTY, unsampled (vision table above is the target, not the engine).

---

### B3 Low — Trend Only

| Operator | Included | Sampling |
|----------|----------|----------|
| **COLLECTION_EMPTY** | Sampled | 33% of collection assertions |
| **EQ_NEGATION** | Not included | — |
| **BOOL_NEGATION** | Not included | — |
| **BOUNDARY_FLIP** | Not included | — |
| **TYPE_COERCION** | Not included | — |
| **NULL_INJECTION** | Not included | — |

**Gate:** Never blocks (Trend-only).  
**Signal:** Survival rate tracked vs rolling 3-run baseline.

**Pilot actual:** nothing seeded (`OPERATOR_SETS["B3"] = []` by design; `--tier B3` always yields 0 mutants).

---

## Operator Applicability Matrix

| Assertion Type | Applicable Operators |
|----------------|---------------------|
| `toBe` / `toEqual` / `toStrictEqual` | EQ_NEGATION |
| `toBeTruthy` / `toBeFalsy` / `toBeTrue` / `toBeFalse` | BOOL_NEGATION |
| `toBeGreaterThan` / `toBeLessThan` / `toBeGreaterThanOrEqual` / `toBeLessThanOrEqual` | BOUNDARY_FLIP |
| `toBe` with type mismatch | TYPE_COERCION |
| `toBeDefined` / `toBeUndefined` / `toBeNull` / `toBeNullish` | NULL_INJECTION |
| `toHaveLength` / `toContain` / `toContainEqual` | COLLECTION_EMPTY |

---

## Sampling Strategy (B2/B3)

### B2 Sampling Rules
- **Target:** ~66% operator coverage (2 of 3 applicable per assertion type)
- **Method:** Deterministic hash-based sampling (mutation_id hash % 3 < 2)
- **Guarantee:** BOUNDARY_FLIP + TYPE_COERCION always run; others 50%

### B3 Sampling Rules
- Only COLLECTION_EMPTY at 33% (1 in 3)
- All other operators excluded

---

## Configuration (CLI Flags)

B2 gate flags (on `verdictgate verdict`):

```bash
# B2 band percentage (default 5)
--b2-band-pct 5

# B2 small-N max survivors (default 1)
--b2-small-n-max 1
```

RMT seeder tier selection (on `verdictgate rmt`):

```bash
# Pilot operator sets per tier (hardcoded in rmt.py OPERATOR_SETS, no CLI override):
# B0/B1 = EQ_NEGATION only; B2 = EQ_NEGATION + COLLECTION_EMPTY; B3 = nothing seeded
--tier B2
```

> Per-tier `--operators-b0/b1/b2/b3` overrides are **planned, not implemented**.
> Sampling (§ Sampling Strategy) is **specified, not built** — the pilot fires every
> applicable operator on every assertion (see LIMITATIONS L1/L4 in rmt-methodology.md).

---

## Mutation Depth by Tier

| Tier | Operator Coverage | Sampling | Max Survivors | Gate Type |
|------|-------------------|----------|---------------|-----------|
| B0 | 100% (all applicable) | None | 0 | Hard fail |
| B1 | 100% (all applicable) | None | 0 | Hard fail |
| B2 | ~66% (sampled) | Deterministic hash | ≤5% (N≥20) / 1 (N<20) | Hard fail |
| B3 | ~33% (sampled) | Deterministic hash | Unlimited | Trend only |

---

## Implementation Notes

### Deterministic Sampling
```python
def should_run_operator(mutation_id: str, operator: str, tier: str) -> bool:
    if tier in ("B0", "B1"):
        return True
    if tier == "B2":
        if operator in ("BOUNDARY_FLIP", "TYPE_COERCION"):
            return True
        # Deterministic hash-based sampling for others
        hash_val = hash(f"{mutation_id}:{operator}") % 3
        return hash_val < 2  # 2/3 = 66%
    if tier == "B3":
        if operator != "COLLECTION_EMPTY":
            return False
        hash_val = hash(f"{mutation_id}:{operator}") % 3
        return hash_val == 0  # 1/3 = 33%
    return False
```

---

## Operator Semantics Reference

| Operator | Mutation Pattern | Example Before → After |
|----------|------------------|------------------------|
| **EQ_NEGATION** | `toBe(x)` → `not.toBe(x)` | `expect(x).toBe(true)` → `expect(x).not.toBe(true)` |
| **BOOL_NEGATION** | `toBeTruthy()` → `toBeFalsy()` | `expect(x).toBeTruthy()` → `expect(x).toBeFalsy()` |
| **BOUNDARY_FLIP** | `>` → `<=` | `expect(x).toBeGreaterThan(10)` → `expect(x).toBeLessThanOrEqual(10)` |
| **TYPE_COERCION** | Strict → Loose | `expect(x).toBe(5)` → `expect(x).toBe("5")` |
| **NULL_INJECTION** | Value → null | `expect(obj.prop).toBeDefined()` → `expect(null).toBeDefined()` |
| **COLLECTION_EMPTY** | `length=n` → `length=0` | `expect(arr).toHaveLength(3)` → `expect(arr).toHaveLength(0)` |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-09-22 | Initial draft |

---

*End of Operator Sets Specification v0.1*