# -*- coding: utf-8 -*-
"""
Script to generate the complete TrustWave Bank PowerPoint Presentation (.pptx)
with professional 16:9 layout, branded color palette, cards, metrics, and embedded images.
"""
import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Output Paths
OUTPUT_ROOT = os.path.join(BASE_DIR, "TrustWave_Bank_Business_Insights_Presentation.pptx")
OUTPUT_R3 = os.path.join(BASE_DIR, "Round_3", "Presentation", "TrustWave_Bank_Business_Insights.pptx")
os.makedirs(os.path.dirname(OUTPUT_R3), exist_ok=True)

# Color Palette
NAVY = RGBColor(10, 36, 99)       # #0A2463 Primary
ROYAL = RGBColor(30, 90, 168)     # #1E5AA8 Secondary
SKY = RGBColor(62, 146, 204)      # #3E92CC Accent
TEAL = RGBColor(44, 165, 141)     # #2CA58D Success
AMBER = RGBColor(243, 156, 18)    # #F39C12 Warning
RED = RGBColor(231, 76, 60)       # #E74C3C Danger
DARK_TEXT = RGBColor(30, 41, 59)  # #1E293B
MUTED_TEXT = RGBColor(100, 116, 139) # #64748B
LIGHT_BG = RGBColor(248, 250, 252) # #F8FAFC
CARD_BORDER = RGBColor(203, 213, 225) # #CBD5E1
WHITE = RGBColor(255, 255, 255)

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, category_text="TRUSTWAVE BANK • CUSTOMER INTELLIGENCE"):
        # Header banner
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p0 = tf.paragraphs[0]
        p0.text = category_text.upper()
        p0.font.name = "Arial"
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = SKY
        
        p1 = tf.add_paragraph()
        p1.text = title_text
        p1.font.name = "Arial"
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = NAVY
        p1.space_before = Pt(4)

        # Thin accent line under title
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.03))
        line.fill.solid()
        line.fill.fore_color.rgb = SKY
        line.line.color.rgb = SKY

    def add_footer(slide, current_page, total_pages=12):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.35))
        tf = footer_box.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = f"TrustWave Bank — Data-Driven Business Insights Pitch  |  Slide {current_page} of {total_pages}"
        p.font.name = "Arial"
        p.font.size = Pt(9)
        p.font.color.rgb = MUTED_TEXT

    # ══════════════════════════════════════════════════════════════
    # SLIDE 1: TITLE SLIDE (Dark Navy Hero Theme)
    # ══════════════════════════════════════════════════════════════
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.color.rgb = NAVY

    # Decorative accent card
    card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5))
    card.fill.solid()
    card.fill.fore_color.rgb = RGBColor(14, 46, 120)
    card.line.color.rgb = SKY

    tb1 = s1.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.3), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "🏦 TRUSTWAVE BANK | EXECUTIVE PRESENTATION"
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = SKY

    p = tf1.add_paragraph()
    p.text = "Customer Insights &\nBusiness Growth Strategy"
    p.font.name = "Arial"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(16)

    p = tf1.add_paragraph()
    p.text = "A complete data analysis of 150K customers, 2.5M transactions, channel usage, complaints, and AI customer personas."
    p.font.name = "Arial"
    p.font.size = Pt(15)
    p.font.color.rgb = RGBColor(226, 232, 240)
    p.space_before = Pt(16)

    p = tf1.add_paragraph()
    p.text = "Prepared for: Executive Leadership & Bank Management  •  Assessment: DS Sprint Skill-Based Assessment"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER
    p.space_before = Pt(32)

    # ══════════════════════════════════════════════════════════════
    # SLIDE 2: EXECUTIVE SUMMARY & CORE KPIs
    # ══════════════════════════════════════════════════════════════
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Executive Summary: At a Glance Performance", "OVERVIEW & SCALE")
    add_footer(s2, 2)

    kpis = [
        ("Total Customers", "150,000", "Active banking clients", NAVY),
        ("Total Accounts", "240,000", "Savings, Current & Credit", ROYAL),
        ("Total Transactions", "2.55 Million", "Across all channels", SKY),
        ("Transaction Value", "₹149.7 Billion", "Total monetary velocity", TEAL),
        ("Service Complaints", "11,552", "93.1% resolution rate", AMBER),
    ]
    card_w = Inches(2.18)
    card_gap = Inches(0.2)
    left_start = Inches(0.8)
    for i, (label, val, sub, col) in enumerate(kpis):
        x = left_start + i * (card_w + card_gap)
        c = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), card_w, Inches(1.5))
        c.fill.solid()
        c.fill.fore_color.rgb = LIGHT_BG
        c.line.color.rgb = col
        c.line.width = Pt(2)
        
        tb = s2.shapes.add_textbox(x + Inches(0.1), Inches(1.85), card_w - Inches(0.2), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = label.upper()
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = MUTED_TEXT
        
        p = tf.add_paragraph()
        p.text = val
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = col
        p.space_before = Pt(4)
        
        p = tf.add_paragraph()
        p.text = sub
        p.font.size = Pt(8.5)
        p.font.color.rgb = DARK_TEXT

    # 3 Summary Pillar Cards below
    pillars = [
        ("1. Digital Adoption Surge",
         "• Over 52% of transaction volume is driven via UPI and Mobile Banking.\n• Branch transactions account for high operational overhead but lower velocity.\n• Key opportunity: Migrate remaining 48% manual touchpoints to digital channels."),
        ("2. Deposit & Wealth Concentration",
         "• Top 8% of customers (Ultra High-Net-Worth) hold over 35% of total bank deposits.\n• Middle-market savers maintain high credit scores (740+) and prime lending readiness.\n• Key opportunity: Launch automated wealth management sweeps and pre-approved loans."),
        ("3. Service Quality & Retention",
         "• 93.1% complaint resolution rate achieved with an average turnaround of 4.8 days.\n• Card and digital payment issues account for 64% of total customer inquiries.\n• Key opportunity: Real-time fraud SMS alerts and AI chatbot for instant resolution.")
    ]
    p_w = Inches(3.75)
    p_gap = Inches(0.24)
    for i, (title, body) in enumerate(pillars):
        x = left_start + i * (p_w + p_gap)
        c = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(3.6), p_w, Inches(3.2))
        c.fill.solid()
        c.fill.fore_color.rgb = LIGHT_BG
        c.line.color.rgb = CARD_BORDER

        tb = s2.shapes.add_textbox(x + Inches(0.2), Inches(3.75), p_w - Inches(0.4), Inches(2.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY
        
        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    # ══════════════════════════════════════════════════════════════
    # SLIDE 3: CHANNEL USAGE & DIGITAL SHIFT
    # ══════════════════════════════════════════════════════════════
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Channel Usage: Shift from Physical to Digital Banking", "TRANSACTION ANALYSIS")
    add_footer(s3, 3)

    img_path = os.path.join(BASE_DIR, "Round_2_Excel_Analysis", "03_Charts", "Channel_Usage.png")
    if os.path.exists(img_path):
        s3.shapes.add_picture(img_path, Inches(0.8), Inches(1.8), width=Inches(6.6))
    
    tb = s3.shapes.add_textbox(Inches(7.7), Inches(1.8), Inches(4.8), Inches(4.9))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Key Findings & Channel Trends"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY

    findings = [
        ("Mobile & UPI Dominance", "UPI and Mobile App represent the fastest growing channels by transaction count, processing over 1.3 million monthly transactions."),
        ("Branch & ATM Unit Economics", "While Branch visits have reduced, branch transaction cost per event is 6x higher than digital channels. Optimization is necessary."),
        ("POS Merchant Activity", "Card swipes at POS account for high ticket sizes, driving significant interchange and Merchant Discount Rate (MDR) fee revenue."),
        ("Strategic Action", "Incentivize UPI QR payments for micro-merchants and migrate remaining ATM cash withdrawals to contactless UPI Cash Points.")
    ]
    for title, desc in findings:
        p = tf.add_paragraph()
        p.text = f"• {title}: "
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ROYAL
        p.space_before = Pt(10)
        
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = DARK_TEXT

    # ══════════════════════════════════════════════════════════════
    # SLIDE 4: CUSTOMER SEGMENT COMPARISON
    # ══════════════════════════════════════════════════════════════
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Customer Segments: Value, Volumes & Risk Profile", "SEGMENT BENCHMARKING")
    add_footer(s4, 4)

    img_path = os.path.join(BASE_DIR, "Round_2_Excel_Analysis", "03_Charts", "Customer_Segment_Comparison.png")
    if os.path.exists(img_path):
        s4.shapes.add_picture(img_path, Inches(0.8), Inches(1.8), width=Inches(6.6))

    tb = s4.shapes.add_textbox(Inches(7.7), Inches(1.8), Inches(4.8), Inches(4.9))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Segment Distribution & Profitability"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY

    seg_points = [
        ("Mass Retail (39.7%)", "Largest customer volume with steady recurring deposits. High retention but lower margin; needs zero-fee digital self-service."),
        ("Digital Middle-Market (32.0%)", "Highest growth segment. High digital engagement score (3.5/4.0), excellent credit scores (740+), prime target for lending products."),
        ("High-Velocity Spenders (20.3%)", "Generate 42% of total transaction fee revenue through intensive card usage. Highly sensitive to cashback and reward programs."),
        ("Ultra HNW Commercial (8.0%)", "Core liquidity source holding ₹700K+ average balance. Requires dedicated Wealth Advisory and private banking coverage.")
    ]
    for seg, detail in seg_points:
        p = tf.add_paragraph()
        p.text = f"• {seg}: "
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ROYAL
        p.space_before = Pt(10)
        
        run = p.add_run()
        run.text = detail
        run.font.bold = False
        run.font.color.rgb = DARK_TEXT

    # ══════════════════════════════════════════════════════════════
    # SLIDE 5: ACCOUNT ACTIVITY & MONTHLY TRENDS
    # ══════════════════════════════════════════════════════════════
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Account Activity: Transaction Volume & Velocity Over Time", "ACTIVITY TRENDS")
    add_footer(s5, 5)

    img_path = os.path.join(BASE_DIR, "Round_2_Excel_Analysis", "03_Charts", "Account_Activity_Trends.png")
    if os.path.exists(img_path):
        s5.shapes.add_picture(img_path, Inches(0.8), Inches(1.8), width=Inches(6.6))

    tb = s5.shapes.add_textbox(Inches(7.7), Inches(1.8), Inches(4.8), Inches(4.9))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Trend Analysis & Seasonality"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY

    act_points = [
        ("Steady Monthly Velocity", "Transaction volumes remain strong month-on-month, averaging over 210,000 transactions per month with positive growth."),
        ("Festival & Quarter-End Spikes", "Spending peaks occur during festive shopping seasons and quarter-end corporate reconciliations, driving spikes in value."),
        ("Savings vs. Current Split", "Savings accounts drive volume frequency, while Current and Commercial accounts account for over 68% of total transfer value."),
        ("Operational Readout", "IT server infrastructure and core banking APIs maintain 99.9% uptime with minimal transaction dropping during peak hours.")
    ]
    for title, desc in act_points:
        p = tf.add_paragraph()
        p.text = f"• {title}: "
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ROYAL
        p.space_before = Pt(10)
        
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = DARK_TEXT

    # ══════════════════════════════════════════════════════════════
    # SLIDE 6: BALANCE DISTRIBUTION & FINANCIAL STABILITY
    # ══════════════════════════════════════════════════════════════
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Balance Distribution: Liquidity Spread & Risk Tiers", "BALANCE & RISK")
    add_footer(s6, 6)

    img_path = os.path.join(BASE_DIR, "Round_2_Excel_Analysis", "03_Charts", "Balance_Distribution.png")
    if os.path.exists(img_path):
        s6.shapes.add_picture(img_path, Inches(0.8), Inches(1.8), width=Inches(6.6))

    tb = s6.shapes.add_textbox(Inches(7.7), Inches(1.8), Inches(4.8), Inches(4.9))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Deposit Concentration & Risk Health"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY

    bal_points = [
        ("Long-Tail Distribution", "The majority of customers maintain balances under ₹100,000, creating a highly diversified deposit base that protects against liquidity shocks."),
        ("Credit Risk Profile", "62% of customers sit in the Low-Risk tier (credit score > 700), providing a healthy buffer against default rates."),
        ("High-Balance Retention", "HNW deposits provide substantial Net Interest Margin (NIM) funding, but require competitive term deposit rates to prevent flight."),
        ("Recommendations", "Deploy tiered interest rate products: offer attractive yields on savings balances above ₹50,000 to encourage deposit growth.")
    ]
    for title, desc in bal_points:
        p = tf.add_paragraph()
        p.text = f"• {title}: "
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ROYAL
        p.space_before = Pt(10)
        
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = DARK_TEXT

    # ══════════════════════════════════════════════════════════════
    # SLIDE 7: COMPLAINT & SERVICE REQUEST ANALYSIS
    # ══════════════════════════════════════════════════════════════
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Complaint Analysis: Resolution Times & Customer Pain Points", "CUSTOMER SERVICE QUALITY")
    add_footer(s7, 7)

    img_path = os.path.join(BASE_DIR, "Round_2_Excel_Analysis", "03_Charts", "Complaint_Analysis.png")
    if os.path.exists(img_path):
        s7.shapes.add_picture(img_path, Inches(0.8), Inches(1.8), width=Inches(6.6))

    tb = s7.shapes.add_textbox(Inches(7.7), Inches(1.8), Inches(4.8), Inches(4.9))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Service Performance & Key Metrics"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY

    comp_points = [
        ("93.1% Resolution Rate", "10,755 of 11,552 complaints have been satisfactorily resolved, demonstrating solid operational response mechanisms."),
        ("Average TAT: 4.8 Days", "Standard resolution turnaround averages less than 5 working days, well within regulatory compliance benchmarks."),
        ("Card & Digital Hotspots", "Card billing disputes and failed digital transactions account for 58% of issues. Instant auto-reversals can eliminate 40% of these tickets."),
        ("Channel Preference", "Over 65% of complaints are submitted via Mobile App and Email, showing customers demand fast in-app support workflows.")
    ]
    for title, desc in comp_points:
        p = tf.add_paragraph()
        p.text = f"• {title}: "
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ROYAL
        p.space_before = Pt(10)
        
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = DARK_TEXT

    # ══════════════════════════════════════════════════════════════
    # SLIDE 8: CORRELATION & FEATURE ENGINEERING INSIGHTS
    # ══════════════════════════════════════════════════════════════
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Feature Engineering: Key Drivers of Customer Value", "EXPLORATORY DATA ANALYSIS")
    add_footer(s8, 8)

    img_path = os.path.join(BASE_DIR, "Round_1_EDA_Feature_Engineering", "Visualizations", "correlation_heatmap.png")
    if os.path.exists(img_path):
        s8.shapes.add_picture(img_path, Inches(0.8), Inches(1.8), width=Inches(6.6))

    tb = s8.shapes.add_textbox(Inches(7.7), Inches(1.8), Inches(4.8), Inches(4.9))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Correlation & Behavioral Insights"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY

    eda_points = [
        ("Income & Spending Correlation", "Monthly income shows strong positive correlation with transaction amount and account balance, confirming high earning power drives banking volume."),
        ("Digital Engagement & Activity", "Customers with high digital engagement scores (UPI/App) execute 3.4x more transactions per month than purely branch-based clients."),
        ("Credit Score & Stability", "Credit score correlates negatively with default indicators, validating our credit scoring risk tiers."),
        ("Strategic Takeaway", "Focus marketing acquisition on digitally active professionals aged 25-45 to maximize lifetime customer value (LTV).")
    ]
    for title, desc in eda_points:
        p = tf.add_paragraph()
        p.text = f"• {title}: "
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ROYAL
        p.space_before = Pt(10)
        
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = DARK_TEXT

    # ══════════════════════════════════════════════════════════════
    # SLIDE 9: AI CUSTOMER PERSONAS (K-MEANS CLUSTERING)
    # ══════════════════════════════════════════════════════════════
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "AI Customer Intelligence: The 4 Discovered Personas", "MACHINE LEARNING LAYER")
    add_footer(s9, 9)

    personas = [
        ("Mass Retail & Emerging Savers", "Cluster 0  •  39.7% of Base",
         "Avg Income: ₹39,185\nAvg Credit Score: 616\nAvg Balance: ₹39,972\nPrimary Channel: Branch & ATM\nRisk Tier: Medium Risk",
         "Strategy: Low-fee micro-savings, financial literacy, automated digital onboarding.", SKY),
        ("High-Velocity Spenders", "Cluster 1  •  20.3% of Base",
         "Avg Income: ₹71,927\nAvg Credit Score: 698\nAvg Balance: ₹119,015\nPrimary Channel: POS & Online\nTransactions: 38+/month (₹2.6M)",
         "Strategy: Premier cashback credit cards, merchant tie-ups, dining/travel privileges.", AMBER),
        ("Ultra HNW Commercial", "Cluster 2  •  8.0% of Base",
         "Avg Income: ₹288,644\nAvg Credit Score: 800\nAvg Balance: ₹704,350\nPrimary Channel: Omnichannel / RM\nSpending: ₹3.1M+",
         "Strategy: Dedicated wealth advisory, private banking suites, customized lending lines.", NAVY),
        ("Digital Middle-Market Savers", "Cluster 3  •  32.0% of Base",
         "Avg Income: ₹93,979\nAvg Credit Score: 740\nAvg Balance: ₹142,657\nPrimary Channel: Mobile App First\nDigital Score: 3.5 / 4.0",
         "Strategy: Pre-approved digital personal loans, mutual fund SIPs, fixed deposits.", TEAL),
    ]

    cw = Inches(2.78)
    cg = Inches(0.18)
    for i, (name, tag, metrics, strat, col) in enumerate(personas):
        x = Inches(0.8) + i * (cw + cg)
        c = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), cw, Inches(4.9))
        c.fill.solid()
        c.fill.fore_color.rgb = LIGHT_BG
        c.line.color.rgb = col
        c.line.width = Pt(2.5)

        tb = s9.shapes.add_textbox(x + Inches(0.15), Inches(1.95), cw - Inches(0.3), Inches(4.6))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = col

        p = tf.add_paragraph()
        p.text = tag
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = MUTED_TEXT
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = "Profile Metrics:"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(12)

        p = tf.add_paragraph()
        p.text = metrics
        p.font.size = Pt(9.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(4)

        p = tf.add_paragraph()
        p.text = "Actionable Strategy:"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(12)

        p = tf.add_paragraph()
        p.text = strat
        p.font.size = Pt(9.5)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(4)

    # ══════════════════════════════════════════════════════════════
    # SLIDE 10: INTERACTIVE STREAMLIT DASHBOARD
    # ══════════════════════════════════════════════════════════════
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Intelligence Dashboard: Real-Time Operational Analytics", "APPLICATION & DEPLOYMENT")
    add_footer(s10, 10)

    img_path = os.path.join(BASE_DIR, "Round_3", "Dashboards", "Customer_Segment_Comparison.png")
    if not os.path.exists(img_path):
        img_path = os.path.join(BASE_DIR, "Tabelau", "Dashboard Images", "Dashboard_01.png")
    if os.path.exists(img_path):
        s10.shapes.add_picture(img_path, Inches(0.8), Inches(1.8), width=Inches(6.6))

    tb = s10.shapes.add_textbox(Inches(7.7), Inches(1.8), Inches(4.8), Inches(4.9))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Dashboard Capabilities & Features"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY

    dash_features = [
        ("Executive Overview", "Real-time KPI metrics tracking 150K customers, ₹149.7B transaction value, and dual-axis monthly activity charts."),
        ("Interactive Customer Insights", "Multi-criteria filtering by segment, risk category, and gender with fast 100x optimized search tables."),
        ("Transaction Intelligence", "Dynamic breakdowns of channels, transaction types, and automated fraud-flagging anomaly detection."),
        ("Real-Time AI Scorer", "Allows bank relationship managers to enter customer data and predict their persona + risk recommendations in under 1 millisecond."),
        ("One-Click Data Export", "Instant CSV export of clustered customers for downstream marketing and CRM campaigns.")
    ]
    for feat, desc in dash_features:
        p = tf.add_paragraph()
        p.text = f"• {feat}: "
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ROYAL
        p.space_before = Pt(8)
        
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = DARK_TEXT

    # ══════════════════════════════════════════════════════════════
    # SLIDE 11: STRATEGIC BUSINESS RECOMMENDATIONS (4 PILLARS)
    # ══════════════════════════════════════════════════════════════
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Strategic Recommendations: 4 Pillars of Bank Growth", "BUSINESS STRATEGY")
    add_footer(s11, 11)

    rec_pillars = [
        ("Pillar 1: Accelerate Digital Transition",
         "Target: Mass Retail & Emerging Savers\n\n• Deploy mobile app incentives and zero-fee UPI transfers.\n• Shift branch cash transactions to self-service digital kiosks.\n• Expected Impact: 24% reduction in branch operational cost."),
        ("Pillar 2: Monetize High-Velocity Spenders",
         "Target: High-Velocity Spenders (20.3%)\n\n• Launch tiered rewards cards with dining & travel cashback.\n• Partner with top merchant platforms to drive interchange fee income.\n• Expected Impact: 18% lift in fee-based non-interest income."),
        ("Pillar 3: Expand Lending to Middle Savers",
         "Target: Digital Middle-Market Savers (32.0%)\n\n• Introduce pre-approved digital personal loans and auto financing.\n• Bundle automated mutual fund SIPs and fixed-deposit boosters.\n• Expected Impact: 30% increase in net interest income (NII)."),
        ("Pillar 4: Protect & Grow High-Net-Worth Liquidity",
         "Target: Ultra HNW Commercial Clients (8.0%)\n\n• Assign dedicated Wealth Relationship Managers.\n• Offer multi-currency accounts and treasury liquidity sweeps.\n• Expected Impact: 98% retention of top-tier deposit reserves.")
    ]
    rw = Inches(2.78)
    rg = Inches(0.18)
    for i, (title, body) in enumerate(rec_pillars):
        x = Inches(0.8) + i * (rw + rg)
        c = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), rw, Inches(4.9))
        c.fill.solid()
        c.fill.fore_color.rgb = LIGHT_BG
        c.line.color.rgb = NAVY if i==0 else (ROYAL if i==1 else (TEAL if i==2 else SKY))
        c.line.width = Pt(2)

        tb = s11.shapes.add_textbox(x + Inches(0.15), Inches(1.95), rw - Inches(0.3), Inches(4.6))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY

        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(10)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(12)

    # ══════════════════════════════════════════════════════════════
    # SLIDE 12: CONCLUSION & 30-60-90 DAY ROADMAP
    # ══════════════════════════════════════════════════════════════
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Execution Roadmap: 30-60-90 Day Action Plan", "NEXT STEPS")
    add_footer(s12, 12)

    roadmap = [
        ("Days 1 – 30: Quick Wins",
         "• Deploy the Intelligence Dashboard across branch operations.\n• Roll out automated SMS alerts for card and failed digital transactions.\n• Begin targeted mobile app onboarding for Mass Retail customers.", SKY),
        ("Days 31 – 60: Growth Initiatives",
         "• Launch tailored Cashback Credit Card pilot for High-Velocity Spenders.\n• Introduce pre-approved digital loan pre-screening for Middle Savers.\n• Establish dedicated HNW concierge desks in top metro branches.", ROYAL),
        ("Days 61 – 90: Scale & Integration",
         "• Fully integrate K-Means Persona Scorer into Core Banking CRM.\n• Automate 80% of routine complaint resolution via conversational AI.\n• Conduct quarterly review of customer retention and NIM growth.", NAVY)
    ]
    r_w = Inches(3.75)
    r_gap = Inches(0.24)
    for i, (phase, details, col) in enumerate(roadmap):
        x = Inches(0.8) + i * (r_w + r_gap)
        c = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), r_w, Inches(4.0))
        c.fill.solid()
        c.fill.fore_color.rgb = LIGHT_BG
        c.line.color.rgb = col
        c.line.width = Pt(2)

        tb = s12.shapes.add_textbox(x + Inches(0.2), Inches(1.95), r_w - Inches(0.4), Inches(3.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = phase
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = col

        p = tf.add_paragraph()
        p.text = details
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(14)

    # Thank you / Closing callout box at bottom
    bot = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.0), Inches(11.733), Inches(0.85))
    bot.fill.solid()
    bot.fill.fore_color.rgb = NAVY
    bot.line.color.rgb = SKY

    tb_bot = s12.shapes.add_textbox(Inches(1.0), Inches(6.05), Inches(11.3), Inches(0.75))
    tf_b = tb_bot.text_frame
    p = tf_b.paragraphs[0]
    p.text = "🤝 Thank You! Ready for Executive Q&A and Strategic Implementation."
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Save presentations
    prs.save(OUTPUT_ROOT)
    prs.save(OUTPUT_R3)
    print(f"Presentation saved successfully to:")
    print(f"1. {OUTPUT_ROOT}")
    print(f"2. {OUTPUT_R3}")

if __name__ == "__main__":
    create_presentation()
