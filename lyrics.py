#Imports
import streamlit as st
import pandas as pd 
import numpy as np 
import seaborn as sns 
import os
from lyricsgenius import Genius

#Master list of beyonces songs, does not include Cowboy Carter
Master_Bey_List = pd.read_csv('beyonce_tracks.csv')
print(Master_Bey_List.head())

#Genius API Access token found and APi defined
genius_token = os.getenv('GENIUS_ACCESS_TOKEN')
genius = Genius(genius_token)

#Function to find lyrics from the Beyonce tracklist
def get_lyrics(artist,song):
    try:
        track_lyrics = genius.search_song(song,artist)
        if track_lyrics:
            return track_lyrics.lyrics
        else:
            return "No lyrics found"
    except TimeoutError:
        return "Request timed out"
    except Exception as e:
        return "Error occured finding song lyrics"
            
#Add lyrics to dataset and create a new file for them. 
if not os.path.isfile('beyonce_tracks_with_lyrics.csv'):
    Master_Bey_List['lyrics'] = Master_Bey_List.apply(lambda row: get_lyrics(row['artist_name'], row['track_name']), axis=1)
    Master_Bey_List.to_csv('beyonce_tracks_with_lyrics.csv', index=False)

#Variable referencing new dataset
Lyric_List = pd.read_csv('beyonce_tracks_with_lyrics.csv')