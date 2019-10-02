<template>
  <div>
    <v-container style="padding-top: 0;">
      <v-layout row align-center style="min-height: 100vh; min-width: 100vw; position: relative; background-size: cover; background-image: url('../../img/background.jpg');">
        <div id="container" style="margin-left: 15rem;">
          <p class="a" style="margin-bottom: 2.5rem; color: #fff; font-size: 5rem; font-family: 'Monoton', cursive; -webkit-animation: neon1 1.5s ease-in-out infinite alternate; -moz-animation: neon1 1.5s ease-in-out infinite alternate; animation: neon1 1.5s ease-in-out infinite alternate;">Fluid</p>
          <p style="color: white; font-size: 1.7rem; font-family: 'Jua', sans-serif;">당신과 함께 울고 웃는 movie mate :)</p>
          <!-- 1. 로그인 여부 -->
          <p v-if="!this.user"><router-link to="/users/signin" class="a">Let's start with us</router-link></p>
          <p v-else><router-link to="/users/signup" class="a">See you again</router-link></p>
        </div>
      </v-layout>
      <v-layout row wrap >
        <v-flex xs12>
          <!-- <h1>(1) 로그인하셨습니까?</h1> -->
          <!-- 1. 로그인 여부 -->
          <div v-if="this.user">
            <!-- 로그인 ID : {{this.user}}<br><br> -->

            <!-- 2, 3. 구독 여부 에 따른 (2), (3), (4) -->
            <div>
              <Subscription
                :user="user"
                :profile_data="profile_data"
                :now_date="now_date"
                :sub_date="subscription_date"
                :approval="this.user_data.approval"
              />
            </div>

          </div>

          <!-- (5) 단순한 영화 나열(조회수, 인기순) -->
          <!-- 대충 영화 10개 정도만..? 가져와봅시다! -->
          <v-layout row wrap pa-5>
            <h1> (5) 기능 : 단순 영화 나열입니다</h1>
            <v-flex>
              <carousel :per-page="pageNum">
                <slide v-for="(movie, index) in this.$store.state.data.movieList_homepage" style="height: 22rem; width: 15rem;">
                  <v-card style="margin:10px; height: 21rem; width: 15rem; border-radius:15px;" color="#424242" dark>
                      <v-img :src="movie.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:16rem; width: 15rem;"></v-img>
                      <v-card-text>
                        <!-- <v-container> -->
                        <div class="movietitle" :id="'movie'+index">
                          {{movie.title.substring(0, movie.title.indexOf("("))}}<br>
                          <span class="hovertext">{{movie.title.substring(0, movie.title.indexOf("("))}}</span>
                        </div>
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

            <v-layout row wrap pa-5>
            <h1>(6) 기능 : 유사 유저 리스트입니다</h1>
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
      if (this.$session.get('id')==undefined) {
        this.$session.set('id', '')
      }
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
<style>
  #container {
    width: 500px;
    margin: auto;
  }

  /*Neon*/
  p {
    text-align: center;
    font-size: 2.5rem;
    margin: 20px 0 20px 0;
  }

  .a {
    text-decoration: none;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
    transition: all 0.5s;
  }

  /* p:nth-child(1) .a {
    color: #fff;
    font-family: 'Monoton', cursive;
    -webkit-animation: neon1 1.5s ease-in-out infinite alternate;
    -moz-animation: neon1 1.5s ease-in-out infinite alternate;
    animation: neon1 1.5s ease-in-out infinite alternate;
  } */

  p:nth-child(3) .a {
    color: #FFDD1B;
    font-family: 'Pacifico', cursive;
  }

  p:nth-child(3) .a:hover {
    -webkit-animation: neon3 1.5s ease-in-out infinite alternate;
    -moz-animation: neon3 1.5s ease-in-out infinite alternate;
    animation: neon3 1.5s ease-in-out infinite alternate;
  }

  p .a:hover {
    color: #ffffff;
  }

  @-webkit-keyframes neon1 {
    from {
      text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #DD00FF, 0 0 70px #DD00FF, 0 0 80px #DD00FF, 0 0 100px #DD00FF, 0 0 150px #DD00FF;
    }
    to {
      text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #DD00FF, 0 0 35px #DD00FF, 0 0 40px #DD00FF, 0 0 50px #DD00FF, 0 0 75px #DD00FF;
    }
  }

  @-moz-keyframes neon1 {
    from {
      text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #DD00FF, 0 0 70px #DD00FF, 0 0 80px #DD00FF, 0 0 100px #DD00FF, 0 0 150px #DD00FF;
    }
    to {
      text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #DD00FF, 0 0 35px #DD00FF, 0 0 40px #DD00FF, 0 0 50px #DD00FF, 0 0 75px #DD00FF;
    }
  }

  @keyframes neon1 {
    from {
      text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #DD00FF, 0 0 70px #DD00FF, 0 0 80px #DD00FF, 0 0 100px #DD00FF, 0 0 150px #DD00FF;
    }
    to {
      text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #DD00FF, 0 0 35px #DD00FF, 0 0 40px #DD00FF, 0 0 50px #DD00FF, 0 0 75px #DD00FF;
    }
  }

  @-webkit-keyframes neon3 {
    from {
      text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #FFDD1B, 0 0 70px #FFDD1B, 0 0 80px #FFDD1B, 0 0 100px #FFDD1B, 0 0 150px #FFDD1B;
    }
    to {
      text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #FFDD1B, 0 0 35px #FFDD1B, 0 0 40px #FFDD1B, 0 0 50px #FFDD1B, 0 0 75px #FFDD1B;
    }
  }

  @-moz-keyframes neon3 {
    from {
      text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #FFDD1B, 0 0 70px #FFDD1B, 0 0 80px #FFDD1B, 0 0 100px #FFDD1B, 0 0 150px #FFDD1B;
    }
    to {
      text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #FFDD1B, 0 0 35px #FFDD1B, 0 0 40px #FFDD1B, 0 0 50px #FFDD1B, 0 0 75px #FFDD1B;
    }
  }

  @keyframes neon3 {
    from {
      text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #FFDD1B, 0 0 70px #FFDD1B, 0 0 80px #FFDD1B, 0 0 100px #FFDD1B, 0 0 150px #FFDD1B;
    }
    to {
      text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #FFDD1B, 0 0 35px #FFDD1B, 0 0 40px #FFDD1B, 0 0 50px #FFDD1B, 0 0 75px #FFDD1B;
    }
  }

</style>
