<p align="center">
  <img src="assets/banner.png" width="100%">
</p>

<h1 align="center">FundSight</h1>

<p align="center">
Mutual Fund Analytics Platform
</p>

A data analytics platform for ingesting, cleaning, storing, and analyzing mutual fund datasets. The project implements a complete ETL pipeline, SQLite-based data warehouse, analytical SQL queries, and reporting modules to generate insights from mutual fund performance and investor transaction data.

---

# 🚀 Features

* ✅ Automated data ingestion pipeline
* ✅ Data cleaning and preprocessing using Pandas
* ✅ SQLite database integration
* ✅ Star schema database design
* ✅ Analytical SQL queries
* ✅ Data quality validation
* ✅ ETL verification and row count checks
* ✅ Dashboard-ready datasets
* ✅ Automated analytics report generation

---

# 📂 Project Structure

```text
fundsight-mutual-fund-analytics/
│
├── dashboard/
│   ├── charts.py
│   └── ...
│
├── data/
│   ├── raw/
│   │   ├── 01_fund_master.csv
│   │   ├── 02_nav_history.csv
│   │   ├── ...
│   │
│   └── processed/
│       ├── clean_nav.csv
│       ├── clean_transactions.csv
│       └── clean_performance.csv
│
├── docs/
│   ├── data_dictionary.md
│   ├── data_quality_summary.md
│   └── day1_todo.md
│
├── etl/
│   ├── data_ingestion.py
│   ├── clean_nav.py
│   ├── clean_transactions.py
│   ├── clean_performance.py
│   ├── load_to_sqlite.py
│   ├── verify_row_counts.py
│   └── check_db.py
│
├── reports/
│   ├── analytics.py
│   ├── sql_queries.sql
│   ├── top_alpha.csv
│   ├── top_sharpe.csv
│   ├── investor_demographics.csv
│   ├── gender_distribution.csv
│   └── state_investment.csv
│
├── sql/
│   ├── schema.sql
│   └── star_schema.sql
│
├── fundsight.db
├── requirements.txt
└── README.md
```

---

# 🔄 ETL Workflow

```text
Raw Mutual Fund Data
        │
        ▼
Data Ingestion
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Processed CSV Files
        │
        ▼
SQLite Database
        │
        ▼
Analytical SQL Queries
        │
        ▼
Analytics Reports
        │
        ▼
Dashboard Visualizations
```

---

# 🛠️ Tech Stack

| Layer                 | Technologies          |
| --------------------- | --------------------- |
| Programming           | Python 3              |
| Data Processing       | Pandas                |
| Database              | SQLite                |
| ORM / Database Access | SQLAlchemy            |
| Data Analysis         | SQL                   |
| Visualization         | Matplotlib            |
| Dashboard             | Streamlit *(planned)* |
| Documentation         | Markdown              |

---

# 📊 Current Progress

## ✅ Phase 1 — Data Ingestion

* Raw mutual fund datasets collected
* Dataset profiling completed
* Data ingestion pipeline implemented

---

## ✅ Phase 2 — ETL & Database

* Cleaned NAV history
* Cleaned investor transactions
* Cleaned scheme performance
* Implemented business rule validations
* KYC validation
* Expense ratio validation
* Anomaly detection
* SQLite database creation
* Star schema design
* Row count verification

---

## ✅ Analytics

Implemented analytical SQL queries for:

* Top funds by Sharpe Ratio
* Top Alpha funds
* Benchmark outperformers
* Investor demographics
* Gender distribution
* State-wise investments
* Fund house comparison
* Top AUM funds
* Expense ratio analysis
* High-risk funds

---

# 📈 Generated Outputs

The project currently generates:

* Cleaned datasets
* SQLite database
* SQL analytical reports
* Investor demographic reports
* Fund performance reports
* Dashboard-ready CSV files

---

# ▶️ Getting Started

## Clone Repository

```bash
git clone https://github.com/krishnavasnani07/fundsight-mutual-fund-analytics.git

cd fundsight-mutual-fund-analytics
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run ETL Pipeline

```bash
python etl/data_ingestion.py

python etl/clean_nav.py

python etl/clean_transactions.py

python etl/clean_performance.py

python etl/load_to_sqlite.py

python etl/verify_row_counts.py
```

---

# 📌 Roadmap

## ✅ Completed

* [x] Project setup
* [x] Data ingestion
* [x] ETL pipeline
* [x] Data cleaning
* [x] SQLite integration
* [x] SQL schema
* [x] Star schema
* [x] Data dictionary
* [x] SQL analytics
* [x] ETL validation

## 🚧 In Progress

* [ ] Interactive dashboard
* [ ] KPI visualizations
* [ ] Advanced analytics
* [ ] Performance optimization

---

# 📄 Documentation

Additional documentation is available in the **docs/** directory:

* Data Dictionary
* Data Quality Summary
* Project Notes

---

# 👨‍💻 Author

**Krishna Vasnani**

GitHub: https://github.com/krishnavasnani07

---

⭐ If you found this project useful, consider giving it a star.
