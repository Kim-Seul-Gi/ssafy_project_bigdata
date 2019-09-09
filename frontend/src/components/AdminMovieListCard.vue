<template>
<div>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>
            <div style="cursor: pointer" @click="SELECT_MovieDetail()">{{title}}</div>
            <div>{{genres_array}}</div>
            <v-btn @click="movie_detail(id); dialog=true">수정</v-btn>
            <v-btn v-on:click="movie_delete(id);">삭제</v-btn>
          </v-container>
        </v-flex>
      </v-layout>
    </v-card>
  </v-hover>
  <v-dialog v-model="dialog" width="500" >
    <v-card flat class="text-xs-center ma-3" min-width="500">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-responsive class="pt-4">
        </v-responsive>

        <v-card-text>
          <v-text-field
            hint="제목을 변경할 수 있습니다."
            v-model="title"
            name="title"
            label="Title"
            id="title"
            prepend-icon=""
            clearable
          ></v-text-field>
          <v-select
            hint="장르를 변경할 수 있습니다."
            v-model="genres_array"
            name="genres_array"
            label="Genres"
            id="genres_array"
            :items="genres"
            attach
            genres_array
            multiple
          ></v-select>
        </v-card-text>
      </v-form>
      <v-btn color="primary" text @click="movie_update(id); dialog=false">
        수정하기
      </v-btn>
      <v-btn color="primary" text @click="dialog=false">
        닫기
      </v-btn>
    </v-card>
  </v-dialog>
</div>
</template>

<script>
import router from "../router";
import axios from "axios"
export default {
  data: () => ({
    valid: true,
    dialog: false,
    genres: ['Action', 'Adventure', 'Animation', 'Comedy',
    'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
    'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western', "Children's"],
    // genres_array : []
  }),
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres_array: {
      type: Array,
      default: () => new Array()
    },
    img: {
      type: String,
      default: ""
    },
    averagerate: {
      type: Number,
      default: 0.0
    },
    watch_count: {
      type: Number,
      default: 0
    },
    score_users: {
      type: Array,
      default: () => new Array()
    }
  },
  mounted() {
    console.log(this.id, 123123)
  },
  computed: {
    genresStr: function() {
      return this.genres_array.join(" / ");
    },
  },
  methods: {
    SELECT_MovieDetail() {
      var movie_data = {'id':this.id, 'title':this.title, 'genres_array':this.genres_array,
                  'img':this.img,'watch_count' : this.watch_count, 'score_users':this.score_users, 'averagerate':this.averagerate}
      router.push({name:'movie-detail', params : {'id':movie_data.id, 'movie_data':movie_data}})
    },
    // _init: function() {
    //   this.title = this.movie_init.title_init;
    //   this.genres_array = this.movie_init.genres_array_init;
    // },
    movie_delete: function(id) {
      const apiUrl = '/api'
      let chk = confirm("정말 삭제하시겠습니까?")
      if (chk == true) {
        console.log(`${apiUrl}/movie/${id}/delete/`)
        axios.delete(`${apiUrl}/movie/${id}/delete/`, {id})
        window.location.reload()
      }
    },
    movie_update: function(id) {
      const apiUrl = '/api'
      let chk = confirm("영화 정보를 변경하시겠습니까?")
      if(chk == true) {
        console.log(`${apiUrl}/movie/${id}/update/`)
        axios.put(`${apiUrl}/movie/${id}/update/`, {
          id:this.id,
          title:this.title,
          genres_array:this.genres_array
        })
      }
    },
    movie_detail: async function(id) {
      const apiUrl = '/api'
      var movie = await axios.get(`${apiUrl}/movies/${id}`)
      console.log(movie.data[0])
      // this.title = movie.data[0].title
      // this.genres_array = movie.data[0].genres_array
    }
  }
};
</script>
