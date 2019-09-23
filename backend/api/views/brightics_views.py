from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rate

from django.core import serializers
from rest_framework.response import Response
import pandas as pd

@api_view(['GET', 'POST', 'DELETE'])
def make(request):

    ## 1. 변수 정의
    # 1-1. array : array 에 있는 데이터를 csv로 변환할 것입니다.
    # 예시 array[0] = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Toy Story (1995)']
    # toy story라는 영화는 0011100000000000이라는 장르데이터를 가진다는 것을 의미합니다.

    # 하나의 영화가 어떠한 장르를 포함하는지 0, 1로 표시할 것이며 행에는 하나의 영화 데이터를 넣을 것입니다.
    # 열에는 장르 이름을 의미합니다.
    array = []

    # 1-2. genre_number: array에 들어가는 장르의 인덱스입니다. ( 열 ) / 총 19개(18+영화이름넣을공간1) 입니다.
    genre_number = {'Action':0,'Adventure':1,'Animation':2,"Children's":3,'Comedy':4,'Crime':5,'Documentary':6,
                    'Drama':7,'Fantasy':8,'Film-Noir':9, 'Horror':10, 'Musical':11, 'Mystery':12,
                    'Romance':13,'Sci-Fi':14,'Thriller':15,'War':16,'Western':17}

    ## 2. array 만들기
    # 2-1. 전체 영화를 가져오고, 총 몇개의 영화인지 확인합니다.
    movies = Movie.objects.all()
    # last_movie_id = movies[len(movies)-1].id
    movies_count = len(movies)
    '''
    id,Action,Adventure,Animation,Children's,Comedy,Crime,Documentary,Drama,Fantasy,Film-Noir,Horror,Musical,Mystery,Romance,Sci-Fi,Thriller,War,Western
    '''
    # 2-2. 하나의 영화데이터를 tmp_array 에 담아서 array로 보내기.
    for i in range(movies_count):
        # print(movies[i], '이게 정보이다.')
        tmp_array = [0]*19
        tmp_array[0]=movies[i].id
        # tmp_array[1]=movies[i].title
        movie_genres = movies[i].genres.split('|')

        for j in range(len(movie_genres)):
            # print(movie_genres[j], end=' ')
            # print(genre_number[movie_genres[j]]+2, end=' ')
            tmp_array[genre_number[movie_genres[j]]+1] = 1

        array.append(tmp_array)

    # 2-3. csv 파일로 array 를 저장하자.
    df = pd.DataFrame(array)
    df.to_csv("test.csv", header=None, index=None)

    return Response(status=status.HTTP_200_OK)





    # serializer = MovieSerializer(movies, many=True)
    # print(type(serializer))
    # print(serializer)
    # print(len(serializer))

    # return Response(data=serializer.data, status=status.HTTP_200_OK)
