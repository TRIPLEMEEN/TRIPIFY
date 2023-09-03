import pandas as pd
import numpy as np

data_orig = pd.read_csv('data.csv')
data_orig['loudness'] = -((data_orig['loudness'])/10)
data_orig['tempo'] = data_orig['tempo']/250

songs1 = data_orig.drop(['id','name','key','mode','duration_ms','release_date','popularity','year','artists'],axis = 1)
Genre = []

for i in range(0,len(songs1)):
    if (max(songs1.loc[i]) == data_orig.loc[i,'acousticness']):
        Genre.append("Slow & Somber Acoustics")

    if (max(songs1.loc[i]) == data_orig.loc[i,'danceability']):
        Genre.append("Happy & Danceable Instrumentals")

    elif (max(songs1.loc[i]) == data_orig.loc[i,'valence']):
        Genre.append("Sad ")

    elif (max(songs1.loc[i]) == data_orig.loc[i,'liveness']):
        Genre.append("Upbeat Songs With Cheerful Vocals")

    elif (max(songs1.loc[i]) == data_orig.loc[i,'energy']):
        Genre.append("Fast & Danceable")

    elif (max(songs1.loc[i]) == data_orig.loc[i,'tempo']):
        Genre.append("Fast, Upbeat & Cheerful")

    elif (max(songs1.loc[i]) == data_orig.loc[i,'speechiness']):
        Genre.append("Rap")

    elif (max(songs1.loc[i]) == data_orig.loc[i,'loudness']):
        Genre.append("Full of energy")

    else :
        Genre.append("Happy & Upbeat Instrumentals")

data_orig['Genre']   = pd.Series(Genre)
data_orig.to_csv('data_orig.csv')