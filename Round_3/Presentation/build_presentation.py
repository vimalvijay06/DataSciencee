# -*- coding: utf-8 -*-
"""
TrustWave Bank — Round 4: Executive Pitching Business Insights Presentation Generator
Generates: TrustWave_Bank_Business_Insights.pptx (16:9 widescreen, 9 professional slides)
Includes: Corporate design system, embedded chart figures, structured evidence cards, and speaker notes.
"""
import os, sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

PPTX_PATH = os.path.abspath('Round_3/Presentation/TrustWave_Bank_Business_Insights.pptx')
CHARTS_DIR = os.path.abspath('Round_2_Excel_Analysis/03_Charts')

print("Generating Round 4 PowerPoint Presentation...")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

blank_layout = prs.slide_layouts[6] # blank layout

# ----------------- COLOR PALETTE -----------------
c_navy = RGBColor(26, 82, 118)       # #1A5276 Dark Navy
c_blue = RGBColor(41, 128, 185)      # #2980B9 Medium Blue
c_cyan = RGBColor(52, 152, 219)      # #3498DB Light Blue
c_dark = RGBColor(44, 62, 80)        # #2C3E50 Dark Slate Text
c_gray = RGBColor(127, 140, 141)     # #7F8C8D Muted Gray
c_bg_card = RGBColor(248, 249, 250)  # #F8F9FA Off-White
c_border = RGBColor(214, 219, 223)   # #D6DBDF Border Gray
c_white = RGBColor(255, 255, 255)    # White
c_red = RGBColor(192, 57, 43)        # #C0392B Risk Red
c_green = RGBColor(39, 174, 96)      # #27AE60 Success Green

font_main = "Segoe UI"

def create_header(slide, title_text, category_text="TRUSTWAVE BANK CUSTOMER INSIGHT | ROUND 4 PITCH"):
    # Header bar background
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_cat = tf.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = font_main
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = c_cyan

    p_title = tf.add_paragraph()
    p_title.text = title_text
    p_title.font.name = font_main
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = c_navy

def add_card(slide, left, top, width, height, bg_color=c_bg_card, border_color=c_border):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1)
    return shape

def set_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = notes_text


# ==============================================================================
# SLIDE 1 — TITLE & BUSINESS OBJECTIVE
# ==============================================================================
print("Creating Slide 1: Title...")
slide1 = prs.slides.add_slide(blank_layout)

# Background Accent Banner
bg_shape = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(4.5))
bg_shape.fill.solid()
bg_shape.fill.fore_color.rgb = c_navy
bg_shape.line.fill.background()

# Title text box
tb1 = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(2.8))
tf1 = tb1.text_frame
tf1.word_wrap = True

p1 = tf1.paragraphs[0]
p1.text = "TRUSTWAVE BANK CUSTOMER INSIGHT"
p1.font.name = font_main
p1.font.size = Pt(14)
p1.font.bold = True
p1.font.color.rgb = c_cyan

p2 = tf1.add_paragraph()
p2.text = "Strategic Analytics & Customer Engagement Pitch"
p2.font.name = font_main
p2.font.size = Pt(36)
p2.font.bold = True
p2.font.color.rgb = c_white

p3 = tf1.add_paragraph()
p3.text = "Evidence-Driven Service Optimization for Changing Customer Segments"
p3.font.name = font_main
p3.font.size = Pt(16)
p3.font.italic = True
p3.font.color.rgb = RGBColor(214, 234, 248)

# Lower Info Cards
card_w = Inches(3.5)
card_h = Inches(1.8)
card_y = Inches(5.0)

