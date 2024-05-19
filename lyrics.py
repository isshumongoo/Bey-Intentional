#Imports
import streamlit as st
import pandas as pd 
import numpy as np 
import seaborn as sns 
import os
from dotenv import load_dotenv
from lyricsgenius import Genius

#Master list of beyonces songs, does not include Cowboy Carter
master_Bey_list = pd.read_csv('beyonce_tracks.csv')
print(master_Bey_list.head())

#Genius API Access token found and APi defined
load_dotenv(r'./env')
#Error saying the variable below isn't defined, even though it's brought from .env file
genius_token = os.getenv(Genius_Access_token)
genius = Genius(genius_token)
