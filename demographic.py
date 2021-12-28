import pandas as pd
import numpy
import statistics
df = pd.read_csv("final.csv")
vote_average = df['vote_average'].tolist()
vote_avg_list = []
for i in vote_average:
   vote_avg_list.append((i))
    
C = statistics.mean(vote_avg_list)

print(C)
'''m = df['vote_count'].quantile(0.9)

q_movies = df.copy().loc[df['vote_count']>=m]

def weightedrating(x,m=m,C=C):
  v = x['vote_count']
  R = x['vote_average']
  score = (v/(v+m) * R) + (m/(m+v) * C)
  return score

q_movies['score'] = q_movies.apply(weightedrating,axis = 1)

q_movies = q_movies.sort_values('score',ascending=False)
output = q_movies[['title','poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].head(20).values.tolist()
print(output)'''