<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex>
        <!-- <h1>(2) 구독하셨습니까??</h1> -->
        <!-- {{this.profile_data.slice(1)}} -->

        <div v-if="this.approval">
          회원님의 구독 유효 기간은 {{sub_date}} 입니다.

          <div v-if="before_extend">
            <div v-for="amount in amounts" style="display:inline-block;">
              <input type="radio" :value="amount" v-model="picked_amount">
              <label style="font-size:10px;">{{amount}}</label> &nbsp;
            </div>
            <v-btn @click="extend_subscription()">구독 연장</v-btn>
          </div>

          <div v-else>
            연장 신청을 하였습니다.
          </div>

          <div id="item" style="display:none;">
            <h1>(3) 기능 : Itembased_movie 나열입니다</h1>
          </div>
          <v-layout row wrap>
            <v-flex>
              <carousel :per-page="pageNum">
                <slide v-for="movie in this.itembased_movies" style="height: 22rem; width: 15rem;">
                  <v-card style="margin:10px; height: 21rem; width: 15rem; border-radius:15px;" color="#424242" dark class="rounded-card">
                      <v-img :src="movie.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:16rem; width: 15rem;"></v-img>
                      <v-card-text>
                        <!-- <v-container> -->
                          <div class="movietitle">
                            {{movie.title.substring(0, movie.title.indexOf("("))}}<br>
                            <span class="hovertext">{{movie.title.substring(0, movie.title.indexOf("("))}}</span>
                          </div>
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

          <div id="user" style="display:none;">
            <h1>(4) 기능 : Userbased_movie 나열입니다</h1>
          </div>
          <v-layout row wrap>
            <v-flex>
              <carousel :per-page="pageNum">
                <slide v-for="movie in this.userbased_movies" style="height: 22rem; width: 15rem;">
                  <v-card style="margin:10px; height: 21rem; width: 15rem; border-radius:15px;" color="#424242" dark>
                      <v-img :src="movie.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:16rem; width: 15rem;"></v-img>
                      <v-card-text>
                        <!-- <v-container> -->
                        <div class="movietitle">
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





        </div>

        <div v-else>
          회원님은 구독 서비스를 이용한 적이 없어요~<br><br>
          <div v-if="before_create">
            <div v-for="amount in amounts" style="display:inline-block;">
              <input type="radio" :value="amount" v-model="picked_amount">
              <label style="font-size:10px;">{{amount}}</label> &nbsp;
            </div>
            <v-btn @click="create_subscription()">구독 신청</v-btn>
          </div>
          <div v-else>
            구독 신청을 하였습니다.
          </div>
        </div>

      </v-flex>


    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
import router from "../router";
import { Carousel, Slide } from 'vue-carousel';

export default {
  components:{
    Carousel,
    Slide
  },
  data: () => ({
    amounts: [30, 90],
    picked_amount:'',
    before_create : true,
    before_extend : true,
    userbased_movies:'',
    itembased_movies:'',
    pageNum: 4
  }),
  props : {
    profile_data : {
      type : Object | Array,
      default:[]
    },
    now_date : { type : String },
    sub_date : { type : String },
    approval : { type : Boolean },
  },
  watch: {
    profile_data() {
      this.getMovies_subscription()
      // console.log(this.profile_data)
    }
  },
  created() {
    // console.log(this.profile_data)
    // this.getMovies_subscription()
  },
  methods : {
    async getMovies_subscription() {
      // console.log(this.profile_data)
      const apiUrl = 'api'
      const id = this.$session.get('id_number')

      var itembased_movies = await axios.get(`${apiUrl}/subscription/itembasedmovies2/${id}`)
      this.itembased_movies = itembased_movies.data

      var userbased_movies = await axios.post(`${apiUrl}/subscription/userbasedmovies/${id}`, {resemble_users : this.profile_data.slice(1)})
      this.userbased_movies = userbased_movies.data

      if (this.profile_data[0].approval) {
        document.querySelector('#item').style.display = 'block';
        document.querySelector('#user').style.display = 'block';
      }


    },
    async create_subscription() {
      const apiUrl = '/api'
      var subscription = await axios.post(`${apiUrl}/subscription/create/`, {user : this.$session.get('id'), request:this.picked_amount})
      if (subscription.data) {
        //
        alert(subscription.data.message)

      }
      this.before_create = false
    },
    async extend_subscription() {
      const apiUrl = '/api'
      var subscription = await axios.post(`${apiUrl}/subscription/create/`, {user : this.$session.get('id'), request:this.picked_amount})
      if (subscription.data) {
        alert(subscription.data.message)
      }
      this.before_extend = false
    },
    SELECT_MovieDetail(movie) {
      var movie_data = {'id':movie.id, 'title':movie.title, 'genres_array':movie.genres_array,
                  'img':movie.img,'watch_count' : movie.watch_count, 'score_users':movie.score_users, 'averagerate':movie.averagerate,
                  'plot':movie.plot,'url':movie.url,'director':movie.director,'casting':movie.casting}

      router.push({name:'movie-detail', params : {'id':movie_data.id, 'movie_data':movie_data}})
      window.location.reload()
    }
  }
};
</script>

<style>
  .movietitle {
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
  }
  .movietitle .hovertext {
    visibility: hidden;
    /* width: 250px; */
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px;
    bottom: 20%;

    /* Position the tooltip */
    position: absolute;
    z-index: 1;
  }
  .movietitle:hover .hovertext {
    visibility: visible;
  }
</style>
