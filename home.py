import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json
import requests

#test
st.set_page_config(page_title="Ex-stream-ly Cool App",
                   page_icon="🧊",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   )


@st.cache
def load_lottie_file(filepath: str):
    with open(filepath) as f:
        return json.load(f)


@st.cache
def load_lottie_url(url: str):
    """Loads Lottie animation from URL"""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def home():
    lottie_coding = load_lottie_file("lottiefiles/programming-computer.json")
    lottie_hello = load_lottie_url("https://assets8.lottiefiles.com/packages/lf20_iVPQC8jyX2.json")

    with st.sidebar:
        # st.image("images/togaylogo.png", width=300)
        # # ToDo: Update and link option menu
        # selected = option_menu(
        #
        #     menu_title="Portfolio Links",
        #     options=["Data Entry", "Visualization", "Analysis", "About"],
        #     icons=["pencil-fill", "bar-chart-fill", "sliders", "graph-up-arrow"],  # https://icons.getbootstrap.com
        #     orientation='vertical',
        #
        # )
        st_lottie(lottie_hello,
                  speed=1,
                  reverse=False,
                  loop=True,
                  quality="medium",
                  height=300,
                  width=300,
                  )


    content = """
    I am a Python programmer, teacher, founder of PythonNow. I am a self taught programmer. 
    I am a Python programmer, teacher, founder of PythonNow. I am a self taught programmer.
    I am a Python programmer, teacher, founder of PythonNow. I am a self taught programmer.
    I am a Python programmer, teacher, founder of PythonNow. I am a self taught programmer.
    """
    st.info(content)

    st.markdown("___")

    col4, empty_col, col5 = st.columns([2, 0.5, 2])

    df = pd.read_csv("data.csv", sep=";")

    with col4:
        for index, row in df[:10].iterrows():
            st.subheader(row['title'])
            st.write(row['description'])
            st.image("images/" + row["image"], width=300)
            st.write(f"[Source Code]({row['url']})")
            st.markdown("___")
    st.markdown("___")
    with col5:
        for index, row in df[10:].iterrows():
            st.subheader(row['title'])
            st.write(row['description'])
            st.image("images/" + row["image"], width=300)
            st.write(f"[Source Code]({row['url']})")
            st.markdown("___")


st.markdown("")
st.image("images/togaylogo.png", width=300)
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
                        icons=["Home", 'cloud-upload', "list-task", 'gear'],
                        menu_icon="cast", default_index=0, orientation="horizontal")


if selected2 == 'Home':
    home()

elif selected2 == "Upload":
    st.write("Togay Tunca")
