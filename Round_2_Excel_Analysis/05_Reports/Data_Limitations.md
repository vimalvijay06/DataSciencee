# TrustWave Bank — Data Limitations & Assumptions Report

## 📌 Overview
This document formally records all data limitations, missing datasets, unsupported analyses, analytical assumptions, and recommended schema enhancements encountered during **Round 2 (Data Analysis Using Excel)**. In compliance with strict academic and professional data integrity standards, no missing data has been fabricated or falsely substituted.

---

## 🚫 1. Unavailable Datasets & Unsupported Analyses

### 1.1 Service Request Ticketing Dataset (`service_requests.csv`)
- **Status:** **Unavailable in Project Repository**
- **Impact on Assessment:** Area 6 requires analysis of *Service request trends (request counts by type, repeated requests, customer identifiers)*.
- **Handling Strategy:**
  - Formally documented as absent per assessment instructions.
  - Complaints (`fact_complaints.csv`) were **NOT** conflated with service requests, maintaining rigorous taxonomy separation between customer grievances/disputes and standard operational service requests.
  - Interaction channel touchpoint inquiry distributions from logged customer support events were analyzed as an operational proxy, accompanied by clear caveat notations.

### 1.2 Channel Usage Time-to-Serve Logs
- **Status:** **Missing Micro-Timestamps**
- **Impact:** `fact_transactions.csv` includes date attributes (`full_date`, `year`, `month`, `year_month`), but lacks millisecond/second execution timestamps or queue-wait durations.
- **Limitation:** In-branch teller queue times, ATM session durations, and online page load latencies cannot be computed from the current transaction schema.

---

## ⚙️ 2. Missing Columns & Schema Gaps

| Table | Missing Attribute | Desired Analytical Purpose | Business Workaround Used |
|---|---|---|---|
| `dim_customers` | `customer_lifetime_value (CLV)` | Precise long-term profitability segmentation | Proxy created using `total_balance` and `monthly_income` |
| `dim_accounts` | `overdraft_limit` & `credit_line` | Available credit line utilization monitoring | Evaluated based on `current_balance` and `account_type` |
| `fact_complaints` | `reopened_ticket_flag` | Measuring customer repeat dissatisfaction | Proxied via customer multi-ticket count in `Data_Complaints` |
| `fact_transactions`| `merchant_sub_category` | Micro-spend categorization (e.g., Grocery vs. Dining) | Relied on high-level `transaction_type` and channel |

---

## 📋 3. Target Schema Blueprint for Service Request Tracking

To fully satisfy operational reporting requirements in subsequent banking sprints, TrustWave Bank should deploy a dedicated `fact_service_requests.csv` data pipeline with the following schema:

```sql
CREATE TABLE fact_service_requests (
    request_id               VARCHAR(32) PRIMARY KEY,     -- Unique ticket ID (e.g., SRQ_100482)
    customer_id              VARCHAR(32) NOT NULL,        -- FK mapping to dim_customers
    account_id               VARCHAR(32),                 -- FK mapping to dim_accounts (nullable)
    request_type             VARCHAR(64) NOT NULL,        -- Cheque Book, Address Update, KYC Refresh, Debit Card Re-issue
    request_category         VARCHAR(32) NOT NULL,        -- Account Maintenance, Cards, Digital Access, Wealth
    intake_channel           VARCHAR(32) NOT NULL,        -- Mobile App, Net Banking, Branch, Phone Banking, ATM
    request_timestamp        TIMESTAMP NOT NULL,          -- Exact ticket opening datetime
    target_sla_hours         INTEGER NOT NULL,            -- Internal target service SLA in hours
    fulfillment_timestamp    TIMESTAMP,                   -- Timestamp when service request completed
    status                   VARCHAR(24) NOT NULL,        -- Open, In Progress, Completed, Cancelled
    first_contact_resolution BOOLEAN NOT NULL,            -- True if resolved during initial customer contact
    csat_score               SMALLINT CHECK (csat_score BETWEEN 1 AND 5), -- Customer satisfaction score
    agent_id                 VARCHAR(32)                  -- Support agent or digital bot identifier
);
```

---

## 📊 4. Analytical Assumptions Applied

1. **Representative Stratification:** The 25,000 transaction sample and 10,000 customer/account samples maintain identical proportional distributions across channels, segments, and account types as the full 2,548,213 population.
2. **Account Balance Valuation:** All account balances are recorded in United States Dollars ($ USD) with settled values.
3. **Resolution Days Metric:** Complaint resolution days represent elapsed business days from ticket logging to formal status closure.
4. **Data Integrity Assurance:** No synthetic rows were introduced into raw or cleaned datasets; all benchmarks mirror verified source data.
