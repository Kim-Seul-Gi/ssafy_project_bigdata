<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 by 영화이름-->
      <v-flex xs-12>
        <div style="color:rgb(255,255,255)">No. {{movie_data[0].id}}</div>
        <v-card class="mx-auto" max-width="600px">
          <v-img :src="movie_data[0].url"
            height="400px" contain
          ></v-img>
          <v-col>
            <h1>{{movie_data[0].title}}</h1>
            <v-btn icon @click="rate_show=!rate_show">{{rate_show ? 'cancel' : '평점 남기기'}}</v-btn>
            <v-flex v-show="rate_show">
              <div class="mx-auto" style="width:200px">
                <v-text-field
                  v-model="score"
                  label="score"
                  :rules="scoreRules"
                  type="number"
                  required>
                </v-text-field>
                <v-btn @click="createRating(movie_data[0].id)">등록</v-btn>
                <v-btn @click="updateRating(movie_data[0].id)">수정</v-btn>
                <v-btn @click="deleteRating(movie_data[0].id)">삭제</v-btn>
              </div>
            </v-flex>
            <div class="grey--text">{{movie_data[0].averagerate}} ({{movie_data[0].watch_count}})</div>
            <div class="grey--text">Director: {{movie_data[0].director}}</div>
          </v-col>
          {{this.movie_data[0].castings}}
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
      </v-flex>
      <v-flex>
      <h2>유사 작품</h2>
        <v-flex v-for="movie in movie_data.slice(1)" pa-2>
          <v-col>
          <v-hover v-slot:default="{ hover }">
            <v-card :elevation="hover ? 12 : 2" 
                    max-width="300" max-height="300" class="mx-auto" 
                    @click="SELECT_MovieDetail(movie)">
              <v-row class="py-4 pl-4">
                <v-img
                  height="200"
                  width="200"
                  contain
                  :src="movie.url"
                ></v-img>
              </v-row>
              <div>{{movie.title}}</div>
            </v-card>
          </v-hover>
          </v-col>
        </v-flex>
        </v-flex>
      </v-layout>
    <v-btn @click="search()">이전으로 이동</v-btn>
  </v-container>
</template>

<script>
import router from "../../router";
import axios from 'axios'

export default {
  components: {
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
  }),
  mounted() {
    this.fetchdata()
  },
  methods: {
    async fetchdata() {
        const apiUrl = '/api'
        const id = this.$route.params.id
        var movie = await axios.get(`${apiUrl}/movies/${id}`)
        this.movie_data = movie.data
        // console.log(this.movie_data)
    },
    search() {
      router.go(-1)
    },
    SELECT_MovieDetail(movie) {
      var movie_data = {'id':movie.id, 'title':movie.title, 'genres_array':movie.genres_array,
                  'img':movie.img,'watch_count' : movie.watch_count, 'score_users':movie.score_users, 'averagerate':movie.averagerate,
                  'plot':movie.plot,'url':movie.url,'director':movie.director,'casting':movie.casting}

      router.push({name:'movie-detail', params : {'id':movie_data.id, 'movie_data':movie_data}})
      window.location.reload()
    },
    checkRating(id) {
      const apiUrl = '/api'
      axios.post(`${apiUrl}/movie/${id}/score/check/`, {
        user_pk:this.$session.get('id_number')
      }).then(res => {
        if(res==true) {alert("이미 평점을 남겼습니다.");}
        else {this.rate_show = true;}
      })
    },
    createRating(id) {
      const apiUrl = '/api'
      axios.post(`${apiUrl}/movie/${id}/score/cdu/`, {
        user_pk:this.$session.get('id_number'),
        score:this.score
      }).then(res => {
        if(res==false) alert("이미 평점을 등록하셨습니다!!")
        else alert("평점을 등록했습니다.")
        
      })
    },
    updateRating(id) {
      const apiUrl = '/api'
      axios.put(`${apiUrl}/movie/${id}/score/cdu/`, {
        user_pk:this.$session.get('id_number'),
        score:this.score
      }).then(res => {
        if(res==false) alert("등록된 평점이 없습니다.")
        else alert("평점을 수정했습니다.")
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
      })
    }
  }
};
</script>
