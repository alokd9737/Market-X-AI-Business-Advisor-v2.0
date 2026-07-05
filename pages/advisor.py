import streamlit as st

from services.advisor_service import AdvisorService

from services.response_formatter import ResponseFormatter

from components.page_title import page_title

from services.report_generator import PDFReport

import os


advisor = AdvisorService()


def render():

    page_title(
        "AI Strategy Advisor",
        "Generate board-level consulting recommendations."
    )

    industry = st.selectbox(

        "Industry",

        [

            "FMCG",

            "Dairy",

            "Agriculture",

            "Food Processing",

            "Manufacturing",

            "Retail",

            "Government",

            "Other"

        ]

    )

    geography = st.text_input(

        "Target Geography",

        placeholder="Example: Uttar Pradesh"

    )

    company = st.selectbox(

        "Company Size",

        [

            "Startup",

            "SME",

            "Mid-size",

            "Enterprise"

        ]

    )

    question = st.text_area(

        "Describe your business challenge",

        height=180,

        placeholder="""
Example:

We manufacture packaged food and want to expand into Bihar and Jharkhand.

How should we design our Route-to-Market strategy?
"""

    )

    if st.button(

        "Generate Executive Recommendation",

        type="primary"

    ):

        if not question.strip():

            st.warning(

                "Please enter your business challenge."

            )

            st.stop()

        with st.spinner(

            "Preparing consulting recommendation..."

        ):

            result = advisor.generate_advisory(

                question,

                industry,

                geography,

                company

            )

        ResponseFormatter.executive_summary()

        st.markdown(result["answer"])

        ResponseFormatter.show_sources(

            result["sources"]

        )

        ResponseFormatter.consulting_note()
