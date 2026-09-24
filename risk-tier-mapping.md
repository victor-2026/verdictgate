# Risk Tier Mapping Rules

**Version:** 0.1  
**Status:** Draft  
**Owner:** W2 (Product)  
**Date:** 2026-09-22  

---

## Purpose

Defines how verification points (behaviors/assertions) are assigned to risk tiers (B0-B3). This mapping is **independent of mutation operators** — risk lives on the *verification point*, not the mutation operator.

---

## Core Principle

> **Risk lives on the verification point, not the operator.**
> 
> The same operator (e.g., `EQ_NEGATION`) has different risk depending on what it verifies:
> - `payment.status == PAID` → **B0** (Critical)
> - `successMessage == "Thank you"` → **B3** (Low)
> 
> *Same `EQ_NEGATION` operator, different risk tiers.*

---

## Tier Definitions

| Tier | Label | Scope | Gate Rule | Score Target | Observed Budget |
|------|-------|-------|-----------|--------------|-----------------|
| **B0** | Critical | Payment, auth, credentials, data integrity paths | 0 survived (always) | ≥90% | ≤10% at survived=0 |
| **B1** | High | Core user journeys, primary CRUD, search, notifications | 0 survived (always) | ≥80% | ≤20% at survived=0 |
| **B2** | Medium | Secondary flows, edge cases | ≤5% survived (N≥20) or max 1 (N<20) | ≥90% | ≤10% |
| **B3** | Low | Cosmetic, copy, layout, non-critical polish | Trend-only (never blocks) | — | — |

---

## Tier Assignment Rules

### Assignment Priority (highest to lowest)

1. **Explicit in `requirements.csv`** — Behavior explicitly listed with `risk_tier`
2. **Domain-based inference** — Based on behavior keywords/domain
3. **Default** — B2 (Medium) if ambiguous

---

## Domain-Based Inference Rules

### B0 Critical — "If it fails, money/identity/data at risk"

| Domain | Keywords / Patterns | Examples |
|--------|---------------------|----------|
| **Payment** | `payment`, `charge`, `refund`, `billing`, `transaction`, `checkout`, `purchase` | Payment submits, refund processes |
| **Auth** | `login`, `auth`, `password`, `credential`, `token`, `session`, `signin`, `signup` | Login, password reset, token refresh |
| **Credentials** | `credential`, `secret`, `key`, `token`, `api_key`, `certificate` | API key rotation, cert renewal |
| **Data Integrity** | `data_integrity`, `audit`, `ledger`, `immutable`, `append_only`, `write_once` | Audit logs, write-once records |

### B1 High — "Core user value at risk"

| Domain | Keywords / Patterns | Examples |
|--------|---------------------|----------|
| **Core Journeys** | `core_journey`, `primary_flow`, `happy_path`, `critical_path` | User registration, main workflow |
| **Primary CRUD** | `create`, `read`, `update`, `delete` on core entities | User profile CRUD, order management |
| **Search** | `search`, `filter`, `query`, `lookup` | Search results, autocomplete |
| **Notifications** | `notification`, `alert`, `email`, `push`, `webhook` | Email sends, webhook delivery |

### B2 Medium — "Secondary flows, edge cases"

| Domain | Keywords / Patterns | Examples |
|--------|---------------------|----------|
| **Secondary Flows** | `secondary`, `alternative`, `fallback`, `edge_case` | Alternative payment method |
| **Edge Cases** | `boundary`, `edge`, `limit`, `max`, `min`, `empty`, `null` | Boundary values, empty states |
| **Settings** | `settings`, `preferences`, `config`, `profile` | User preferences, notifications settings |
| **Admin** | `admin`, `dashboard`, `report`, `analytics` | Admin panel, reports |

### B3 Low — "Cosmetic, polish, non-critical"

| Domain | Keywords / Patterns | Examples |
|--------|---------------------|----------|
| **Cosmetic** | `copy`, `text`, `label`, `message`, `tooltip`, `placeholder`, `banner` | Welcome banner, success message |
| **Layout** | `layout`, `style`, `css`, `theme`, `responsive`, `alignment` | CSS, spacing, colors |
| **Copy** | `copy`, `text`, `wording`, `phrase`, `sentence` | Button labels, error messages |
| **Non-critical** | `optional`, `nice_to_have`, `cosmetic` | Footer links, decorative icons |

