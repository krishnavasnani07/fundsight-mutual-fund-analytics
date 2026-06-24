# Data Quality Summary

> Document findings on data completeness, accuracy, and consistency.

# Dataset Quality Summary

## 01_fund_master.csv
Rows: 40
Columns: 15
Missing Values: 0

Observations:
- Contains master fund information
- Primary key candidate: amfi_code
- No missing values

---

## 02_nav_history.csv
Rows: 46000
Columns: 3
Missing Values: 0

Observations:
- Daily NAV history
- Join key: amfi_code
- Date column stored as string

---

## 03_aum_by_fund_house.csv
Rows: 90
Columns: 5
Missing Values: 0

Observations:
- Fund house level AUM data
- Date column stored as string

---

## 04_monthly_sip_inflows.csv
Rows: 48
Columns: 6
Missing Values: 12

Observations:
- Missing values found in yoy_growth_pct
- Likely unavailable for early periods

---

## 05_category_inflows.csv
Rows: 144
Columns: 3
Missing Values: 0

Observations:
- Category-wise inflow data
- No data quality issues found

---

## 06_industry_folio_count.csv
Rows: 21
Columns: 6
Missing Values: 0

Observations:
- Industry folio statistics
- Quarterly snapshots

---

## 07_scheme_performance.csv
Rows: 40
Columns: 19
Missing Values: 0

Observations:
- Contains Sharpe, Sortino, Alpha, Beta
- Join key: amfi_code

---

## 08_investor_transactions.csv
Rows: 32778
Columns: 13
Missing Values: 0

Observations:
- Transaction-level dataset
- Join key: amfi_code
- transaction_date stored as string

---

## 09_portfolio_holdings.csv
Rows: 322
Columns: 8
Missing Values: 0

Observations:
- Portfolio holdings by scheme
- Join key: amfi_code
- portfolio_date stored as string

---

## 10_benchmark_indices.csv
Rows: 8050
Columns: 3
Missing Values: 0

Observations:
- Benchmark index history
- Date stored as string

---

# Validation Results

## AMFI Code Validation

- Total Fund Master Codes: 40
- Total NAV History Codes: 40
- Missing Codes: 0

Result:
All AMFI scheme codes from the fund master dataset were successfully matched with NAV history records.

---

## Live NAV API Validation

API Endpoint:
https://api.mfapi.in/mf/125497

Result:
- Status Code: 200 (Success)
- Live NAV data fetched successfully
- Response contains metadata and historical NAV records
- API integration validated for ETL pipeline

---

## Overall Assessment

- Data quality is excellent across all datasets.
- Only one notable issue was identified:
  - 12 missing values in `yoy_growth_pct` within `04_monthly_sip_inflows.csv`.
- `amfi_code` has been identified as the primary join key across multiple datasets.
- Several date fields require datetime conversion during ETL processing.
- Live NAV API integration has been successfully tested.