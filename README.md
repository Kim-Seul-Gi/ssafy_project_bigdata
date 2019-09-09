# 빅데이터 스켈레톤(1주차)

## 목차

1. Clone, Setting
2. Page 소개



## 1. Clone, Setting

### (1) Clone

- Git clone (~/)

  ```bash
  $ git clone https://lab.ssafy.com/Kim-Seul-Gi/bigdata-sub1.git
  ```

### (2) Setting

- Backend ( ~/bigdata-sub1/backend)

  ```bash
  $ pip install -r requirements.txt
  $ python manage.py makemigraions
  $ python manage.py migrate
  $ python manage.py runserver
  ```

- Frontend ( ~/bigdata-sub1/frontend)

  ```bash
  $ npm install
  $ npm run serve
  ```



## 2. Page 소개

### (1) Backend 관련 (http://127.0.0.1:8000)

```python
# models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)

#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation']
    )

    return profile

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    watch_count = models.IntegerField(default=0)
    averagerate = models.IntegerField(default=0)

    score_users = models.ManyToManyField(User, through='Rate', related_name='score_movies')

    @property
    def genres_array(self):
        return self.genres.strip().split('|')

    def __str__(self):
        return f'{self.title}'

class Rate(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rate")
    MovieID = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="user_movie")
    rating = models.IntegerField(default=0)
    Timestamp = models.IntegerField()
```



- Admin 페이지 (ex, <http://127.0.0.1:8000/admin/>)

  - Api, Auth 관련 확인 가능

- Api 페이지

  - api/movies : 영화 전체 리스트 출력
  - api/movies/id값 : 특정 영화 데이터 출력

  - api/users : 유저 전체 리스트 출력
  - api/users/id값 : 특정 유저의 프로필 데이터 출력



### (2) Front 관련 (http://localhost:8080/)

- 영화 검색
  - 장르는 radio 버튼을 통해 검색 가능, 영화 이름으로 검색하기 가능
  - 검색은 엔터 클릭 또는 search 버튼을 통해 가능함
  - 검색을 하면 해당 내용이 조회 순으로 나열됨 (default)
  - 평점 순 버튼을 통해 평점 순으로 가능
  - 카드를 누르면 디테일 페이지로 이동함, 새로고침 누르면 django를 통해 db를 가져옴

- 유저 검색
  - 유저 이름을 통해 검색하기 가능
  - 엔터 클릭, search 로 가능
  - 순서나열은 따로 적용하지 않음
  - 카드를 누르면 유저 프로필 페이지로 이동함