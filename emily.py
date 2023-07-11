import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("C:/Users/Sebastian Arce/Documents/Data Science/streamlit_app/dani_bday/emily/"))

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13,tab14 = st.tabs(
    ["H", "A", "P", "P", "Y"," ","B", "I", "R", "T", "H", "D", "A", "Y"])

with tab1:
    # image_1 = """
    #         <iframe src="https://drive.google.com/file/d/1soyz08SSsIFrzNwP5vK88fP9gUQSoiZB/preview" width="400" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_1, unsafe_allow_html=True)
    image_1=Image.open("emily/Screenshot_20230709-220246.jpg")
    image_1=image_1.resize((400,500))
    st.image(image_1)

with tab2:
    # image_2 = """
    #         <iframe src="https://drive.google.com/file/d/1sFegmdRlHLTrgLpmarrDf09_lDFYYEHm/preview" width="400" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_2, unsafe_allow_html=True)
    image_2=Image.open("emily/Screenshot_20230709-203739.jpg")
    image_2=image_2.resize((600,400))
    st.image(image_2)

with tab3:
    # image_3 = """
    #         <iframe src="https://drive.google.com/file/d/1lQmDTCrA3qI3Ahs_ZmCYL7-z2taiMlRN/preview" width="700" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_3, unsafe_allow_html=True)
    image_3=Image.open("emily/IMG-20230621-WA0043.jpg")
    image_3=image_3.resize((600,400))
    st.image(image_3)

with tab4:
    # image_4 = """
    #         <iframe src="https://drive.google.com/file/d/1IEWieG1mnwsiWDZlBmZ9L8beFMN9hb80/preview" width="700" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_4, unsafe_allow_html=True)
    image_4=Image.open("emily/IMG-20230621-WA0028.jpg")
    image_4=image_4.resize((600,400))
    st.image(image_4)

with tab5:
    # image_5 = """
    #         <iframe src="https://drive.google.com/file/d/1wOnWScr6jRpT4zopMw1HMPv_Mvs2wBS9/preview" width="700" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_5, unsafe_allow_html=True)
    image_5=Image.open("emily/IMG-20230621-WA0020.jpg")
    image_5=image_5.resize((600,400))
    st.image(image_5)

with tab7:
    # image_7 = """
    #         <iframe src="https://drive.google.com/file/d/1rZJ_Yri1qNC2LGaeTYFT88SKm67GWTsa/preview" width="550" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_7, unsafe_allow_html=True)
    image_7=Image.open("emily/IMG-20230621-WA0015.jpg")
    image_7=image_7.resize((600,400))
    st.image(image_7)

with tab8:
    # image_8 = """
    #         <iframe src="https://drive.google.com/file/d/1nhyllbeJRbH69wBWuHA1225tntjPQEbi/preview" width="600" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_8, unsafe_allow_html=True)
    image_8=Image.open("emily/IMG-20230621-WA0024.jpg")
    image_8=image_8.resize((600,400))
    st.image(image_8)

with tab9:
    # image_9 = """
    #         <iframe src="https://drive.google.com/file/d/1SquTtEjRGSunxqkHb58W0wS385fDltl7/preview" width="350" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_9, unsafe_allow_html=True)
    image_9=Image.open("emily/IMG-20230621-WA0038.jpg")
    image_9=image_9.resize((400,500))
    st.image(image_9)

with tab10:
    # image_10 = """
    #         <iframe src="https://drive.google.com/file/d/1OHhRpP3jPj0HiS4D3DR3hxuVQs0kjpfl/preview" width="350" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_10, unsafe_allow_html=True)
    image_10=Image.open("emily/IMG-20230621-WA0037.jpg")
    image_10=image_10.resize((400,500))
    st.image(image_10)

with tab11:
    # image_11 = """
    #         <iframe src="https://drive.google.com/file/d/1DIJqdYI521-c1mf8uJZI--2H6Nx0wJ2I/preview" width="350" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_11, unsafe_allow_html=True)
    image_11=Image.open("emily/IMG-20230621-WA0036.jpg")
    image_11=image_11.resize((400,500))
    st.image(image_11)

with tab12:
    # image_12 = """
    #         <iframe src="https://drive.google.com/file/d/1PhOQ49L4LikHauZJCVcv02y1lfLW2Eye/preview" width="350" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_12, unsafe_allow_html=True)
    image_12=Image.open("emily/IMG-20230621-WA0039.jpg")
    image_12=image_12.resize((400,500))
    st.image(image_12)

with tab13:
    # image_13 = """
    #         <iframe src="https://drive.google.com/file/d/1PmPvYwhZ3ZPHpz5OanHAdaRZ1ccBDX6v/preview" width="400" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_13, unsafe_allow_html=True)
    image_13=Image.open("emily/IMG-20230621-WA0029.jpg")
    image_13=image_13.resize((400,500))
    st.image(image_13)

with tab14:
    # image_14 = """
    #         <iframe src="https://drive.google.com/file/d/1sFkmBbGmjC1VtIKEBt0qMpa7r3MELBw0/preview" width="400" height="500" allow="autoplay"></iframe>
    #         """
    # st.markdown(image_14, unsafe_allow_html=True)
    image_14=Image.open("emily/Screenshot_20230709-203721.jpg")
    image_14=image_14.resize((400,500))
    st.image(image_14)
