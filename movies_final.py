import pandas as pd
import pickle

r_cols = ('movieId','rating')
ratings = pd.read_csv('movie.csv', names=r_cols, usecols=range(2), skiprows=1)
m_cols = ('movieId','title')
movies = pd.read_csv('movies.csv', names=m_cols, usecols=range(2), skiprows=1)

corrMatrix=pickle.load(open("filmovi2.sav", 'rb'))
ratings = pd.merge(movies,ratings)
ratings = ratings.drop(columns=['movieId'])
ratings.set_index('title', inplace=True)
#print(ratings.head(10))

simCandidates = pd.Series()
for i in range(0, len(ratings.index)):
  #print("working.. on: " + ratings.index[i] + '... ')
  sims = corrMatrix[ratings.index[i]].dropna()
  sims = sims.map(lambda x: x * ratings.rating[i])
  simCandidates = simCandidates.append(sims)
print("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
simCandidates.head(100)
filtered = simCandidates.drop(ratings.index, errors='ignore')
print(filtered.head(15))
