import csv 

all_movies = []
all_movies_links = []
headers = []

with open('movies.csv', "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    headers = data[0]
    all_movies = data[1:]

headers.append("poster_link")

with open('movie_links.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies_links = data[1:]

with open('final.csv', "a+", encoding="utf-8")as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    

for movie_item in all_movies:
    poster_found = any( movie_item[8] in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        for movie_link_item in all_movies_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+", encoding="utf-8") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)