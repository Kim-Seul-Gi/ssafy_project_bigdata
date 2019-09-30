from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Profile, Rate
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

@api_view(['PUT', 'POST', 'DELETE'])
def cduRating(request, movie_pk):
  rates = Rate.objects.filter(MovieID=movie_pk)
  user_pk = request.objects.get("user_pk")
  profile = Profile.objects.get(user=user_pk)
  rate = rates.filter(UserID=profile.pk)
  if request.method == "POST":
    if(rate!=[]):
      return Response(data=False, status=status.HTTP_200_OK)
    else:
      score = request.data.get("score")
      Rate(UserID=profile,
				MovieID=Movie.objects.get(pk=movie_pk),
				rating=score, Timestamp=0).save()
  elif request.method == "DELETE":
    if(rate==[]): 
      return Response(data=False, status=status.HTTP_200_OK)
    else:
      rate.delete()
  elif request.method == "PUT":
    if(rate==[]):
      return Response(data=False, status=status.HTTP_200_OK)
    else:
      rate.rating = score
      rate.save()
  return Response(data=True, status=status.HTTP_200_OK)
