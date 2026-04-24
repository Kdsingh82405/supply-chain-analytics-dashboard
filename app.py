import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="APL Logistics Dashboard", layout="wide")

st.markdown("""
<style>

/* =================================================
   PAGE BACKGROUND + WIDTH
================================================= */
.stApp{
    background:linear-gradient(135deg,#f8fafc,#eef2ff,#ffffff);
}

.block-container{
    max-width:1550px;
    padding-top:2rem;
    padding-left:1.25rem;
    padding-right:1.25rem;
}

/* =================================================
   TITLE
================================================= */
h1{
    font-size:2.3rem !important;
    font-weight:800 !important;
    color:#0f172a !important;
    line-height:1.10 !important;
    margin-bottom:8px !important;
    padding-bottom: 0.3rem !important;
    letter-spacing:-1px;
    text-shadow:0 2px 4px rgba(0,0,0,0.18);
    text-align:center !important;

}

/* =================================================
   FINAL SIDEBAR CORPORATE PREMIUM
================================================= */

section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#0b1220,#172554,#1e3a8a);
    border-right:1px solid rgba(255,255,255,.08);
    width:340px !important;
}

/* Sidebar container */
section[data-testid="stSidebar"] .block-container{
    padding-top:0.75rem !important;
    padding-left:1rem !important;
    padding-right:1rem !important;
    padding-bottom:0.4rem !important;
}

/* All text */
section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Headings */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    font-size:1.35rem !important;
    font-weight:800 !important;
    letter-spacing:.2px;
}

/* Labels */
section[data-testid="stSidebar"] label{
    font-size:14px !important;
    font-weight:700 !important;
    margin-bottom:4px !important;
}

/* ==========================================
   INPUTS / SELECT BOXES
========================================== */
section[data-testid="stSidebar"] div[data-baseweb="select"] > div,
section[data-testid="stSidebar"] div[data-baseweb="base-input"] > div{
    background:rgba(255,255,255,.08) !important;
    border:1px solid rgba(255,255,255,.14) !important;
    border-radius:14px !important;
    min-height:48px !important;
    transition:all .25s ease;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover{
    border-color:rgba(255,255,255,.28) !important;
    background:rgba(255,255,255,.10) !important;
}

/* ==========================================
   MULTISELECT TAGS
========================================== */
section[data-testid="stSidebar"] span[data-baseweb="tag"]{
    background:linear-gradient(135deg,#3558ff,#4f46e5) !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    font-weight:600 !important;
    padding:3px 8px !important;
}

/* ==========================================
   RESET BUTTON
========================================== */

section[data-testid="stSidebar"] button[kind="primary"]{
    background:linear-gradient(135deg,#ef4444,#dc2626,#b91c1c) !important;
    color:white !important;
    border:none !important;
    border-radius:12px !important;

    height:35px !important;
    min-height:40px !important;
    padding:0 14px !important;

    font-size:16px !important;
    font-weight:700 !important;

    box-shadow:0 8px 18px rgba(239,68,68,.18);
    transition:all .25s ease;
}
section[data-testid="stSidebar"] button[kind="primary"]:hover{
    transform:translateY(-2px);
    background:linear-gradient(135deg,#dc2626,#b91c1c) !important;
    box-shadow:0 14px 28px rgba(239,68,68,.30);
}

section[data-testid="stSidebar"] button[kind="primary"]:active{
    transform:scale(.98);
}

/* Normal buttons */
section[data-testid="stSidebar"] button{
    border-radius:10px !important;
    font-weight:700 !important;
}

/* ==========================================
   SLIDER
========================================== */
section[data-testid="stSidebar"] .stSlider{
    margin-top:0.20rem !important;
    margin-bottom:0.20rem !important;
}

section[data-testid="stSidebar"] .stSlider label{
    margin-bottom:12px !important;
}

section[data-testid="stSidebar"] [role="slider"]{
    background:#ffffff !important;
    border:3px solid #2563eb !important;
    width:16px !important;
    height:16px !important;
    box-shadow:0 0 0 4px rgba(37,99,235,.18);
}

section[data-testid="stSidebar"] .stSlider span,
section[data-testid="stSidebar"] .stSlider div{
    color:white !important;
    font-size:13px !important;
    font-weight:700 !important;
}

/* ==========================================
   DIVIDER
========================================== */
section[data-testid="stSidebar"] hr{
    margin:0.55rem 0 0.65rem 0 !important;
    border:none !important;
    height:1px !important;
    background:rgba(255,255,255,.14) !important;
}

/* ==========================================
   SPACING
========================================== */
section[data-testid="stSidebar"] .element-container{
    margin-bottom:0.55rem !important;
}

section[data-testid="stSidebar"] [data-testid="stVerticalBlock"]{
    gap:0.30rem !important;
}

/* Caption */
section[data-testid="stSidebar"] .stCaption{
    color:rgba(255,255,255,.72) !important;
    font-size:12px !important;
}
            
/* KPI Card */
.kpi-card{
    background:linear-gradient(135deg,#0f172a,#1e293b,#1e3a8a);
    border:1px solid rgba(255,255,255,.08);
    border-radius:18px;
    padding:12px 12px;
    height:118px;
    display:flex;
    flex-direction:column;
    justify-content:flex-start;
    padding-top:14px;
    align-items:center;
    text-align:center;
    position:relative;
    overflow:hidden;
    box-shadow:0 10px 22px rgba(15,23,42,.18);
    transition:all .25s ease;
}

/* glow circle */
.kpi-card::before{
    content:"";
    position:absolute;
    top:-28px;
    right:-28px;
    width:100%;
    height:4px;
    border-radius:50%;
    background:rgba(255,255,255,.05);
}

/* hover */
.kpi-card:hover{
    transform:translateY(-6px) scale(1.02);
    box-shadow:0 18px 35px rgba(37,99,235,.28);
}
/* =================================================
   KPI DISPLAY 
================================================= */         

/* KPI label */
.kpi-label{
    font-size:10px;
    font-weight:800;
    text-transform:uppercase;
    letter-spacing:.5px;
    color:#93c5fd;
    min-height:auto;
    margin-bottom:6px;
    line-height:1.1;
    overflow:hidden;
    white-space:normal;
    text-overflow:ellipsis;
}

/* KPI value */
.kpi-value{
    font-size:1.60rem;
    font-weight:900;
    color:#ffffff;
    line-height:1.05;
    margin-top:2px;
    text-align:center;
}


/* column spacing */
[data-testid="column"]{
    padding:0.18rem 0.26rem !important;
    box-shadow:0 6px 16px rgba(15,23,42,.12);
}
/* =====================================
   MINI KPI CARD
===================================== */

.mini-kpi-card{
    background:linear-gradient(135deg,#ffffff,#f8fafc);
    border:1px solid #e2e8f0;
    border-radius:14px;
    padding:14px 16px;
    min-height:95px;

    display:flex;
    flex-direction:column;
    justify-content:center;

    box-shadow:0 8px 18px rgba(15,23,42,.05);
}

.mini-kpi-label{
    font-size:13px;
    font-weight:700;
    color:#334155;
    margin-bottom:8px;
}

.mini-kpi-value{
    font-size:1.7rem;
    font-weight:900;
    color:#0f172a;
    line-height:1;
}
            
/* =================================================
   TABS PREMIUM (UPGRADED)
================================================= */

div[data-testid="stTabs"]{
    background:#ffffff;
    padding:6px 8px 0 8px;
    border-radius:14px;
    border:1px solid #e5e7eb;
    box-shadow:0 4px 14px rgba(15,23,42,.05);
    margin-bottom:10px;
}

/* Tabs row */
.stTabs [data-baseweb="tab-list"]{
    gap:4px !important;
    padding:0 !important;
    flex-wrap:nowrap !important;
}

/* Each tab */
.stTabs [data-baseweb="tab"]{
    background:#f8fafc !important;
    color:#334155 !important;

    padding:8px 14px !important;
    margin:0 !important;

    border-radius:10px 10px 0 0 !important;

    font-weight:600 !important;
    font-size:13px !important;

    min-width:auto !important;
    border:none !important;

    transition:all .25s ease;
}

/* Active tab */
.stTabs [data-baseweb="tab"][aria-selected="true"]{
    background:linear-gradient(135deg,#2563eb,#4f46e5) !important;
    color:white !important;
    box-shadow:0 6px 14px rgba(37,99,235,.22);
}

/* Hover */
.stTabs [data-baseweb="tab"]:hover{
    background:#eff6ff !important;
    color:#2563eb !important;
}
            
/* =================================================
   ALERTS
================================================= */
div[data-testid="stAlert"]{
    border-radius:14px;
}
/* =================================================
   PERFECT GAP BETWEEN KPI ROW AND TABS
================================================= */

div[data-testid="stHorizontalBlock"]{
    margin-bottom:0 !important;
    padding-bottom:0 !important;
}

div[data-testid="stTabs"]{
    margin-top:24px !important;
}
/* =================================================
   MOBILE
================================================= */
@media(max-width:900px){

h1{
    font-size:1.8rem !important;
}

div[data-testid="metric-container"]{
    min-height:110px;
}

div[data-testid="metric-container"] > div:nth-child(2){
    font-size:1.55rem !important;
}

}

</style>
""", unsafe_allow_html=True)
# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/APL_Logistics_Cleaned.csv", encoding='latin1')

