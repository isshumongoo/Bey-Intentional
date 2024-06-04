import streamlit as st
from lyrics import *

#streamlit run hive.py --server.enableCORS=False
# python -m streamlit run hive.py --server.enableCORS=False
if "start_button" not in st.session_state:
    st.session_state.start_button = False

if "reset_button" not in st.session_state:
    st.session_state.reset_button = False

st.markdown("<h2 style='color:#A5A9B4;font-family: Monaco;'>Bey-Intentional</h2>")

title1, title2 = st.columns(2)
with title1:
    st.image(Bey_title_page.jpg)
with title2:
    st.markdown("<h4 style='color:#A5A9B4;font-family: Monaco;'>**Bey-Intentional** is a fan-built project dedicated to delving deeper into the world of Beyoncé's music. This project uses data analysis to unlock the hidden meaning within her lyrics.</h4>")

user_song = st.text_input("What song's intent do you want to know?")
