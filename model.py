import pandas as pd
import sys
import numpy as np
import pickle

data_final  = pd.read_csv('data_orig.csv')
filename = 'data_model_2.sav'

loaded_model = pickle.load(open(filename, 'rb'))


song_input = sys.argv[1]
a = data_final['id'].where(data_final['name'] == '{}'.format(song_input)).any()

a = data_final[['valence','acousticness','danceability', 'energy', 'instrumentalness', 
                'loudness', 'popularity', 'speechiness','tempo']].where(data_final['name'] == song_input)

a= a.dropna()

pred = loaded_model.predict(a)

print(pred[0])

z = data_final.groupby('Genre').groups[pred[0]]

data_final["name"].iloc[z].head(20).to_excel("temp.xlsx")

