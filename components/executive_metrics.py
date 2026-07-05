import streamlit as st


def executive_metrics():

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Market Readiness", "82%")

    with c2:
        st.metric("Risk Level", "Medium")

    with c3:
        st.metric("Growth Potential", "High")

    with c4:
        st.metric("Execution", "Moderate")
