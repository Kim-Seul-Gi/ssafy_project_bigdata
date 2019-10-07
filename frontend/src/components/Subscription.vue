<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex v-if="this.user != 'admin'">
        <!-- <h1>(2) 구독하셨습니까??</h1> -->
        <!-- {{this.profile_data.slice(1)}} -->

        <div v-if="this.approval" class="mx-auto">
          <v-card v-if="before_extend" color="#424242" dark class="mx-3 my-3 px-8 py-3">
            <v-card-title style="font-size: 1.2rem;">{{this.user}}님의 구독 유효 기간 <span style="padding-left: 0.7rem;">{{sub_date}}</span></v-card-title>
            <v-card-text>
            <v-radio-group v-model="picked_amount" style="display:inline-block;" row>
              <v-radio value=30 label="30 days" color=""></v-radio>
              <v-radio value=90 label="90 days" color=""></v-radio>
              <!-- <label style="font-size:10px;">{{amount}}</label> &nbsp; -->
            </v-radio-group>
            <v-btn @click="extend_subscription()" style="margin-left: 0.7rem;">구독 연장</v-btn>
            </v-card-text>
          </v-card>

          <v-card v-else color="#424242" dark class="mx-3 my-3  px-3 py-3">
            <v-card-text>연장 신청이 완료되었어요. 관리자 승인 중입니다. :)</v-card-text>
          </v-card>

          <!-- <div id="item" style="display:none;"> -->
          <v-layout row wrap pa-8>
            <div id="item">
              <span style="color: white; font-size: 1.7rem; margin-left: 0.9rem; font-family: 'Jua', sans-serif;"><v-icon size="2rem" color="white">mdi-movie</v-icon> {{this.user}}님을 위한 영화 추천</span>
            </div>
            <v-flex>
              <carousel :per-page="pageNum">
                <slide v-for="movie in this.$store.state.data.movieList_homepage_itembased" style="height: 22rem; width: 15rem;">
                  <v-card style="margin:10px; height: 21rem; width: 15rem; border-radius:15px;" color="#424242" dark class="rounded-card">
                      <v-img :src="movie.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:16rem; width: 15rem;"></v-img>
                      <v-card-text>
                        <!-- <v-container> -->
                          <div class="movietitle">
                            {{movie.title.substring(0, movie.title.indexOf("("))}}<br>
                            <span class="hovertext" style="vertical-align: middle;">{{movie.title.substring(0, movie.title.indexOf("("))}}</span>
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

          <!-- <div id="user" style="display:none;"> -->
          <v-layout row wrap pa-8>
            <div id="user">
              <span style="color: white; font-size: 1.7rem; margin-left: 0.9rem; font-family: 'Jua', sans-serif;"><v-icon size="2rem" color="white">mdi-movie</v-icon> 유사한 사용자의 선호 영화</span>
            </div>
            <v-flex>
              <carousel :per-page="pageNum">
                <slide v-for="movie in this.$store.state.data.movieList_homepage_userbased" style="height: 22rem; width: 15rem;">
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

        <div v-else class="mx-auto">
          <v-card v-if="before_create" color="#424242" dark class="mx-3 my-3 px-8 py-3">
            <v-card-text>
              <p style="font-size: 1rem; text-align: left;">{{this.user}}님은 구독 서비스를 이용한 적이 없어요.</p>
              <p style="font-size: 1rem; text-align: left;">영화 추천을 위한 구독을 원하시나요?</p>
              <v-radio-group v-model="picked_amount" style="display:inline-block;" row>
                <v-radio value=30 label="30 days" color=""></v-radio>
                <v-radio value=90 label="90 days" color=""></v-radio>
                <!-- <label style="font-size:10px;">{{amount}}</label> &nbsp; -->
              </v-radio-group>
              <v-btn @click="create_subscription()" style="margin-left: 0.7rem;">구독 신청</v-btn>
            </v-card-text>
          </v-card>
          <v-card v-else color="#424242" dark class="mx-3 my-3 px-3 py-3">
            <v-card-text>구독 신청이 완료되었어요. 관리자 승인 중입니다 :)</v-card-text>
          </v-card>
        </div>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
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
    user : { type : String },
    sub_date : { type : String },
    approval : { type : Boolean },
  },
  watch: {
    profile_data() {
      // this.getMovies_subscription()
      // const id = this.$session.get(id_number)
      const params = {
        id : this.$session.get('id_number'),
        approval : this.profile_data[0].approval,
        resemble_users : this.profile_data.slice(1)
      }
      // console.log(this.profile_data[0].approval)
      this.getMovies_subscription_itembased(params)
      this.getMovies_subscription_userbased(params)
      // this.getMovies_subscription_userbased()
      // console.log(this.profile_data)
    }
  },
  created() {
    // console.log(this.profile_data)
    // this.getMovies_subscription()
  },
  methods : {
    ...mapActions("data", ["getMovies_subscription_itembased", "getMovies_subscription_userbased"]),
    // async getMovies_subscription() {
    //   // console.log(this.profile_data)
    //   const apiUrl = 'api'
    //   const id = this.$session.get('id_number')
    //
    //   var itembased_movies = await axios.get(`${apiUrl}/subscription/itembasedmovies2/${id}`)
    //   this.itembased_movies = itembased_movies.data
    //
    //   var userbased_movies = await axios.post(`${apiUrl}/subscription/userbasedmovies/${id}`, {resemble_users : this.profile_data.slice(1)})
    //   this.userbased_movies = userbased_movies.data
    //
    //   if (this.profile_data[0].approval) {
    //     document.querySelector('#item').style.display = 'block';
    //     document.querySelector('#user').style.display = 'block';
    //   }
    //
    //
    // },
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
    white-space:normal;
    /* Position the tooltip */
    position: absolute;
    z-index: 1;
  }
  .movietitle:hover .hovertext {
    visibility: visible;
  }
</style>
