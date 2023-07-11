import streamlit as st
import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
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
    lottie_cake = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ZarLnF7zef.json")
    st_lottie(
        lottie_cake,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",  # medium ; high
        height=300,
        width=300,
        key=None,
    )


placeholder = st.empty()
st.button("Click me :)",on_click=nextpage,disabled=(st.session_state.page > 3))

if st.session_state.page == 0:
    # Replace the placeholder with some text:
    with placeholder.container():
        lottie_bday = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_shlwmfns.json")
        st_lottie(
            lottie_bday,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",  # medium ; high
            height=400,
            width=400,
            key=None,
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
        st.image(image_amorcito,caption="Te amo <3")

        st.button("Restart",on_click=restart)

#
# if opt == ':cake: Happy Birthday':
#     st.session_state.page == 0
#     # Replace the placeholder with some text:
#     with placeholder.container():
#             # st.title(':champagne:Happy:birthday:Birthday:tada:')
#             # first_image = Image.open('C:/Users/Sebastian Arce/Documents/Data Science/streamlit_app/dani_bday/birthday.jpg')
#             # st.image(first_image,width=400)
#             lottie_bday = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_shlwmfns.json")
#             st_lottie(
#                 lottie_bday,
#                 speed=1,
#                 reverse=False,
#                 loop=True,
#                 quality="high",  # medium ; high
#                 height=400,
#                 width=400,
#                 key=None,
#             )
#
#     # with pictures:
#     #     sl.title("Introduction")
#     #     sl.subheader('*Description of Arsenal FC*')
#     #
#     #     filteredImages = ['first_image.jpg', 'second_image.jpg', 'third_image.jpg',
#     #                       'fourth_image.jpg', 'fifth_image.jpg', 'sixth_image.jpg']  # your images here
#     #
#     #     cols = cycle(sl.columns(3))  # st.columns here since it is out of beta at the time I'm writing this
#     #     for idx, filteredImage in enumerate(pictures_bday):
#     #         next(cols).image(filteredImage, width=600)
#
# if opt == ':film_projector: Hello':
#     st.session_state.page = 1
#     with placeholder.container():
#         video_html="""
#         <div style="height: 533.33px; width: 300.00px; position:relative;"><iframe allow="autoplay; gyroscope;" allowfullscreen height="100%" referrerpolicy="strict-origin" src="https://www.kapwing.com/e/64a9844f8fb1380011b94d2d?autoplay=true" style="border:0; height:100%; left:0; overflow:hidden; position:absolute; top:0; width:100%" title="Embedded content made on Kapwing" width="100%"></iframe></div><p style="font-size: 12px; text-align: right;"></a></p>
#         """
#         st.markdown(video_html, unsafe_allow_html=True)
#
# if opt == ':camera_with_flash: Friends':
#         st.session_state.page = 2
#         with placeholder.container():
#             n_cols = 2
#             n_rows = 1 + len(resize_images) // int(n_cols)
#             rows = [sl.container() for _ in range(n_rows)]
#             cols_per_row = [r.columns(n_cols) for r in rows]
#             cols = [column for row in cols_per_row for column in row]
#
#             for image_index, picture_image in enumerate(resize_images):
#                 cols[image_index].image(picture_image, use_column_width=True)
#
# if opt == ':heartbeat: Bonus':
#     st.session_state.page = 2
#     with placeholder.container():
#         n_cols = 2
#         n_rows = 1 + len(resize_images) // int(n_cols)
#         rows = [sl.container() for _ in range(n_rows)]
#         cols_per_row = [r.columns(n_cols) for r in rows]
#         cols = [column for row in cols_per_row for column in row]
#         for image_index, picture_image in enumerate(resize_images):
#             cols[image_index].image(picture_image, use_column_width=True)


# Using List Comprehension to read all images
# mypath = "C:/Users/Sebastian Arce/Documents/Data Science/streamlit_app/dani_bday/pictures/*.jpg"
# mypath2 = "C:/Users/Sebastian Arce/Documents/Data Science/streamlit_app/dani_bday/bonus/*.jpg"
#
# glob.glob(mypath)

# images_path1 = [cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB) for image in glob.glob(mypath)]
# images_path2 = [cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB) for image in glob.glob(mypath2)]
#
# resize_images1 = []
# for img in images_path1:
#     img = cv2.resize(img, dsize=(1000, 2000))
#     resize_images1.append(img)
#
# resize_images2 = []
# for img in images_path2:
#     img = cv2.resize(img, dsize=(1000, 2000))
#     resize_images2.append(img)
