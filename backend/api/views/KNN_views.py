import pandas as pd
import numpy as np
import pprint
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie

label = ["Action","Adventure","Animation","Children's",
                "Comedy","Crime","Documentary","Drama","Fantasy",
                "Film-Noir","Horror","Musical","Mystery","Romance",
                "Sci-Fi","Thriller","War","Western"]

def distance(input_movie, input_movie_genre, movie_genre, title):
  movie = Movie.objects.get(title=title)
  print(type(input_movie_genre))
  print(type(movie_genre))
  dist = np.linalg.norm(input_movie_genre - movie_genre)
  for cast in movie.Casting.split("|"):
    if cast in input_movie.Casting:
      dist -= 0.1
  if movie.Director == input_movie.Director:
    dist -= 0.1
  return dist

def create_Movie():
  Movies = pd.read_csv('./api/fixtures/movie_genre.csv', header=0)
  titles = Movies['title']
  Movies = Movies[label]
  Movies.head()
  return Movies, titles

def find_near_movie(movie):
  near_movie = min(movie)
  idx = movie.index(near_movie)

  return idx

@api_view(['GET', 'POST'])
def KNN_algorithm(request):
  input_movie = {"pk":3953, 
          "title":"test", 
          "genres":["Comedy","Romance"],
          "Casting":["Robert De Niro",
                      "Ben Stiller",
                      "Teri Polo",
                      "Blythe Danner"],
          "Director":"Jay Roach"}

  input_movie_genre = [0 for i in range(len(label)-1)];

  for genre in input_movie["genres"]:
    idx = label.index(genre)
    input_movie_genre[idx] = 1

  Movies, titles = create_Movie()
  Nearest_movie = []
  dist_movie = []

  input_movie_genre = np.array(input_movie_genre)
  for i in range(len(Movies)):
    temp = distance(input_movie, input_movie_genre, Movies.values[i], titles.values[i])
    dist_movie.append(temp)
  print(dist_movie)

  for i in range(5):
    idx = find_near_movie(dist_movie)
    Nearest_movie.append(idx)
    dist_movie[idx] = 100
  print(Nearest_movie)



