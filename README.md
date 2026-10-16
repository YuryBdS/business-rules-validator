# Business Rules Validator

Rule-based validation engine for converting business requirements into structured, traceable and automated validations.

## Business Problem

Operational processes often depend on business rules documented in spreadsheets, procedures, emails or individual knowledge.

When these rules are interpreted manually, the operation becomes vulnerable to inconsistent decisions, rework and validation errors.

This project demonstrates how business requirements can be translated into clear, executable and traceable validation rules.

## Scenario

The project simulates an operational process in which records must comply with predefined business rules before being considered valid.

Each record contains information such as:

- Start date
- End date
- Category
- Discount
- Customer segment
- Status

All data used in this project is synthetic and created exclusively for portfolio purposes.

## Business Rules

### RULE_001 — Date Validation

The start date cannot be greater than the end date.

### RULE_002 — Discount Validation

The discount must be between 0% and 100%.

### RULE_003 — Mandatory Category

Category is a mandatory field.

### RULE_004 — Customer Segment Validation

Customer segment must belong to the accepted values:

- Retail
- Enterprise
- SMB

### RULE_005 — Active Record Validation

Active records must contain valid start and end dates.

Detailed rule definitions are available in:

[`rules/business_rules.md`](rules/business_rules.md)

## Validation Logic

Each record is evaluated against all applicable business rules.

A record is classified as:

`VALID`

when no rule is violated.

A record is classified as:

`INVALID`

when one or more rules are violated.

All violated rules are returned to ensure decision traceability.

## Results

The validator processed **10 records**.

| Result | Records |
|---|---:|
| Valid | 4 |
| Invalid | 6 |
| Total | 10 |

### Validation Examples

**Record 001**

`VALID`

**Record 002**

`INVALID`

`RULE_001: Start date is greater than end date.`

**Record 003**

`INVALID`

`RULE_003: Category is missing.`

`RULE_004: Invalid customer segment.`

### Rule Violations Detected

| Rule | Violations |
|---|---:|
| RULE_001 — Date Validation | 1 |
| RULE_002 — Discount Validation | 2 |
| RULE_003 — Mandatory Category | 1 |
| RULE_004 — Customer Segment Validation | 2 |
| RULE_005 — Active Record Validation | 1 |

The complete validation output is available here:

[`outputs/validation_results.csv`](outputs/validation_results.csv)

## Automation

The validation process is automatically executed using GitHub Actions.

The workflow:

1. Downloads the repository
2. Sets up Python
3. Installs the required dependencies
4. Executes the business rules validator
5. Generates the validation results
6. Publishes the result as a workflow artifact

Workflow file:

[`.github/workflows/run-business-rules-validator.yml`](.github/workflows/run-business-rules-validator.yml)

## Project Structure

~~~text
business-rules-validator/
│
├── README.md
│
├── data/
│   └── validation_dataset.csv
│
├── rules/
│   └── business_rules.md
│
├── validator/
│   └── rules_validator.py
│
├── outputs/
│   ├── README.md
│   └── validation_results.csv
│
└── .github/
    └── workflows/
        └── run-business-rules-validator.yml
~~~

## Technologies

- Python
- Pandas
- GitHub Actions
- Rule-Based Validation
- Decision Modeling

## Project Objective

The objective is to demonstrate how operational knowledge can be converted into structured decision rules that are consistent, traceable and ready for automation.

The model separates business rules from execution logic, helping reduce ambiguity and improve consistency in operational decision-making.

## Project Status

✅ Completed — Version 1
