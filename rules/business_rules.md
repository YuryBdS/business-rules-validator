# Business Rules

This document defines the validation rules used by the Business Rules Validator.

## RULE_001 — Date Validation

**Condition**

Start date must be less than or equal to end date.

**Validation**

If `start_date > end_date`, the record must be classified as `INVALID`.

**Error message**

`RULE_001: Start date is greater than end date.`

---

## RULE_002 — Discount Validation

**Condition**

Discount must be between 0 and 100.

**Validation**

If `discount < 0` or `discount > 100`, the record must be classified as `INVALID`.

**Error message**

`RULE_002: Discount must be between 0 and 100.`

---

## RULE_003 — Mandatory Category

**Condition**

Category is mandatory.

**Validation**

If `category` is empty or missing, the record must be classified as `INVALID`.

**Error message**

`RULE_003: Category is missing.`

---

## RULE_004 — Customer Segment Validation

**Condition**

Customer segment must belong to the accepted list.

Accepted values:

- Retail
- Enterprise
- SMB

**Validation**

If `customer_segment` is not in the accepted list, the record must be classified as `INVALID`.

**Error message**

`RULE_004: Invalid customer segment.`

---

## RULE_005 — Active Record Validation

**Condition**

Active records must contain both start date and end date.

**Validation**

If `status = Active` and either `start_date` or `end_date` is missing, the record must be classified as `INVALID`.

**Error message**

`RULE_005: Active record must contain valid start and end dates.`

---

## Decision Rule

A record is considered `VALID` when no validation rule is violated.

A record is considered `INVALID` when one or more validation rules are violated.

All violated rules must be returned for traceability.
