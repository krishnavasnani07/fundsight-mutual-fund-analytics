import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

db_path = BASE_DIR / "fundsight.db"

conn = sqlite3.connect(db_path)

# Load cleaned datasets
nav = pd.read_csv(BASE_DIR / "data" / "processed" / "clean_nav.csv")
transactions = pd.read_csv(BASE_DIR / "data" / "processed" / "clean_transactions.csv")
performance = pd.read_csv(BASE_DIR / "data" / "processed" / "clean_performance.csv")

# Write to SQLite
nav.to_sql("nav_history", conn, if_exists="replace", index=False)
transactions.to_sql("investor_transactions", conn, if_exists="replace", index=False)
performance.to_sql("scheme_performance", conn, if_exists="replace", index=False)

print("Database created successfully!")
print("fundsight.db")

conn.close()