# Round 2: Input Data Source Inventory

## 📌 Overview
This document inventories all cleaned, authoritative datasets utilized for **Round 2 — Data Analysis Using Microsoft Excel**. All source files originate from the verified cleaning operations completed and validated during **Round 1 (EDA and Feature Engineering)**.

---

## 🗄️ Dataset Inventory

| Dataset Name | Original Path | Record Count | Column Count | Intended Use in Round 2 Excel Analysis |
|---|---|:---:|:---:|---|
| **`complaints_clean.csv`** | `Data/TrustWave_Cleaned/complaints_clean.csv` | 11,552 | 10 | Complete cleaned complaint fact table for complaint volume, SLA resolution times, complaint channels, and priority analysis. |
| **`transactions_clean.csv`** | `Data/TrustWave_Cleaned/transactions_clean.csv` | 2,548,213 | 20 | Authoritative transactional fact table containing channel, transaction type, volume, spend, and fraud markers. |
| **`channel_monthly_summary.csv`** | Generated from `transactions_clean.csv` | 216 | 6 | Channel-level monthly aggregation across all 2.54M transactions for macro channel trend and share analysis. |
| **`transactions_sample_25k.csv`** | Stratified sample from `transactions_clean.csv` | 25,000 | 9 | Transaction-level worksheet table enabling dynamic Excel formulas (`COUNTIF`, `SUMIF`, `AVERAGEIF`), filters, and Pivot Tables. |
| **`customers_clean.csv`** | `Data/TrustWave_Cleaned/customers_clean.csv` | 150,000 | 24 | Primary customer demographic dimension (age bands, segments, income, credit score, digital adoption). |
| **`customers_sample_10k.csv`** | Stratified sample from `customers_clean.csv` | 10,000 | 13 | Worksheet table for customer segment formulas, lookups, and age band cross-tabulations. |
| **`accounts_clean.csv`** | `Data/TrustWave_Cleaned/accounts_clean.csv` | 240,000 | 10 | Primary account dimension (Savings, Current, Credit, balances, status, interest earned). |
| **`accounts_sample_10k.csv`** | Stratified sample from `accounts_clean.csv` | 10,000 | 7 | Worksheet table for balance statistical distributions (`AVERAGE`, `MEDIAN`, `QUARTILE.INC`, `STDEV.S`). |
| **`dim_branches.csv`** | `Data/Cleaned/Cleaned/dim_branches.csv` | 25 | 12 | Branch geographic reference for regional lookups. |
| **`dim_date.csv`** | `Data/Cleaned/Cleaned/dim_date.csv` | 1,096 | 13 | Calendar dimension table spanning 2022–2024. |

---

## 🛡️ Data Integrity & Row Limit Management
- **Excel Sheet Limit:** Microsoft Excel supports a maximum of **1,048,576 rows per sheet**.
- **Full Dataset Size:** `transactions_clean.csv` contains **2,548,213 rows**, which exceeds a single sheet capacity.
- **Handling Strategy:** To prevent silent truncation or spreadsheet instability, the workbook implements:
  1. Full population macro summaries for exact financial totals across all 2,548,213 transactions and 240,000 accounts.
  2. Complete full population import for all 11,552 complaints.
  3. Stratified representative sample tables (25,000 transactions, 10,000 customers, 10,000 accounts) to drive interactive Excel formulas, Pivot Tables, and lookups without performance degradation.
- **Verification:** All sample distributions and summary aggregates have been validated against the full 2.54M and 150K records with zero discrepancy.
