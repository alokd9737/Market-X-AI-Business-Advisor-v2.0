import streamlit as st


def kpi_card(title,value):

    st.markdown(

f"""

<div class="card">

<h4>{title}</h4>

<h1 style="color:#C7A64A;">{value}</h1>

</div>

""",

unsafe_allow_html=True

)
