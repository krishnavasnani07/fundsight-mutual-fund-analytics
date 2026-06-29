# FundSight Data Dictionary

## investor_transactions

| Column             | Type    | Description                |
| ------------------ | ------- | -------------------------- |
| investor_id        | TEXT    | Unique investor identifier |
| transaction_date   | DATE    | Date of transaction        |
| amfi_code          | INTEGER | AMFI scheme code           |
| transaction_type   | TEXT    | SIP, Lumpsum or Redemption |
| amount_inr         | REAL    | Transaction amount in INR  |
| state              | TEXT    | Investor state             |
| city               | TEXT    | Investor city              |
| city_tier          | TEXT    | Tier classification        |
| age_group          | TEXT    | Investor age bucket        |
| gender             | TEXT    | Investor gender            |
| annual_income_lakh | REAL    | Annual income in lakhs     |
| payment_mode       | TEXT    | Payment method             |
| kyc_status         | TEXT    | KYC verification status    |

---

## scheme_performance

| Column             | Type    | Description                   |
| ------------------ | ------- | ----------------------------- |
| amfi_code          | INTEGER | AMFI scheme code              |
| scheme_name        | TEXT    | Scheme name                   |
| fund_house         | TEXT    | AMC/Fund house                |
| category           | TEXT    | Fund category                 |
| plan               | TEXT    | Regular/Direct plan           |
| return_1yr_pct     | REAL    | 1-year return                 |
| return_3yr_pct     | REAL    | 3-year return                 |
| return_5yr_pct     | REAL    | 5-year return                 |
| benchmark_3yr_pct  | REAL    | Benchmark return              |
| alpha              | REAL    | Alpha value                   |
| beta               | REAL    | Beta value                    |
| sharpe_ratio       | REAL    | Sharpe ratio                  |
| sortino_ratio      | REAL    | Sortino ratio                 |
| std_dev_ann_pct    | REAL    | Annualized standard deviation |
| max_drawdown_pct   | REAL    | Maximum drawdown              |
| aum_crore          | REAL    | Assets under management       |
| expense_ratio_pct  | REAL    | Expense ratio                 |
| morningstar_rating | INTEGER | Morningstar rating            |
| risk_grade         | TEXT    | Risk category                 |

---

## nav_history

| Column    | Type    | Description      |
| --------- | ------- | ---------------- |
| nav_date  | DATE    | NAV date         |
| amfi_code | INTEGER | AMFI scheme code |
| nav       | REAL    | Net Asset Value  |
