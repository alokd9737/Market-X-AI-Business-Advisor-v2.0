import streamlit as st

from services.readiness import ReadinessEngine

from components.page_title import page_title


QUESTIONS = [

"Business Strategy",

"Sales Capability",

"Distribution Strength",

"Marketing Effectiveness",

"Financial Management",

"Operations",

"Leadership",

"Technology Adoption",

"Customer Understanding",

"Innovation"

]


def render():

    page_title(

        "Growth Assessment",

        "Evaluate your organization's growth readiness."

    )

    scores = []

    st.markdown("### Rate each capability")

    for q in QUESTIONS:

        score = st.slider(

            q,

            1,

            10,

            5

        )

        scores.append(score*10)

    if st.button(

        "Generate Assessment",

        type="primary"

    ):

        result = ReadinessEngine.calculate(scores)

        st.success(

            f"Growth Readiness Score : {result.score}/100"

        )

        st.progress(result.score/100)

        c1,c2,c3 = st.columns(3)

        with c1:

            st.metric(

                "Readiness",

                result.maturity

            )

        with c2:

            st.metric(

                "Overall Score",

                result.score

            )

        with c3:

            st.metric(

                "Consulting View",

                "Expansion Ready" if result.score>70 else "Needs Improvement"

            )

        st.markdown("### Recommendations")

        for r in result.recommendations:

            st.write("✅",r)
