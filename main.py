import csv 
from flask import Flask, jsonify
from demographic import output
from content import getrecomend

all_movies = []
liked_movies = []
unliked_movies = []
didnot_watch_movies = []

with open("movies.csv", "r", encoding= "utf-8") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_movies = data[1:]

app = Flask(__name__)

@app.route("/")
def movie():
    return jsonify({
        "data": all_movies,
        "message" : "success"
    })

@app.route("/liked-movies", methods = ["POST"])
def liked_movies():
    movie_name = all_movies[0]
    liked_movies.append(movie_name)
    all_movies = all_movies[1:]
    return jsonify({
        "status": "success"
    })

@app.route("/unliked-movies" , methods = ["POST"])
def unliked():
    movie_name = all_movies[0]
    unliked_movies.append(movie_name)
    all_movies = all_movies[1:]
    return jsonify({
        "message":"success"
    })

@app.route("/didnotwatch" , methods = ["POST"])
def didnotwatch():
    movienames = all_movies[0]
    didnot_watch_movies.append(movienames)
    all_movies = all_movies[1:]
    return jsonify({
        "message":"success"
    })

@app.route("/popular-movies")
def popularmovies():
    movie_data = []
    for movie in output:
        d = {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date": movie[2],
            "duration": movie[3],
            "rating": movie[4],
            "overview": movie[5]
        }
        movie_data.append(d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    })
    

if __name__ == "__main__":
    app.run(debug = True)