
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

fund_master = pd.read_csv(DATA_DIR / "01_fund_master.csv")
nav_history = pd.read_csv(DATA_DIR / "02_nav_history.csv")


master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Total Fund Master Codes:", len(master_codes))
print("Total NAV Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if missing_codes:
    print(missing_codes)
else:
    print("All AMFI codes validated successfully.")