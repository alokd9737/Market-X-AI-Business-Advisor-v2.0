import streamlit as st

from streamlit_option_menu import option_menu


def render_sidebar():

    with st.sidebar:

        st.markdown("## Navigation")

        selected = option_menu(
            menu_title=None,
            options=[
                "Home",
                "Executive Advisor",
                "Growth Assessment",
                "Solutions",
                "Consultation",
            ],
            icons=[
                "house",
                "robot",
                "graph-up-arrow",
                "briefcase",
                "telephone",
            ],
            default_index=0,
        )

        st.divider()

        st.markdown(
            """
### Why Market X?

✔ Strategy

✔ Execution

✔ Route-to-Market

✔ Market Research

✔ Business Growth

✔ Government Advisory
"""
        )

        return selected
