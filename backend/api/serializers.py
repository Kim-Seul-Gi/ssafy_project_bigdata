from django.contrib.auth.models import User
from .models import Profile, Movie, Rate
from rest_framework import serializers
from django.db.models import Avg

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation')

    def get_username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff

class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    averagerate = serializers.SerializerMethodField('get_averagerate')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', 'watch_count', 'score_users', 'averagerate')

    def get_averagerate(self, obj):

        ## version 1
        average_rate = Rate.objects.filter(MovieID=obj.id).aggregate(Avg('rating'))
        if average_rate['rating__avg']!=None:
            return round(average_rate['rating__avg'], 2)
        else:
            return 0
        ##

        ## version 2
        # result = 0
        # count = 0
        # movie = Movie.objects.get(pk=obj.id)
        # rates = movie.rate_set.all()
        # for rate in rates:
        #     count += 1
        #     result += rate.rating
        # # print(type(obj.id), '2') 이건 그거 자체
        # if count==0:
        #     return 0
        # else:
        #     print(result/count, obj.title)
        #     return result/count

class Movie_Age_Serializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    title = serializers.SerializerMethodField('get_title')
    genres_array = serializers.SerializerMethodField('get_genres_array')
    watch_count = serializers.SerializerMethodField('get_watch_count')
    averagerate = serializers.SerializerMethodField('get_averagerate')

    class Meta:
        model = Movie
        # fields = ('id', 'title', 'genres_array', 'watch_count', 'averagerate')
        fields = ('id', 'title', 'genres_array','watch_count','averagerate')
    def get_id(self, obj):
        return obj['MovieID']
    def get_title(self, obj):
        return obj['MovieID__title']
    def get_genres_array(self, obj):
        return obj['MovieID__genres']
    def get_watch_count(self, obj):
        return obj['MovieID__watch_count']
    def get_averagerate(self, obj):
        return obj['rating__avg']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields =  "__all__"
        fields = ('id', 'username')
