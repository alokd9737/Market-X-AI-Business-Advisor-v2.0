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

st.info(
    "This is the initial shell of Market X AI Business Advisor v2.0. Advisor modules will be connected in the next steps."
)

render_footer()