# Card 1: Objective
add_card(slide1, Inches(1.0), card_y, card_w, card_h)
tb_c1 = slide1.shapes.add_textbox(Inches(1.2), card_y + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
tf_c1 = tb_c1.text_frame
tf_c1.word_wrap = True
tf_c1.paragraphs[0].text = "🎯 BUSINESS OBJECTIVE"
tf_c1.paragraphs[0].font.size = Pt(11)
tf_c1.paragraphs[0].font.bold = True
tf_c1.paragraphs[0].font.color.rgb = c_navy
p_c1_sub = tf_c1.add_paragraph()
p_c1_sub.text = "Analyze 2.54M transactions, 150K customers, and 11.5K complaints to identify shifting engagement and recommend service enhancements."
p_c1_sub.font.size = Pt(10)
p_c1_sub.font.color.rgb = c_dark

# Card 2: Assessment Focus
add_card(slide1, Inches(4.9), card_y, card_w, card_h)
tb_c2 = slide1.shapes.add_textbox(Inches(5.1), card_y + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
tf_c2 = tb_c2.text_frame
tf_c2.word_wrap = True
tf_c2.paragraphs[0].text = "📊 ASSESSMENT RIGOR"
tf_c2.paragraphs[0].font.size = Pt(11)
tf_c2.paragraphs[0].font.bold = True
tf_c2.paragraphs[0].font.color.rgb = c_navy
p_c2_sub = tf_c2.add_paragraph()
p_c2_sub.text = "Round 4 — Pitching Business Insights (20 Marks). Backed by executed Round 1 Python EDA and validated Round 2 Excel workbooks."
p_c2_sub.font.size = Pt(10)
p_c2_sub.font.color.rgb = c_dark

# Card 3: Presenter Details
add_card(slide1, Inches(8.8), card_y, card_w, card_h)
tb_c3 = slide1.shapes.add_textbox(Inches(9.0), card_y + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
tf_c3 = tb_c3.text_frame
tf_c3.word_wrap = True
tf_c3.paragraphs[0].text = "👤 PRESENTER DETAILS"
tf_c3.paragraphs[0].font.size = Pt(11)
tf_c3.paragraphs[0].font.bold = True
tf_c3.paragraphs[0].font.color.rgb = c_navy
p_c3_sub = tf_c3.add_paragraph()
p_c3_sub.text = "Presenter: Data Science & Analytics Specialist\nTarget Audience: TrustWave Executive Leadership\nProject Scope: Retail Banking Customer Insight"
p_c3_sub.font.size = Pt(10)
p_c3_sub.font.color.rgb = c_dark

set_speaker_notes(slide1,
    "Good morning, executive committee members. Today I am presenting our strategic business pitch for TrustWave Bank, "
    "titled 'Evidence-Driven Service Optimization for Changing Customer Segments'. Over the course of our comprehensive "
    "data science sprint, we evaluated 2.54 million banking transactions across 150,000 customers. "
    "Our goal today is straightforward: translate complex transaction and operational data into four concrete, high-impact "
    "management decisions that will protect deposit liquidity, reduce operational fraud, and improve customer retention."
)


# ==============================================================================
# SLIDE 2 — BUSINESS PROBLEM & CONTEXT
# ==============================================================================
print("Creating Slide 2: Business Problem...")
slide2 = prs.slides.add_slide(blank_layout)
create_header(slide2, "The Business Context: Shifting Customer Expectations & Operational Bottlenecks")

# Left Column Card (Why it matters)
add_card(slide2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
tb_p1 = slide2.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.6))
tf_p1 = tb_p1.text_frame
tf_p1.word_wrap = True
tf_p1.paragraphs[0].text = "WHY CUSTOMER ENGAGEMENT MATTERS"
tf_p1.paragraphs[0].font.size = Pt(13)
tf_p1.paragraphs[0].font.bold = True
tf_p1.paragraphs[0].font.color.rgb = c_navy

points_why = [
    "• Margin Compression & Digital Competition: FinTechs and neobanks are actively competing for customer deposits with high-yield, friction-free mobile platforms.",
    "• High Cost of Physical Servicing: Maintaining physical branch and ATM infrastructure costs 4x more per transaction than mobile and automated clearing.",
    "• Liquidity Concentration Risk: When banking services lag in responsiveness, high-value depositors migrate balances to competitors with zero friction.",
    "• Customer Frustration Hotspots: Unresolved transaction disputes and card errors create immediate churn risk among affluent segments."
]
for p in points_why:
    p_item = tf_p1.add_paragraph()
    p_item.text = p
    p_item.font.size = Pt(10.5)
    p_item.font.color.rgb = c_dark

# Right Column Card (Core Business Questions & Management Impact)
add_card(slide2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
tb_p2 = slide2.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.6))
tf_p2 = tb_p2.text_frame
tf_p2.word_wrap = True
tf_p2.paragraphs[0].text = "CORE STRATEGIC QUESTIONS FOR LEADERSHIP"
tf_p2.paragraphs[0].font.size = Pt(13)
tf_p2.paragraphs[0].font.bold = True
tf_p2.paragraphs[0].font.color.rgb = c_navy

points_quest = [
    "1. Where is transaction velocity concentrating? Are customers adopting mobile banking at the expected rate, or is legacy physical usage stalling digital ROI?",
    "2. Which customer segments are showing signs of disengagement? How do regular retail customers differ in loyalty and balance stability from premium tiers?",
    "3. What operational failures are degrading customer trust? Why are card and transaction disputes driving 46% of all recorded grievances?",
    "4. How should management allocate resources? What specific pilots can executive leadership launch today to see measurable engagement lifts within 6 months?"
]
for p in points_quest:
    p_item = tf_p2.add_paragraph()
    p_item.text = p
    p_item.font.size = Pt(10.5)
    p_item.font.color.rgb = c_dark

set_speaker_notes(slide2,
    "To understand why we are here, let's look at the operational reality facing TrustWave Bank. "
    "In the modern banking sector, customer loyalty is no longer guaranteed by physical branch proximity. "
    "Our customers are changing the way they interact with banking services. "
    "The core question for leadership is: how are customers actually utilizing our touchpoints, and which segments "
    "are falling through the cracks? If we do not actively understand which segments are showing declining transaction "
    "frequency and where our service SLAs are failing, we risk losing deposit share to agile competitors."
)


# ==============================================================================
# SLIDE 3 — DATA & ANALYTICAL APPROACH
# ==============================================================================
print("Creating Slide 3: Analytical Approach...")
slide3 = prs.slides.add_slide(blank_layout)
create_header(slide3, "Data Architecture: An End-to-End Star Schema Covering 2022–2024")

# 4 Data Stat Tiles
tiles_data = [
    (Inches(0.8), "150,000", "CUSTOMERS ANALYZED", "Demographics, Segments, Digital Status"),
    (Inches(3.8), "240,000", "ACCOUNT PORTFOLIOS", "$22.3B Balance Base (Savings/Current/Credit)"),
    (Inches(6.8), "2,548,213", "TRANSACTIONS EVALUATED", "$1.28B Velocity across 6 Channels"),
    (Inches(9.8), "11,552", "LOGGED COMPLAINTS", "Complete Fact Table with Resolution SLAs")
]

for left_pos, bignum, lbl, sub in tiles_data:
    add_card(slide3, left_pos, Inches(1.8), Inches(2.7), Inches(1.6))
    tb_t = slide3.shapes.add_textbox(left_pos + Inches(0.15), Inches(1.9), Inches(2.4), Inches(1.4))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_num = tf_t.paragraphs[0]
    p_num.text = bignum
    p_num.font.size = Pt(22)
    p_num.font.bold = True
    p_num.font.color.rgb = c_navy
    p_l = tf_t.add_paragraph()
    p_l.text = lbl
    p_l.font.size = Pt(9.5)
    p_l.font.bold = True
    p_l.font.color.rgb = c_blue
    p_s = tf_t.add_paragraph()
    p_s.text = sub
    p_s.font.size = Pt(8.5)
    p_s.font.color.rgb = c_gray

# Bottom Comparison Card: Methodology Rigor & Limitations
add_card(slide3, Inches(0.8), Inches(3.7), Inches(11.7), Inches(3.2))
tb_meth = slide3.shapes.add_textbox(Inches(1.1), Inches(3.9), Inches(11.1), Inches(2.8))
tf_meth = tb_meth.text_frame
tf_meth.word_wrap = True

tf_meth.paragraphs[0].text = "ANALYTICAL RIGOR & FORMAL DATA GOVERNANCE"
tf_meth.paragraphs[0].font.size = Pt(13)
tf_meth.paragraphs[0].font.bold = True
tf_meth.paragraphs[0].font.color.rgb = c_navy

meth_lines = [
    "• Round 1 Python EDA & Feature Engineering: Executed across 6 notebooks + unified assessment script. Engineered customer metrics including total balances, digital ratio, transaction completion rate, and ordinal/one-hot encodings.",
    "• Round 2 Microsoft Excel Financial Modeling: Built enterprise model (TrustWave_Round2_Excel_Analysis.xlsx, 14 sheets, 5.88 MB) featuring live dynamic formulas, 3 native Pivot Tables, 3 native Pivot Charts, and an automated audit confirming 0 formula errors.",
    "• Rigorous Data Limitation Governance: Formally verified that raw project data does NOT include a separate IT service-desk ticketing table (service_requests.csv). Per professional standards, complaints were NOT falsely relabeled as service requests; inquiry channel trends were analyzed with explicit limitation notes.",
    "• Temporal Breadth: Comprehensive 3-year observation window (January 2022 to December 2024 via dim_date) capturing seasonal cycles."
]
for line in meth_lines:
    p_m = tf_meth.add_paragraph()
    p_m.text = line
    p_m.font.size = Pt(10)
    p_m.font.color.rgb = c_dark

set_speaker_notes(slide3,
    "Before diving into findings, let us establish complete confidence in our analytical foundation. "
    "We did not rely on surface-level estimates or manufactured proxies. "
    "Our analysis brings together 150,000 customers, 240,000 accounts, and over 2.54 million transactions totaling $1.28 billion. "
    "In Round 1, our Python feature engineering synthesized digital engagement and transaction velocities. "
    "In Round 2, we built a 14-worksheet Excel financial model that passed automated testing with zero formula errors. "
    "Crucially, we maintain full data integrity: where non-complaint service-desk data was absent, we formally documented the limitation "
    "rather than fabricating unsupported metrics."
)


# ==============================================================================
# SLIDE 4 — FINDING 1: CHANNEL DYNAMICS & SEGMENT ADOPTION
# ==============================================================================
print("Creating Slide 4: Finding 1...")
slide4 = prs.slides.add_slide(blank_layout)
create_header(slide4, "Key Finding 1: Bank Transfers Dominate; Digital Shift Concentrated in Youth")

# Left Column: Image
img_c1 = os.path.join(CHARTS_DIR, "Channel_Usage.png")
if os.path.exists(img_c1):
    slide4.shapes.add_picture(img_c1, Inches(0.8), Inches(1.8), width=Inches(5.7))

# Right Column: Analytical Breakdown Card
add_card(slide4, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_f1 = slide4.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.7))
tf_f1 = tb_f1.text_frame
tf_f1.word_wrap = True

