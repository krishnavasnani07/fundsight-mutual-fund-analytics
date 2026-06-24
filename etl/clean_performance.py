import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "raw" / "07_scheme_performance.csv"
output_file = BASE_DIR / "data" / "processed" / "clean_performance.csv"

df = pd.read_csv(input_file)

# Remove duplicates
df = df.drop_duplicates()

# Standardize text fields
text_cols = [
    "scheme_name",
    "fund_house",
    "category",
    "plan"
]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# Numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.to_csv(output_file, index=False)

print(f"Saved: {output_file}")
print(df.shape)