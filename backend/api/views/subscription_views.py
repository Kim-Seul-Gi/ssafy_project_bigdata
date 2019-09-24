from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from api.models import Profile, Subscription_manager, Rate, Cluster, Movie
from rest_framework.response import Response
from api.serializers import SubscriptionSerializer, MovieSerializer
import datetime
import pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import normalize, StandardScaler
import random

@api_view(['POST'])
def create(request):
    if request.method == 'POST':

    # Subscription_manager 이라는 모델에 생성을 해야 한다.
        username = request.data.get('user')
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)

        check_subscription_request = Subscription_manager.objects.filter(Profile=profile, approval=False)
        if check_subscription_request:
            message = {'message':'이미 구독 신청을 한 상태입니다.'}
            return Response(data=message, status=status.HTTP_200_OK)
        else:
            subscription_request = Subscription_manager.objects.create(
                Profile=profile,
                request=request.data.get('request'),
                approval=False,
            )
            return Response(status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def manager(request):
    if request.method == 'GET':
        subscriptions = Subscription_manager.objects.filter(approval=False)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        subscription = request.data.get('subscription')
        profile = Profile.objects.get(pk=subscription['Profile'])

        # 1. Profile 변경 (처음 신청했을 때, 만료 이후 재신청했을 때, 연장신청했을 때 모두 여기에 해당한다.)

        if profile.subscription.strftime("%Y%m%d") > datetime.datetime.now().strftime("%Y%m%d"):
            # 이것이 바로 연장
            profile.subscription = profile.subscription + datetime.timedelta(days=subscription['request'])
            profile.save()
        else:
            # 이것은 처음 신청, 또는 만료 이후 다시 신청
            profile.approval = True
            profile.subscription = datetime.datetime.now() + datetime.timedelta(days=subscription['request'])
            profile.save()

        # 2. Subscription_manager 에서 해당 객체 승인 되었다고 변경
        subscription_instance = Subscription_manager.objects.get(pk=subscription['id'])
        subscription_instance.approval = True
        subscription_instance.save()

        return Response(status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def getmovies(request, profile_pk):
    # 이 함수는 구독서비스를 이용하는 사용자에게 itembased 추천을 하는 함수입니다.
    #
    profile = Profile.objects.get(pk=profile_pk)

    rates = Rate.objects.filter(UserID=profile.user.id).order_by('-rating')[:5]

    # rate 의 영화를 조회하여 해당 영화의 장르 평점을 담기 위한 것 : box
    # rate 는 일차배열입니다.
    box = [0]*18
    genre_number = {'Action':0,'Adventure':1,'Animation':2,"Children's":3,'Comedy':4,
                       'Crime':5,'Documentary':6,'Drama':7,'Fantasy':8,'Film-Noir':9,
                       'Horror':10, 'Musical':11, 'Mystery':12,'Romance':13,'Sci-Fi':14,
                       'Thriller':15,'War':16,'Western':17}
    for rate in rates:
        genres = rate.MovieID.genres.strip().split('|')
        # print(genres)
        for genre in genres:
            box[genre_number[genre]] += 1/5

    # User 의 영화 장르 평점입니다! 이걸 이용해서 클러스링 돌리고 친구들 가져옵시다!
    # print(box)

    cluster = Cluster.objects.get(pk=1)
    cluster_n = cluster.n_component
    cluster_way = cluster.way

    # n : 7, way : K

    # 1. csv 가져오기 > 배열이잖아?
    # 2. 배열에 box 추가하고
    # 3. 클러스터링 돌리고
    # 4. 마지막 클러스터링 넘버랑 같은 넘버 영화를 가져온다 > 이 때 단축평가 [x for x in range()] 이런거 사용
    # 이게 오래걸린다면...?!?!


    # data = pd.read_csv("../data/movie_clu.csv")
    data = pd.read_csv("./api/fixtures/movie_clu.csv")

    data_slice = data[['Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']]

    # print(data_slice[-1:][:])
    data_slice.loc[3883,:] = box
    # print(data_slice[-1:][:])

    data_scaled = StandardScaler().fit_transform(data_slice)
    df = pd.DataFrame(data_scaled)

    model = GaussianMixture(n_components=5, max_iter=20, random_state=0, covariance_type='spherical').fit(df)
    y_predict = model.fit_predict(df)

    cluster_number = y_predict[-1]


    cluster_movies = [data[x:x+1].values[0][-1] for x in range(len(y_predict)-1) if y_predict[x]==y_predict[-1]]
    pick_movies = random.sample(cluster_movies, k=30)

    movies = Movie.objects.filter(title__in=pick_movies).order_by('-watch_count')
    serializer = MovieSerializer(movies, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
