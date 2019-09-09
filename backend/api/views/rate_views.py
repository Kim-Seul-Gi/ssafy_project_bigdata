from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rate, Profile
from api.serializers import MovieSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['GET', 'POST', 'DELETE'])
def ratings(request):
 	# if request.method == 'GET':
    #     id = request.GET.get('id', request.GET.get('movie_id', None))
    #     title = request.GET.get('title', None)
	#
    #     movies = Movie.objects.all()
	#
    #     if id:
    #         movies = movies.filter(pk=id)
    #     if title:
    #         movies = movies.filter(title__icontains=title)
	#
    #     serializer = MovieSerializer(movies, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

	if request.method == 'POST':
		rating_data = request.data.get('ratings', None)
		for rating in rating_data:

			UserID = rating.get('UserID', None)
			MovieID = rating.get('MovieID', None)
			Rating = rating.get('Rating', None)
			Timestamp = rating.get('Timestamp', None)
			
			Rate(UserID=Profile.objects.get(pk=UserID),
				MovieID=Movie.objects.get(pk=int(MovieID)),
				rating=Rating, Timestamp=Timestamp).save()

		return Response(status=status.HTTP_200_OK)