import streamlit as st
from PIL import Image

def header(image=False):
    st.title("COVID-19 Vaccine Malaysia")
    st.markdown(
        ":link: [Dataset from MoH-Malaysia](https://github.com/CITF-Malaysia/citf-public/tree/main/vaccination)"
    )

    if image:
        image = Image.open('vaccine.jpeg')
        st.image(image, caption='Image from Unsplash', width=830)

def sidebar():
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

    # Using "with" notation
    with st.sidebar:
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )