import pandas as pd
import numpy as np
import pickle

r_cols = ('userId','movieId','rating')
ratings = pd.read_csv('ratings.csv',names=r_cols,usecols=range(3), skiprows=1)
m_cols = ('movieId','title')
movies = pd.read_csv('movies.csv',names=m_cols,usecols=range(2), skiprows=1)

myratings = pd.merge(movies,ratings)
print(myratings.head(1000))

userRatings = myratings.pivot_table(index=['userId'], values='rating',columns=['title'])
print("STOP")
print(userRatings.head(20))

corrMatrix = userRatings.corr(method='pearson',min_periods=100)
print("STOP")
print(corrMatrix.head(10))

pickle.dump(corrMatrix,open('filmovi2.sav','wb'))
