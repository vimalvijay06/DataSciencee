# 🏦 TrustWave Bank — Customer Intelligence Dashboard

A professional, interactive banking analytics dashboard built with **Streamlit**, **Plotly**, and **Scikit-learn**.

## 📋 Features

| Page | Description |
|------|-------------|
| **📊 Overview** | Executive KPI cards, segment distribution, monthly trends, account types, age bands, risk & digital adoption |
| **👥 Customer Insights** | Filterable demographics, income/credit distributions, occupation breakdown, gender×segment heatmap, customer search |
| **💳 Transaction Analysis** | Type/channel analysis, monthly trends, amount distribution, fraud detection summary |
| **📞 Complaint Analysis** | Complaint types, priority breakdown, resolution performance, channel & status analysis |
| **🧠 Intelligence Layer** | K-Means clustering results, persona cards, radar charts, real-time persona scorer (manual + lookup), CSV export |

## 🚀 Quick Start

```bash
# 1. Navigate to this folder
cd Intelligence_Dashboard

# 2. Install dependencies (if not already installed)
pip install -r requirements.txt

# 3. Launch the dashboard
streamlit run app.py
```

The dashboard will open automatically at **http://localhost:8501**.

## 📁 File Structure

```
Intelligence_Dashboard/
├── app.py                  # Main Streamlit dashboard application
├── train_model.py          # K-Means model training script
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── models/
│   ├── kmeans_model.joblib # Trained K-Means model
│   ├── scaler.joblib       # StandardScaler for feature normalization
│   └── model_metadata.json # Model metrics, centroids, and persona definitions
└── data/                   # Dashboard-specific data extracts
```

## 📊 Data Sources

The dashboard reads cleaned data from `../Data/TrustWave_Cleaned/`:

- `customer_features.csv` — 150,000 customer profiles with 39 engineered features
- `accounts_clean.csv` — 240,000 account records
- `transactions_clean.csv` — 2.5M+ transaction records
- `complaints_clean.csv` — 11,552 complaint records

## 🧠 ML Model

- **Algorithm:** K-Means Clustering (k=4)
- **Features:** monthly_income, credit_score, total_balance, total_txn_count, total_txn_amount, digital_engagement_score
- **Personas Discovered:**
  1. Mass Retail & Emerging Savers (39.7%)
  2. High-Velocity Spenders (20.3%)
  3. Ultra High-Net-Worth Commercial (8.0%)
  4. Digital Middle-Market Savers (32.0%)
