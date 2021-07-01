import pandas as pd
import streamlit as st


@st.cache
def data():
    url = "https://raw.githubusercontent.com/CITF-Malaysia/citf-public/main/vaccination/vax_malaysia.csv"
    df = pd.read_csv(url, index_col=0).reset_index()

    return df


def getDailyVaxMalaysia(start_time):
    df = data()
    dosecum = df[["date", "dose1_daily", "dose2_daily"]]
    dosecum.rename(
        columns={"dose1_daily": "Dose 1", "dose2_daily": "Dose 2"}, inplace=True
    )
    dosecum["date"] = pd.to_datetime(dosecum["date"])
    dosecum = dosecum[dosecum["date"] >= str(start_time)]
    dosecum.set_index("date", inplace=True)

    st.line_chart(dosecum, use_container_width=True)
