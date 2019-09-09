<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 by 영화이름-->
      <v-flex xs6>

        <div class="display-2 pa-10">
        영화 상세 내용<br>
        {{movie_data[0].id}}, {{movie_data[0].title}}
        <br><br>

        <v-flex v-for="(movie,i) in movie_data.slice(1)" :key="i" pa-2>

          <v-hover v-slot:default="{ hover }">

            <v-card :elevation="hover ? 8 : 2">
              <v-layout align-center py-4 pl-4>
                <v-flex text-center>
                  <v-container grid-list-lg pa-0>

                    <v-layout column @click="SELECT_MovieDetail(movie)">
                      <v-list-item>
                        <v-list-item-content>
                          <v-list-item-title class="headline">
                            {{movie.id}}
                            <!-- ID : {{ id }}, username : {{ username }} -->

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
        </div>

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
    movie_data:'',
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
    },
    search() {
      router.go(-1)
    },
    SELECT_MovieDetail(movie) {
      var movie_data = {'id':movie.id, 'title':movie.title, 'genres_array':movie.genres_array,
                  'img':movie.img,'watch_count' : movie.watch_count, 'score_users':movie.score_users, 'averagerate':movie.averagerate}

      router.push({name:'movie-detail', params : {'id':movie_data.id, 'movie_data':movie_data}})
      window.location.reload()
    }
  }
};
</script>
