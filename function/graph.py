import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.offline as py
import plotly.graph_objs as go
from function.read_data import data


def getDailyVaxMalaysia(start_time):
    df = data()
    dosecum = df[["date", "dose1_daily", "dose2_daily"]]
    dosecum.rename(
        columns={"dose1_daily": "Dose 1", "dose2_daily": "Dose 2"}, inplace=True
    )
    dosecum["date"] = pd.to_datetime(dosecum["date"])
    dosecum['date'] +=  pd.to_timedelta(18, unit='h')
    dosecum = dosecum[dosecum["date"] >= str(start_time)]
    # dosecum["date"] = dosecum["date"].dt.date

    color1 = "#9467bd"
    color2 = "#D08B00"

    trace1 = go.Scatter(
        x=dosecum["date"], y=dosecum["Dose 1"], name="Dose 1", line=dict(color=color1)
    )
    trace2 = go.Scatter(
        x=dosecum["date"], y=dosecum["Dose 2"], name="Dose 2", line=dict(color=color2)
    )
    data2 = [trace1, trace2]

    layout = go.Layout(yaxis=dict(title="Dose"))
    fig = go.Figure(data=data2, layout=layout)
    st.plotly_chart(fig, use_container_width=True)
