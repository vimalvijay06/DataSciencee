# -*- coding: utf-8 -*-
"""
TrustWave Bank — Customer Intelligence Dashboard
A high-performance, interactive banking analytics dashboard built with Streamlit & Plotly.
"""
import os
import json
import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# ═══════════════════════════════════════════════════════════════════
# CONFIGURATION & PATHS
# ═══════════════════════════════════════════════════════════════════
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'Data', 'TrustWave_Cleaned')
MODEL_DIR = os.path.join(BASE_DIR, 'models')
CACHE_DIR = os.path.join(BASE_DIR, 'data_cache')

# Color palette — navy / blue / teal accent theme on white
COLORS = {
    'primary': '#0A2463',       # Navy
    'secondary': '#1E5AA8',     # Royal Blue
    'accent': '#3E92CC',        # Sky Blue
    'success': '#2CA58D',       # Teal
    'warning': '#F39C12',       # Amber
    'danger': '#E74C3C',        # Red
    'text': '#2C3E50',          # Dark Slate
    'muted': '#95A5A6',         # Grey
    'bg': '#FFFFFF',            # White
    'card': '#F8F9FA',          # Light Grey
}

PALETTE = ['#0A2463', '#1E5AA8', '#3E92CC', '#2CA58D', '#F39C12', '#E74C3C', '#8E44AD', '#27AE60']
PERSONA_COLORS = {
    'Mass Retail & Emerging Savers': '#3E92CC',
    'High-Velocity Spenders': '#F39C12',
    'Ultra High-Net-Worth (HNW) Commercial': '#0A2463',
    'Digital Middle-Market Savers': '#2CA58D',
}

# ═══════════════════════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="TrustWave Bank — Customer Intelligence Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ═══════════════════════════════════════════════════════════════════
# CUSTOM CSS — Light Professional Theme
# ═══════════════════════════════════════════════════════════════════
st.markdown("""
<style>
    /* Global Light Theme Typography */
    .stApp {
        background-color: #FFFFFF;
        color: #1E293B;
    }
    .stApp p, .stApp span, .stApp label {
        color: #1E293B;
    }

    /* All Widget Labels (Multiselect, Selectbox, Inputs, Sliders) */
    div[data-testid="stWidgetLabel"] label,
    div[data-testid="stWidgetLabel"] p,
    .stSelectbox label,
    .stMultiSelect label,
    .stTextInput label,
    .stNumberInput label,
    .stSlider label,
    .stRadio label {
        color: #0A2463 !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        opacity: 1 !important;
    }

    /* Expander Container & Header */
    div[data-testid="stExpander"] details {
        border-color: #CBD5E1 !important;
        background-color: #F8FAFC !important;
        border-radius: 8px !important;
    }
    div[data-testid="stExpander"] details summary,
    div[data-testid="stExpander"] details summary span,
    div[data-testid="stExpander"] summary p {
        color: #0A2463 !important;
        font-weight: 700 !important;
    }
    div[data-testid="stExpander"] summary svg {
        fill: #0A2463 !important;
    }

    /* Dropdown & Input Controls */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
    }
    div[data-baseweb="select"] * {
        color: #0A2463 !important;
    }
    div[data-baseweb="input"] input {
        color: #0A2463 !important;
        background-color: #FFFFFF !important;
    }
    
    /* Multiselect Selected Tags */
    span[data-baseweb="tag"] {
        background-color: #E2E8F0 !important;
    }
    span[data-baseweb="tag"] * {
        color: #0A2463 !important;
    }

    /* Tabs */
    button[data-baseweb="tab"] p, button[data-baseweb="tab"] div {
        color: #0A2463 !important;
        font-weight: 600 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] p {
        color: #1E5AA8 !important;
        font-weight: 700 !important;
    }

    /* Sidebar Overrides - White Text on Navy Gradient */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0A2463 0%, #1E5AA8 100%) !important;
    }
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div[data-testid="stWidgetLabel"] label {
        color: #FFFFFF !important;
    }
    /* KPI Cards */
    .kpi-card {
        background: #F8F9FA;
        border-radius: 12px;
        padding: 16px 10px 14px 10px;
        text-align: center;
        border-left: 5px solid #1E5AA8;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        transition: transform 0.2s;
        min-height: 96px;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.10);
    }
    .kpi-value {
        font-size: 1.65rem;
        font-weight: 700;
        color: #0A2463;
        margin: 4px 0 2px 0;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .kpi-label {
        font-size: 0.78rem;
        font-weight: 600;
        color: #5D6D7E;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        line-height: 1.25;
        min-height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .kpi-delta {
        font-size: 0.78rem;
        margin-top: 2px;
        white-space: nowrap;
    }
    /* Section headers */
    .section-header {
        color: #0A2463;
        font-size: 1.35rem;
        font-weight: 700;
        margin: 24px 0 10px 0;
        padding-bottom: 6px;
        border-bottom: 3px solid #3E92CC;
    }
    /* Chart description */
    .chart-desc {
        color: #7F8C8D;
        font-size: 0.85rem;
        margin: -4px 0 10px 0;
    }
    /* Persona card */
    .persona-card {
        background: linear-gradient(135deg, #F8F9FA, #EBF5FB);
        border-radius: 10px;
        padding: 18px;
        margin: 8px 0;
        border-left: 4px solid #1E5AA8;
    }
    .persona-name {
        font-weight: 700;
        color: #0A2463;
        font-size: 1.05rem;
    }
    .persona-detail {
        color: #5D6D7E;
        font-size: 0.88rem;
        margin-top: 4px;
    }
    /* Metric tooltip */
    .metric-tip {
        color: #95A5A6;
        font-size: 0.78rem;
        font-style: italic;
        margin-top: 2px;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# HIGH-PERFORMANCE DATA LOADING (Parquet + Memory Caching)
# ═══════════════════════════════════════════════════════════════════
@st.cache_data(show_spinner=False)
def load_customers():
    parquet_path = os.path.join(CACHE_DIR, 'customers.parquet')
    if os.path.exists(parquet_path):
        return pd.read_parquet(parquet_path)
    return pd.read_csv(os.path.join(DATA_DIR, 'customer_features.csv'))

@st.cache_data(show_spinner=False)
def load_accounts():
    parquet_path = os.path.join(CACHE_DIR, 'accounts.parquet')
    if os.path.exists(parquet_path):
        return pd.read_parquet(parquet_path)
    return pd.read_csv(os.path.join(DATA_DIR, 'accounts_clean.csv'))

@st.cache_data(show_spinner=False)
def load_complaints():
    parquet_path = os.path.join(CACHE_DIR, 'complaints.parquet')
    if os.path.exists(parquet_path):
        return pd.read_parquet(parquet_path)
    return pd.read_csv(os.path.join(DATA_DIR, 'complaints_clean.csv'))

@st.cache_data(show_spinner=False)
def load_overview_stats():
    stats_path = os.path.join(CACHE_DIR, 'overview_stats.json')
    if os.path.exists(stats_path):
        with open(stats_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

@st.cache_data(show_spinner=False)
def load_transactions():
    parquet_path = os.path.join(CACHE_DIR, 'transactions_opt.parquet')
    if os.path.exists(parquet_path):
        return pd.read_parquet(parquet_path)
    cols = ['amount', 'transaction_type', 'channel', 'is_fraud', 'year_month']
    return pd.read_csv(os.path.join(DATA_DIR, 'transactions_clean.csv'), usecols=cols)

@st.cache_resource(show_spinner=False)
def load_model():
    model_path = os.path.join(MODEL_DIR, 'kmeans_model.joblib')
    scaler_path = os.path.join(MODEL_DIR, 'scaler.joblib')
    meta_path = os.path.join(MODEL_DIR, 'model_metadata.json')
    if not os.path.exists(model_path):
        return None, None, None
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    with open(meta_path, 'r', encoding='utf-8') as f:
        meta = json.load(f)
    return model, scaler, meta

@st.cache_data(show_spinner=False)
def get_clustered_csv_bytes():
    cache_csv = os.path.join(CACHE_DIR, 'trustwave_customer_clusters.csv')
    if os.path.exists(cache_csv):
        with open(cache_csv, 'rb') as f:
            return f.read()
    return b""


# ═══════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════
def format_number(n, prefix=""):
    """Pretty-print large numbers with K/M/B suffixes."""
    if n >= 1_000_000_000:
        return f"{prefix}{n/1_000_000_000:.1f}B"
    elif n >= 1_000_000:
        return f"{prefix}{n/1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{prefix}{n/1_000:.1f}K"
    return f"{prefix}{n:,.0f}"

def render_kpi(label, value, delta=None, border_color="#1E5AA8"):
    delta_html = ""
    if delta:
        color = "#2CA58D" if "+" in str(delta) or float(str(delta).replace('%','').replace('+','')) > 0 else "#E74C3C"
        delta_html = f'<div class="kpi-delta" style="color:{color}">{delta}</div>'
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color:{border_color}">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def plotly_defaults(fig, title="", height=400):
    """Apply consistent theme to Plotly charts."""
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['primary']), x=0.01),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(248,249,250,0.5)',
        font=dict(family="Inter, Segoe UI, sans-serif", size=12, color=COLORS['text']),
        height=height,
        margin=dict(l=40, r=30, t=45, b=35),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode="x unified",
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='rgba(0,0,0,0.06)')
    return fig


# ═══════════════════════════════════════════════════════════════════
# SIDEBAR NAVIGATION
# ═══════════════════════════════════════════════════════════════════
st.sidebar.markdown("""
<div style="text-align:center; padding: 20px 0 10px 0;">
    <div style="font-size:2.4rem;">🏦</div>
    <div style="font-size:1.2rem; font-weight:700; letter-spacing:0.5px; margin-top:4px;">TrustWave Bank</div>
    <div style="font-size:0.75rem; opacity:0.8; letter-spacing:1px;">Customer Intelligence Dashboard</div>
</div>
<hr style="border-color: rgba(255,255,255,0.2); margin: 0 0 15px 0;">
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigate to",
    ["📊 Overview", "👥 Customer Insights", "💳 Transaction Analysis",
     "📞 Complaint Analysis", "🧠 Smart Customer Groups"],
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="font-size:0.7rem; opacity:0.6; text-align:center; padding-top:10px;">
    TrustWave Bank | Customer Analytics
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# PAGE 1 — OVERVIEW
# ═══════════════════════════════════════════════════════════════════
if page == "📊 Overview":
    st.markdown('<h1 style="color:#0A2463; margin-bottom:0;">📊 Banking Overview</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#7F8C8D; margin-top:0;">Get a quick view of customers, accounts, transactions, and banking activity.</p>', unsafe_allow_html=True)
    st.markdown("---")

    # Load high-speed precomputed data
    df_cust = load_customers()
    df_acct = load_accounts()
    df_comp = load_complaints()
    ov_stats = load_overview_stats()

    if ov_stats:
        total_txns = ov_stats['total_transactions']
        total_txn_val = ov_stats['total_transaction_value']
    else:
        df_txn = load_transactions()
        total_txns = len(df_txn)
        total_txn_val = float(df_txn['amount'].sum())

    # ── KPI Row ──
    k1, k2, k3, k4, k5 = st.columns(5)
    with k1:
        render_kpi("Total Customers", format_number(len(df_cust)), border_color="#0A2463")
    with k2:
        render_kpi("Total Accounts", format_number(len(df_acct)), border_color="#1E5AA8")
    with k3:
        render_kpi("Total Transactions", format_number(total_txns), border_color="#3E92CC")
    with k4:
        render_kpi("Total Transaction Value", format_number(total_txn_val, prefix="₹"), border_color="#2CA58D")
    with k5:
        render_kpi("Total Complaints", format_number(len(df_comp)), border_color="#F39C12")

    st.markdown("")

    # ── Row 2: Charts ──
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">Customer Groups</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-desc">How customers are divided across different banking segments.</div>', unsafe_allow_html=True)
        seg_counts = df_cust['customer_segment'].value_counts().reset_index()
        seg_counts.columns = ['Segment', 'Count']
        if len(seg_counts) > 0:
            fig = px.pie(seg_counts, values='Count', names='Segment', hole=0.45,
                         color_discrete_sequence=PALETTE)
            fig = plotly_defaults(fig, height=360)
            fig.update_traces(textposition='inside', textinfo='percent+label',
                              textfont_size=11, pull=[0.03]*len(seg_counts))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data is available for this chart.")

    with col2:
        st.markdown('<div class="section-header">Monthly Transaction Activity</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-desc">Number of transactions and their total value each month.</div>', unsafe_allow_html=True)
        if ov_stats and 'monthly' in ov_stats:
            monthly = pd.DataFrame(ov_stats['monthly'])
        else:
            df_txn = load_transactions()
            monthly = df_txn.groupby('year_month', observed=True).agg(
                txn_count=('amount', 'count'),
                txn_value=('amount', 'sum')
            ).reset_index().sort_values('year_month')
        if len(monthly) > 0:
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(go.Bar(x=monthly['year_month'], y=monthly['txn_count'],
                                 name='Transaction Count', marker_color=COLORS['accent'], opacity=0.7), secondary_y=False)
            fig.add_trace(go.Scatter(x=monthly['year_month'], y=monthly['txn_value'],
                                     name='Total Value (₹)', line=dict(color=COLORS['primary'], width=2.5),
                                     mode='lines+markers', marker=dict(size=5)), secondary_y=True)
            fig.update_yaxes(title_text="Transaction Count", secondary_y=False)
            fig.update_yaxes(title_text="Total Value (₹)", secondary_y=True)
            fig = plotly_defaults(fig, height=360)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data is available for this chart.")

    # ── Row 3: More Charts ──
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="section-header">Accounts by Type</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-desc">Number of accounts for each account type — Savings, Current, Credit, etc.</div>', unsafe_allow_html=True)
        acct_type = df_acct['account_type'].value_counts().reset_index()
        acct_type.columns = ['Type', 'Count']
        if len(acct_type) > 0:
            fig = px.bar(acct_type, x='Type', y='Count', color='Type',
                         color_discrete_sequence=PALETTE, text='Count')
            fig = plotly_defaults(fig, height=340)
            fig.update_traces(textposition='outside', textfont_size=11)
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data is available for this chart.")

    with col4:
        st.markdown('<div class="section-header">Customers by Age Group</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-desc">Number of customers in each age group.</div>', unsafe_allow_html=True)
        age_order = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
        age_counts = df_cust['age_band'].value_counts().reindex(
            [a for a in age_order if a in df_cust['age_band'].unique()]).reset_index()
        age_counts.columns = ['Age Group', 'Count']
        if len(age_counts) > 0:
            fig = px.bar(age_counts, x='Age Group', y='Count', color='Count',
                         color_continuous_scale='Blues', text='Count')
            fig = plotly_defaults(fig, height=340)
            fig.update_traces(textposition='outside', textfont_size=11)
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data is available for this chart.")

    # ── Row 4: Risk & Digital ──
    col5, col6 = st.columns(2)

    with col5:
        st.markdown('<div class="section-header">Customer Risk Overview</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-desc">Customers grouped by their risk category — Low, Medium, or High.</div>', unsafe_allow_html=True)
        risk = df_cust['risk_category'].value_counts().reset_index()
        risk.columns = ['Risk', 'Count']
        risk_colors = {'Low Risk': '#2CA58D', 'Medium Risk': '#F39C12', 'High Risk': '#E74C3C'}
        if len(risk) > 0:
            fig = px.bar(risk, x='Risk', y='Count', color='Risk',
                         color_discrete_map=risk_colors, text='Count')
            fig = plotly_defaults(fig, height=330)
            fig.update_traces(textposition='outside')
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data is available for this chart.")

    with col6:
        st.markdown('<div class="section-header">Digital Banking Usage</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-desc">Percentage of customers using digital banking, UPI payments, and the mobile app.</div>', unsafe_allow_html=True)
        digital_cols = ['is_digital_banking_user', 'is_upi_user', 'is_mobile_app_user']
        digital_data = []
        for c in digital_cols:
            label = c.replace('is_', '').replace('_user', '').replace('_', ' ').title()
            rate = float(df_cust[c].mean()) * 100
            digital_data.append({'Channel': label, 'Adoption %': round(rate, 1)})
        digi_df = pd.DataFrame(digital_data)
        fig = px.bar(digi_df, x='Channel', y='Adoption %', color='Channel',
                     color_discrete_sequence=[COLORS['primary'], COLORS['accent'], COLORS['success']],
                     text='Adoption %')
        fig = plotly_defaults(fig, height=330)
        fig.update_traces(textposition='outside', texttemplate='%{text:.1f}%')
        fig.update_layout(showlegend=False, yaxis_range=[0, 100])
        st.plotly_chart(fig, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════
# PAGE 2 — CUSTOMER INSIGHTS
# ═══════════════════════════════════════════════════════════════════
elif page == "👥 Customer Insights":
    st.markdown('<h1 style="color:#0A2463;">👥 Know Your Customers</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#7F8C8D;">Explore customer profiles, income, credit scores, and digital banking activity.</p>', unsafe_allow_html=True)
    st.markdown("---")

    df_cust = load_customers()

    # Filters
    with st.expander("🔍 Filter Customers", expanded=True):
        fc1, fc2, fc3 = st.columns(3)
        with fc1:
            seg_filter = st.multiselect("Choose Customer Group", df_cust['customer_segment'].unique().tolist(),
                                         default=df_cust['customer_segment'].unique().tolist())
        with fc2:
            risk_filter = st.multiselect("Choose Risk Category", df_cust['risk_category'].unique().tolist(),
                                          default=df_cust['risk_category'].unique().tolist())
        with fc3:
            gender_filter = st.multiselect("Choose Gender", df_cust['gender'].unique().tolist(),
                                            default=df_cust['gender'].unique().tolist())

    mask = (df_cust['customer_segment'].isin(seg_filter) &
            df_cust['risk_category'].isin(risk_filter) &
            df_cust['gender'].isin(gender_filter))
    df_f = df_cust[mask]

    if len(df_f) == 0:
        st.warning("No records match your selected filters. Try changing them.")
    else:
        # KPIs
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            render_kpi("Customers Matching Filters", format_number(len(df_f)), border_color="#0A2463")
        with k2:
            render_kpi("Average Monthly Income", format_number(df_f['monthly_income'].mean(), prefix="₹"), border_color="#1E5AA8")
        with k3:
            render_kpi("Average Credit Score", f"{df_f['credit_score'].mean():.0f}", border_color="#3E92CC")
        with k4:
            render_kpi("Average Digital Engagement Score", f"{df_f['digital_engagement_score'].mean():.2f}", border_color="#2CA58D")

        st.markdown("")

        # Charts row 1
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="section-header">Income by Customer Group</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">Spread of monthly income across different customer groups.</div>', unsafe_allow_html=True)
            # Sample up to 5,000 rows to ensure zero lag in the browser
            box_sample = df_f.sample(min(len(df_f), 5000), random_state=42) if len(df_f) > 5000 else df_f
            fig = px.box(box_sample, x='customer_segment', y='monthly_income', color='customer_segment',
                         color_discrete_sequence=PALETTE)
            fig = plotly_defaults(fig, height=380)
            fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Monthly Income (₹)")
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.markdown('<div class="section-header">Credit Score Distribution</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">How credit scores are spread across all matching customers.</div>', unsafe_allow_html=True)
            valid_scores = df_f['credit_score'].dropna().values
            if len(valid_scores) > 0:
                counts, bin_edges = np.histogram(valid_scores, bins=40)
                bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
                fig = px.bar(x=bin_centers, y=counts, labels={'x': 'Credit Score', 'y': 'Number of Customers'},
                             color_discrete_sequence=[COLORS['accent']])
                fig = plotly_defaults(fig, height=380)
                fig.update_layout(xaxis_title="Credit Score", yaxis_title="Number of Customers")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No credit score data available.")

        # Charts row 2
        c3, c4 = st.columns(2)
        with c3:
            st.markdown('<div class="section-header">Customers by Occupation</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">Top 10 occupations among the selected customers.</div>', unsafe_allow_html=True)
            occ = df_f['occupation'].value_counts().head(10).reset_index()
            occ.columns = ['Occupation', 'Count']
            fig = px.bar(occ, x='Count', y='Occupation', orientation='h', color='Count',
                         color_continuous_scale='Blues', text='Count')
            fig = plotly_defaults(fig, height=380)
            fig.update_traces(textposition='outside')
            fig.update_coloraxes(showscale=False)
            fig.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig, use_container_width=True)

        with c4:
            st.markdown('<div class="section-header">Customer Groups by Gender</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">A heatmap showing how many customers fall into each group by gender.</div>', unsafe_allow_html=True)
            pivot = df_f.groupby(['gender', 'customer_segment']).size().reset_index(name='count')
            pivot_wide = pivot.pivot(index='gender', columns='customer_segment', values='count').fillna(0)
            fig = px.imshow(pivot_wide, text_auto=True, aspect="auto",
                            color_continuous_scale='Blues')
            fig = plotly_defaults(fig, height=380)
            fig.update_layout(xaxis_title="", yaxis_title="")
            st.plotly_chart(fig, use_container_width=True)

    # Searchable Customer Table (Vectorized fast filtering)
    st.markdown('<div class="section-header">🔎 Find a Customer</div>', unsafe_allow_html=True)
    search = st.text_input("Enter Customer ID, city, or state", "", placeholder="e.g. CUST_00001, Mumbai, Maharashtra")
    display_cols = ['customer_id', 'age', 'gender', 'occupation', 'monthly_income', 'credit_score',
                    'customer_segment', 'risk_category', 'city', 'state', 'digital_engagement_score']
    df_display = df_f[display_cols] if len(df_f) > 0 else df_cust[display_cols]
    if search.strip():
        s = search.strip()
        m1 = df_display['customer_id'].astype(str).str.contains(s, case=False, na=False)
        m2 = df_display['city'].astype(str).str.contains(s, case=False, na=False)
        m3 = df_display['state'].astype(str).str.contains(s, case=False, na=False)
        df_display = df_display[m1 | m2 | m3]
    if len(df_display) > 0:
        st.markdown(f"**Matching Customers** — showing {min(len(df_display), 200)} of {len(df_display):,} records")
        st.dataframe(df_display.head(200), use_container_width=True, height=380)
    else:
        st.info("No customers match your search. Try a different Customer ID, city, or state.")


# ═══════════════════════════════════════════════════════════════════
# PAGE 3 — TRANSACTION ANALYSIS
# ═══════════════════════════════════════════════════════════════════
elif page == "💳 Transaction Analysis":
    st.markdown('<h1 style="color:#0A2463;">💳 Explore Transactions</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#7F8C8D;">Understand how customers use banking channels and how transaction activity changes over time.</p>', unsafe_allow_html=True)
    st.markdown("---")

    df_txn = load_transactions()

    # Filters
    with st.expander("🔍 Filter Transactions", expanded=True):
        fc1, fc2, fc3 = st.columns(3)
        with fc1:
            txn_types = st.multiselect("Choose Transaction Type", df_txn['transaction_type'].cat.categories.tolist(),
                                        default=df_txn['transaction_type'].cat.categories.tolist())
        with fc2:
            channels = st.multiselect("Choose Banking Channel", df_txn['channel'].cat.categories.tolist(),
                                       default=df_txn['channel'].cat.categories.tolist())
        with fc3:
            fraud_opt = st.selectbox("Fraud Status", ["All Transactions", "Flagged as Fraud", "Not Flagged as Fraud"])

    mask = df_txn['transaction_type'].isin(txn_types) & df_txn['channel'].isin(channels)
    if fraud_opt == "Flagged as Fraud":
        mask = mask & (df_txn['is_fraud'] == 1)
    elif fraud_opt == "Not Flagged as Fraud":
        mask = mask & (df_txn['is_fraud'] == 0)
    df_f = df_txn[mask]

    if len(df_f) == 0:
        st.warning("No records match your selected filters. Try changing them.")
    else:
        # KPIs
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            render_kpi("Matching Transactions", format_number(len(df_f)), border_color="#0A2463")
        with k2:
            render_kpi("Total Transaction Value", format_number(float(df_f['amount'].sum()), prefix="₹"), border_color="#1E5AA8")
        with k3:
            render_kpi("Average Transaction Amount", format_number(float(df_f['amount'].mean()), prefix="₹"), border_color="#3E92CC")
        with k4:
            fraud_rate = (int(df_f['is_fraud'].sum()) / max(len(df_f), 1)) * 100
            render_kpi("Flagged Transaction Rate", f"{fraud_rate:.2f}%", border_color="#E74C3C")

        st.markdown("")

        # Charts row 1
        c1, c2 = st.columns(2)

        with c1:
            st.markdown('<div class="section-header">Transactions by Type</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">Share of each transaction type — purchases, transfers, withdrawals, etc.</div>', unsafe_allow_html=True)
            type_dist = df_f['transaction_type'].value_counts().reset_index()
            type_dist.columns = ['Type', 'Count']
            fig = px.pie(type_dist, values='Count', names='Type', hole=0.4,
                         color_discrete_sequence=PALETTE)
            fig = plotly_defaults(fig, height=360)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.markdown('<div class="section-header">Transaction Value by Channel</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">Total money moved through each banking channel.</div>', unsafe_allow_html=True)
            ch_val = df_f.groupby('channel', observed=True)['amount'].sum().reset_index()
            ch_val.columns = ['Channel', 'Total Value']
            fig = px.bar(ch_val.sort_values('Total Value', ascending=True),
                         x='Total Value', y='Channel', orientation='h', color='Total Value',
                         color_continuous_scale='Blues', text='Total Value')
            fig = plotly_defaults(fig, height=360)
            fig.update_traces(textposition='outside', texttemplate='₹%{text:.2s}')
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(fig, use_container_width=True)

        # Charts row 2
        c3, c4 = st.columns(2)

        with c3:
            st.markdown('<div class="section-header">Monthly Transaction Trends</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">How transaction value changes month-by-month for each type.</div>', unsafe_allow_html=True)
            monthly_type = df_f.groupby(['year_month', 'transaction_type'], observed=True)['amount'].sum().reset_index()
            fig = px.line(monthly_type, x='year_month', y='amount', color='transaction_type',
                          color_discrete_sequence=PALETTE, markers=True)
            fig = plotly_defaults(fig, height=360)
            fig.update_layout(xaxis_title="Month", yaxis_title="Value (₹)")
            st.plotly_chart(fig, use_container_width=True)

        with c4:
            st.markdown('<div class="section-header">Transaction Amount Distribution</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">How transaction amounts are spread. Very large outliers are excluded for clarity.</div>', unsafe_allow_html=True)
            # High-performance server-side binning: passes 50 points to Plotly instead of 2.5 million!
            cap = float(df_f['amount'].quantile(0.99))
            sub_amt = df_f['amount'][df_f['amount'] <= cap].values
            if len(sub_amt) > 0:
                counts, bin_edges = np.histogram(sub_amt, bins=50)
                bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
                fig = px.bar(x=bin_centers, y=counts, labels={'x': 'Amount (₹)', 'y': 'Number of Transactions'},
                             color_discrete_sequence=[COLORS['accent']])
                fig = plotly_defaults(fig, height=360)
                fig.update_layout(xaxis_title="Amount (₹)", yaxis_title="Number of Transactions")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No transaction data available.")

    # Fraud Analysis
    st.markdown('<div class="section-header">🔒 Transaction Security Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-desc">Transactions flagged by the system for potential fraud. These are flags, not confirmed fraud cases.</div>', unsafe_allow_html=True)
    fc1, fc2, fc3 = st.columns(3)
    fraud_mask = (df_txn['is_fraud'] == 1)
    fraud_count = int(fraud_mask.sum())
    fraud_df = df_txn[fraud_mask]
    with fc1:
        render_kpi("Flagged Transactions", format_number(fraud_count), border_color="#E74C3C")
    with fc2:
        fraud_value = float(fraud_df['amount'].sum()) if fraud_count > 0 else 0.0
        render_kpi("Value of Flagged Transactions", format_number(fraud_value, prefix="₹"), border_color="#E74C3C")
    with fc3:
        avg_fraud = float(fraud_df['amount'].mean()) if fraud_count > 0 else 0.0
        render_kpi("Average Flagged Transaction Amount", format_number(avg_fraud, prefix="₹"), border_color="#E74C3C")

    # Fraud by channel
    if fraud_count > 0:
        st.markdown('<div class="section-header">Flagged Transactions by Channel</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-desc">Which banking channels have the most fraud-flagged transactions.</div>', unsafe_allow_html=True)
        fraud_by_ch = fraud_df.groupby('channel', observed=True).size().reset_index(name='Flagged Count')
        fig = px.bar(fraud_by_ch.sort_values('Flagged Count', ascending=False),
                     x='channel', y='Flagged Count', color='Flagged Count',
                     color_continuous_scale='Reds', text='Flagged Count')
        fig = plotly_defaults(fig, height=330)
        fig.update_traces(textposition='outside')
        fig.update_coloraxes(showscale=False)
        st.plotly_chart(fig, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════
# PAGE 4 — COMPLAINT ANALYSIS
# ═══════════════════════════════════════════════════════════════════
elif page == "📞 Complaint Analysis":
    st.markdown('<h1 style="color:#0A2463;">📞 Customer Service and Complaints</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#7F8C8D;">Understand customer complaints, response times, and service performance.</p>', unsafe_allow_html=True)
    st.markdown("---")

    df_comp = load_complaints()

    if len(df_comp) == 0:
        st.info("No complaint data is available.")
    else:
        # KPIs
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            render_kpi("Total Complaints", format_number(len(df_comp)), border_color="#F39C12")
        with k2:
            avg_res = float(df_comp['resolution_days'].mean())
            render_kpi("Average Resolution Time", f"{avg_res:.1f} days", border_color="#1E5AA8")
        with k3:
            resolved = int((df_comp['status'].str.lower() == 'resolved').sum())
            res_rate = resolved / max(len(df_comp), 1) * 100
            render_kpi("Complaints Resolved", f"{res_rate:.1f}%", border_color="#2CA58D")
        with k4:
            high_p = int((df_comp['priority'].str.lower() == 'high').sum())
            render_kpi("High-Priority Complaints", format_number(high_p), border_color="#E74C3C")

        st.markdown("")
        st.markdown(
            f'<div class="chart-desc">On average, complaints take <strong>{avg_res:.1f} days</strong> to resolve. '
            f'<strong>{res_rate:.1f}%</strong> of all complaints have been resolved so far.</div>',
            unsafe_allow_html=True
        )

        # Charts
        c1, c2 = st.columns(2)

        with c1:
            st.markdown('<div class="section-header">Complaints by Type</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">What types of complaints customers raise most often.</div>', unsafe_allow_html=True)
            comp_type = df_comp['complaint_type'].value_counts().reset_index()
            comp_type.columns = ['Type', 'Count']
            fig = px.pie(comp_type, values='Count', names='Type', hole=0.4,
                         color_discrete_sequence=PALETTE)
            fig = plotly_defaults(fig, height=360)
            fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=10)
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.markdown('<div class="section-header">Complaints by Priority</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">Number of complaints at each priority level.</div>', unsafe_allow_html=True)
            pri = df_comp['priority'].value_counts().reset_index()
            pri.columns = ['Priority', 'Count']
            pri_colors = {'High': '#E74C3C', 'Medium': '#F39C12', 'Low': '#2CA58D'}
            fig = px.bar(pri, x='Priority', y='Count', color='Priority',
                         color_discrete_map=pri_colors, text='Count')
            fig = plotly_defaults(fig, height=360)
            fig.update_traces(textposition='outside')
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

        c3, c4 = st.columns(2)

        with c3:
            st.markdown('<div class="section-header">Resolution Time by Complaint Type</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">How long each type of complaint takes to resolve.</div>', unsafe_allow_html=True)
            fig = px.box(df_comp, x='complaint_type', y='resolution_days', color='complaint_type',
                         color_discrete_sequence=PALETTE)
            fig = plotly_defaults(fig, height=360)
            fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Days to Resolve")
            st.plotly_chart(fig, use_container_width=True)

        with c4:
            st.markdown('<div class="section-header">Complaints by Contact Channel</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">Which channels customers use to submit complaints — phone, email, branch, etc.</div>', unsafe_allow_html=True)
            ch_comp = df_comp['channel'].value_counts().reset_index()
            ch_comp.columns = ['Channel', 'Count']
            fig = px.bar(ch_comp, x='Channel', y='Count', color='Channel',
                         color_discrete_sequence=PALETTE, text='Count')
            fig = plotly_defaults(fig, height=360)
            fig.update_traces(textposition='outside')
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

        # Status breakdown
        st.markdown('<div class="section-header">Complaint Status</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-desc">Current status of all complaints — resolved, pending, escalated, or open.</div>', unsafe_allow_html=True)
        status_data = df_comp['status'].value_counts().reset_index()
        status_data.columns = ['Status', 'Count']
        status_colors = {'Resolved': '#2CA58D', 'Pending': '#F39C12', 'Escalated': '#E74C3C', 'Open': '#3E92CC'}
        fig = px.bar(status_data, x='Status', y='Count', color='Status',
                     color_discrete_map=status_colors, text='Count')
        fig = plotly_defaults(fig, height=320)
        fig.update_traces(textposition='outside')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════
# PAGE 5 — SMART CUSTOMER GROUPS (Intelligence Layer)
# ═══════════════════════════════════════════════════════════════════
elif page == "🧠 Smart Customer Groups":
    st.markdown('<h1 style="color:#0A2463;">🧠 Smart Customer Groups</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#7F8C8D;">Our machine-learning model groups customers with similar financial and banking activity. '
        'Explore these groups to better understand customer needs.</p>',
        unsafe_allow_html=True
    )
    st.markdown("---")

    model, scaler, meta = load_model()

    if model is None:
        st.error("The model is not available yet. Please train the model first by running `train_model.py`.")
    else:
        df_cust = load_customers()

        # Model metrics
        st.markdown('<div class="section-header">About the Model</div>', unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            render_kpi("Model Used", "K-Means", border_color="#0A2463")
            st.markdown('<div class="metric-tip">K-Means is an algorithm that groups similar customers together.</div>', unsafe_allow_html=True)
        with m2:
            render_kpi("Number of Customer Groups", str(meta['k_clusters']), border_color="#1E5AA8")
            st.markdown('<div class="metric-tip">The model divides all customers into this many groups.</div>', unsafe_allow_html=True)
        with m3:
            render_kpi("Group Separation Score", f"{meta['silhouette_score']:.4f}", border_color="#3E92CC")
            st.markdown('<div class="metric-tip">Ranges from −1 to 1. Higher means groups are more distinct. Values above 0.2 are reasonable.</div>', unsafe_allow_html=True)
        with m4:
            render_kpi("Cluster Comparison Score", f"{meta['davies_bouldin_index']:.4f}", border_color="#2CA58D")
            st.markdown('<div class="metric-tip">Lower is better. Measures how compact and separate the groups are.</div>', unsafe_allow_html=True)

        st.markdown("")

        # Persona Overview
        st.markdown('<div class="section-header">Meet the Customer Groups</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-desc">Each group represents customers with similar banking behaviour and financial profiles.</div>', unsafe_allow_html=True)
        centroids = meta['centroids']
        personas = meta['personas']

        pcols = st.columns(4)
        for i, c in enumerate(centroids):
            persona = personas[str(c['Cluster_ID'])]
            with pcols[i]:
                pcolor = list(PERSONA_COLORS.values())[i % len(PERSONA_COLORS)]
                st.markdown(f"""
                <div class="persona-card" style="border-left-color:{pcolor}">
                    <div class="persona-name">{persona['name']}</div>
                    <div class="persona-detail">
                        👥 {c['Customer_Count']:,} customers ({c['Population_Share']:.1f}% of total)<br>
                        💰 Avg Income: ₹{c['monthly_income']:,.0f}<br>
                        📊 Avg Credit Score: {c['credit_score']:.0f}<br>
                        📱 Common Channel: {persona['primary_channel']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("")

        # Cluster Comparison Charts
        c1, c2 = st.columns(2)

        with c1:
            st.markdown('<div class="section-header">Customers in Each Group</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">How many customers belong to each group.</div>', unsafe_allow_html=True)
            cluster_df = pd.DataFrame(centroids)
            fig = px.bar(cluster_df, x='Persona_Name', y='Customer_Count', color='Persona_Name',
                         color_discrete_map=PERSONA_COLORS, text='Customer_Count')
            fig = plotly_defaults(fig, height=380)
            fig.update_traces(textposition='outside', texttemplate='%{text:,.0f}')
            fig.update_layout(showlegend=False, xaxis_title="")
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.markdown('<div class="section-header">Compare Customer Groups</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-desc">A radar chart comparing the average profile of each group across key metrics.</div>', unsafe_allow_html=True)
            features = meta['features']
            feature_labels = {
                'monthly_income': 'Income',
                'credit_score': 'Credit Score',
                'total_balance': 'Balance',
                'total_txn_count': 'Txn Count',
                'total_txn_amount': 'Txn Amount',
                'digital_engagement_score': 'Digital Score'
            }
            display_features = [feature_labels.get(f, f) for f in features]

            fig = go.Figure()
            for i, c in enumerate(centroids):
                vals = [c[f] for f in features]
                max_vals = [max(abs(cent[f]) for cent in centroids) for f in features]
                norm_vals = [v / m if m > 0 else 0 for v, m in zip(vals, max_vals)]
                norm_vals.append(norm_vals[0])
                pname = personas[str(c['Cluster_ID'])]['name']
                pcolor = list(PERSONA_COLORS.values())[i % len(PERSONA_COLORS)]
                fig.add_trace(go.Scatterpolar(
                    r=norm_vals,
                    theta=display_features + [display_features[0]],
                    fill='toself',
                    name=pname,
                    line=dict(color=pcolor),
                    opacity=0.6
                ))
            fig = plotly_defaults(fig, height=380)
            fig.update_layout(polar=dict(
                radialaxis=dict(visible=True, range=[0, 1.1]),
                bgcolor='rgba(248,249,250,0.5)'
            ))
            st.plotly_chart(fig, use_container_width=True)

        # ── Real-Time Persona Scorer ──
        st.markdown('<div class="section-header">🎯 Explore a Customer Profile</div>', unsafe_allow_html=True)
        st.markdown("Enter customer details or look up an existing customer to see which customer group the model assigns.")

        scorer_tab1, scorer_tab2 = st.tabs(["✏️ Enter Details Manually", "🔍 Look Up an Existing Customer"])

        with scorer_tab1:
            sc1, sc2, sc3 = st.columns(3)
            with sc1:
                inp_income = st.number_input("Monthly Income (₹)", min_value=0, max_value=1_000_000, value=50000, step=5000)
                inp_credit = st.number_input("Credit Score", min_value=300, max_value=850, value=650, step=10,
                                             help="Credit bureau score between 300 and 850.")
            with sc2:
                inp_balance = st.number_input("Account Balance (₹)", min_value=0, max_value=5_000_000, value=100000, step=10000)
                inp_txn_count = st.number_input("Number of Transactions", min_value=0, max_value=200, value=15, step=1)
            with sc3:
                inp_txn_amt = st.number_input("Total Transaction Amount (₹)", min_value=0, max_value=20_000_000, value=500000, step=50000)
                inp_digital = st.slider("Digital Engagement Score", min_value=0.0, max_value=4.0, value=2.5, step=0.1,
                                        help="A score from 0 to 4 measuring how actively a customer uses digital banking.")

            if st.button("🔮 Find Customer Group", type="primary", use_container_width=True):
                input_arr = np.array([[inp_income, inp_credit, inp_balance, inp_txn_count, inp_txn_amt, inp_digital]])
                scaled = scaler.transform(input_arr)
                cluster_id = int(model.predict(scaled)[0])
                persona = personas[str(cluster_id)]

                pcolor = list(PERSONA_COLORS.values())[cluster_id % len(PERSONA_COLORS)]
                st.markdown(f"""
                <div class="persona-card" style="border-left-color:{pcolor}; margin-top:12px;">
                    <div class="persona-name">🏷️ Assigned Customer Group: {persona['name']}</div>
                    <div class="persona-detail" style="margin-top:8px;">
                        <strong>What This Group Means:</strong> {persona['description']}<br><br>
                        <strong>Typical Group Characteristics:</strong><br>
                        Risk Level: {persona['risk_tier']} &nbsp;|&nbsp;
                        Common Channel: {persona['primary_channel']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Comparison radar
                st.markdown("**How this profile compares to the group average:**")
                centroid = centroids[cluster_id]
                input_vals = [inp_income, inp_credit, inp_balance, inp_txn_count, inp_txn_amt, inp_digital]
                centroid_vals = [centroid[f] for f in features]
                max_vals = [max(abs(iv), abs(cv), 1) for iv, cv in zip(input_vals, centroid_vals)]
                norm_input = [v / m for v, m in zip(input_vals, max_vals)] + [input_vals[0] / max_vals[0]]
                norm_centroid = [v / m for v, m in zip(centroid_vals, max_vals)] + [centroid_vals[0] / max_vals[0]]

                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(r=norm_input, theta=display_features + [display_features[0]],
                                              fill='toself', name='Your Input', line=dict(color='#E74C3C')))
                fig.add_trace(go.Scatterpolar(r=norm_centroid, theta=display_features + [display_features[0]],
                                              fill='toself', name='Group Average', line=dict(color=pcolor), opacity=0.5))
                fig = plotly_defaults(fig, height=360)
                fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1.2]),
                                             bgcolor='rgba(248,249,250,0.5)'))
                st.plotly_chart(fig, use_container_width=True)

        with scorer_tab2:
            st.markdown("**Look Up an Existing Customer**")
            cust_id = st.text_input("Enter Customer ID", "", placeholder="e.g. CUST_00001")
            if cust_id and st.button("🔍 View Customer Profile", type="primary", use_container_width=True):
                match = df_cust[df_cust['customer_id'] == cust_id.strip()]
                if len(match) == 0:
                    st.warning(f"Customer ID '{cust_id}' was not found. Please enter a valid Customer ID.")
                else:
                    row = match.iloc[0]
                    input_arr = np.array([[row['monthly_income'], row['credit_score'], row['total_balance'],
                                           row['total_txn_count'], row['total_txn_amount'], row['digital_engagement_score']]])
                    scaled = scaler.transform(input_arr)
                    cluster_id = int(model.predict(scaled)[0])
                    persona = personas[str(cluster_id)]
                    pcolor = list(PERSONA_COLORS.values())[cluster_id % len(PERSONA_COLORS)]

                    st.success("Customer details loaded successfully.")
                    st.markdown(f"""
                    <div class="persona-card" style="border-left-color:{pcolor}; margin-top:12px;">
                        <div class="persona-name">🏷️ {cust_id.strip()} → {persona['name']}</div>
                        <div class="persona-detail" style="margin-top:8px;">
                            Age: {row.get('age', 'N/A')} | Gender: {row.get('gender', 'N/A')} |
                            Occupation: {row.get('occupation', 'N/A')}<br>
                            Income: ₹{row['monthly_income']:,.0f} | Credit Score: {row['credit_score']:.0f} |
                            Balance: ₹{row['total_balance']:,.0f}<br>
                            Transactions: {row['total_txn_count']:.0f} | Total Spent: ₹{row['total_txn_amount']:,.0f} |
                            Digital Score: {row['digital_engagement_score']:.2f}<br><br>
                            <strong>What This Group Means:</strong> {persona['description']}<br>
                            <strong>Risk Level:</strong> {persona['risk_tier']} &nbsp;|&nbsp;
                            <strong>Common Channel:</strong> {persona['primary_channel']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        # Download section (Instantaneous downloads from pre-computed cache)
        st.markdown("---")
        st.markdown('<div class="section-header">📥 Download Your Analysis</div>', unsafe_allow_html=True)

        ec1, ec2 = st.columns(2)
        with ec1:
            st.markdown("**Download Customer Analysis (CSV)**")
            st.markdown('<div class="chart-desc">A CSV file with all customers and their assigned group. You can open this in Excel.</div>', unsafe_allow_html=True)
            csv_data = get_clustered_csv_bytes()
            if not csv_data:
                feat_cols = meta['features']
                df_ml = df_cust[['customer_id'] + feat_cols].dropna()
                X_scaled = scaler.transform(df_ml[feat_cols].values)
                df_ml['Cluster_ID'] = model.predict(X_scaled)
                df_ml['Persona'] = df_ml['Cluster_ID'].map(lambda x: personas[str(x)]['name'])
                csv_data = df_ml.to_csv(index=False).encode('utf-8')

            st.download_button(
                "⬇️ Download Customer Analysis (CSV)",
                csv_data,
                "trustwave_customer_clusters.csv",
                "text/csv",
                use_container_width=True
            )

        with ec2:
            st.markdown("**Download Model Information (JSON)**")
            st.markdown('<div class="chart-desc">A JSON file with model settings, scores, and group definitions. Useful for documentation.</div>', unsafe_allow_html=True)
            report_json = json.dumps(meta, indent=2)
            st.download_button(
                "⬇️ Download Model Information (JSON)",
                report_json,
                "model_metadata.json",
                "application/json",
                use_container_width=True
            )
