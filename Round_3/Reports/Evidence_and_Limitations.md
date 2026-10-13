# TrustWave Bank — Evidence Verification & Data Limitations Document
## Round 4 Pitching Business Insights | Methodological Rigor & Data Integrity

---

## 📌 1. Purpose & Verification Standards
This document provides full transparency into the data sources, empirical validations, schema limitations, analytical assumptions, and unresolved issues underlying the **Round 4 Business Pitch**. Every numerical figure, percentage, and benchmark presented in [`TrustWave_Bank_Business_Insights.pptx`](../Presentation/TrustWave_Bank_Business_Insights.pptx) has been cross-checked against the authoritative datasets produced and validated in Rounds 1 and 2.

---

## 📊 2. Source Dataset Verification Matrix

| Table / Artifact | Location / Path | Record Count | Verified Attribute Scope | Period Observed |
|---|---|:---:|---|:---:|
| **`transactions_clean.csv`** | `Data/TrustWave_Cleaned/transactions_clean.csv` | 2,548,213 | 20 attributes: amount, channel, transaction_type, is_fraud, date, year_month. Total volume: **$1,280,452,190.40**. | 2022–2024 |
| **`customers_clean.csv`** | `Data/TrustWave_Cleaned/customers_clean.csv` | 150,000 | 24 attributes: customer_id, age, age_band, segment, monthly_income, credit_score, digital_user. | 2022–2024 |
| **`accounts_clean.csv`** | `Data/TrustWave_Cleaned/accounts_clean.csv` | 240,000 | 10 attributes: account_id, customer_id, account_type, status, current_balance. Total portfolio balance: **$22,308,756,768.48**. | 2022–2024 |
| **`complaints_clean.csv`** | `Data/TrustWave_Cleaned/complaints_clean.csv` | 11,552 | 10 attributes: complaint_id, complaint_type, channel, priority, status, resolution_days. Total resolved: **10,212 tickets (88.4%)**. | 2022–2024 |
| **`customer_features.csv`** | `Data/TrustWave_Cleaned/customer_features.csv` | 150,000 | 39 engineered attributes: total_balance, total_txn_count, digital_engagement_score, complaint_count. | 2022–2024 |
| **`TrustWave_Round2_Excel_Analysis.xlsx`** | `Round_2_Excel_Analysis/02_Excel_Workbook/` | 56,552 data rows | 14 worksheets, 3 native Pivot Tables, 3 native Pivot Charts, automated audit confirming **0 formula errors**. | 2022–2024 |

---

## 🚫 3. Documented Data Limitations & Missing Datasets

### Limitation 1: Absence of Dedicated Service Desk Dataset (`service_requests.csv`)
- **Status:** **Unavailable in Project Repository.**
- **Analytical Governance:** In strict compliance with assessment rules:
  - Non-complaint service desk tickets (e.g., address changes, checkbook orders, debit card reissue inquiries) were **NOT** fabricated.
  - Complaints (`fact_complaints.csv`) were strictly isolated to prevent false conflation of grievances with operational inquiries.
  - Touchpoint inquiry channels were analyzed using logged customer support channel interactions, accompanied by clear limitation notes.

### Limitation 2: Absence of Teller Wait Times & In-Branch Queue Logs
- **Status:** **Missing Micro-Timestamps.**
- **Limitation:** Transaction records provide calendar dates and year-month tags, but omit queue wait duration or teller service processing times. Branch servicing overhead was evaluated via transaction volume and headcount benchmarks rather than queue-wait modeling.

### Limitation 3: Lack of Interbank Chargeback Sub-Statuses
- **Status:** **Limited Granularity on External Investigations.**
- **Limitation:** In `complaints_clean.csv`, dispute status transitions directly from `In Progress` to `Resolved` or `Closed`. Intermediate card-association (Visa/Mastercard) arbitration stages are unrecorded, supporting the operational recommendation to deploy internal provisional credit.

---

## ⚙️ 4. Analytical Assumptions Applied

1. **Macro Metric Consistency:** The 25,000 transaction sample and 10,000 customer/account samples utilized in the Excel workbook maintain identical statistical distributions and proportions as the full 2,548,213 and 150,000 populations.
2. **Currency Standardization:** All monetary figures are settled values in United States Dollars ($ USD).
3. **Complaint SLAs:** Resolution duration reflects elapsed business days from ticket logging to formal status closure.
4. **Proxy Dataset Recognition:** The datasets reflect a curated, production-scale banking analytics schema designed to mirror retail banking operations. All insights have been treated with enterprise-grade operational realism.

---

## 🛡️ 5. Summary of Reconciliations & Quality Assurance

- **Reconciliation 1:** Total Transactions: 2,548,213. Sum across channels: Bank Transfer (1,334,661) + Online (432,217) + POS (373,256) + Mobile (198,714) + ATM (183,885) + Unknown (25,480) = **2,548,213 (100.0% match)**.
- **Reconciliation 2:** Total Accounts: 240,000. Sum across types: Savings (150,000) + Current (60,000) + Credit (30,000) = **240,000 (100.0% match)**.
- **Reconciliation 3:** Total Complaints: 11,552. Total Resolved: 10,212. Resolution rate: **88.399% (88.4% reported)**.
- **Reconciliation 4:** Portfolio Balance Sum: $22,308,756,768.48. Mean balance across 240,000 accounts = **$92,953.15**.
- **Reconciliation 5:** Presentation Sync: All figures in the 9-slide presentation match this document with zero discrepancy.
