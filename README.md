<div align="center">

<img src="https://img.shields.io/badge/-%F0%9F%8F%A6%20BANKING%20ANALYTICS%20PROJECT-1A5276?style=for-the-badge&labelColor=0D2137" alt="title" width="500"/>

<br><br>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1200&color=2E9EF7&center=true&vCenter=true&width=900&lines=End-to-End+Banking+Analytics+Project;Transforming+Raw+Banking+Data+into+Business+Insights;150K%2B+Customers+%7C+240K%2B+Accounts+%7C+2M%2B+Transactions;Customer+Analytics+%7C+Fraud+Analysis+%7C+Loan+Portfolio+Analysis;Interactive+Tableau+Dashboards+for+Business+Decision+Making" alt="Typing SVG" />
</p>
<br>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)]()
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)]()
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)](https://public.tableau.com/views/BankingProject_17829830247920/Dashboard1)

<br>


![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)
![Domain](https://img.shields.io/badge/Domain-Banking%20%26%20Finance-1A5276?style=flat-square)
![Dashboards](https://img.shields.io/badge/Dashboards-3-orange?style=flat-square)
![Notebooks](https://img.shields.io/badge/EDA%20Notebooks-6-blueviolet?style=flat-square)
![Data Sources](https://img.shields.io/badge/Data%20Sources-9%20CSV%20Files-blue?style=flat-square)
![Customers](https://img.shields.io/badge/Customers%20Analyzed-1%2C50%2C000-red?style=flat-square)

<br>

> *An end-to-end Business Intelligence project transforming raw banking data into strategic insights — covering customer segmentation, transaction behavior, fraud monitoring, loan portfolio health, branch operations, and complaint management across 1,50,000+ customers.*

<br>

### 🔗 [View Live Tableau Dashboard](https://public.tableau.com/views/BankingProject_17829830247920/Dashboard1) &nbsp;|&nbsp; [Browse EDA Notebooks](#-exploratory-data-analysis) &nbsp;|&nbsp; [See Key Insights](#-key-insights)

</div>

---

<div align="center">

## 📊 Project at a Glance

| 👥 Customers | 🏦 Accounts | 💳 Transactions | 🏢 Dashboards |
|:------------:|:-----------:|:---------------:|:-------------:|
| **1,50,000** | **2,40,000** | **20L+** | **3** |
</div>

---

## 📌 Table of Contents

- [🎯 Business Problem](#-business-problem)
- [🎯 Project Objectives](#-project-objectives)
- [🗄️ Data Architecture](#️-data-architecture)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [📊 Exploratory Data Analysis](#-exploratory-data-analysis)
- [📈 Tableau Dashboards](#-tableau-dashboards)
- [🔍 Key Insights](#-key-insights)
- [🚀 Skills Demonstrated](#-skills-demonstrated)
- [📌 Future Improvements](#-future-improvements)
- [👨‍💻 Author](#-author)

---

## 🎯 Business Problem

> *Modern banks generate millions of records across customers, accounts, transactions, loans, cards, branches, and complaints. Without proper analytics, it becomes difficult to understand customer behavior, monitor business performance, identify operational bottlenecks, detect fraud, and support strategic decision-making.*

This project answers **critical business questions** that banking leadership needs:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  💼 Who are the bank's most valuable customers?                            │
│  💰 Which customer segments maintain the highest balances?                 │
│  👥 How do customers behave across different age groups and occupations?   │
│  💳 Which transaction channels generate the most activity?                 │
│  🚨 Are fraud patterns changing over time?                                 │
│  🏠 Which loan types carry the highest financial exposure?                 │
│  🏢 Which branches process the highest transaction volume?                 │
│  📋 Which complaint types require immediate operational improvements?      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Project Objectives

- ✅ Clean and prepare 9 raw banking datasets for analysis
- ✅ Build a Star Schema data model connecting all 9 CSV files
- ✅ Perform deep Exploratory Data Analysis (EDA) across 6 notebooks
- ✅ Identify customer behavior patterns and financial trends
- ✅ Analyze transaction, fraud, merchant, branch, and loan performance
- ✅ Evaluate complaint handling and operational efficiency
- ✅ Build 3 interactive, multi-dimensional Tableau dashboards for business users

---

## 🗄️ Data Architecture

### Star Schema Model

```
                         ┌──────────────────┐
                         │   dim_date.csv   │
                         │  (Date Dimension)│
                         └────────┬─────────┘
                                  │
 ┌──────────────────┐   ┌─────────▼──────────────┐   ┌──────────────────┐
 │ dim_customers    │   │                        │   │  dim_merchants   │
 │ .csv             ├───►  fact_transactions.csv  ◄───┤  .csv           │
 │ (Customer Dim)   │   │  (Central Fact Table)  │   │  (Merchant Dim)  │
 └──────────────────┘   └─────────┬──────────────┘   └──────────────────┘
                                  │
 ┌──────────────────┐   ┌─────────▼──────────────┐   ┌──────────────────┐
 │ dim_accounts     │   │   fact_loans.csv       │   │  dim_branches    │
 │ .csv             ├───►   fact_complaints.csv   ◄───┤  .csv           │
 │ (Account Dim)    │   │   (Supporting Facts)   │   │  (Branch Dim)    │
 └──────────────────┘   └────────────────────────┘   └──────────────────┘
 ┌──────────────────┐
 │  dim_cards.csv   │
 │  (Card Dim)      │
 └──────────────────┘
```

### Dataset Summary

| # | Dataset | Key Fields | Purpose |
|---|---------|------------|---------|
| 1 | `dim_customers.csv` | Customer ID, Segment, Age, Occupation, Risk Category, Credit Score, Income | Customer profiling & segmentation |
| 2 | `dim_accounts.csv` | Account ID, Account Type, Current Balance, Avg Monthly Balance, Status | Account performance analysis |
| 3 | `fact_transactions.csv` | Transaction ID, Amount, Channel, Type, Status, Fraud Flag, Merchant | Transaction & fraud analytics |
| 4 | `fact_loans.csv` | Loan ID, Type, Amount, EMI, Interest Rate, Status (Active/Closed/Default) | Loan portfolio health |
| 5 | `dim_branches.csv` | Branch ID, Name, City, Region, Zone, Manager, Employee Count | Branch performance benchmarking |
| 6 | `dim_cards.csv` | Card ID, Card Type, Card Status, Fee Waived, Annual Fee | Card product analytics |
| 7 | `dim_merchants.csv` | Merchant ID, Category, City | Merchant category analysis |
| 8 | `fact_complaints.csv` | Complaint ID, Type, Status, Channel, Resolution Days | Complaint SLA monitoring |
| 9 | `dim_date.csv` | Date, Month, Quarter, Year | Time-based trend analysis |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Data cleaning & analysis |
| **Data Processing** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Data cleaning & transformation |
| **Visualization (Python)** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat-square) | EDA charts & statistical plots |
| **BI Dashboards** | ![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat-square&logo=tableau&logoColor=white) | Interactive business dashboards |
| **Environment** | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white) | Development & notebooks |

</div>

---

## 📂 Project Structure

```text
📦 Banking-Analytics-Project/
│
├── 📁 Data/
│   ├── 📂 Raw Data/                         ← Original banking CSV files
│   └── 📂 Cleaned Data/                     ← Cleaned datasets ready for analysis
│
├── 📁 Python/
│   ├── 📓 01_Data_Understanding.ipynb       ← Dataset exploration & initial assessment
│   ├── 📓 02_Data_Cleaning.ipynb            ← Data cleaning & preprocessing
│   ├── 📓 03_Customer_Account_EDA.ipynb     ← Customer & account exploratory analysis
│   ├── 📓 04_Transaction_EDA.ipynb          ← Transaction & fraud analysis
│   ├── 📓 05_Loan_Complaint_Branch_EDA.ipynb← Loan, complaint & branch analysis
│   └── 📓 06_Business_Insights.ipynb        ← Key business insights & recommendations
│
├── 📁 Tableau/
│   ├── 🗂️ Banking_Analytics_Dashboard.twbx  ← Tableau workbook
│   └── 📁 Dashboard Images/                 ← Dashboard preview images
│
└── 📄 README.md
```

---

## 📊 Exploratory Data Analysis

> *6 Jupyter Notebooks covering the complete analytics workflow — from understanding raw data to generating business insights.*

<details>
<summary><b>📓 Notebook 1 — Data Understanding</b></summary>

**Key Questions Answered:**
- What datasets are included in the project?
- What is the structure of each dataset?
- What are the data types and column descriptions?
- How many records and features are available?
- Which columns contain missing values?
- What data quality issues need to be addressed before analysis?

</details>

<details>
<summary><b>📓 Notebook 2 — Data Cleaning</b></summary>

**Key Tasks Performed:**
- Removed duplicate records
- Handled missing values
- Corrected inconsistent data formats
- Standardized categorical values
- Converted date columns to appropriate formats
- Optimized data types for analysis
- Exported cleaned datasets for EDA and Tableau

</details>

<details>
<summary><b>📓 Notebook 3 — Customer & Account Analysis</b></summary>

**Key Questions Answered:**
- What is the gender distribution of customers?
- Which age groups dominate the customer base?
- Which occupations are most common?
- How are customers distributed across income brackets?
- Which customer segments maintain the highest balances?
- Which account types (Savings, Current, Credit) are most common?
- How are customers distributed across different risk categories?
- Which occupations have the highest number of customers?

</details>

<details>
<summary><b>📓 Notebook 4 — Transaction Analysis</b></summary>

**Key Questions Answered:**
- How are transaction volumes trending over time?
- Which transaction types generate the highest volume?
- Which transaction channels are used most frequently?
- Which merchant categories process the most transactions?
- Which cities record the highest transaction activity?
- How are fraud transactions changing over time?
- What is the overall transaction completion rate?

</details>

<details>
<summary><b>📓 Notebook 5 — Branch, Merchant, Complaint & Loan Analysis</b></summary>

**Key Questions Answered:**
- Which branches process the highest transaction volumes?
- Which merchant categories generate the highest business activity?
- Which loan types are issued most frequently?
- Which loan types have the highest average loan amount?
- Which complaint types are reported most often?
- What is the average complaint resolution time?
- Which branches perform best across different business metrics?

</details>

<details>
<summary><b>📓 Notebook 6 — Business Insights</b></summary>

**Key Deliverables:**
- Executive summary of analytical findings
- Customer segmentation insights
- Transaction and fraud trends
- Loan portfolio insights
- Branch performance recommendations
- Complaint management observations
- Actionable business recommendations supported by data

</details>
---

## 📈 Tableau Dashboards

### 🔗 [Live on Tableau Public → Click to Explore](https://public.tableau.com/views/BankingProject_17829830247920/Dashboard1)

---

### 🏦 Dashboard 1 — Customer & Account Dashboard

**6 KPI Tiles**

| KPI | Value | Insight |
|-----|-------|---------|
| 🔵 Total Customers | **1,50,000** | Full customer base size |
| 🔵 Total Accounts | **2,40,000** | Avg 1.6 accounts per customer |
| 🟢 Avg Current Balance | **₹92,953** | Bank-wide average |
| 🔵 Premium Customers | **33,196** | 22% of customer base |
| 🔴 High Risk Customers | **26,430** | 17.6% of customer base |
| 🔵 Total Savings Accounts | **1,27,262** | 53% of all accounts |

**Visualization Sheets**

| Sheet | Chart Type |
|-------|------------|
| Customer Segments | Horizontal Bar | 
| Risk Distribution Across Occupations | Stacked Bar | 
| Customer Density Highlight Table | Square Heatmap | 
| Account Types | Horizontal Bar | 
| Customer Segment Mix by Occupation | Stacked Bar |
| Avg Balance — Age Group × Segment | Square Heatmap | 

---

### 💳 Dashboard 2 — Banking Transaction Dashboard

**Focus Areas:** Monthly trends, transaction types, channels, merchant categories, fraud patterns, city-wise volumes, transaction status

| Sheet | Chart Type | 
|-------|------------|
| Monthly Transaction Volume | Line Chart |
| Transaction Type Distribution | Horizontal Bar |
| Transactions by Channel | Horizontal Bar | 
| Top 10 Merchant Categories | Horizontal Bar | 
| Top 10 Transaction Cities | Bar Chart | 
| Monthly Fraud Trend | Line Chart | 
| Transaction Status Distribution | Horizontal Bar | 

---

### 📋 Dashboard 3 — Loans, Complaints & Branch Performance

**Focus Areas:** Loan portfolio health, default distribution, complaint SLA, branch benchmarking

| Sheet | Chart Type | 
|-------|------------|
| Loan Status Distribution | Horizontal Bar | 
| Loan Type Distribution | Horizontal Bar | 
| Average Loan Amount by Type | Horizontal Bar | 
| Complaint Status Distribution | Horizontal Bar | 
| Resolution Time by Complaint Type | Horizontal Bar |
| Top 10 Branches by Transactions | Horizontal Bar | 

---

## 🔍 Key Insights

### 👥 Customer Insights
```
📍 Regular segment is the largest (61,393 customers) but holds the lowest avg balance (₹30,278)
💎 Premium customers (33,196) hold avg ₹2,48,885 — 2.7× the bank average
⚠️  17.6% of customers (26,430) are High Risk — concentrated in Self-Employed & Business Owners
🏦  Savings accounts dominate at 53% — cross-sell opportunity for Current/Credit products
```

### 💳 Transaction Insights
```
📈  Transaction volume grew consistently from 2022 to 2025
💰  Deposits (14,17,776) far outpace Purchases (6,60,056) — savings-dominant behavior
🔄  Bank Transfer is the most used channel (12,84,914 transactions)
🛒  Groceries, Online Shopping, and Dining are the top merchant categories
🚨  Fraud represents a very small % of total transactions but shows rising trend
```

### 🏠 Loan Insights
```
📋  Personal Loans are issued most frequently (36,106 loans)
🏠  Home Loans carry the highest avg amount (₹47,50,148) — largest risk concentration
⚡  Higher-risk customers show significantly greater loan default proportions
📊  EMI increases proportionally with loan amount across all loan types
```

### 📋 Complaint Insights
```
✅  70% of complaints (7,798 of 11,124) are successfully resolved
📞  Phone is the primary complaint channel
🚨  Fraud & Transaction Disputes require the longest resolution times
⏱️  Resolution time is relatively consistent across standard complaint types
```

### 🏢 Branch & Merchant Insights
```
🏆  Kochi Branch 2 leads with 2,12,142 transactions
📊  Transaction volume varies significantly across branches
💡  Salary Credit generates high transaction value despite fewer merchant records
🗺️  Top cities: Kochi, Hyderabad, Kolkata, Jaipur, Kolkata Branch
```

---

## 🚀 Skills Demonstrated

<div align="center">

| Category | Skills |
|----------|--------|
| **Python** | Pandas Data Cleaning, EDA, Feature Engineering, Null Handling, Data Type Conversion |
| **Visualization** | Matplotlib, Seaborn, Statistical Plotting, Chart Selection, EDA Storytelling |
| **Tableau** | Multi-Dimensional Charts, Heatmaps, 100% Stacked Bars, KPI Scorecards, Highlight Tables, Calculated Fields, Table Calculations, Dashboard Layout, Action Filters, Tooltip Customization |
| **Analytics** | Customer Segmentation, Risk Profiling, Fraud Analysis, Portfolio Health Assessment, Branch Benchmarking, SLA Analysis |
| **Business** | Banking Domain Knowledge, Data Storytelling, Insight Communication, Decision Support |

</div>

---

## 📌 Future Improvements

- 🤖 Loan default prediction using Machine Learning (Logistic Regression, Random Forest, XGBoost)
- 📉 Customer churn prediction model
- 🚨 Real-time fraud detection pipeline
- 📈 Customer lifetime value (CLV) prediction
- 🔄 Automated ETL workflows using Apache Airflow
- 🗄️ Data warehouse implementation using PostgreSQL or Snowflake
- 📊 Power BI version of the dashboards for cross-platform comparison

---

## 📸 Dashboard Preview

### 🏦 Customer & Account Dashboard
![Dashboard 1](https://github.com/Deepanshugahlot/Banking-Analytics-Project/blob/main/Tabelau/Dashboard%20Images/Dashboard_01.png)

### 💳 Transaction Dashboard
![Dashboard 2](https://github.com/Deepanshugahlot/Banking-Analytics-Project/blob/main/Tabelau/Dashboard%20Images/Dashboard_02.png)

### 📋 Loans, Complaints & Branch Dashboard
![Dashboard 3](https://github.com/Deepanshugahlot/Banking-Analytics-Project/blob/main/Tabelau/Dashboard%20Images/Dashboard_03.png)

---

## 👨‍💻 Author

<div align="center">

### Deepanshu Gahlot

*Data Analyst | Python • Pandas • Tableau • Matplotlib • Seaborn*

<br>

[![Email](https://img.shields.io/badge/Email-deepanshugahlot001%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:deepanshugahlot001@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Deepanshugahlot-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Deepanshugahlot)
[![Tableau](https://img.shields.io/badge/Tableau-Live%20Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/views/BankingProject_17829830247920/Dashboard1)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deepanshugahlot001)

</div>

---

<div align="center">

### ⭐ If this project helped you or inspired your own work, please consider giving it a Star!

