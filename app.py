import streamlit as st
from datetime import datetime, timedelta

from function.read_data import getDailyVaxMalaysia

datenow = datetime.now()
defaultvalue = datetime.now() - timedelta(weeks=4)

st.set_page_config(
    page_title="#VaksinMalaysia",
    layout="wide",
    page_icon=":memo:",
    initial_sidebar_state="expanded",
)

st.title("#VaksinMalaysia")
st.markdown(
    ":link: where i get this data? [check by yourself](https://github.com/CITF-Malaysia/citf-public/tree/main/vaccination)"
)

st.markdown("""---""")

st.title("Daily Dose")
start_time = st.slider(
    "",
    min_value=datetime(2021, 2, 24),
    max_value=datetime(datenow.year, datenow.month, datenow.day),
    value=datetime(defaultvalue.year, defaultvalue.month, defaultvalue.day),
    format="DD-MM-YYYY",
)

st.markdown(
    ":calendar: you have choose data from **{}**".format(str(start_time).split(" ")[0])
)
getDailyVaxMalaysia(start_time)
st.markdown("""---""")
