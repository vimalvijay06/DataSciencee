# Round 2: Data Analysis Using Microsoft Excel (30 Marks)
## TrustWave Bank Customer Insight | Implementation Guide & Deliverable Index

---

## 📌 1. Project Objective & Status
- **Assessment Sprint:** Round 2 — Data Analysis Using Microsoft Excel
- **Organization:** TrustWave Bank (Retail & Digital Banking Division)
- **Status:** **Completed & Validated**
- **Score Weight:** 30 Marks
- **Core Focus:** Multi-dimensional exploratory and statistical analysis across Banking Channels, Customer Segments, Account Activity, Complaints, Balance Distributions, and Service Touchpoints.

---

## 📂 2. Round 2 Directory Architecture

```text
Round_2_Excel_Analysis/
│
├── 01_Data/
│   ├── Source_Inventory.md            (Complete dataset catalog & record mappings)
│   ├── benchmarks.json                (Full population benchmarks for validation)
│   └── Cleaned_CSV_Files/             (Authoritative cleaned input CSVs for Excel)
│       ├── complaints_clean.csv       (11,552 records)
│       ├── transactions_sample_25k.csv(25,000 records)
│       ├── customers_sample_10k.csv   (10,000 records)
│       ├── accounts_sample_10k.csv    (10,000 records)
│       ├── channel_monthly_summary.csv(216 records)
│       ├── dim_branches.csv           (25 records)
│       └── dim_date.csv               (1,096 records)
│
├── 02_Excel_Workbook/
│   └── TrustWave_Round2_Excel_Analysis.xlsx [PRIMARY DELIVERABLE — 4.8 MB]
│
├── 03_Charts/
│   ├── Channel_Usage.png              (Channel volume vs. average spend)
│   ├── Customer_Segment_Comparison.png(Segment income vs. digital adoption)
│   ├── Account_Activity_Trends.png    (Total vs. active accounts portfolio)
│   ├── Complaint_Analysis.png         (Ticket volume vs. resolution SLAs)
│   ├── Balance_Distribution.png       (Histogram & IQR boxplots)
│   └── Service_Request_Trends.png     (Touchpoint inquiries & limitation notice)
│
├── 04_Pivot_Analysis/
│   └── Pivot_Table_Inventory.md       (Documentation of 3 native Pivot Tables & Charts)
│
├── 05_Reports/
│   ├── Round2_Analysis_Report.md      (Comprehensive analytical report)
│   └── Data_Limitations.md           (Documented missing datasets & target schema)
│
├── 06_Validation/
│   └── Validation_Report.md           (Audit matrix with 100% PASS on all checks)
│
├── build_model.py                     (Automated reproducible openpyxl generator script)
└── README.md                          (This comprehensive index)
```

---

## 📗 3. Primary Deliverable: `TrustWave_Round2_Excel_Analysis.xlsx`
The primary workbook deliverable is located at:
[`Round_2_Excel_Analysis/02_Excel_Workbook/TrustWave_Round2_Excel_Analysis.xlsx`](02_Excel_Workbook/TrustWave_Round2_Excel_Analysis.xlsx)

### Worksheets Breakdown (14 Sheets Total):
1. **`Summary_Dashboard`**: Executive dashboard with 6 KPI cards, cross-functional summary tables, and embedded chart figures.
2. **`Read_Me`**: Project overview, methodology, metadata, and sheet navigation index.
3. **`Data_Dictionary`**: Enterprise definitions, allowable values, and schema mappings across 20 core fields.
4. **`Channel_Analysis`**: Banking channel volume, spend share, and fraud risk cross-tabulations.
5. **`Customer_Segments`**: Segment performance breakdown (Loyal, New, Premium, Regular) and Age Band cohorts.
6. **`Account_Activity`**: Portfolio health across Savings, Current, and Credit accounts, active rates, and interest.
7. **`Complaint_Analysis`**: Complaint categories, SLA resolution durations, intake channels, and priority breakdowns.
8. **`Balance_Analysis`**: Descriptive statistics (`AVERAGE`, `MEDIAN`, `MIN`, `MAX`, `STDEV.S`, `QUARTILE.INC` Q1/Q3, `IQR`).
9. **`Service_Requests`**: Customer service touchpoint analysis and formal documentation of the IT service desk limitation.
10. **`Pivot_Analysis`**: Three native Microsoft Excel Pivot Tables and three interactive Pivot Charts.
11. **`Data_Transactions`**: Cleaned representative transaction records (25,000 rows).
12. **`Data_Customers`**: Cleaned customer demographic records (10,000 rows).
13. **`Data_Accounts`**: Cleaned account portfolio records (10,000 rows).
14. **`Data_Complaints`**: Complete cleaned complaint records (11,552 rows).

---

## 🚀 4. Instructions for Opening & Interacting with the Workbook
1. Open [`TrustWave_Round2_Excel_Analysis.xlsx`](02_Excel_Workbook/TrustWave_Round2_Excel_Analysis.xlsx) in **Microsoft Excel 2016, 2019, 2021, or Microsoft 365**.
2. **Enable Editing** if opened in Protected View.
3. **Review Formulas:** Click any calculated cell to inspect live dynamic formulas (`COUNTIF`, `SUMIF`, `AVERAGEIF`, `MEDIAN`, `STDEV.S`, `QUARTILE.INC`).
4. **Interact with Pivot Tables:** Navigate to the `Pivot_Analysis` tab. Click any cell inside the Pivot Tables to trigger the **PivotTable Fields** panel, filter by category, or click **Data -> Refresh All** (`Ctrl + Alt + F5`).

---

## 🛡️ 5. Known Data Limitations
As detailed in [`05_Reports/Data_Limitations.md`](05_Reports/Data_Limitations.md):
- The repository does not include a dedicated non-complaint service-desk dataset (`service_requests.csv`).
- In strict adherence to assessment rules, complaints have **not** been falsely fabricated as service requests. Inquiry touchpoints were analyzed and a target relational schema was documented.

---

## ⏭️ 6. Next Steps
- **Round 1 (EDA & Feature Engineering):** Completed & Executed.
- **Round 2 (Excel Data Analysis):** Completed & Validated.
- **Round 3:** Not started (prepared folder remains empty pending Round 3 requirements).
