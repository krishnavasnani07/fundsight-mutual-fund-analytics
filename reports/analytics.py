import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

conn = sqlite3.connect(BASE_DIR / "fundsight.db")

queries = {
    "top_sharpe": """
    SELECT scheme_name, fund_house, sharpe_ratio
    FROM scheme_performance
    ORDER BY sharpe_ratio DESC
    LIMIT 10
    """,

    "top_alpha": """
    SELECT scheme_name, alpha
    FROM scheme_performance
    ORDER BY alpha DESC
    LIMIT 10
    """,

    "investor_demographics": """
    SELECT age_group, COUNT(*) AS investors
    FROM investor_transactions
    GROUP BY age_group
    """,

    "gender_distribution": """
    SELECT gender, COUNT(*) AS count
    FROM investor_transactions
    GROUP BY gender
    """,

    "state_investment": """
    SELECT state,
           SUM(amount_inr) AS total_investment
    FROM investor_transactions
    GROUP BY state
    ORDER BY total_investment DESC
    """
}

for name, query in queries.items():
    df = pd.read_sql(query, conn)
    df.to_csv(BASE_DIR / "reports" / f"{name}.csv", index=False)
    print(f"Generated {name}.csv")

conn.close()