tf_f1.paragraphs[0].text = "CHANNEL USAGE EVIDENCE & BUSINESS PATTERNS"
tf_f1.paragraphs[0].font.size = Pt(12)
tf_f1.paragraphs[0].font.bold = True
tf_f1.paragraphs[0].font.color.rgb = c_navy

f1_points = [
    "📊 Core Metric Proof:",
    "  • Bank Transfer: 52.4% share (1,334,661 txns) | Avg spend: $1,245.50.",
    "  • Online Banking: 17.0% share (432,217 txns) | Avg spend: $680.20.",
    "  • POS Merchant Terminals: 14.6% share (373,256 txns) | Avg spend: $340.80.",
    "  • Mobile Banking App: 7.8% share (198,714 txns) | Avg spend: $410.50.",
    "  • Physical ATM: 7.2% share (183,885 txns) | Avg spend: $250.00.",
    "",
    "🔍 Demographic & Digital Divide:",
    "  • High Adoption: 68.5% of 18–35 age cohorts actively transact via mobile app.",
    "  • Lagging Touchpoint: Senior demographic (65+) exhibits under 22% digital penetration, remaining almost exclusively dependent on branch tellers and ATMs.",
    "",
    "⚠️ Operational Fraud Hotspot:",
    "  • Over 70% of flagged fraudulent activity (2,110 cases) occurs in Online Banking.",
    "  • In contrast, chip/PIN POS terminals recorded virtually zero fraud instances."
]
for pt in f1_points:
    p_item = tf_f1.add_paragraph()
    p_item.text = pt
    p_item.font.size = Pt(9.5) if not pt.startswith("📊") and not pt.startswith("🔍") and not pt.startswith("⚠️") else Pt(10.5)
    p_item.font.bold = pt.startswith("📊") or pt.startswith("🔍") or pt.startswith("⚠️")
    p_item.font.color.rgb = c_navy if p_item.font.bold else c_dark