with st.spinner("Loading Dashboard... Please wait"):
    df = load_data()

# -------------------------------
# CUSTOMER SEGMENT (SAFE)
# -------------------------------
customer_df = df.groupby(
    'Customer Id')['Order Profit Per Order'].sum().reset_index()

customer_df['Segment'] = pd.qcut(
    customer_df['Order Profit Per Order'],
    q=3,
    labels=['Low', 'Medium', 'High'],
    duplicates='drop'
)

df = df.merge(
    customer_df[['Customer Id', 'Segment']], 
    on='Customer Id', how='left')

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.header("🎛️ Dashboard Controls")
st.sidebar.caption("Refine dashboard results using filters below")

# Reset Button
if st.sidebar.button("🔄 Reset Filters", use_container_width=True, type="primary"):
    st.cache_data.clear()
    st.rerun()

st.sidebar.markdown("---")

# -------------------------------
# CUSTOMER SEGMENT
# -------------------------------
segment = st.sidebar.multiselect(
    "Customer Segment",
    sorted(df["Segment"].dropna().unique()),
    default=list(df["Segment"].dropna().unique()),
    placeholder="Select Segment"
)

# -------------------------------
# CATEGORY
# -------------------------------
category = st.sidebar.multiselect(
    "Category",
    sorted(df["Category Name"].dropna().unique()),
    placeholder="Select Category"
)

