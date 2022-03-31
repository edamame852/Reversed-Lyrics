#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:39:14 2022

@author: miltonchow
"""
# Draws lyrics from the website: Genius
import lyricsgenius as lg

# RE (as in Regular Expression) for string splicing 
import re as re

# Load dotenv lib 
from dotenv import load_dotenv
load_dotenv()

# Calling en variables

import os
api_key = os.getenv("API_KEY") # API Token (Do not distribute)

#Shows all location of where API_KEY is found
print(os.getenv("PATH"))

genius = lg.Genius(api_key, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
artist = genius.search_artist("Owl City", max_songs=3)

#song_lyrics = artist.song("Not All Heroes Wear Capes").lyrics
#song_lyrics = artist.song("Vanilla Twilight").lyrics
song_lyrics = artist.song("Fireflies").lyrics

updated_lyrics = re.split(r"(\s+)", song_lyrics)



targetedWord = 0
for idx, words in enumerate(updated_lyrics):
    if words == "Lyrics":
        targetedWord = idx+2
del(updated_lyrics[0:targetedWord])

# Erasing "\* Embed" wordings at the end of lyrics
for idx, words in enumerate(updated_lyrics):
    if "Em" in words:
        print(words)
        print(idx, "\n")
        #tuple_test = [re.findall(r'(\w+?)(\d+)', words)[0]]
        
        tuple_test = re.split(r"[0-9]|[0-9][0-9]",words)
        if tuple_test[0] == "":
            del(updated_lyrics[idx])
        else:
            updated_lyrics[idx] = tuple_test[0]

#List Comprehension for identifying word or non-word

finalOutput = []
[finalOutput.append(element[::-1])for idx, element in enumerate(updated_lyrics)]


with open("songReversed.txt", "w") as textfile:
    for element in finalOutput:
        textfile.write(element)


        
        
        
        
    