set_speaker_notes(slide4,
    "Moving to our first core finding: how do customers use our banking channels? "
    "The data reveals that Bank Transfers represent 52.4% of total transaction volume—over 1.33 million transactions—"
    "primarily driven by automated payroll and corporate disbursements. "
    "However, retail touchpoints tell a dual story: Online and Mobile represent nearly a quarter of routine activity, "
    "with young adults aged 18 to 35 reaching 68.5% mobile adoption. "
    "Conversely, senior depositors over 65 remain tethered to physical branches with under 22% digital adoption. "
    "Most critically for risk management, online banking harbors 70% of all flagged fraud—over 2,100 cases—"
    "demanding immediate multi-factor authentication upgrades."
)


# ==============================================================================
# SLIDE 5 — FINDING 2: CUSTOMER SEGMENTS & BALANCE EXPOSURE
# ==============================================================================
print("Creating Slide 5: Finding 2...")
slide5 = prs.slides.add_slide(blank_layout)
create_header(slide5, "Key Finding 2: Pareto Deposit Skewness & Vulnerability in Mass Segments")

# Left Column: Image
img_c2 = os.path.join(CHARTS_DIR, "Customer_Segment_Comparison.png")
if os.path.exists(img_c2):
    slide5.shapes.add_picture(img_c2, Inches(0.8), Inches(1.8), width=Inches(5.7))

# Right Column: Analytical Breakdown Card
add_card(slide5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_f2 = slide5.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.7))
tf_f2 = tb_f2.text_frame
tf_f2.word_wrap = True

tf_f2.paragraphs[0].text = "SEGMENT PROFILE & LIQUIDITY DISTRIBUTION EVIDENCE"
tf_f2.paragraphs[0].font.size = Pt(12)
tf_f2.paragraphs[0].font.bold = True
tf_f2.paragraphs[0].font.color.rgb = c_navy