if not category:
    category = df["Category Name"].dropna().unique()

# -------------------------------
# PRODUCT
# -------------------------------
product = st.sidebar.multiselect(
    "Product",
    sorted(df["Product Name"].dropna().unique())[:300],
    placeholder="Select Product"
)

if not product:
    product = df["Product Name"].dropna().unique()

# -------------------------------
# ORDER REGION
# -------------------------------
region = st.sidebar.multiselect(
    "Order Region",
    sorted(df["Order Region"].dropna().unique()),
    placeholder="Select Region"
)

if not region:
    region = df["Order Region"].dropna().unique()

# -------------------------------
# MARKET
# -------------------------------
market = st.sidebar.multiselect(
    "Market",
    sorted(df["Market"].dropna().unique()),
    placeholder="Select Market"
)

if not market:
    market = df["Market"].dropna().unique()

# -------------------------------
# SHIPPING MODE
# -------------------------------
ship = st.sidebar.multiselect(
    "Shipping Mode",
    sorted(df["Shipping Mode"].dropna().unique()),
    placeholder="Select Shipping Mode"
)

if not ship:
    ship = df["Shipping Mode"].dropna().unique()

st.sidebar.markdown("---")

# -------------------------------
# DISCOUNT SLIDER
# -------------------------------
discount_min = float(df["Order Item Discount Rate"].min())
discount_max = float(df["Order Item Discount Rate"].max())

discount_range = st.sidebar.slider(
    "Discount Rate",
    discount_min,
    discount_max,
    (discount_min, discount_max)
)

# -------------------------------
# APPLY FILTERS (SAFE)
# -------------------------------
filtered_df = df[
    (df['Segment'].isin(segment)) &
    (df['Category Name'].isin(category)) &
    (df['Product Name'].isin(product)) &
    (df['Order Region'].isin(region)) &
    (df['Market'].isin(market)) &
    (df["Shipping Mode"].isin(ship)) &
    (df['Order Item Discount Rate'].between(discount_range[0], discount_range[1]))
]

