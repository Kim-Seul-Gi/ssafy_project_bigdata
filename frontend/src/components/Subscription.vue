<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex>
        <h1>(2) 구독하셨습니까??</h1>
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
            <v-flex v-for="movie in this.itembased_movies" style="margin-bottom: 2rem;" xs12 sm6 md4 lg3 xl2>

                <v-card style="margin:10px;">
                    <v-img :src="movie.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:25vw;"></v-img>
                    <v-card-text>
                      <v-container>
                        {{movie.title.substring(0, movie.title.indexOf("("))}}<br>
                        평점 : {{movie.averagerate}}
                        <v-btn text color="primary" @click="SELECT_MovieDetail(movie)">explore</v-btn>
                      </v-container>
                    </v-card-text>
                </v-card>
            </v-flex>
          </v-layout>

          <div id="user" style="display:none;">
            <h1>(4) 기능 : Userbased_movie 나열입니다</h1>
          </div>
          <v-layout row wrap>
            <v-flex v-for="movie in this.userbased_movies" style="margin-bottom: 2rem;" xs12 sm6 md4 lg3 xl2>

                <v-card style="margin:10px;">
                    <v-img :src="movie.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:25vw;"></v-img>
                    <v-card-text>
                      <v-container>
                        {{movie.title.substring(0, movie.title.indexOf("("))}}<br>
                        평점 : {{movie.averagerate}}
                        <v-btn text color="primary" @click="SELECT_MovieDetail(movie)">explore</v-btn>
                      </v-container>
                    </v-card-text>
                </v-card>
            </v-flex>
          </v-layout>





        </div>

        <div v-else>
          회원님은 구독 서비스를 이용한 적이 없어요~
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

export default {
  data: () => ({
    amounts: [30, 90],
    picked_amount:'',
    before_create : true,
    before_extend : true,
    userbased_movies:'',
    itembased_movies:'',

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

      var itembased_movies = await axios.get(`${apiUrl}/subscription/itembasedmovies/${id}`)
      this.itembased_movies = itembased_movies.data
      document.querySelector('#item').style.display = 'block';
      // console.log(itembased_movies.data)
      // console.log(this.profile_data)
      var userbased_movies = await axios.post(`${apiUrl}/subscription/userbasedmovies/${id}`, {resemble_users : this.profile_data.slice(1)})
      this.userbased_movies = userbased_movies.data
      document.querySelector('#user').style.display = 'block';
      // console.log(this.userbased_movies)

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
