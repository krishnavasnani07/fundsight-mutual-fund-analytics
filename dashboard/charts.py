import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

conn = sqlite3.connect(BASE_DIR / "fundsight.db")

# -------------------------
# Chart 1: Top Sharpe Ratio
# -------------------------

query = """
SELECT scheme_name, sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(10, 6))
plt.barh(df["scheme_name"], df["sharpe_ratio"])
plt.title("Top 10 Funds by Sharpe Ratio")
plt.xlabel("Sharpe Ratio")
plt.tight_layout()
plt.savefig(BASE_DIR / "dashboard" / "sharpe_ratio.png")
plt.close()

# -------------------------
# Chart 2: State Investment
# -------------------------

query = """
SELECT state,
       SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(10, 6))
plt.bar(df["state"], df["total_investment"])
plt.title("Top States by Investment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(BASE_DIR / "dashboard" / "state_investment.png")
plt.close()

# -------------------------
# Chart 3: Age Distribution
# -------------------------

query = """
SELECT age_group,
       COUNT(*) AS investors
FROM investor_transactions
GROUP BY age_group
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8, 5))
plt.bar(df["age_group"], df["investors"])
plt.title("Investor Age Distribution")
plt.tight_layout()
plt.savefig(BASE_DIR / "dashboard" / "demographics.png")
plt.close()

# -------------------------
# Chart 4: Gender Distribution
# -------------------------

query = """
SELECT gender,
       COUNT(*) AS count
FROM investor_transactions
GROUP BY gender
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(6, 6))
plt.pie(
    df["count"],
    labels=df["gender"],
    autopct="%1.1f%%"
)
plt.title("Gender Distribution")
plt.savefig(BASE_DIR / "dashboard" / "gender_distribution.png")
plt.close()

conn.close()

print("Charts created successfully!")