if filtered_df.empty:
    st.warning("❌ No matching records found. Please change filters.")
    st.stop()
# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("📊 Customer, Product, and Profitability Performance Analysis in Supply Chain Operations")
st.caption(f"Last Updated: {datetime.now().strftime('%d %b %Y | %I:%M %p')}")
# ==========================================================
# KPI CALCULATION SECTION
# ==========================================================

total_revenue = filtered_df['Sales'].sum()
total_profit = filtered_df['Order Profit Per Order'].sum()

profit_margin = (total_profit / total_revenue * 100) if total_revenue != 0 else 0

customer_value = filtered_df.groupby('Customer Id')['Order Profit Per Order'].sum().mean()

category_margin = filtered_df.groupby('Category Name').apply(
    lambda x: (
        (x['Order Profit Per Order'].sum() / x['Sales'].sum()) * 100
        if x['Sales'].sum() != 0 else 0
    )
).mean()

discount_impact = (
    filtered_df['Order Item Discount'].sum() / total_revenue
) * 100 if total_revenue != 0 else 0

total_orders = len(filtered_df)

# ---------------------------------------------------
# KPI DISPLAY 
# ---------------------------------------------------

cols = st.columns(6)

kpis = [
    ("💰","Total Revenue",f"{total_revenue/1e6:.2f}M"),
    ("📈","Total Profit",f"{total_profit/1e6:.2f}M"),
    ("📊","Profit Margin %",f"{profit_margin:.2f}%"),
    ("👥","Customer Value Index",f"{customer_value:.2f}"),
    ("🏷️","Category Margin",f"{category_margin:.2f}%"),
    ("🎯","Discount Impact Ratio",f"{discount_impact:.2f}%")
]

for col,(icon,label,val) in zip(cols,kpis):
    with col:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-badge">{icon}</div>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{val}</div>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# TABS
# -------------------------------
tab1, tab2, tab3, tab4, tab5= st.tabs([
    "Revenue & Profit Overview",
    "Product & Category Performance",
    "Customer Value Dashboard",
    "Discount & Regional Analysis",
    "Supply Chain"
])
# =====================================================
# TAB 1 : REVENUE & PROFIT OVERVIEW
# =====================================================