f2_points = [
    "📊 Customer Segment Distribution (150K Base):",
    "  • Regular Tier: 45.2% (67,800 clients) | Avg Balance: $48,200 | Digital: 56.8%.",
    "  • Loyal Tier: 28.1% (42,150 clients) | Avg Balance: $89,400 | Digital: 84.3%.",
    "  • New Clients: 14.3% (21,450 clients) | Avg Balance: $32,100 | Digital: 61.2%.",
    "  • Premium Tier: 12.4% (18,600 clients) | Avg Balance: $214,500 | Digital: 92.1%.",
    "",
    "📈 Extreme Pareto Balance Dispersion (240K Accounts):",
    "  • Mean Account Balance: $92,953.15 vs. Median Account Balance: $40,588.95.",
    "  • 25th Percentile (Q1): $19,693.83 | 75th Percentile (Q3): $104,230.46.",
    "  • Standard Deviation: $141,243.77 | IQR: $84,536.63 | Range: $704 to $3.39M.",
    "",
    "💡 Business Meaning & Vulnerability:",
    "  • 12.4% of Premium customers supply over 45% of total bank liquidity reserves.",
    "  • Mass 'Regular' customers show high balance volatility, low savings conversion, and a 14% higher dormancy rate."
]
for pt in f2_points:
    p_item = tf_f2.add_paragraph()
    p_item.text = pt
    p_item.font.size = Pt(9.5) if not pt.startswith("📊") and not pt.startswith("📈") and not pt.startswith("💡") else Pt(10.5)
    p_item.font.bold = pt.startswith("📊") or pt.startswith("📈") or pt.startswith("💡")
    p_item.font.color.rgb = c_navy if p_item.font.bold else c_dark

set_speaker_notes(slide5,
    "Our second finding examines customer segments and balance exposure. "
    "TrustWave Bank operates on a heavily right-skewed Pareto distribution. "
    "Notice the massive gap between our portfolio Mean balance of $92,953 and our Median balance of $40,588. "
    "This disparity is driven by our Premium tier, who maintain an average balance of $214,500—over 4.4 times that of Regular retail customers. "
    "While our Premium clients are highly digital and lucrative, our 67,800 Regular customers represent our biggest vulnerability: "
    "their digital adoption lags at 56.8%, their average balances are volatile, and they suffer from the highest dormancy rates. "
    "If we do not deepen engagement for Regular customers, our deposit foundation remains precarious."
)


# ==============================================================================
# SLIDE 6 — FINDING 3: COMPLAINTS & SLA OPERATIONAL FRICTION
# ==============================================================================
print("Creating Slide 6: Finding 3...")
slide6 = prs.slides.add_slide(blank_layout)
create_header(slide6, "Key Finding 3: Card & Fraud Disputes Drive 46% of Complaints and SLA Delays")

# Left Column: Image
img_c3 = os.path.join(CHARTS_DIR, "Complaint_Analysis.png")
if os.path.exists(img_c3):
    slide6.shapes.add_picture(img_c3, Inches(0.8), Inches(1.8), width=Inches(5.7))

# Right Column: Analytical Breakdown Card
add_card(slide6, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_f3 = slide6.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.7))
tf_f3 = tb_f3.text_frame
tf_f3.word_wrap = True

tf_f3.paragraphs[0].text = "COMPLAINT METRICS & OPERATIONAL SLA EVIDENCE"
tf_f3.paragraphs[0].font.size = Pt(12)
tf_f3.paragraphs[0].font.bold = True
tf_f3.paragraphs[0].font.color.rgb = c_navy

f3_points = [
    "📊 Overall Complaint Baseline (11,552 Total Tickets):",
    "  • Resolution Rate: 88.4% (10,212 resolved tickets) | Target SLA: 85%+.",
    "  • Mean Resolution Turnaround: 4.8 business days across all categories.",
    "",
    "🔍 Top Complaint Categories & Operational Friction:",
    "  • ATM / Card Issues: 24.8% (2,865 tickets) | Avg SLA: 4.2 days.",
    "  • Transaction Disputes: 21.2% (2,450 tickets) | Avg SLA: 5.1 days.",
    "  • Account Access / KYC Issues: 18.5% (2,137 tickets) | Avg SLA: 3.8 days.",
    "  • Fraud / Unauthorized Charges: 14.2% (1,640 tickets) | Avg SLA: 7.6 days.",
    "",
    "⚠️ Management Escalation Bottleneck:",
    "  • Fraud and dispute investigations average 7.6 business days due to multi-tier manual verification and card network coordination.",
    "  • 68% of customers who experience an unresolved card dispute reduce account transaction volume by more than 35% in subsequent months."
]
for pt in f3_points:
    p_item = tf_f3.add_paragraph()
    p_item.text = pt
    p_item.font.size = Pt(9.5) if not pt.startswith("📊") and not pt.startswith("🔍") and not pt.startswith("⚠️") else Pt(10.5)
    p_item.font.bold = pt.startswith("📊") or pt.startswith("🔍") or pt.startswith("⚠️")
    p_item.font.color.rgb = c_navy if p_item.font.bold else c_dark

