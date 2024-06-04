import streamlit as st
from lyrics import *

#streamlit run hive.py --server.enableCORS=False
# python -m streamlit run hive.py --server.enableCORS=False

#Initializing session states
if "start_button" not in st.session_state:
    st.session_state.start_button = False
if "reset_button" not in st.session_state:
    st.session_state.reset_button = False

#Functions for buttons, preventing site refresh
def start_on_click():
    st.session_state.start_button = True
def reset_on_click():
    st.session_state.reset_button = True

#Title with pictrue and description
st.markdown("<h2 style='color:#A5A9B4;font-family: Monaco;'>Bey-Intentional</h2>", unsafe_allow_html=True)

title1, title2 = st.columns(2)
with title1:
    st.image("Bey_title_photo.jpg")
with title2:
    st.markdown("<h4 style='color:#A5A9B4;font-family: Monaco;'>Bey-Intentional is a fan-built project dedicated to delving deeper into the world of Beyoncé's music. This project uses data analysis to unlock the hidden meaning within her lyrics.</h4>", unsafe_allow_html=True)

#user input and buttons with respective functions
user_song = st.text_input("What song's intent do you want to know?")
starter = st.button("Start", on_click=start_on_click())
reseter = st.button("Reset", on_click=reset_on_click())
