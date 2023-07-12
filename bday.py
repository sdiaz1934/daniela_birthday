import streamlit as st
import requests  # pip install requests
import base64
import streamlit.components.v1 as components

# Importing database and libraries

import warnings

import cv2
import numpy as np
from matplotlib import pyplot as plt
from past.builtins import raw_input
from sympy import div

warnings.filterwarnings('ignore')

# get_ipython().run_line_magic('matplotlib', 'inline')

from st_aggrid import AgGrid
from PIL import Image

# Importing python files
import sys
import os
import io

sys.path.append(os.path.abspath("C:/Users/Sebastian Arce/Documents/Data Science/streamlit_app/dani_bday/emily"))

from itertools import cycle
import glob


# Database

def inject_CSS_table(xzy):
    # CSS to inject contained in a string
    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    # Display a static table
    st.table(xzy)


def inject_CSS_dataframe(xyz):
    # CSS to inject contained in a string
    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    # Display an interactive table
    st.dataframe(xyz)


# .css-yyj0jg.edgvbvh3
# css-h5rgaw egzxvld1 Footer

st.markdown("""
<style>

.css-9s5bis.edgvbvh3
{
    visibility:hidden;
}
.css-h5rgaw.egzxvld1
{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = 0

# Importing images



#Definign function for Lotties

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Creating buttons for next nd restart
def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0

# Creating a sidebar
st.sidebar.title(':champagne:Happy:birthday:Birthday:tada:')
with st.sidebar:
        image_sidebar = """
                <a title="Images of happy birthday, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Cartoon_Happy_Birthday_Cake.svg"><img width="300" alt="Cartoon Happy Birthday Cake" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Cartoon_Happy_Birthday_Cake.svg/512px-Cartoon_Happy_Birthday_Cake.svg.png"></a>
                """
        st.markdown(image_sidebar, unsafe_allow_html=True)


placeholder = st.empty()
st.button("Click me :)",on_click=nextpage,disabled=(st.session_state.page > 3))

if st.session_state.page == 0:
    # Replace the placeholder with some text:
    with placeholder.container():
        # image_home = """
        #         <iframe src="https://drive.google.com/file/d/1R2Pic6cKB1qkh7OXEdwXhCrUifaL0EGe/preview" width="640" height="480" allow="autoplay"></iframe>
        #         """
        # st.markdown(image_home, unsafe_allow_html=True)

        file_ = open("bday-752.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )

elif st.session_state.page == 1:
    # Replace the text with a chart:
    with placeholder.container():
        with open("video.py") as f:
            exec(f.read())

elif st.session_state.page == 2:
    with placeholder.container():
        with open("friends.py") as f:
            exec(f.read())


elif st.session_state.page == 3:
    with placeholder.container():
        with open("emily.py") as f:
            exec(f.read())
else:
    with placeholder.container():
        image_amorcito=Image.open("amorcito_corazon.png")
        image_amorcito = image_amorcito.resize((400, 500))
        st.image(image_amorcito,caption="Te amo <3")

        st.button("Restart",on_click=restart)