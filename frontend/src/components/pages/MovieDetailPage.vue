<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 by 영화이름-->
      <v-flex>
        <div style="color:rgb(255,255,255)">No. {{movie_data[0].id}}</div>
        <v-card class="mx-auto" max-width="600px" color="#424242" dark>
          <v-img :src="movie_data[0].url"
            height="400px" contain
          ></v-img>
          <v-col>
            <h1>{{movie_data[0].title}}</h1>
            <div v-if="this.$session.get('id_number')!=''">
              <v-btn icon v-if="!this.rate_flag" @click="rate_show=!rate_show">{{rate_show ? 'cancel' : '평점 남기기'}}</v-btn>
              <v-btn icon v-if="this.rate_flag" @click="rate_show=!rate_show">{{rate_show ? 'cancel' : '평점 수정하기'}}</v-btn>
            </div>
            <v-flex v-show="rate_show">
              <div class="mx-auto" style="width:200px">
                <v-text-field
                  v-model="score"
                  label="score"
                  :rules="scoreRules"
                  type="number"
                  required>
                </v-text-field>
                <v-btn v-if="!this.rate_flag" @click="createRating(movie_data[0].id)">등록</v-btn>
                <v-btn v-if="this.rate_flag" @click="deleteRating(movie_data[0].id)">삭제</v-btn>
                <v-btn v-if="this.rate_flag" @click="updateRating(movie_data[0].id)">수정</v-btn>
                <v-btn @click="rate_show = !rate_show">취소</v-btn>
              </div>
            </v-flex>
            <div class="grey--text">{{movie_data[0].averagerate}} ({{movie_data[0].watch_count}})</div>
            <div class="grey--text">Director: {{movie_data[0].director}}</div>
          </v-col>
          <!-- {{this.movie_data[0].castings.split("|")}} -->
          {{this.castingList}}
          <!-- {{this.movie_data[0].castings}} -->
          <br>
          <v-btn icon @click="show = !show">
            <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
          </v-btn>

          <v-expand-transition>
            <div v-show="show">
              <v-card-text>{{movie_data[0].plot}}</v-card-text>
            </div>
          </v-expand-transition>
        </v-card>
        <p style="font-size: 3rem; color: white; font-family: 'Jua', sans-serif;">
          Similar Movies</p>
      </v-flex>



      <v-flex>
        <carousel :per-page="4">
          <slide v-for="movie in this.movie_data.slice(1)" style="height: 22rem; width: 15rem;">
            <v-card style="margin:10px; height: 21rem; width: 15rem; border-radius:15px;" color="#424242" dark>
              <v-img contain :src="movie.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:16rem; width: 15rem;"></v-img>
              <v-card-text>
                <div class="movietitle">
                  <!-- {{movie.title.substring(0, movie.title.indexOf("("))}}<br> -->
                  <!-- <span class="hovertext">{{movie.title.substring(0, movie.title.indexOf("("))}}</span> -->
                </div>
                  <i class="fas fa-star" style="color: #FFB600; margin-right: 0.5rem;"></i><span>평점 </span><span style="font-weight: bold;">{{movie.averagerate}}</span>
                  <v-btn text color="primary" @click="SELECT_MovieDetail(movie)" style="padding-right: 0; margin-left: 2rem; margin-right: 0;">explore</v-btn>
                </v-card-text>
              </v-card>
            </slide>
          </carousel>
        </v-flex>



      </v-layout>

    <v-btn @click="search()">검색으로 이동</v-btn>
  </v-container>
</template>

<script>
import router from "../../router";
import axios from 'axios'
import { Carousel, Slide } from 'vue-carousel';

export default {
  components: {
    Carousel,
    Slide
  },
  props: {
    id : {type:Number | String},
    // movie_data : {type:Object}
  },
  data: () => ({
    score: 0.0,
    show: false,
    rate_show: false,
    scoreRules: [
      v => (v < 6) || 'score is maximum of 5',
    ],
    castingList: [],
    movie_data:[
      {"id":''},
      {"averagerate":''},
      {"castings":''},
      {"director":''},
      {"genres_array":''},
      {"plot":''},
      {"score_users":''},
      {"title":''},
      {"url":''},
      {"watch_count":''}
    ],
    rate_flag:false,
  }),
  mounted() {
    this.fetchdata()
    // this.castingList = movie_data[0].casting.split("|")
  },
  methods: {
    async fetchdata() {
        const apiUrl = '/api'
        const id = this.$route.params.id

        var movie = await axios.get(`${apiUrl}/movies/${id}`)
        this.movie_data = movie.data
        this.castingList = this.movie_data[0].castings.split("|")
        // console.log(this.movie_data)

        // 내가 댓글을 남겼다면..? 해당점수를 가져와야죠!
        var myrate = await axios.get(`${apiUrl}/movies/${id}/${this.$session.get('id_number')}`)
        if (myrate.data.flag===true) {
          this.rate_flag = true
          this.score = myrate.data.rate
        }

    },
    search() {
      router.push({name:'movie-search'})
    },
    SELECT_MovieDetail(movie) {
      var movie_data = {'id':movie.id, 'title':movie.title, 'genres_array':movie.genres_array,
                  'img':movie.img,'watch_count' : movie.watch_count, 'score_users':movie.score_users, 'averagerate':movie.averagerate,
                  'plot':movie.plot,'url':movie.url,'director':movie.director,'casting':movie.casting}

      router.push({name:'movie-detail', params : {'id':movie_data.id, 'movie_data':movie_data}})
      window.location.reload()
    },
    // checkRating(id) {
    //   const apiUrl = '/api'
    //   axios.post(`${apiUrl}/movie/${id}/score/check/`, {
    //     user_pk:this.$session.get('id_number')
    //   }).then(res => {
    //     if(res==true) {alert("이미 평점을 남겼습니다.");}
    //     else {this.rate_show = true;}
    //   })
    // },
    createRating(id) {
      const apiUrl = '/api'
      axios.post(`${apiUrl}/movie/${id}/score/cdu/`, {
        user_pk:this.$session.get('id_number'),
        score:this.score
      }).then(res => {
        if(res.data==false) alert("이미 평점을 등록하셨습니다.")
        else alert("평점을 등록했습니다.")
        this.rate_flag = !this.rate_flag
        this.rate_show = !this.rate_show
      })
    },
    updateRating(id) {
      const apiUrl = '/api'
      axios.put(`${apiUrl}/movie/${id}/score/cdu/`, {
        user_pk:this.$session.get('id_number'),
        score:this.score
      }).then(res => {
        if(res.data==false) alert("등록된 평점이 없습니다.")
        else alert("평점을 수정했습니다.")
        this.rate_show = !this.rate_show
      })
    },
    deleteRating(id) {
      const apiUrl = '/api'
      axios.delete(`${apiUrl}/movie/${id}/score/cdu/`, {
        data: {user_pk:this.$session.get('id_number')}
      }).then(res => {
        console.log(res.data)
        if(res.data==false) alert("등록된 평점이 없습니다.")
        else alert("평점을 삭제했습니다.")
        this.rate_show = !this.rate_show
        this.rate_flag = !this.rate_flag
      })
    }
  }
};
</script>
