import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data.keys())
print(data["meta"])

nav_df = pd.DataFrame(data["data"])

print(nav_df.head())

output_file = DATA_DIR / "live_nav_sbi_smallcap.csv"

nav_df.to_csv(output_file, index=False)

print(f"CSV saved successfully at:\n{output_file}")