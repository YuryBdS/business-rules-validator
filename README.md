# Business Rules Validator

Rule-based validation engine for converting business requirements into structured, traceable and automated validations.

## Business Problem

Operational processes often depend on business rules documented in spreadsheets, procedures, emails or individual knowledge.

When these rules are interpreted manually, the operation becomes vulnerable to inconsistent decisions, rework and validation errors.

This project demonstrates how business requirements can be translated into clear and executable validation rules.

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

### RULE_004 — Customer Segment

Customer segment must belong to the accepted values.

### RULE_005 — Active Record Validation

Active records must contain valid start and end dates.

## Expected Output

Each record will be classified as `VALID` or `INVALID`.

When a record is invalid, the validator will also return the rule that caused the rejection.

Example:

~~~text
Record 001 → VALID

Record 002 → INVALID
RULE_001: Start date is greater than end date.

Record 003 → INVALID
RULE_003: Category is missing.
RULE_004: Invalid customer segment.
~~~

## Project Structure

~~~text
business-rules-validator/
│
├── README.md
├── data/
│   └── validation_dataset.csv
│
├── rules/
│   └── business_rules.md
│
├── validator/
│   └── rules_validator.py
│
└── outputs/
    └── validation_results.csv
~~~

## Technologies

- Python
- Pandas
- GitHub Actions
- Rule-Based Validation
- Decision Modeling

## Project Objective

The objective is to demonstrate how operational knowledge can be converted into structured decision rules that are consistent, traceable and ready for automation.

## Project Status

🚧 Work in progress