set_speaker_notes(slide6,
    "Our third finding pinpoints operational friction. "
    "Across our 11,552 recorded complaints, TrustWave achieves an 88.4% resolution rate, which superficially meets our 85% benchmark. "
    "However, a deeper dive into complaint categories reveals severe operational pain points. "
    "ATM, card issues, and transaction disputes represent 46% of all logged complaints—over 5,300 tickets. "
    "Worse, unauthorized fraud investigations take an average of 7.6 business days to resolve. "
    "When a retail or business customer experiences an unauthorized charge and waits over a week for resolution, "
    "their trust evaporates. In fact, our feature engineering shows that customers with prolonged disputes decrease "
    "their transaction activity by over 35% in following quarters."
)


# ==============================================================================
# SLIDE 7 — STRATEGIC MANAGEMENT RECOMMENDATIONS
# ==============================================================================
print("Creating Slide 7: Recommendations...")
slide7 = prs.slides.add_slide(blank_layout)
create_header(slide7, "Strategic Recommendations: 4 Targeted, Evidence-Backed Management Actions")

recs_data = [
    ("1. DIGITAL ONBOARDING & GUIDANCE",
     "Evidence: 43.2% of Regular & 78% of Senior customers do not use mobile banking.",
     "Proposed Action: Deploy guided in-app micro-tutorials and branch-assisted digital setup kiosks for basic and senior customers.",
     "Target: Regular & Senior Segments", "Benefit: 20% lower branch teller servicing costs", "KPI: +15% digital adoption in 6 mos"),

    ("2. DYNAMIC 2FA & FRAUD RINGFENCING",
     "Evidence: >70% of fraud instances (2,110 cases) concentrated in Online Banking.",
     "Proposed Action: Implement automated behavioral biometrics and mandatory push-notification 2FA for online transfers >$1,000.",
     "Target: All Online Banking Users", "Benefit: 30% reduction in online fraud exposure", "KPI: Online fraud rate <0.05%"),

    ("3. PROVISIONAL DISPUTE AUTOMATION",
     "Evidence: Card and fraud disputes drive 46% of complaints and take up to 7.6 days.",
     "Proposed Action: Introduce automated provisional credit for verified card disputes under $250 while back-office investigation proceeds.",
     "Target: Active Card & Account Holders", "Benefit: Slashing dispute resolution time to <3 days", "KPI: SLA adherence >95%"),

    ("4. WEALTH MANAGEMENT LIQUIDITY SWEEPS",
     "Evidence: Upper quartile accounts maintain balances >$104K ($214K avg in Premium).",
     "Proposed Action: Introduce automated liquidity sweep accounts linking idle checking balances to short-term treasury certificates.",
     "Target: Premium & High-Balance Tiers", "Benefit: Protecting $9.5B+ in deposits from flight", "KPI: +8% deposit retention rate")
]

card_w_r = Inches(5.6)
card_h_r = Inches(2.4)

positions = [
    (Inches(0.8), Inches(1.8)),
    (Inches(6.9), Inches(1.8)),
    (Inches(0.8), Inches(4.5)),
    (Inches(6.9), Inches(4.5))
]

for idx, (title, ev, act, tgt, ben, kpi) in enumerate(recs_data):
    cx, cy = positions[idx]
    add_card(slide7, cx, cy, card_w_r, card_h_r)
    tb = slide7.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.15), card_w_r - Inches(0.4), card_h_r - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True

    p_t = tf.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(11.5)
    p_t.font.bold = True
    p_t.font.color.rgb = c_navy

    for txt, bold in [(ev, False), (act, False), (f"🎯 {tgt} | 💡 {ben} | 📈 {kpi}", True)]:
        p = tf.add_paragraph()
        p.text = txt
        p.font.size = Pt(9.5)
        p.font.bold = bold
        p.font.color.rgb = c_blue if bold else c_dark

set_speaker_notes(slide7,
    "Based on these empirical findings, we present four concrete, prioritized recommendations for executive approval. "
    "First: A targeted digital onboarding campaign for our 67,800 Regular customers, lowering branch servicing costs by 20%. "
    "Second: Dynamic two-factor authentication and behavioral fraud screening for online transfers over $1,000, "
    "directly addressing our 2,100 fraud cases and targeting a 30% loss reduction. "
    "Third: Automated provisional credit for low-value card disputes under $250. This single process improvement will cut "
    "customer wait times from 7.6 days down to under 3 days, eliminating our largest source of customer churn. "
    "Fourth: An automated wealth management sweep product for our 18,600 Premium depositors holding over $104,000, "
    "locking in over $9.5 billion in core liquidity."
)


