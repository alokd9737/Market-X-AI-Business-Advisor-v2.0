import streamlit as st


def show_sections(answer):

    sections = answer.split("#")

    for section in sections:

        if section.strip():

            title = section.split("\n")[0]

            body = "\n".join(section.split("\n")[1:])

            with st.expander(title, expanded=(title.lower() == "executive summary")):
                st.markdown(body)
