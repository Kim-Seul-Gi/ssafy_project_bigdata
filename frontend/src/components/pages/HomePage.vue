<template>
  <div>
    <v-layout row align-center style="min-height: 100vh; position: fixed; top: 0; left: 0; background-size: cover; background-image: url('img/background.jpg');">
    </v-layout>
    <v-container>
      <v-layout row wrap>
        <v-flex xs12>

          <!-- <span class="display-3 grey--text">Select menu</span> -->

          <!-- Homepage에서 보여주고자 하는 기능들은 아래와 같습니다. -->
              <!-- (1) 로그인 하셨습니까? -->
              <!-- (2) 구독 관리 -->
              <!-- (3) MovieBased 영화 추천 -->
              <!-- (4) UserBased 영화 추천 -->
              <!-- (5) 단순한 영화 나열(조회수, 인기순) -->
              <!-- (6) 단순한 유사유저 리스트 -->


          <!-- 유저의 상태는 로그인 여부(this.user) / 구독 여부(Subscription) 에서 다룹니다. -->
              <!-- 1. 로그인 X / 보여줄 기능 : (1), (5) -->
              <!-- 2. 로그인 O , 구독 X / 보여줄 기능 : (1), (2), (5), (6) -->
              <!-- 3. 로그인 O , 구독 O / 보여줄 기능 : (1), (2), (3), (4), (5), (6) -->

          <!-- <h1>(1) 로그인하셨습니까?</h1> -->
          <!-- 1. 로그인 여부 -->
          <div v-if="!this.user">
            <!-- 로그인을 하지 않았습니다!! -->
            로그인을 하시면 영화를 추천해드릴게요.<br>
            클러스터링 알고리즘 을 이용하여 영화를 추천합니다.<br>
            사용된 알고리즘 : K-means, H, EM, MatrixFactorization<br><br>
            <!-- (1) 로그인 하러가기 -->
            <!-- <v-btn @click="goTo()">로그인하기</v-btn> -->

          </div>

          <div v-else>
            로그인 ID : {{this.user}}<br><br>

            <!-- 2, 3. 구독 여부 에 따른 (2), (3), (4) -->
            <div>
              <Subscription
                :profile_data="profile_data"
                :now_date="now_date"
                :sub_date="subscription_date"
                :approval="this.user_data.approval"
              />
            </div>

          </div>

          <!-- (5) 단순한 영화 나열(조회수, 인기순) -->
          <!-- 대충 영화 10개 정도만..? 가져와봅시다! -->
          <h1> (5) 기능 : 단순 영화 나열입니다</h1>
          <v-layout row wrap>
            <v-flex>
              <carousel :per-page="pageNum">
                <slide v-for="movie in this.$store.state.data.movieList_homepage" style="height: 21rem; width: 15rem;">
                  <v-card style="margin:10px; height: 20rem; width: 15rem;" color="#424242" dark>
                      <v-img :src="movie.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:16rem; width: 15rem;"></v-img>
                      <v-card-text>
                        <!-- <v-container> -->
                          <!-- {{movie.title.substring(0, movie.title.indexOf("("))}}<br> -->
                          <i class="fas fa-star" style="color: #FFB600; margin-right: 0.5rem;"></i><span>평점 </span><span style="font-weight: bold;">{{movie.averagerate}}</span>
                          <v-btn text color="primary" @click="SELECT_MovieDetail(movie)" style="padding-right: 0; margin-left: 2rem; margin-right: 0;">explore</v-btn>
                        <!-- </v-container> -->
                      </v-card-text>
                  </v-card>
                </slide>
              </carousel>
            </v-flex>
          </v-layout>

          <div v-if="this.user">
            <!-- (6) 유사 유저는 여기에서 가져올 수 있네요..?! -->
            <h1>(6) 기능 : 유사 유저 리스트입니다</h1>
            <v-layout row wrap>
              <v-flex>
                <carousel :per-page="pageNum">
                  <slide v-for="person in this.profile_data.slice(1)" style="height: 21rem; width: 15rem;">
                    <v-card style="margin:10px; height: 20rem; width: 15rem;" color="#424242" dark>
                        <v-card-text>
                          <v-container>
                            <p style="color: black; font-size: 1.4rem;">id: {{person.id}}, {{ person.username }}</p>
                            <p>{{ person.age }} / {{ person.gender }}</p>
                            <p>{{ person.occupation }}</p>
                            <v-btn text color="primary" @click="SELECT_UserDetail(person.id, person.username)">explore</v-btn>
                          </v-container>
                        </v-card-text>
                    </v-card>
                  </slide>
                </carousel>
              </v-flex>
            </v-layout>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../../router";
import axios from 'axios'
import Subscription from "../Subscription";
import { Carousel, Slide } from 'vue-carousel';

export default {
  components:{
    Subscription,
    Carousel,
    Slide
  },
  data() {
    return {
      user:'',
      profile_data:'',
      user_data:'',
      subscription_date:'',
      now_date:'',
      movie_row: '',
      pageNum: 4
    }
  },
  computed: {
  },
  created() {
    this.getMovies_homepage()
    this.fetchdata()
  },
  methods : {
    ...mapActions("data", ["getMovies_homepage"]),
    // getmoveis 는 단순 영화 나열을 위한 것입니다 = 로그인 여부와 관련 없는 것.
    async fetchdata() {
      this.user = this.$session.get('id')
      if (this.$session.get('id')=='') {
      } else {
        const apiUrl = '/api';
        const id = this.$session.get('id_number')
        var profile = await axios.get(`${apiUrl}/users/${id}`)
        this.profile_data = profile.data
        // 구독 날짜 확인하기,
        // 오늘 날짜 : this.now_date , ex) 20190910
        // 회원의 구독 날짜 : this.subscription_date, ex) 20190801
        this.user_data = this.profile_data[0]
        this.subscription_date = this.user_data.subscription.substring(0, 10).replace(/-/g,'')
        var now = new Date()
        var year = now.getFullYear()
        var month = now.getMonth() + 1
        var date = now.getDate()
        if ( month < 10 ) {
          month = '0' + String(month)
        } else {
          month = String(month)
        }
        if ( date < 10) {
          date = '0' + String(date)
        } else {
          date = String(date)
        }
        this.now_date = String(year)+month+date
      }
    },
    SELECT_MovieDetail(movie) {
      var movie_data = {'id':movie.id, 'title':movie.title, 'genres_array':movie.genres_array,
                  'img':movie.img,'watch_count' : movie.watch_count, 'score_users':movie.score_users, 'averagerate':movie.averagerate,
                  'plot':movie.plot,'url':movie.url,'director':movie.director,'casting':movie.casting}

      router.push({name:'movie-detail', params : {'id':movie_data.id, 'movie_data':movie_data}})
      window.location.reload()
    },
    SELECT_UserDetail(id, username) {
      var user_data = {'id':id, 'username':username}
      router.push({name:'user-detail', params : {'id':user_data.id, 'user_data':user_data}})
    },
    goTo() {
      router.push({name:"sign-in"})
    }
  }
}
</script>
