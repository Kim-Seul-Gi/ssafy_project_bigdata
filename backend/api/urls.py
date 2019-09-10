from django.urls import path
from api.views import movie_views
from api.views import auth_views
from api.views import rate_views
from api.views import user_views
from api.views import admin_views

from api.views import Kmeans_views
from api.views import Hcluster_views
from api.views import EMcluster_views

from api.views import cluster_views
from api.views import subscription_views
urlpatterns = [
    # user 관리
    path('auth/signup-many/', auth_views.signup_many, name='sign_up_many'),
    path('auth/signup/', auth_views.signup, name='sign_up'),
    path('auth/signin/', auth_views.signin, name='sign_in'),
    path('auth/userState/', auth_views.userstate, name='user_state'),
    path('auth/logout/', auth_views.logout, name='logout'),
    # path('auth/logout/', auth_views.logout, name='user_state'),

    path('movies/', movie_views.movies, name='movie_list'),
    path('movies/<int:movie_id>', movie_views.detail, name='movie_datail'),

    path('users/', user_views.users, name='user_list'),
    path('users/<int:user_id>', user_views.detail, name='user_list'),

    # parse_data / rating 관련
    path('ratings/', rate_views.ratings, name='rate_list'),

    # search 관련
    path('genres/', movie_views.genres, name="movies_by_genre"),
    path('ages/', movie_views.ages, name="movies_by_age"),
    path('occupations/', movie_views.occupations, name="movies_by_occupation"),
    path('genders/', movie_views.genders, name="movies_by_gender"),

    # user 및 movie UD
    path('movie/<int:movie_pk>/update/', admin_views.movie_update, name='movie_update'),
    path('movie/<int:movie_pk>/delete/', admin_views.movie_delete, name='movie_delete'),
    path('profile/<int:user_pk>/update/', admin_views.profile_update, name='profile_update'),
    path('profile/<int:user_pk>/delete/', admin_views.profile_delete, name='profile_delete'),

    path('movies/getarray/', movie_views.getarray, name="getarray"),
    path('cluster/hcluster/user/', Hcluster_views.user_hcluster, name="hcluster_user"),
    path('cluster/hcluster/movie/', Hcluster_views.movie_hcluster, name="hcluster_movie"),
    path('cluster/emcluster/user/', EMcluster_views.user_emcluster, name="emcluster_user"),
    path('cluster/emcluster/movie/', EMcluster_views.movie_emcluster, name="emcluster_movie"),

    # # Kmeans_clustering DB 추가
    # path('km_clu/movie/', Kmeans_views.create_movie_clu, name="movie_kmclu"),
    # path('km_clu/movie/delete/', Kmeans_views.delete_movie, name="movie_delete"),
    # path('km_clu/user/', Kmeans_views.create_user_clu, name="user_kmclu"),
    # path('cluster/km/movie/', Kmeans_views.kmeans_movie, name="kmeans_movie"),

    # cluster 관련 정보를 조회, 변경합니다.
    path('cluster/', cluster_views.cluster, name='cluster'),

    # # subscription 관련 정보를 생성, 관리 합니다.
    # create : 유저가 구독신청하기
    # apply : 관리자가 구독관련된 것을 적용하기
    path('subscription/create/', subscription_views.create, name='subscription_create'),
    path('subscription/manager/', subscription_views.manager, name="subscription_manager"),

]
