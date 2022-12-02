import streamlit as st
from PIL import Image
from datetime import datetime, timedelta
import time
from function.components import header, sidebar
from function.graph import getDailyVaxMalaysia

datenow = datetime.now()



st.set_page_config(
    page_title="COVID-19 Vaccine Malaysia",
    layout="wide",
    page_icon=":chart_with_upwards_trend:",
    initial_sidebar_state="expanded",
)

header()

st.markdown("""---""")

today = datetime.today().strftime('%Y-%m-%d')
default_value = 1
defaultvalue = datetime.now() - timedelta(weeks=int(default_value))

my_expander = st.expander(
    label=f'Default filter show data for the latest {default_value} week')
with my_expander:

    start_time = st.slider(
        "",
        min_value=datetime(2021, 2, 24),
        max_value=datetime(datenow.year, datenow.month, datenow.day),
        value=datetime(defaultvalue.year,
                       defaultvalue.month, defaultvalue.day),
        format="DD-MM-YYYY",
    )

    st.markdown(
        ":calendar: you have choose data from **{}** until **{}**".format(
            str(start_time).split(" ")[0], today)
    )

getDailyVaxMalaysia(start_time)
st.markdown("""---""")
