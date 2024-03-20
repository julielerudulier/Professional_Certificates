## This file is a snippet of the code that I used for the Streamlit App

import pandas as pd 
import numpy as np
import requests
import json
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
from scipy.spatial.distance import pdist, squareform
import graphviz 
import plotly.express as px

# Import datasets
dataset = pd.read_csv("final_red.csv", index_col = 0)
dfm = pd.read_csv("df_matrix.csv", index_col = 'artist_track')
dfm2 = pd.read_csv("df_matrix.csv")
dataset_sample = pd.read_csv("dataset.csv", index_col = 0)
pop_genre = pd.read_csv("pop_genre.csv", index_col = 0)
numgenres = pd.read_csv("numgenres.csv", index_col = 0)
top10artists = pd.read_csv("top10artists.csv", index_col = 0)
top15artists = pd.read_csv("top15artists.csv", index_col = 0)
top15titres = pd.read_csv("top15titres.csv", index_col = 0)
top15genres = pd.read_csv("top15genres.csv", index_col = 0)

# Cluster-based function: 
def reco(track):
       df_track = dataset.loc[(dataset['artist_track'] == track)][['artists', 'track_name', 'artist_track', 'track_genre', 'cluster_genres', 'tempo', 'energy', 'loudness', 'popularity']]
       artist = df_track['artists']
  
       track_infos = pd.DataFrame()
       for i, j, k, l, m, n, o in zip(dataset['artist_track'], dataset['cluster_attributs'], dataset['tempo'], dataset['loudness'], dataset['energy'], dataset['acousticness'], dataset['danceability']):
           if i == track:
               track_infos = dataset.loc[(dataset['cluster_attributs'] == j) 
               & ((dataset['tempo'] > (k - 5)) & (dataset['tempo'] < (k + 5))) 
               | ((dataset['tempo'] > ((k/2) - 5)) & (dataset['tempo'] < ((k/2) + 5)))
               | ((dataset['tempo'] > ((k*2) - 5)) & (dataset['tempo'] < ((k*2) + 5)))
               & (dataset['loudness'] > (l - 1)) & (dataset['loudness'] < (l + 1)) 
               & (dataset['energy'] > (m - 0.2)) & (dataset['energy'] < (m + 0.2))
               & (dataset['acousticness'] > (n - 0.3)) & (dataset['acousticness'] < (n + 0.3))
               & (dataset['danceability'] > (o - 0.3)) & (dataset['danceability'] < (o + 0.3))][['artists', 'track_name', 'artist_track', 'track_genre', 'cluster_genres', 'tempo', 'energy', 'loudness', 'popularity']]
  
       track_infos = track_infos.drop_duplicates(subset = ['artist_track'])
       track_infos = track_infos[track_infos['artist_track'] != track]
       track_infos = track_infos[~track_infos['artist_track'].str.contains(track[:20])]
       track_infos = track_infos.sort_values('popularity', ascending = False)
  
       list_genres = list(df_track['track_genre'])
       df_genre = dataset[dataset['track_genre'].isin(list_genres)]

       for i, j, k, l, m, n, o in zip(df_genre['artist_track'], df_genre['cluster_genres'], df_genre['tempo'], df_genre['loudness'], df_genre['energy'], dataset['acousticness'], dataset['danceability']):
           if i == track:
               df_genre = df_genre.loc[(df_genre['cluster_genres'] == j)
               & (df_genre['tempo'] > (k - 7)) & (df_genre['tempo'] < (k + 7))
               | ((df_genre['tempo'] > ((k/2) - 7)) & (df_genre['tempo'] < ((k/2) + 7)))
               | ((df_genre['tempo'] > ((k*2) - 7)) & (df_genre['tempo'] < ((k*2) + 7)))
               & (df_genre['loudness'] > (l - 2.5)) & (df_genre['loudness'] < (l + 2.5)) 
               & (df_genre['energy'] > (m - 0.2)) & (df_genre['energy'] < (m + 0.2))
               & (dataset['acousticness'] > (n - 0.2)) & (dataset['acousticness'] < (n + 0.2))
               & (dataset['danceability'] > (o - 0.2)) & (dataset['danceability'] < (o + 0.2))][['artists', 'track_name', 'artist_track', 'track_genre', 'cluster_genres', 'tempo', 'energy', 'loudness', 'popularity']]
  
        df_genre = df_genre[df_genre['artist_track'] != track]
        df_genre = df_genre.drop_duplicates(subset = ['artist_track'])
        df_genre = df_genre[~df_genre['artist_track'].str.contains(track[:20])]
        df_genre = df_genre.sort_values('popularity', ascending = False)
 
        df_artist = dataset.loc[(dataset['artists'].isin(artist)) 
        | (dataset['artists'].str.contains(track[:9]))][['artists', 'track_name', 'artist_track', 'track_genre', 'cluster_genres', 'tempo', 'energy', 'loudness', 'popularity']]   
  
        df_artist = df_artist.drop_duplicates(subset = ['artist_track'])
        df_artist = df_artist[df_artist['artist_track'] != track] 
        df_artist = df_artist[~df_artist['artist_track'].str.contains(track[:20])]
        df_artist = df_artist.sort_values('popularity', ascending = False)
   
        if not df_artist.empty:
            return df_artist['artist_track'].values[:1]
        elif not df_genre.empty:  
            return df_genre['artist_track'].values[:1]
        elif not track_infos.empty:
            return track_infos['artist_track'].values[:1]        

