import pandas as pd

print("\nTRANSACTIONS")
df1 = pd.read_csv("data/raw/08_investor_transactions.csv")
print(df1.columns.tolist())

print("\nPERFORMANCE")
df2 = pd.read_csv("data/raw/07_scheme_performance.csv")
print(df2.columns.tolist())