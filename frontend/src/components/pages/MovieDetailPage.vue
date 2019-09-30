<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 by 영화이름-->
      <v-flex xs6>
        <div>No. {{movie_data[0].id}}</div>
        <v-card class="mx-auto" max-width="600px">
          <v-img :src="movie_data[0].url"
            height="400px"
            contain
          ></v-img>

          <v-card-title align="center">{{movie_data[0].title}}</v-card-title>
          <v-col>
            <div class="grey--text">{{movie_data[0].averagerate}} ({{movie_data[0].watch_count}})</div>
            <div class="grey--text">Director: {{movie_data[0].director}}</div>
          </v-col>
          {{this.movie_data[0].castings.split("|")}}
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
  
        <!-- <div style="width:200px;">
          <h2>평점 추가하기</h2>
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
        </div> -->
        <br><br>
        <h3>유사 작품</h3>
        <v-flex v-for="movie in movie_data.slice(1)" pa-2>
          <v-hover v-slot:default="{ hover }">
            <v-card :elevation="hover ? 8 : 2">
              <v-layout align-center py-4 pl-4>
                <v-flex text-center>
                  <v-container grid-list-lg pa-0>

                    <v-layout column @click="SELECT_MovieDetail(movie)">
                      <v-list-item>
                        <v-list-item-content>
                          <v-list-item-title class="headline">
                            No. {{movie.id}}
                            <br> 
                            {{movie.title}}
                          </v-list-item-title>
                          <!-- <v-list-item-subtitle>{{ genresStr }}</v-list-item-subtitle> -->
                        </v-list-item-content>
                      </v-list-item>
                      <v-card-text>
                        <v-layout justify-center>

                        </v-layout>
                      </v-card-text>
                      <v-card-text>
                        <v-layout justify-center>
                          프로필 보러가기
                          <v-icon color="black">mdi-eye</v-icon>
                          <!-- <div class="grey--text ml-4">{{ viewCnt }}</div> -->
                        </v-layout>
                      </v-card-text>
                    </v-layout>

                  </v-container>
                </v-flex>
              </v-layout>
            </v-card>
          </v-hover>
        </v-flex>

        <v-btn @click="search()">이전으로 이동</v-btn>

      </v-flex>
    </v-layout>
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
    this.castingList = movie_data[0].casting.split("|")
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
    createRating(id) {
      const apiUrl = '/api'
      axios.post(`${apiUrl}/movie/${id}/score/cdu/`, {
        user_pk:this.$session.get('id_number'),
        score:this.score
      }).then(res => {
        if(res==false) {
          alert("이미 평점을 등록하셨습니다!!")
        } else {
          alert("평점을 등록했습니다.")
        }
      })
    },
    updateRating(id) {
      const apiUrl = '/api'
      axios.put(`${apiUrl}/movie/${id}/score/cdu/`, {
        user_pk:this.$session.get('id_number'),
        score:this.score
      }).then(res => {
        if(res==false) {
          alert("등록된 평점이 없습니다.")
        } else {
          alert("평점을 수정했습니다.")
        }
      })
    },
    deleteRating(id) {
      const apiUrl = '/api'
      axios.delete(`${apiUrl}/movie/${id}/score/cdu/`, {
        user_pk:this.$session.get('id_number')
      }).then(res => {
        if(res==false) {
          alert("등록된 평점이 없습니다.")
        } else {
          alert("평점을 삭제했습니다.")
        }
      })
    }
  }
};
</script>