# Similarity matrix
new_index = list(dfm.index)
pairwise = pd.DataFrame(squareform(pdist(dfm, 'mahalanobis')))
pairwise['artist_track'] = new_index
 
# Matrix-based function:
def recom(track):
       df = pairwise[pairwise['artist_track'] == track]
       df = df.reset_index(drop = True).T
       df = df[df[0] != track]
       df['artist_track'] = new_index
       df = df.rename(columns = {0 : 'distance'})
       df = df[df['distance'] != 0]
       df = df.sort_values(by = 'distance')
       if not df.empty:
            return df['artist_track'].values[:1]
       else:
            return st.write("") 

# Deezer player:
def player(reco):
       url = "https://api.deezer.com/search?q=" + reco
       request = requests.get(url)
       parsing = json.loads(request.text)
       reco_id = str(parsing['data'][0]['id'])
       link = "https://widget.deezer.com/widget/auto/track/" + reco_id
       return components.html(f'<iframe title="deezer-widget" src={link} width="100%" height="150" frameborder="0" allowtransparency="true" allow="encrypted-media; clipboard-write"></iframe>')

# Seed track:
OG = "Taylor Swift - Lover"
OG_index = int(dfm2[dfm2['artist_track'] == OG].index.values)
options = dfm2['artist_track']
search_bar = st.selectbox("", options, index = OG_index, label_visibility = "collapsed", key = "search")
player(search_bar)
    
# Search bar update:
def callback1():
       st.session_state.search = options[index_reco1]
        
def callback2():
       st.session_state.search = options[index_reco2]

# Display of recommendations:
if search_bar != OG:
       st.markdown('#')
       st.write(f"You selected the song **{search_bar}**, here are the tracks the system recommends:")
       track = str(search_bar) 
       reco1 = reco(track)[0]
       reco2 = recom(track)[0]
       index_reco1 = int(dfm2[dfm2['artist_track'] == reco1].index.values)
       index_reco2 = int(dfm2[dfm2['artist_track'] == reco2].index.values)
       col1, col2 = st.columns([1,1])
       with col1:
           st.write(f"**{reco1}**")
           player(reco1)
           bouton1 = st.button('Next recommendation', on_click = callback1, key = 1)
       with col2:
           st.write(f"**{reco2}**")
           player(reco2)
           bouton2 = st.button('Next recommendation', on_click = callback2, key = 2)  

    
