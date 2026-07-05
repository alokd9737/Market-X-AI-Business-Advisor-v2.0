import plotly.graph_objects as go

import streamlit as st


def gauge(score):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={"text":"Growth Readiness"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"darkblue"}

            }

        )

    )

    st.plotly_chart(

        fig,

        use_container_width=True
    )

def radar(labels,values):

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=values,

            theta=labels,

            fill="toself"

        )

    )

    fig.update_layout(

        polar=dict(

            radialaxis=dict(

                visible=True,

                range=[0,100]

            )

        ),

        showlegend=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )
