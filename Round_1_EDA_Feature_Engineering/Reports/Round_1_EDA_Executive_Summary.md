# TrustWave Bank — Round 1: EDA & Feature Engineering Executive Summary

## 📌 Executive Overview
- **Project:** TrustWave Bank — Customer Engagement & Analytics
- **Sprint Assessment:** Round 1 — Exploratory Data Analysis & Feature Engineering
- **Status:** **Completed & Executed**
- **Primary Notebook:** [`Round_1_EDA_Feature_Engineering/Notebooks/TrustWave_Bank_EDA_FeatureEngineering.ipynb`](../Notebooks/TrustWave_Bank_EDA_FeatureEngineering.ipynb)

---

## 🔍 Core Business Insights from Actual Data

### 1. Digital Adoption & Transaction Channels
- **Dominance of Digital:** Mobile and Internet banking account for over **55%** of all customer transaction volume.
- **Branch Reliance by Age Band:** Older demographics (56+ age bands) continue to show significantly higher physical branch touchpoint reliance, whereas customers aged 18–35 are predominantly mobile-first.
- **ATM Channel:** Primarily utilized for cash withdrawals, remaining steady across suburban and rural regions.

### 2. High-Risk Customer & Account Balance Segments
- **Balance Volatility:** Standard/Basic account segments exhibit higher balance fluctuations and lower liquidity buffers compared to Premium and Wealth segments.
- **Risk Category Correlation:** Customers identified in higher risk tiers have lower credit scores and an increased rate of declined transactions.

### 3. Service Interactions & Complaints
- **Resolution Cycle:** Average complaint resolution duration ranges from 3 to 7 business days, with digital transaction disputes and billing issues representing the highest volume of inquiries.
- **Regional Disparities:** Branches located in high-density urban zones record higher complaint volumes, corresponding directly to higher throughput and transaction frequency.

---

## ⚙️ Feature Engineering Summary
From the primary datasets, the following customer-level features were engineered and exported to `Data/TrustWave_Cleaned/`:
1. **`total_accounts`**: Total active accounts associated with each customer.
2. **`total_balance` & `avg_balance`**: Consolidated liquidity and mean balance per customer.
3. **`total_transactions`, `total_spend`, `avg_txn_amount`**: Aggregated transaction velocity and monetary exposure.
4. **`digital_txn_ratio`**: Ratio of digital transactions (Mobile + Online) to total transactions.
5. **`complaint_count` & `avg_resolution_days`**: Historical service interaction frequency and resolution duration.
6. **`loan_count` & `total_loan_amount`**: Outstanding borrowing and credit product utilization.
7. **Encoding**:
   - Ordinal Encoding applied to hierarchical bands (`Age_Band`, `Risk_Category`).
   - One-Hot Encoding applied to nominal categorical variables (`Region`, `Segment`).

---

## 📊 Visualizations Generated
All visual outputs are preserved in `Round_1_EDA_Feature_Engineering/Visualizations/`:
- `amount_distribution.png`: Skewness and distribution of transaction amounts.
- `correlation_heatmap.png`: Inter-feature correlation matrix of engineered features.
- `q1_channel_usage.png`: Breakdown of transaction frequency across banking channels.
- `q2_channel_by_age.png`: Channel preference stratified by age cohorts.
- `q3_account_trends.png`: Account status and balance distributions across types.
- `q4_complaints_region.png`: Geographic distribution of complaints and SLA metrics.
- `q5_balance_segment.png` & `q5_balance_risk.png`: Segmented liquidity and risk exposure.
- `q6_service_requests.png`: Complaint category volume and resolution performance.
