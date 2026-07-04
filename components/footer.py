import streamlit as st

from config import COMPANY_WEBSITE


def render_footer():

    st.markdown("---")

    st.markdown(
        f"""
<div class="footer">

<b>Market X AI Business Advisor</b>

<br><br>

Strategy • Market Expansion • Distribution • Business Growth

<br><br>

{COMPANY_WEBSITE}

<br><br>

© 2026 Market X

</div>
""",
        unsafe_allow_html=True,
    )
