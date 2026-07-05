import streamlit as st


def info_card(title, value, description):

    st.markdown(
        f"""
<div class="card">

<h4 style="margin-bottom:10px;color:#081C3A;">
{title}
</h4>

<h2 style="margin-top:0;color:#C7A64A;">
{value}
</h2>

<p style="color:#6B7280;">
{description}
</p>

</div>
""",
        unsafe_allow_html=True,
    )