---

## Explicit Override (requirements.csv)

```csv
behavior_name,risk_tier,acceptance_criteria,description
Valid login shows welcome,B0,"Given valid username and password when clicking Sign in then the welcome message is visible",User can sign in
Payment submits successfully,B0,"Given valid payment details when submitting then charge succeeds",Payment processes
Login rejects wrong password,B0,"Given invalid password when signing in then error shown",Auth rejects invalid
Login button visible,element_remove,B1,Y,fail,,,,,,,,
Username placeholder,duplicate_field,B1,Y,pass,two identical username inputs,,,,,reviewer,run-042,username input #2
```

**Rule:** `requirements.csv` `risk_tier` **always wins** over inference. The `--requirements` flag enforces this at parse time (tier-laundering guard).

---

## Inference Algorithm (when no explicit mapping)

```python
def infer_risk_tier(behavior_name: str, description: str = "") -> str:
    text = (behavior_name + " " + description).lower()
    
    # B0 keywords (highest priority)
    b0_keywords = ["payment", "charge", "refund", "billing", "transaction", "purchase",
                   "login", "auth", "password", "credential", "token", "session",
                   "credential", "secret", "key", "api_key", "certificate",
                   "data_integrity", "audit", "ledger", "immutable", "write_once"]
    
    # B1 keywords
    b1_keywords = ["core_journey", "primary_flow", "happy_path", "critical_path",
                   "create", "read", "update", "delete", "crud",
                   "search", "filter", "query", "lookup",
                   "notification", "alert", "email", "push", "webhook"]
    
    # B2 keywords
    b2_keywords = ["secondary", "alternative", "fallback", "edge_case",
                   "boundary", "edge", "limit", "max", "min", "empty", "null",
                   "settings", "preferences", "config", "profile",
                   "admin", "dashboard", "report", "analytics"]
    
    # B3 keywords (lowest)
    b3_keywords = ["cosmetic", "copy", "text", "label", "message", "tooltip",
                   "placeholder", "banner", "layout", "style", "css", "theme",
                   "responsive", "alignment", "optional", "nice_to_have"]
    
    # Priority: B0 > B1 > B2 > B3
    if any(kw in text for kw in b0_keywords):
        return "B0"
    if any(kw in text for kw in b1_keywords):
        return "B1"
    if any(kw in text for kw in b2_keywords):
        return "B2"
    if any(kw in text for kw in b3_keywords):
        return "B3"
    return "B2"  # Default
```

---

## Tier Assignment Checklist

When assigning a tier to a new behavior:

- [ ] Check `requirements.csv` for explicit mapping
- [ ] Apply domain inference rules (B0 > B1 > B2 > B3)
- [ ] Document reasoning in `requirements.csv` or mutation matrix
- [ ] Verify with stakeholder (Product Owner / QA Lead)
- [ ] Record in `requirements.csv` for audit trail

---

## Anti-Patterns (What NOT to Do)

| Anti-Pattern | Why Wrong | Correct |
|--------------|-----------|---------|
| Tier based on operator | `EQ_NEGATION` = B0 always | Tier on verification point |
| Tier by file location | `src/payment/*` = B0 always | Tier by behavior semantics |
| Tier by team ownership | `payments-team` = B0 | Tier by business impact |
| Default to B0 | "Safe side" | Default to B2, escalate with evidence |

---

## Verification Checklist

Before finalizing tier assignments:

- [ ] Every behavior in `results.csv` has a `risk_tier`
- [ ] No behavior relies solely on operator for tier
- [ ] B0/B1 have explicit justification in `requirements.csv`
- [ ] `requirements.csv` tiers match mutation matrix tiers
- [ ] Cross-check: `--requirements` flag passes without tier mismatches

---

*End of Risk Tier Mapping Rules v0.1*
EOF
echo "Created risk-tier-mapping.md"