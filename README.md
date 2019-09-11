# 빅데이터 스켈레톤(2주차)

## 목차

1. Clone, Setting
2. User Edit 
3. Subscription



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



## 2. User Edit 

### (1) POST요청 (http://127.0.0.1:8000)

```python
# user_views.py

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def detail(request, user_id):
    user = User.objects.get(pk=user_id)
    user_profile = Profile.objects.get(user=user)
    # ...
    
    elif request.method == 'POST':
        user_profile.username = request.data.get('username', None)
        user_profile.age = request.data.get('age', None)
        user_profile.gender = request.data.get('gender', None)
        user_profile.occupation = request.data.get('occupation', None)
        user_profile.save()
        return Response(status=status.HTTP_200_OK)
    
```

- mypage 내 edit 버튼을 누르면 modal 형태로 된 form 수정이 가능하도록 함

```javascript
// edit 버튼을 눌렀을 때

async edit() {
      let __this = this;
      const id = this.$session.get('id_number');
      const apiUrl = '/api';
      let tmp = await axios.post(`${apiUrl}/users/${id}`, {
        username: __this.username,
        gender: __this.gender,
        age: __this.age,
        occupation: __this.occupation
      }).then(async res => {
        var profile = await axios.get(`${apiUrl}/users/${id}`)
        this.profile_data = profile.data
        this.user = this.profile_data[0]
      })
    }

```



## 3. Subscription

### (1) model 정의

```python
# models.py

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)
    approval = models.BooleanField(default=False)
    subscription = models.DateTimeField(default=datetime.datetime.now() - datetime.timedelta(days=1))

class Subscription_manager(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_sub")
    request = models.IntegerField(default=0)
    approval = models.BooleanField(default=False)
    request_day = models.DateTimeField(auto_now_add=True)
    apply_day = models.DateTimeField(auto_now=True)

    # ...
```

