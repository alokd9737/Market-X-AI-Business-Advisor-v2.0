import streamlit as st


class ResponseFormatter:

    @staticmethod
    def executive_summary():

        st.markdown(
            """
## Executive Recommendation
"""
        )

    @staticmethod
    def consulting_note():

        st.info(
            """
Recommendations are generated using the Market X Consulting Framework and should be validated through commercial due diligence and market research.
"""
        )

    @staticmethod
    def show_sources(files):

        if not files:

            return

        with st.expander("Knowledge Sources Used"):

            for f in files:

                st.write("•", f)
