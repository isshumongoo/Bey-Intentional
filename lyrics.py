#Imports
import streamlit as st
import pandas as pd 
import numpy 
import seaborn
import os
from lyricsgenius import Genius
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import google.generativeai as genai

#Master list of beyonces songs, does not include Cowboy Carter
Master_Bey_List = pd.read_csv('beyonce_tracks.csv')
print(Master_Bey_List.head())

#Genius API Access token found and APi defined
genius_token = os.getenv('GENIUS_ACCESS_TOKEN')
genius = Genius(genius_token)

#Establishing Gemini GenAI
genai_api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=genai_api_key)
lyric_model = genai.GenerativeModel('gemini-pro')

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
    
#GenAi Analyzes lyrics with the snetiment score and returns that
def analyze_lyrics(lyrics,sentiment):
    lyric_analysis = lyric_model.generate_content("Analyze these lyrics: " + lyrics +" Alongside this sentiment score of", sentiment, ". Tell me the message behind the lyrics in this song.")
    return lyric_analysis.text
            
#Add lyrics to dataset and create a new file for them. 
if not os.path.isfile('beyonce_tracks_with_lyrics.csv'):
    Master_Bey_List['lyrics'] = Master_Bey_List.apply(lambda row: get_lyrics(row['artist_name'], row['track_name']), axis=1)
    Master_Bey_List.to_csv('beyonce_tracks_with_lyrics.csv', index=False)

#Variable referencing new dataset
Lyric_List = pd.read_csv('beyonce_tracks_with_lyrics.csv')

#Download for nltk and then sentiment analysis
nltk.download('all')

#Grabs polarity from the
def get_sentiment(lyrics):
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(lyrics)

#Add sentiment score to dataset
Lyric_List['sentiment'] = Lyric_List.apply(lambda row: get_sentiment(row['lyrics']))