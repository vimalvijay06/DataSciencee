# Pivot Table & Pivot Chart Inventory

## 📌 Overview
This document catalogs the native Microsoft Excel Pivot Tables and interactive Pivot Charts implemented in the `Pivot_Analysis` worksheet of [`TrustWave_Round2_Excel_Analysis.xlsx`](../02_Excel_Workbook/TrustWave_Round2_Excel_Analysis.xlsx). All Pivot Tables are dynamically linked to the underlying cleaned data tables and refresh automatically upon data model updates.

---

## 📊 Pivot Table Inventory

### 1. Pivot Table: `PT_Channel_Summary`
- **Destination:** Worksheet `Pivot_Analysis`, Cell `A4`
- **Source Table / Range:** `Data_Transactions!A1:I25001` (Representative clean transaction base)
- **Rows (Row Field):** `channel` (`ATM`, `Bank Transfer`, `Mobile App`, `Online`, `POS`, `Unknown`)
- **Columns (Column Field):** `transaction_type` (`Bill Payment`, `Deposit`, `Purchase`, `Transfer`, `Withdrawal`)
- **Values (Data Field):** `Count of transaction_id` (Name: `Txn Count`)
- **Aggregation Method:** `Count` (`xlCount`)
- **Related Pivot Chart:** `Pivot Chart 1` — Clustered Column Chart (Cell `I4`)
- **Business Question Answered:** How do customers interact with different transaction types across digital and physical banking channels, and which touchpoints capture the highest transaction velocity?

---

### 2. Pivot Table: `PT_Segment_Risk`
- **Destination:** Worksheet `Pivot_Analysis`, Cell `A24`
- **Source Table / Range:** `Data_Customers!A1:M10001` (Cleaned customer demographic base)
- **Rows (Row Field):** `customer_segment` (`Loyal`, `New`, `Premium`, `Regular`)
- **Columns (Column Field):** `risk_category` (`Low`, `Medium`, `High`)
- **Values (Data Field):** `Count of customer_id` (Name: `Customer Count`)
- **Aggregation Method:** `Count` (`xlCount`)
- **Related Pivot Chart:** `Pivot Chart 2` — Clustered Bar Chart (Cell `I24`)
- **Business Question Answered:** What is the risk distribution across customer segments, and does the high-value Premium tier exhibit lower credit risk compared to Mass Regular customers?

---

### 3. Pivot Table: `PT_Complaint_Priority`
- **Destination:** Worksheet `Pivot_Analysis`, Cell `A44`
- **Source Table / Range:** `Data_Complaints!A1:J11553` (Complete cleaned complaint fact table)
- **Rows (Row Field):** `complaint_type` (`ATM / Card Issue`, `Account Issue`, `Fraud / Unauthorized Transaction`, `Loan / EMI Issue`, `Other`, `Service Quality`, `Transaction Dispute`)
- **Columns (Column Field):** `priority` (`High`, `Medium`, `Low`)
- **Values (Data Field):** `Count of complaint_id` (Name: `Ticket Count`)
- **Aggregation Method:** `Count` (`xlCount`)
- **Related Pivot Chart:** `Pivot Chart 3` — Clustered Column Chart (Cell `I44`)
- **Business Question Answered:** Which complaint categories generate the highest volume of High-Priority operational escalations requiring rapid executive SLA intervention?

---

## 🛠️ Instructions for Interacting & Refreshing in Microsoft Excel
1. Open [`TrustWave_Round2_Excel_Analysis.xlsx`](../02_Excel_Workbook/TrustWave_Round2_Excel_Analysis.xlsx) in Microsoft Excel.
2. Navigate to the `Pivot_Analysis` tab.
3. Click inside any Pivot Table to display the native **PivotTable Fields** task pane.
4. To refresh all Pivot Tables with updated source data:
   - Navigate to the **Data** tab on the Excel Ribbon -> Click **Refresh All** (or keyboard shortcut `Ctrl + Alt + F5`).
5. Filter by channel, segment, or priority using the drop-down filter arrows on each Pivot Table header.
