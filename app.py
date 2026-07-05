import streamlit as st

from config import (
    APP_NAME,
    APP_ICON,
)

from styles import load_css

from components.header import render_header
from components.sidebar import render_sidebar
from components.footer import render_footer

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------
# LOAD STYLES
# ----------------------------------------

load_css()

# ----------------------------------------
# HEADER
# ----------------------------------------

render_header()

# ----------------------------------------
# SIDEBAR
# ----------------------------------------

selected_page = render_sidebar()

if selected_page == "Dashboard":

    st.info(
        "Welcome to Market X AI Business Advisor"
    )

elif selected_page == "AI Strategy Advisor":

    from pages.advisor import render

    render()

elif selected_page=="Growth Assessment":

    from pages.diagnostic import render

    render()

elif selected_page == "Solutions":

    st.info(
        "Coming soon..."
    )

elif selected_page == "Contact Market X":

    st.info(
        "Coming soon..."
    )

render_footer()

# ----------------------------------------
# HOME PAGE (Temporary)
# ----------------------------------------

st.markdown(
    """
<div class="hero">

<div class="hero-title">
AI-Powered Business Growth Advisory
</div>

<div class="hero-sub">

Helping CXOs, founders and business leaders make better growth decisions through consulting-grade AI.

</div>

</div>
""",
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Consulting Areas", "6+")

with c2:
    st.metric("Industries", "FMCG | Dairy | Agriculture")

with c3:
    st.metric("Reports", "Executive Ready")

from components.kpi_cards import kpi_card

st.markdown("## Executive Dashboard")

c1,c2,c3,c4=st.columns(4)

with c1:
    kpi_card(
        "Industries",
        "12+"
    )

with c2:
    kpi_card(
        "Frameworks",
        "25+"
    )

with c3:
    kpi_card(
        "Assessments",
        "10"
    )

with c4:
    kpi_card(
        "AI Advisor",
        "Ready"
    )

st.markdown("---")

st.markdown(
"""
### Welcome to Market X AI Business Advisor

Generate consulting-grade recommendations,
assess business readiness,
prepare executive reports,
and identify growth opportunities.

Use the navigation panel to begin.
"""
)

render_footer()
