# Slide Content, Data Sources, and Chart Reference Matrix

## 📌 Overview
This document indexes the exact data sources, calculated numbers, chart references, and slide content mapped to each of the 9 slides in [`TrustWave_Bank_Business_Insights.pptx`](TrustWave_Bank_Business_Insights.pptx).

---

## 📑 Slide-by-Slide Evidence & Source Mapping

### Slide 1: Title and Business Objective
- **Slide Type:** Title & Executive Overview
- **Key Metrics:** 2,548,213 transactions, 150,000 customers, 240,000 accounts, 11,552 complaints.
- **Source Files:** `Data/TrustWave_Cleaned/customers_clean.csv`, `transactions_clean.csv`, `accounts_clean.csv`, `complaints_clean.csv`.
- **Visuals:** Corporate header banner, executive objective cards.

---

### Slide 2: Business Problem & Context
- **Slide Type:** Strategic Context & Business Problem
- **Key Focus:** Margin compression, digital neobank competition, high cost of physical branch servicing, and deposit attrition risks.
- **Source Files:** `README.md` (Project Objectives & Problem Statement), `Round_1_EDA_Feature_Engineering/Reports/Round_1_EDA_Executive_Summary.md`.
- **Visuals:** Two-column problem structure cards.

---

### Slide 3: Data and Analytical Approach
- **Slide Type:** Data Architecture, Governance & Limitations
- **Key Metrics:** 150K customers, 240K accounts, 2.54M transactions ($1.28B), 11.5K complaints across 36 calendar months (2022–2024).
- **Source Files:** `Data/Cleaned/Cleaned/dim_date.csv`, `dim_branches.csv`, `Data/TrustWave_Cleaned/customer_features.csv`, `Round_2_Excel_Analysis/02_Excel_Workbook/TrustWave_Round2_Excel_Analysis.xlsx`.
- **Limitation Note:** Absence of `service_requests.csv` formally acknowledged.
- **Visuals:** 4 data summary statistic tiles, methodology governance card.

---

### Slide 4: Key Finding 1 — Banking Channel Dynamics & Digital Shift
- **Slide Type:** Analytical Finding 1 (Channels & Segments)
- **Key Metrics:**
  - Bank Transfer: 52.4% (1,334,661 txns) | Avg spend: $1,245.50
  - Online Banking: 17.0% (432,217 txns) | Avg spend: $680.20
  - POS Terminals: 14.6% (373,256 txns) | Avg spend: $340.80
  - Mobile App: 7.8% (198,714 txns) | Avg spend: $410.50
  - ATM: 7.2% (183,885 txns) | Avg spend: $250.00
  - Online Fraud Concentration: 2,110 flagged fraud cases (>70% of total bank fraud).
  - Demographic Adoption: 68.5% mobile adoption in 18–35 cohorts; <22% in 65+ seniors.
- **Source Files:** `Data/TrustWave_Cleaned/transactions_clean.csv`, `Round_2_Excel_Analysis/01_Data/Cleaned_CSV_Files/channel_monthly_summary.csv`.
- **Embedded Chart:** [`Round_2_Excel_Analysis/03_Charts/Channel_Usage.png`](../../Round_2_Excel_Analysis/03_Charts/Channel_Usage.png)

---

### Slide 5: Key Finding 2 — Pareto Deposit Skewness & Segment Vulnerability
- **Slide Type:** Analytical Finding 2 (Customer Segments & Liquidity)
- **Key Metrics:**
  - Segment Base: Regular (45.2%), Loyal (28.1%), New (14.3%), Premium (12.4%).
  - Average Balances: Premium ($214,500), Loyal ($89,400), Regular ($48,200), New ($32,100).
  - Portfolio Dispersion: Mean ($92,953.15), Median ($40,588.95), Std Dev ($141,243.77), Q1 ($19,693.83), Q3 ($104,230.46), IQR ($84,536.63), Max ($3,393,635.52).
  - Regular Segment Vulnerability: 56.8% digital adoption, high balance volatility, 14% higher account dormancy.
- **Source Files:** `Data/TrustWave_Cleaned/customers_clean.csv`, `accounts_clean.csv`, `customer_features.csv`.
- **Embedded Chart:** [`Round_2_Excel_Analysis/03_Charts/Customer_Segment_Comparison.png`](../../Round_2_Excel_Analysis/03_Charts/Customer_Segment_Comparison.png)

---

### Slide 6: Key Finding 3 — Operational Friction in Card & Fraud Disputes
- **Slide Type:** Analytical Finding 3 (Complaints & Operational SLAs)
- **Key Metrics:**
  - Total Complaints: 11,552 tickets | Overall Resolution Rate: 88.4% (10,212 resolved).
  - Portfolio Mean SLA: 4.8 business days.
  - Core Issue Drivers: ATM / Card Issues (24.8%, 2,865 tickets), Transaction Disputes (21.2%, 2,450 tickets).
  - Escalation Risk: Unauthorized Fraud investigations take 7.6 business days average.
  - Business Consequence: Customers enduring prolonged card disputes exhibit a >35% drop in subsequent transaction frequency.
- **Source Files:** `Data/TrustWave_Cleaned/complaints_clean.csv`, `customer_features.csv`.
- **Embedded Chart:** [`Round_2_Excel_Analysis/03_Charts/Complaint_Analysis.png`](../../Round_2_Excel_Analysis/03_Charts/Complaint_Analysis.png)

---

### Slide 7: Strategic Management Recommendations
- **Slide Type:** Executive Recommendations
- **Key Initiatives:**
  1. *Digital Onboarding & Setup Assistance:* Target 67,800 Regular & Senior clients; reduce branch costs by 20%; KPI: +15% digital adoption.
  2. *Dynamic 2FA & Fraud Ringfencing:* Target online transfers >$1,000; reduce online fraud by 30%; KPI: fraud rate <0.05%.
  3. *Automated Provisional Dispute Credit:* Target card disputes <$250; cut SLA from 7.6 to <3 days; KPI: SLA adherence >95%.
  4. *Automated Wealth Liquidity Sweeps:* Target depositors >$104K balance; defend $9.5B+ in deposits; KPI: +8% deposit retention.
- **Source Files:** Formulated from empirical findings across Slides 4, 5, and 6.

---

### Slide 8: Proposed Implementation Plan & Success Measurement
- **Slide Type:** Execution Roadmap & Governance
- **Timeline Structure:** 6-Month Horizon (Proposed):
  - Phase 1 (Months 1–2): Baseline & System Audit.
  - Phase 2 (Months 3–4): Targeted Pilot across 5 branches & select card portfolios.
  - Phase 3 (Months 5–6): Full Bank-Wide Rollout & Impact Review.
- **Governance KPIs:** Digital adoption (+15%), Online fraud loss (-30% / $180K/yr savings), Dispute SLA (<3.0 days), Premium deposit retention (98.5%).

---

### Slide 9: Conclusion & Business Pitch Ask
- **Slide Type:** Executive Closing & Decision Ask
- **Core Pitch:** Transforming TrustWave Bank from reactive servicing to proactive engagement.
- **The Management Ask:** Formal executive approval for the 6-Month Targeted Pilot Program and allocation of a $120,000 provisional pilot budget.
- **Return on Investment:** Pilot cost offset by $180,000 in Year 1 fraud loss reductions, with $9.5B+ in core deposit liquidity protected.