with tab1:
    st.subheader("📊 Revenue & Profit Overview")

    # ---------------------------------
    # REVENUE VS PROFIT CHART
    # ---------------------------------

    chart_df = pd.DataFrame({
        "Metric": ["Revenue", "Profit"],
        "Value": [
            total_revenue / 1e6,
            total_profit / 1e6
        ]
    })

    fig = px.bar(
        chart_df,
        x="Metric",
        y="Value",
        text="Value",
        color="Metric",
        color_discrete_map={
            "Revenue": "#2563eb",
            "Profit": "#60a5fa" 
        },

        title="Revenue vs Profit Comparison"
    )

    fig.update_traces(
        texttemplate='%{text:.2f}M',
        textposition='outside',
        marker_line_width=0,
        hovertemplate="<b>%{x}</b><br>$ %{y:.2f} Million<extra></extra>"
    )
    fig.update_layout(
        height=500,
        xaxis_title="",
        yaxis_title="Million ($)",
        showlegend=False,
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(
            size=14,
            color="#334155",
        ),
        xaxis=dict(
            showgrid=False
        ),
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.success("Insight: Revenue is high, but profit margin must improve.")
    st.divider()
    
    # ---------------------------------
    # MARGIN TREND CHART
    # ---------------------------------

    market_margin = filtered_df.groupby(
        "Market"
    ).apply(
        lambda x: (
            x["Order Profit Per Order"].sum() /
            x["Sales"].sum()
        ) * 100
    ).reset_index(name="Margin %")

    fig = px.line(
        market_margin,
        x="Market",
        y="Margin %",
        text="Margin %",
        title="📈 Margin Trend by Market",
        color_discrete_sequence=["seagreen"],
        markers=True
    )

    fig.update_layout(
        height=500,
        xaxis_title="Market Region",
        yaxis_title="Profit Margin (%)"
    )
    fig.update_traces(
        line=dict(
            color="#16a34a",
            width=3,
            shape="spline"
        ),

        marker=dict(
            size=9,
            color="#16a34a",
            line=dict(width=2, color="white")
        ),

        texttemplate="%{text:.2f}%",
        textposition="top center",
        textfont=dict(
            size=12,
            color="#0f172a"
        ),
        cliponaxis=False
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("Insight: Profit margins vary across markets, showing stronger and weaker business zones.")
    # -------------------------------
    # DOWNLOAD Filtered_Data
    # -------------------------------
    csv = filtered_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 Download Filtered Data",
        data=csv,
        file_name="APL_Filtered_Data.csv",
        mime="text/csv"
    )
# =====================================================
# TAB 2 :
# =====================================================
with tab2:

    st.subheader("📦 Category Profitability")

    category_df = filtered_df.groupby('Category Name').agg({
        'Sales': 'sum',
        'Order Profit Per Order': 'sum'
    }).reset_index()

    category_df['Margin %'] = (
        category_df['Order Profit Per Order'] / category_df['Sales'] * 100
    )

    top_cat = category_df.sort_values(
        by='Margin %',
        ascending=False
    ).head(10)

    fig = px.bar(
        top_cat,
        x="Margin %",
        y="Category Name",
        orientation="h",
        text="Margin %",
        title="Top Category Profitability"
    )

    fig.update_traces(texttemplate='%{text:.2f}%', textposition='inside')
    fig.update_layout(
        height=500,
        yaxis=dict(autorange="reversed")
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        "Insight: Focus on categories with strong margins."
    )

    st.divider()

# ------------------- "🏷️ Product-Level Margin" -----------------------------------

    product_df = filtered_df.groupby('Product Name').agg({
        'Sales': 'sum',
        'Order Profit Per Order': 'sum'
    }).reset_index()

    product_df['Margin %'] = (
        product_df['Order Profit Per Order'] / product_df['Sales'] * 100
    )

    top_products = product_df.sort_values(
        by='Margin %',
        ascending=False
    ).head(10)

    # Short product names
    top_products['Product Name'] = (
        top_products['Product Name'].str[:32]
    )

    fig = px.bar(
        top_products,
        x="Margin %",
        y="Product Name",
        orientation="h",
        text="Margin %",
        title="🏷️ Product-Level Margin"
    )

    fig.update_traces(
        texttemplate='%{text:.2f}%',
        textposition='inside'
    )

    fig.update_layout(
        height=500,
        yaxis={'categoryorder':'total ascending'}
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        "Insight: High-margin products deserve priority promotion."
    )

    st.divider()
# ----------------- Category Profitability Heatmap --------------------------

    heatmap_df = filtered_df.pivot_table(
        values='Order Profit Per Order',
        index='Category Name',
        columns='Market',
        aggfunc='sum'
    )

    heatmap_df = heatmap_df.sort_values(
        by=heatmap_df.columns[0],
        ascending=False
    ).head(15)

    fig = px.imshow(
        heatmap_df,
        text_auto=True,
        aspect="auto",
        title="🔥 Category Profitability Heatmap",
        color_continuous_scale="RdBu"
    )

    fig.update_layout(height=500)

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        "Insight: Compare profitability across markets and categories."
    )

    st.divider()

# =====================================================
# TAB 3 : CUSTOMER VALUE DASHBOARD
# =====================================================
with tab3:

    cust = filtered_df.groupby(
        'Customer Id'
    )['Order Profit Per Order'].sum().reset_index()

    col1, col2 = st.columns(2)

    # -------------------------------------------------
    # TOP 10 CUSTOMERS
    # -------------------------------------------------
    with col1:

        st.markdown("### 🔝 Top 10 Customers")

        top = cust.sort_values(
            by="Order Profit Per Order",
            ascending=False
        ).head(10)

        top["Customer_Label"] = "C-" + top["Customer Id"].astype(str)

        fig = px.bar(
            top.sort_values("Order Profit Per Order"),
            x="Order Profit Per Order",
            y="Customer_Label",
            orientation="h",
            text="Order Profit Per Order",
            title="Most Profitable Customers",
            color_discrete_sequence=["seagreen"]
        )

        fig.update_traces(
            texttemplate='%{text:.0f}',
            textposition='inside',
            textfont_color='white'
        )

        fig.update_layout(
            height=500,
            margin=dict(l=20, r=80, t=30, b=20),
            yaxis_title="Customer",
            xaxis_title="Profit",
            yaxis=dict(type="category")
            
        )

        st.plotly_chart(fig, use_container_width=True)

    # -------------------------------------------------
    # BOTTOM 10 CUSTOMERS
    # -------------------------------------------------
    with col2:

        st.markdown("### 🔻 Bottom 10 Customers")

        bottom = cust.sort_values(
            by="Order Profit Per Order",
            ascending=True
        ).head(10)

        bottom["Customer_Label"] = "C-" + bottom["Customer Id"].astype(str)

        fig = px.bar(
            bottom.sort_values("Order Profit Per Order", ascending=False),
            x="Order Profit Per Order",
            y="Customer_Label",
            orientation="h",
            text="Order Profit Per Order",
            title="Highest Loss Customers",
            color_discrete_sequence=["crimson"]
        )

        fig.update_traces(
            texttemplate='%{text:.0f}',
            textposition='inside',
            textfont_color='white'
        )

        fig.update_layout(
            height=500,
            margin=dict(l=20, r=80, t=30, b=20),
            yaxis_title="Customer",
            xaxis_title="Loss / Profit",
            yaxis=dict(type="category")
        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

    # -------------------------------------------------
    # CUSTOMER SEGMENT PIE CHART
    # -------------------------------------------------

    seg_df = filtered_df["Segment"].value_counts().reset_index()
    seg_df.columns = ["Segment", "Count"]

    fig = px.pie(
        seg_df,
        names="Segment",
        values="Count",
        hole=0.35,
        title="🥧 Customer Segment Distribution",
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.success(
        "Insight: High-value customer retention drives profitability."
    )
# =====================================================
# TAB 4 : DISCOUNT & REGIONAL ANALYSIS
# =====================================================
with tab4:
    # ---------------------------------
    # Discount vs Margin Visualization
    # ---------------------------------
    st.subheader("📉 Discount vs Margin Visualization")

    disc_df = filtered_df.groupby(
        "Order Item Discount Rate"
    )["Order Item Profit Ratio"].mean().reset_index()

    fig = px.line(
        disc_df,
        x="Order Item Discount Rate",
        y="Order Item Profit Ratio",
        markers=True,
        title="Average Profit Margin by Discount Level"
    )

    fig.update_traces(line_width=3)
    fig.update_yaxes(
        tickformat=".1%",
        range=[0.10, 0.14]
    )

    fig.update_layout(
        height=500,
        xaxis_title="Discount Rate",
        yaxis_title="Average Profit Margin"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.success("Insight: Profit margin remains stable near 12%, with weaker margins around 3% and 20% discount levels.")
    st.divider()
    # ---------------------------------
    # WHAT IF SCENARIO
    # ---------------------------------
    st.subheader("🧮 What-if Discount Scenario")

    discount_input = st.slider(
        "Select Discount %",
        min_value=0,
        max_value=50,
        value=10,
        step=1,
        format="%d%%"
    ) / 100

    simulated_revenue = (
        filtered_df["Sales"] * (1 - discount_input)
    ).sum()

    simulated_profit = (
        filtered_df["Order Profit Per Order"] * (1 - discount_input)
    ).sum()

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="mini-kpi-card">
            <div class="mini-kpi-label">💰 Estimated Revenue</div>
            <div class="mini-kpi-value">{simulated_revenue/1e6:.2f}M</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="mini-kpi-card">
            <div class="mini-kpi-label">📈 Estimated Profit</div>
            <div class="mini-kpi-value">{simulated_profit/1e6:.2f}M</div>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        f"Scenario Applied: {discount_input:.0%} discount across selected data."
    )
    st.divider()

    # ---------------------------------
    # REGIONAL PROFIT
    # ---------------------------------
    st.subheader("🌍 Top Regions by Profit")

    region_df = filtered_df.groupby(
        "Order Region"
    )["Order Profit Per Order"].sum().reset_index()

    top_regions = region_df.sort_values(
        by="Order Profit Per Order",
        ascending=False
    ).head(10)

    top_regions["Profit_K"] = (
        top_regions["Order Profit Per Order"] / 1000
    )

    fig = px.bar(
        top_regions.sort_values("Profit_K"),
        x="Profit_K",
        y="Order Region",
        orientation="h",
        text="Profit_K",
        title="Regional Profitability"
    )

    fig.update_traces(
        texttemplate='%{text:.0f}K',
        textposition='inside'
    )

    fig.update_layout(
        height=500,
        xaxis_title="Profit (K)",
        yaxis_title="Order Region"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        "Insight: Focus on high-profit regions and optimize weak zones."
    )
    st.divider()
    # ---------------------------------
    # DISCOUNT IMPACT
    # ---------------------------------
    st.subheader("📉 Discount Impact Analysis")

    fig = px.box(
        filtered_df,
        x="Order Item Discount Rate",
        y="Order Item Profit Ratio",
        points="outliers",
        title="Discount Rate vs Profit Ratio Distribution"
    )

    fig.update_layout(
        height=500,
        xaxis_title="Discount Rate",
        yaxis_title="Profit Ratio"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        "Insight: Higher discounts may reduce profitability."
    )

    st.divider()

# =====================================================
# TAB 5 : SUPPLY CHAIN
# =====================================================
with tab5:

    # ---------------------------------
    # SHIPPING PERFORMANCE
    # ---------------------------------
    st.subheader("🚚 Shipping Performance")

    shipping_avg = filtered_df[
        [
            "Days for shipping (real)",
            "Days for shipment (scheduled)"
        ]
    ].mean().reset_index()

    shipping_avg.columns = ["Type", "Days"]

    shipping_avg["Type"] = [
        "Actual Shipping Days",
        "Scheduled Shipping Days"
    ]

    fig = px.bar(
        shipping_avg,
        x="Type",
        y="Days",
        text="Days",
        color="Type",
        title="Average Shipping Time Comparison"
    )

    fig.update_traces(
        texttemplate='%{text:.1f}',
        textposition='outside',
        textfont=dict(
            size=13,
            color="#334155"
        )
    )

    fig.update_layout(
        height=500,
        yaxis_title="Average Days",
        xaxis_title="",
        showlegend=False,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig, use_container_width=True)

    delay = shipping_avg["Days"].iloc[0] - shipping_avg["Days"].iloc[1]

    st.success(
        f"Insight: Actual shipping is slower by {delay:.1f} days on average."
    )

    st.divider()

    # ---------------------------------
    # SHIPPING MODE PROFITABILITY
    # ---------------------------------

    ship_profit = filtered_df.groupby(
        "Shipping Mode"
    )["Order Profit Per Order"].sum().reset_index()

    fig = px.bar(
        ship_profit.sort_values("Order Profit Per Order", ascending=False),
        x="Shipping Mode",
        y="Order Profit Per Order",
        text="Order Profit Per Order",
        title="💰 Shipping Mode Profitability"
    )

    fig.update_traces(
        texttemplate='%{text:,.0f}',
        textposition='outside',
        textfont=dict(
            size=13,
            color="#334155"
        )
    )

    fig.update_layout(
        height=500,
        xaxis_title="Shipping Mode",
        yaxis_title="Total Profit",
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    best_mode = ship_profit.sort_values(
        "Order Profit Per Order",
        ascending=False
    ).iloc[0]["Shipping Mode"]

    st.success(
        f"Insight: {best_mode} is currently the most profitable shipping mode."
    )

st.markdown("""
<div style='
background:linear-gradient(135deg,#0f172a,#1e293b,#2563eb);
padding:10px 14px;
border-radius:12px;
text-align:center;
margin-top:8px;
box-shadow:0 8px 18px rgba(15,23,42,.14);
'>

<div style='
font-size:16px;
font-weight:800;
color:white;
margin-bottom:3px;
line-height:1.2;
'>
🚀 Developed by Kundan Kumar Singh
</div>

<div style='
font-size:12px;
color:#cbd5e1;
margin-bottom:4px;
line-height:1.2;
'>
Internship Project 2026 | APL Logistics Profitability Dashboard
</div>

<div style='
font-size:11px;
color:#93c5fd;
line-height:1.2;
'>
Built with Python • Streamlit • Plotly • Pandas
</div>

</div>
""", unsafe_allow_html=True)