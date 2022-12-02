import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.offline as py
import plotly.graph_objs as go
from function.read_data import data
pd.options.mode.chained_assignment = None


def getDailyVaxMalaysia(start_time):

    color1 = "#9467bd"
    color2 = "#D08B00"
    color3 = "#4181C8"

    df = data()
    dosecum = df[["date", "daily_full", "daily_booster",
                  "daily_booster2", "cumul_full", "cumul_booster", "cumul_booster2"]]
    dosecum.rename(
        columns={"daily_full": "Dose Full", "daily_booster": "Dose Booster 1", "daily_booster2": "Dose Booster 2", "cumul_full": "Cumul Dose Full", "cumul_booster": "Cumul Dose Booster 1", "cumul_booster2": "Cumul Dose Booster 2"}, inplace=True
    )
    dosecum["date"] = pd.to_datetime(dosecum["date"])
    dosecum['date'] += pd.to_timedelta(18, unit='h')
    dosecum = dosecum[dosecum["date"] >= str(start_time)]
    # dosecum["date"] = dosecum["date"].dt.date

    trace1 = go.Scatter(
        x=dosecum["date"], y=dosecum["Dose Full"], name="Dose Full", line=dict(color=color1)
    )
    trace2 = go.Scatter(
        x=dosecum["date"], y=dosecum["Dose Booster 1"], name="Dose Booster 1", line=dict(color=color2)
    )

    trace3 = go.Scatter(
        x=dosecum["date"], y=dosecum["Dose Booster 2"], name="Dose Booster 2", line=dict(color=color3)
    )

    data2 = [trace1, trace2, trace3]

    layout = go.Layout(yaxis=dict(title="Dose"))
    fig = go.Figure(data=data2, layout=layout)
    st.plotly_chart(fig, use_container_width=True)

    # cumulative
    dosecum["date"] = pd.to_datetime(dosecum["date"])
    dosecum['date'] += pd.to_timedelta(18, unit='h')
    dosecum = dosecum[dosecum["date"] >= str(start_time)]
    # dosecum["date"] = dosecum["date"].dt.date

    color1 = "#9467bd"
    color2 = "#D08B00"

    trace1 = go.Scatter(
        x=dosecum["date"], y=dosecum["Cumul Dose Full"], name="Cumul Dose Full", line=dict(color=color1)
    )
    trace2 = go.Scatter(
        x=dosecum["date"], y=dosecum["Cumul Dose Booster 1"], name="Cumul Dose Booster 1", line=dict(color=color2)
    )
    trace3 = go.Scatter(
        x=dosecum["date"], y=dosecum["Cumul Dose Booster 2"], name="Cumul Dose Booster 2", line=dict(color=color3)
    )
    data2 = [trace1, trace2, trace3]

    layout = go.Layout(yaxis=dict(title="Cumul Dose"))
    fig = go.Figure(data=data2, layout=layout)
    st.plotly_chart(fig, use_container_width=True)
