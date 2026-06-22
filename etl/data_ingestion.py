# data_ingestion.py
# Handles ingestion of mutual fund data from various sources.
import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
print("Looking in:", DATA_DIR)

print("Files found:", list(DATA_DIR.glob("*")))

for file in DATA_DIR.glob("*.csv"):
    print("\n" + "="*60)
    print(f"DATASET: {file.name}")
    print("="*60)

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())