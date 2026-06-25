import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

conn = sqlite3.connect(BASE_DIR / "fundsight.db")

checks = [
    ("clean_nav.csv", "nav_history"),
    ("clean_transactions.csv", "investor_transactions"),
    ("clean_performance.csv", "scheme_performance"),
]

for csv_file, table in checks:
    csv_rows = len(pd.read_csv(BASE_DIR / "data" / "processed" / csv_file))
    db_rows = pd.read_sql(f"SELECT COUNT(*) AS cnt FROM {table}", conn)["cnt"][0]

    print(f"{table}")
    print(f"CSV Rows : {csv_rows}")
    print(f"DB Rows  : {db_rows}")

    if csv_rows == db_rows:
        print("Status   : PASS\n")
    else:
        print("Status   : FAIL\n")

conn.close()