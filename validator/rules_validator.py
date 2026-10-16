from pathlib import Path
import pandas as pd


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "validation_dataset.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_FILE = OUTPUT_DIR / "validation_results.csv"


# Accepted business values
ACCEPTED_SEGMENTS = {
    "Retail",
    "Enterprise",
    "SMB",
}


def validate_record(row):
    errors = []

    start_date = row["start_date"]
    end_date = row["end_date"]
    category = row["category"]
    discount = row["discount"]
    customer_segment = row["customer_segment"]
    status = row["status"]

    # RULE_001 — Date Validation
    if pd.notna(start_date) and pd.notna(end_date):
        if start_date > end_date:
            errors.append(
                "RULE_001: Start date is greater than end date."
            )

    # RULE_002 — Discount Validation
    if pd.isna(discount) or discount < 0 or discount > 100:
        errors.append(
            "RULE_002: Discount must be between 0 and 100."
        )

    # RULE_003 — Mandatory Category
    if pd.isna(category) or str(category).strip() == "":
        errors.append(
            "RULE_003: Category is missing."
        )

    # RULE_004 — Customer Segment Validation
    if customer_segment not in ACCEPTED_SEGMENTS:
        errors.append(
            "RULE_004: Invalid customer segment."
        )

    # RULE_005 — Active Record Validation
    if status == "Active":
        if pd.isna(start_date) or pd.isna(end_date):
            errors.append(
                "RULE_005: Active record must contain valid start and end dates."
            )

    validation_status = "VALID" if not errors else "INVALID"

    return pd.Series(
        {
            "validation_status": validation_status,
            "violated_rules": " | ".join(errors),
        }
    )


# Load dataset
df = pd.read_csv(
    DATA_FILE,
    dtype={"record_id": str},
)

# Convert dates
df["start_date"] = pd.to_datetime(
    df["start_date"],
    errors="coerce"
)

df["end_date"] = pd.to_datetime(
    df["end_date"],
    errors="coerce"
)

# Apply validation rules
validation_results = df.apply(
    validate_record,
    axis=1
)

df = pd.concat(
    [df, validation_results],
    axis=1
)

# Create output folder
OUTPUT_DIR.mkdir(exist_ok=True)

# Save results
df.to_csv(
    OUTPUT_FILE,
    index=False,
)

# Summary
total_records = len(df)
valid_records = (df["validation_status"] == "VALID").sum()
invalid_records = (df["validation_status"] == "INVALID").sum()

print("BUSINESS RULES VALIDATION SUMMARY")
print("-" * 40)
print(f"Total records: {total_records}")
print(f"Valid records: {valid_records}")
print(f"Invalid records: {invalid_records}")

print("\nVALIDATION RESULTS")
print("-" * 40)

for _, row in df.iterrows():
    print(
        f"Record {row['record_id']} -> "
        f"{row['validation_status']}"
    )

    if row["validation_status"] == "INVALID":
        print(row["violated_rules"])

print(
    "\nResults saved to: "
    "outputs/validation_results.csv"
)
