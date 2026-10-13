# TrustWave Bank — Round 2: Data Analysis Using Excel Report

## 📌 Executive Summary & Assessment Objective
This report details the comprehensive Excel data analytics implementation conducted for **TrustWave Bank** under **Round 2 (Data Analysis Using Excel — 30 Marks)**. The analytical objective is to evaluate multi-dimensional customer engagement across banking channels, demographic segments, account portfolio health, customer complaint resolution, balance liquidity reserves, and customer service touchpoints.

The primary deliverable is [`TrustWave_Round2_Excel_Analysis.xlsx`](../02_Excel_Workbook/TrustWave_Round2_Excel_Analysis.xlsx), containing 14 fully integrated worksheets, real dynamic formulas, statistical distributions, native Pivot Tables, native Pivot Charts, and an executive summary dashboard.

---

## 🗄️ 1. Data Sources & Preprocessing

### Input Datasets
All analyses build upon the cleaned, verified datasets produced during Round 1 EDA and Feature Engineering:
- **`transactions_clean.csv`**: 2,548,213 transactions across 20 attributes ($1.28B total volume).
- **`customers_clean.csv`**: 150,000 customers across 24 demographic and credit attributes.
- **`accounts_clean.csv`**: 240,000 accounts across 10 balance and operational fields ($22.3B balance portfolio).
- **`complaints_clean.csv`**: 11,552 verified complaints across categories, channels, and SLA resolution times.
- **`dim_branches.csv` & `dim_date.csv`**: Supporting geographic (25 branches) and temporal (1,096 dates) dimensions.

### Excel Row Capacity Management
- **Worksheet Constraint:** Microsoft Excel supports a maximum limit of **1,048,576 rows** per worksheet.
- **Implementation Design:** Because the complete transactional fact table (2.54M records) exceeds the single-sheet limit, the workbook employs a dual-tiered architecture:
  1. **Macro Population Metrics:** Direct full-population financial benchmarks embedded in summary tables.
  2. **Representative Structured Tables:** Stratified sample tables (`Data_Transactions` 25,000 rows, `Data_Customers` 10,000 rows, `Data_Accounts` 10,000 rows) alongside the full population of all 11,552 records in `Data_Complaints`.
  3. **Formulaic Evaluation:** Formulas evaluate cleanly without workbook lag or memory truncation.

---

## ⚙️ 2. Methods and Excel Formulas Employed

The workbook implements strictly dynamic Excel formulas rather than hardcoded calculations:
- **Volume & Cross-Tabulations:** `=COUNTIF(range, criteria)`, `=COUNTIFS(range1, crit1, range2, crit2)`
- **Financial Aggregations:** `=SUMIF(range, criteria, sum_range)`, `=SUMIFS(...)`
- **Unit Averages & Yields:** `=AVERAGEIF(...)`, `=IFERROR(Total_Amount / Count, 0)`
- **Parametric & Non-Parametric Statistics:**
  - Center of Mass: `=AVERAGE(range)`
  - Robust Center (Median): `=MEDIAN(range)`
  - Spread & Dispersion: `=STDEV.S(range)`, `=MIN(range)`, `=MAX(range)`
  - Percentiles & IQR: `=QUARTILE.INC(range, 1)`, `=QUARTILE.INC(range, 3)`, `IQR = Q3 - Q1`
- **Data Lookup & Linking:** `=XLOOKUP(lookup_val, lookup_arr, return_arr, "N/A")`

---

## 🔍 3. In-Depth Findings Across the Six Required Analysis Areas

### Area 1: Channel Usage
- **Dominant Channel:** **Bank Transfer** is the primary volume driver, accounting for **52.4%** of all transactions (1,334,661 txns), reflecting automated corporate payroll, merchant settlement, and recurring bill transfers.
- **Digital Engagement:** **Online Banking** (17.0%, 432,217 txns) and **POS card terminals** (14.6%, 373,256 txns) represent the next highest share. **Mobile App** transactions account for **7.8%** (198,714 txns).
- **Physical ATM Reliance:** ATM cash withdrawals account for **7.2%** (183,885 txns), concentrated in suburban retail branches.
- **Fraud Distribution:** Online banking accounts for over **70%** of flagged fraudulent transactions (2,110 cases), while physical POS terminals recorded zero fraud cases.
- **Visual Chart:** [`Channel_Usage.png`](../03_Charts/Channel_Usage.png) illustrates the dual-axis relationship between transaction volume and average dollar spend per channel.

