import streamlit as st


def page_title(title, subtitle):

    st.markdown(
        f"""
<div style="margin-bottom:25px;">

<h2 style="color:#081C3A;
font-size:34px;
font-weight:700;
margin-bottom:5px;">

{title}

</h2>

<p style="font-size:18px;
color:#6B7280;">

{subtitle}

</p>

</div>
""",
        unsafe_allow_html=True,
    )
