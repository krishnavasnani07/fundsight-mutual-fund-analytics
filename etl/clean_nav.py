import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "raw" / "02_nav_history.csv"
output_file = BASE_DIR / "data" / "processed" / "clean_nav.csv"

# Load data
nav_df = pd.read_csv(input_file)

print("Original Shape:", nav_df.shape)

# Convert date column
nav_df["date"] = pd.to_datetime(
    nav_df["date"],
    dayfirst=True,
    errors="coerce"
)

# Remove invalid dates
nav_df = nav_df.dropna(subset=["date"])

# Sort records
nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicates
nav_df = nav_df.drop_duplicates()

# Keep only positive NAV
nav_df = nav_df[nav_df["nav"] > 0]

# Forward fill NAV values fund-wise
nav_df["nav"] = nav_df.groupby(
    "amfi_code"
)["nav"].ffill()

# Save cleaned file
output_file.parent.mkdir(
    parents=True,
    exist_ok=True
)

nav_df.to_csv(
    output_file,
    index=False
)

print("Cleaned Shape:", nav_df.shape)
print("Saved:", output_file)