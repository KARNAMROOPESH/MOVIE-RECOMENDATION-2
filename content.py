import pandas as pd
import numpy as ny
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('final.csv')

df = df[df['soup'].notna()]

count = CountVectorizer(stop_words='english')

countmatrix = count.fit_transform(df['soup'])

cosinesim = cosine_similarity(countmatrix,countmatrix)

df = df.reset_index()
indices = pd.Series(df.index,index=df['title'])

def getrecomend(title,cosinesim):
  index = indices[title]
  simscore = list(enumerate(cosinesim[index]))
  simscore = sorted(simscore,key=lambda x:x[1] , reverse=True)
  simscore = simscore[1:11]
  movieindises = [i[0] for i in simscore]
  return df[['title','poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].iloc[movieindises].values.tolist()
  