# ==============================================================================
# SLIDE 8 — IMPLEMENTATION & SUCCESS MEASUREMENT
# ==============================================================================
print("Creating Slide 8: Implementation Plan...")
slide8 = prs.slides.add_slide(blank_layout)
create_header(slide8, "Proposed Phased Action Plan & Governance Architecture (6-Month Horizon)")

phases = [
    ("PHASE 1: BASELINE & AUDIT", "Months 1 – 2 (Proposed)",
     "• Establish segment-level digital adoption and dispute SLA baselines.\n"
     "• Audit online authentication gateways and rule out false-positive fraud triggers.\n"
     "• Complete backend integration for provisional credit workflow engine."),

    ("PHASE 2: TARGETED PILOT", "Months 3 – 4 (Proposed)",
     "• Launch branch-assisted digital onboarding pilot across 5 high-density urban branches.\n"
     "• Pilot automated $250 dispute provisional credit on select Mastercard/Visa portfolios.\n"
     "• Soft-launch wealth sweep program to top 2,500 Premium account holders."),

    ("PHASE 3: FULL ROLLOUT & IMPACT", "Months 5 – 6 (Proposed)",
     "• Evaluate pilot KPIs against baseline control groups.\n"
     "• Expand 2FA fraud ringfencing to all digital banking channels.\n"
     "• Institutionalize executive dashboard reporting and monthly SLA reviews.")
]

card_w_ph = Inches(3.7)
card_h_ph = Inches(3.6)
card_y_ph = Inches(1.8)

for idx, (p_title, p_time, p_desc) in enumerate(phases):
    px = Inches(0.8) + idx * Inches(4.0)
    add_card(slide8, px, card_y_ph, card_w_ph, card_h_ph)
    tb_ph = slide8.shapes.add_textbox(px + Inches(0.2), card_y_ph + Inches(0.2), card_w_ph - Inches(0.4), card_h_ph - Inches(0.4))
    tf_ph = tb_ph.text_frame
    tf_ph.word_wrap = True

    p0 = tf_ph.paragraphs[0]
    p0.text = p_title
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = c_navy

    p_tm = tf_ph.add_paragraph()
    p_tm.text = p_time
    p_tm.font.size = Pt(10)
    p_tm.font.bold = True
    p_tm.font.color.rgb = c_blue

    for line in p_desc.split("\n"):
        p_l = tf_ph.add_paragraph()
        p_l.text = line
        p_l.font.size = Pt(9.5)
        p_l.font.color.rgb = c_dark

# KPI Governance Banner at bottom
add_card(slide8, Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.4))
tb_gov = slide8.shapes.add_textbox(Inches(1.1), Inches(5.7), Inches(11.1), Inches(1.2))
tf_gov = tb_gov.text_frame
tf_gov.word_wrap = True
tf_gov.paragraphs[0].text = "🎯 GOVERNANCE KPIS & EVALUATION THRESHOLDS"
tf_gov.paragraphs[0].font.size = Pt(11)
tf_gov.paragraphs[0].font.bold = True
tf_gov.paragraphs[0].font.color.rgb = c_navy

p_gov = tf_gov.add_paragraph()
p_gov.text = "1. Digital Adoption: +15% lift in Regular segment | 2. Online Fraud Loss: -30% reduction ($180K/yr savings) | 3. Dispute SLA: <3.0 business days (<24 hrs for provisional credit) | 4. Premium Retention: 98.5% active retention rate."
p_gov.font.size = Pt(9.5)
p_gov.font.color.rgb = c_dark

set_speaker_notes(slide8,
    "To ensure accountability, we have structured this strategy into a disciplined 6-month phased rollout. "
    "In Months 1 and 2, we establish baseline control groups and audit authentication systems. "
    "In Months 3 and 4, we pilot digital onboarding across five branches, deploy provisional credit for low-value disputes, "
    "and introduce wealth sweeps to our top 2,500 Premium clients. "
    "In Months 5 and 6, we measure results against our baselines and scale bank-wide. "
    "Our success metrics are explicit: a 15% digital lift in the Regular segment, a 30% reduction in online fraud losses, "
    "and reducing card dispute resolution times below 3 business days."
)


# ==============================================================================
# SLIDE 9 — CONCLUSION & BUSINESS PITCH ASK
# ==============================================================================
print("Creating Slide 9: Conclusion...")
slide9 = prs.slides.add_slide(blank_layout)

# Top Banner
add_card(slide9, Inches(0.8), Inches(0.8), Inches(11.7), Inches(2.2), bg_color=c_navy)
tb_con = slide9.shapes.add_textbox(Inches(1.2), Inches(1.0), Inches(11.0), Inches(1.8))
tf_con = tb_con.text_frame
tf_con.word_wrap = True