### Area 2: Customer Segment Comparison
- **Portfolio Segments:** TrustWave Bank categorizes customers into four commercial tiers: `Regular` (45.2%), `Loyal` (28.1%), `New` (14.3%), and `Premium` (12.4%).
- **Liquidity Disparity:** Premium customers maintain average balances of **$214,500**, compared to **$48,200** for Regular customers (a 4.45x multiple).
- **Digital Adoption:** Digital banking penetration reaches **92.1%** in the Premium segment and **84.3%** in the Loyal segment, whereas New customers lag at **56.8%**.
- **Age Cohorts:** The 18–25 and 26–35 age groups have the highest digital app utilization (68.5%), while the 65+ demographic remains reliant on in-branch banking.
- **Visual Chart:** [`Customer_Segment_Comparison.png`](../03_Charts/Customer_Segment_Comparison.png) highlights segment income against digital adoption rates.

### Area 3: Account Activity
- **Account Distribution:** The 240,000 account portfolio comprises **Savings** (62.5%), **Current** (25.0%), and **Credit** (12.5%).
- **Active Operational State:** Overall portfolio active rate stands at **83.2%**. Inactive and dormant accounts are concentrated primarily in secondary savings accounts.
- **Balance Exposure:** Savings accounts hold over **$16.8 Billion** in liquidity reserves, representing the core deposit funding base for TrustWave Bank.
- **Visual Chart:** [`Account_Activity_Trends.png`](../03_Charts/Account_Activity_Trends.png) contrasts total vs. active accounts across portfolio categories.

### Area 4: Complaint Analysis
- **Ticket Volume:** 11,552 customer complaints were logged across 7 operational categories.
- **Top Issue Drivers:**
  1. *ATM / Card Issues:* 24.8% of all complaints (2,865 tickets).
  2. *Transaction Disputes:* 21.2% (2,450 tickets).
  3. *Account Access / Maintenance Issues:* 18.5% (2,137 tickets).
- **Resolution SLAs:** Average resolution duration is **4.8 business days**. Overall ticket resolution rate reaches **88.4%**.
- **Operational Bottleneck:** Fraud and unauthorized transaction disputes take an average of **7.6 days** to resolve due to multi-party card network investigations.
- **Visual Chart:** [`Complaint_Analysis.png`](../03_Charts/Complaint_Analysis.png) maps complaint frequency against mean turnaround days.

### Area 5: Balance Distribution
- **Portfolio Population Statistics (240,000 Accounts):**
  - **Mean Balance:** `$92,953.15`
  - **Median Balance:** `$40,588.95`
  - **Standard Deviation:** `$141,243.77`
  - **Minimum:** `$703.88` | **Maximum:** `$3,393,635.52`
  - **25th Percentile (Q1):** `$19,693.83`
  - **75th Percentile (Q3):** `$104,230.46`
  - **Interquartile Range (IQR):** `$84,536.63`
- **Skewness Analysis:** The substantial delta between the Mean ($92,953) and Median ($40,589) confirms significant positive skewness (right-skewed Pareto distribution), typical of retail banking where high-net-worth commercial balances pull the arithmetic average upwards.
- **Visual Chart:** [`Balance_Distribution.png`](../03_Charts/Balance_Distribution.png) exhibits the distribution histogram and IQR boxplot across account types.

### Area 6: Service Request Trends & Data Limitation
- **Available Data:** Customer interaction channel logs show **Branch** (34.2%), **Call Center** (28.4%), and **Mobile App Support** (21.5%) as primary customer touchpoints.
- **Data Limitation Documentation:** A dedicated non-complaint IT service desk ticketing table (e.g. `service_requests.csv`) is absent in the source data. As mandated, complaints were not falsely relabeled as service requests.
- **Blueprint Schema:** Detailed specifications for implementing a dedicated service request tracking log are documented in [`Data_Limitations.md`](Data_Limitations.md).
- **Visual Chart:** [`Service_Request_Trends.png`](../03_Charts/Service_Request_Trends.png) depicts channel inquiry volume with formal limitation notations.

---

## 📊 4. Pivot Tables and Pivot Charts Implementation
The workbook contains three native Microsoft Excel Pivot Tables on the `Pivot_Analysis` worksheet:
1. **`PT_Channel_Summary`**: Cross-tabulates channel vs. transaction type with a Clustered Column Pivot Chart.
2. **`PT_Segment_Risk`**: Evaluates customer segment vs. risk category with a Clustered Bar Pivot Chart.
3. **`PT_Complaint_Priority`**: Maps complaint category against ticket priority with a Clustered Column Pivot Chart.

---

## 💡 5. Strategic Recommendations for TrustWave Bank
1. **Digital Channel Migration:** Expand self-service features for routine transfers to transition volume from branches to mobile, targeting an operational cost reduction of 22%.
2. **Fraud Prevention Enhancement:** Implement dynamic biometric 2-factor authentication on online transactions exceeding $1,000 to mitigate the high fraud concentration in digital channels.
3. **SLA Automation for Card Disputes:** Deploy automated provisional credit workflows for ATM and card disputes under $250 to reduce resolution times from 7.6 to under 3 days.
4. **Targeted Wealth Management Offerings:** Introduce automated wealth management sweeps for customers holding balances above the 75th percentile ($104,230) to increase fee-based revenue.
