import streamlit as st
from lyrics import *
import pandas as pd

#streamlit run hive.py --server.enableCORS=False
# python -m streamlit run hive.py --server.enableCORS=False

#Initializing session states
if "start_button" not in st.session_state:
    st.session_state.start_button = False
if "index_button" not in st.session_state:
    st.session_state.index_button = False
if "Master_List" not in st.session_state:
      st.session_state.Master_List = pd.read_csv('beyonce_tracks_with_lyrics&sentiment.csv')

#Functions for buttons, preventing site refresh
def start_on_click():
    st.session_state.start_button = True
def index_button_on_click():
     st.session_state.index_button = True
    

#Setting CSS file
with open('bey_style.css') as f:
    		css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#Function for user to pick which song they're talking about if multiple matches are returned
def further_find(matches):
    #If there is only one or zero matches, simply return ot
    if len(matches) <= 1:
        return matches

    else:
        #turn to list, then iterate through using a counter to show user index and the song name
        matches_list = matches.values.tolist()
        counter = 1
        for i in matches_list:
             st.write(counter, ": ", i[2])

        #take user input and turn to integer to be used as index
        index = int(st.text_input("Type the index of the song in specific you're looking for"))
        index_button = st.button("Index chosen", on_click=index_button_on_click)

        #edge cases
        if index_button and index > len(matches_list) or index < len(matches_list):
             st.write("Invalid Index.")
        elif index_button and not index.isnumeric():
             st.write("Input a number please!")
        else:
            #If button is pressed and everything is fine, return specific row user chose
            if index_button:
                return matches.iloc[index-1]



#Title with picture and description
st.markdown("<h2 style='color:#A5A9B4;font-family: Monaco;'>Bey-Intentional</h2>", unsafe_allow_html=True)

title1, title2 = st.columns(2)
with title1:
    st.image("Bey_title_photo.jpg")
with title2:
    st.markdown("<h4 style='color:#A5A9B4;font-family: Monaco;'>Bey-Intentional is a fan-built project dedicated to delving deeper into the world of Beyoncé's music. This project uses data analysis to unlock the hidden meaning within her lyrics.</h4>", unsafe_allow_html=True)

#user input and buttons with respective functions
user_song = st.text_input("What song's intent do you want to know?")

b1,b2 = st.columns(2)
with b1:
    starter = st.button("Start", on_click=start_on_click)
with b2:
    reseter = st.button("Reset")

if not user_song and st.session_state.start_button:
    st.write("Put in a song by the QUEEN.")
elif user_song and st.session_state.start_button:
    matches = find_song(user_song,st.session_state.Master_List)