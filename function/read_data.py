import pandas as pd
import streamlit as st
pd.options.mode.chained_assignment = None


@st.cache
def data():
    url = "https://raw.githubusercontent.com/CITF-Malaysia/citf-public/main/vaccination/vax_malaysia.csv"
    df = pd.read_csv(url, index_col=0).reset_index()
    return df