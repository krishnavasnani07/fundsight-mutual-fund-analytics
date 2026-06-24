import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "raw" / "08_investor_transactions.csv"
output_file = BASE_DIR / "data" / "processed" / "clean_transactions.csv"

df = pd.read_csv(input_file)

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Remove rows with missing critical fields
df = df.dropna(
    subset=[
        "investor_id",
        "amfi_code",
        "transaction_type",
        "amount_inr"
    ]
)

# Standardize text columns
df["transaction_type"] = df["transaction_type"].str.strip().str.upper()
df["state"] = df["state"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()

df.to_csv(output_file, index=False)

print(f"Saved: {output_file}")
print(df.shape)