<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>

            <v-layout column @click="SELECT_MovieDetail()">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">
                    {{ title }}
                  </v-list-item-title>
                  <v-list-item-subtitle>{{ genresStr }}</v-list-item-subtitle>
                  <v-list-item-subtitle>평점 : {{averagerate}}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-card-text>
                <v-layout justify-center>
                  <v-rating
                    :value="averagerate"
                    color="indigo"
                    background-color="indigo"
                    half-increments
                    dense
                    readonly
                  />
                  <div class="grey--text ml-4">{{ averagerate.toFixed(1) }}</div>
                </v-layout>
              </v-card-text>
              <v-card-text>
                <v-layout justify-center>
                  <v-icon color="black">mdi-eye</v-icon>
                  <div class="grey--text ml-4">{{ watch_count }}</div>
                </v-layout>
              </v-card-text>
            </v-layout>

          </v-container>
        </v-flex>
      </v-layout>
    </v-card>
  </v-hover>
</template>

<script>
import router from "../router";

export default {
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
      type: Array | String ,
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
    },
    plot: {
      type: String,
      default: ""
    },
    url: {
      type: String,
      default: ""
    },
    director: {
      type: String,
      default: ""
    },
    casting: {
      type: String,
      default: ""
    }
  },
  computed: {
    genresStr: function() {
      if (typeof(this.genres_array)=="object") {
        return this.genres_array.join(" / ");
      } else {
        return this.genres_array.split('|').join(" / ");
      }
    },
  },
  methods: {
    SELECT_MovieDetail() {

      var movie_data = {'id':this.id, 'title':this.title, 'genres_array':this.genres_array,
                  'img':this.img,'watch_count' : this.watch_count, 'score_users':this.score_users, 'averagerate':this.averagerate}
      // router.push({name:'movie-detail', params : {'id':movie_data.id, 'movie_data':movie_data}})
      router.push({name:'movie-detail', params : {'id':movie_data.id}})
    }
  }
};
</script>
