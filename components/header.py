import streamlit as st
import os

from config import (
    LOGO,
    COMPANY_NAME,
    APP_SUBTITLE,
)


def render_header():

    c1, c2 = st.columns([1, 5])

    with c1:

        if os.path.exists(LOGO):
            st.image(LOGO, width=120)

    with c2:

        st.markdown(
            f"""
<h1 style="margin-bottom:0;color:#081C3A;">
{COMPANY_NAME}
</h1>

<p style="font-size:22px;color:#6B7280;margin-top:-10px;">
{APP_SUBTITLE}
</p>
""",
            unsafe_allow_html=True,
        )

    st.divider()