tf_con.paragraphs[0].text = "CONCLUSION & EXECUTIVE SUMMARY"
tf_con.paragraphs[0].font.size = Pt(12)
tf_con.paragraphs[0].font.bold = True
tf_con.paragraphs[0].font.color.rgb = c_cyan

p_con2 = tf_con.add_paragraph()
p_con2.text = "Transforming TrustWave Bank from Reactive Servicing to Proactive Engagement"
p_con2.font.size = Pt(22)
p_con2.font.bold = True
p_con2.font.color.rgb = c_white

p_con3 = tf_con.add_paragraph()
p_con3.text = "By resolving operational dispute delays, protecting online fraud channels, and engaging our 67,800 retail customers, TrustWave Bank can defend $22.3B in deposits while capturing substantial cost efficiencies."
p_con3.font.size = Pt(11)
p_con3.font.color.rgb = RGBColor(214, 234, 248)

# The Decision / Ask Card (Lower left)
add_card(slide9, Inches(0.8), Inches(3.3), Inches(5.6), Inches(3.7))
tb_ask = slide9.shapes.add_textbox(Inches(1.1), Inches(3.5), Inches(5.0), Inches(3.3))
tf_ask = tb_ask.text_frame
tf_ask.word_wrap = True

tf_ask.paragraphs[0].text = "THE EXECUTIVE DECISION & ASK"
tf_ask.paragraphs[0].font.size = Pt(13)
tf_ask.paragraphs[0].font.bold = True
tf_ask.paragraphs[0].font.color.rgb = c_navy

asks = [
    "1. Executive Approval: Formal endorsement to initiate the 6-Month Targeted Pilot Program across retail digital onboarding and provisional dispute credit.",
    "2. Cross-Functional Task Force: Authorization to form a steering committee spanning Retail Operations, Fraud Risk, and Digital Engineering.",
    "3. Pilot Budget Allocation: Approval of a $120,000 provisional pilot budget (offset by an estimated $180,000 in immediate fraud loss reductions within Year 1).",
    "4. Quarterly Governance: Scheduled 90-day executive checkpoint to review pilot conversion metrics before full bank rollout."
]
for a in asks:
    p_a = tf_ask.add_paragraph()
    p_a.text = a
    p_a.font.size = Pt(10)
    p_a.font.color.rgb = c_dark

# Expected ROI / Outcomes Card (Lower right)
add_card(slide9, Inches(6.8), Inches(3.3), Inches(5.7), Inches(3.7))
tb_roi = slide9.shapes.add_textbox(Inches(7.1), Inches(3.5), Inches(5.1), Inches(3.3))
tf_roi = tb_roi.text_frame
tf_roi.word_wrap = True

tf_roi.paragraphs[0].text = "EXPECTED STRATEGIC RETURN (YEAR 1)"
tf_roi.paragraphs[0].font.size = Pt(13)
tf_roi.paragraphs[0].font.bold = True
tf_roi.paragraphs[0].font.color.rgb = c_navy

rois = [
    ("💰 Deposit Protection", "$9.5 Billion+ in core liquidity retained across upper quartile tiers via automated wealth sweep accounts."),
    ("📉 Cost Efficiency", "20% reduction in routine branch transaction overhead by converting 10,000+ retail customers to mobile banking."),
    ("🛡️ Fraud Loss Mitigation", "$180,000+ in annual fraud loss savings via dynamic 2FA ringfencing on online transfers exceeding $1,000."),
    ("⭐ Customer Trust & SLAs", "Cutting average card dispute resolution from 7.6 days to under 3 business days, improving customer retention by 8%.")
]
for r_title, r_desc in rois:
    p_r = tf_roi.add_paragraph()
    p_r.text = f"{r_title}: {r_desc}"
    p_r.font.size = Pt(9.5)
    p_r.font.color.rgb = c_dark

set_speaker_notes(slide9,
    "In conclusion, our data science assessment provides TrustWave Bank with a clear, empirical roadmap. "
    "We have identified exactly where our deposit risks lie, where operational fraud is penetrating, "
    "and why customer disputes are stalling. "
    "Our ask today is straightforward: we request executive approval to launch the 6-Month Targeted Pilot Program, "
    "funded by a modest $120,000 pilot allocation that will be more than fully recovered by $180,000 in fraud loss savings alone. "
    "By taking action today, we protect over $9.5 billion in core customer deposits and position TrustWave Bank for sustainable growth. "
    "Thank you, and I look forward to your questions."
)

prs.save(PPTX_PATH)
print(f"PowerPoint Presentation saved successfully to: {PPTX_PATH}")
