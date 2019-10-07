from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile, Profile, User
from api.serializers import ProfileSerializer
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
def signup_many(request):
  print("회원가입!")
  if request.method == 'POST':
      profiles = request.data.get('profiles', None)
      for profile in profiles:
          username = profile.get('username', None)
          password = profile.get('password', None)
          age = profile.get('age', None)
          occupation = profile.get('occupation', None)
          gender = profile.get('gender', None)

          create_profile(username=username, password=password, age=age,
                          occupation=occupation, gender=gender)

      return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def signup(request):
  if request.method == 'POST':
      name = request.data.get('username', None)
      if(User.objects.filter(username=name)):
        return Response(data=False, status=status.HTTP_201_CREATED)
        
      age = request.data.get('age', None)
      gender = request.data.get('gender', None)
      occupation = request.data.get('occupation', None)
      password = request.data.get('password')
      create_profile(username=name, password=password, age=age, occupation=occupation, gender=gender)

      return Response(data=True, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def signin(request):
    if request.method == 'POST':
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            data = {'user': username, 'id_number':user.id, 'admin':user.is_superuser}
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = {'user': '', 'admin':False}
            return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def userstate(request):
    if request.user.is_authenticated:
        user = request.user
        data = {'user': user.username}
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        data = {'user': ''}
        return Response(data=data, status=status.HTTP_200_OK)

@login_required
def logout(request):
    user = request.user
    auth_logout(request)
    return Response(status=status.HTTP_200_OK)