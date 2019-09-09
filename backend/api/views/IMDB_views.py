from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rate, Cluster, Profile
from api.serializers import MovieSerializer, Movie_Age_Serializer
from rest_framework.response import Response
from django.db.models import Avg
import pandas as pd
import random

from imdb import IMDb

@api_view(['GET', 'POST', 'DELETE'])
def getmovies(request):

    # create an instance of the IMDb class
    ia = IMDb()

    # setting movies
    movies = Movie.objects.all()[27:100]
    # print(movies)

    a = []
    cnt = 1
    for mov in movies:
        name = mov.title
        # 뭐든 없는게 있을거다 믿지마라 그러므로 value는 get으로 꺼내자
        getmovie = ia.search_movie(name)
        if getmovie:
            movieid = getmovie[0].movieID
            movie = ia.get_movie(movieid)
            
            title = movie.data.get('original title')
            print('title : {}'.format(title))

            # castings = movie.data.get('cast')
            # casting = []
            # for i in castings:
            #     casting.append(i['name'])
            # print('castings : {}'.format(casting))

            url = movie.data.get('cover url')
            print(url)
            # url = url[:url.index('._V1')] + '._V1_SY1000_SX670_AL_.jpg'
            # print('cover url : {}'.format(url))
            # @._V1_SX101_CR0,0,101,150_.jpg -> @._V1_SY1000_SX670_AL_.jpg

            # director = movie.data.get('directors')
            # if director:
            #   direcor = director[0]
            # print('director : {}'.format(director))
            # # print(movie.data) # data.get('plot')
            # plot = movie.data.get('plot')
            # if plot:
            #     plot = plot[0]
            #     if '::' in plot:
            #         plot = plot[:plot.index('::')]
            # print('plot : {}'.format(plot))

            # cnt += 1
            # print()
            # print()
            # print()
            # print()
            # print()
        else:
            print(name, '999999999999i')

    print('끝')
    return Response(status=status.HTTP_200_OK)
