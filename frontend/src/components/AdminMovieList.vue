<!-- disable eslint-plugin-vue -->
<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout row wrap>
      <v-flex pa-2 v-for="(card, i) in movieListCardsSliced" :key="i" xs12 sm6 md4 lg3 xl2>
        <!-- id img title genres_array averagerate watch_count score_users -->
        <AdminMovieListCard
          :movie_init="card"
          :id="card.id"
          :img="card.img"
          :title="card.title"
          :genres_array="card.genres_array"
          :averagerate="card.averagerate"
          :watch_count="card.watch_count"
          :score_users="card.score_users"
          :plot="card.plot"
          :url="card.url"
          :director="card.director"
          :casting="card.casting"
        />
      </v-flex>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-container>
</template>

<script>
import AdminMovieListCard from "./AdminMovieListCard"

export default {
  components: {
    AdminMovieListCard,
  },
  props: {
    movieListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
    cardsPerPage: 12,
    page: 1,
    tmp_movieList:[],
  }),
  computed: {
    // pagination related variables
    movieListEmpty: function() {
      return this.movieListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.movieListCards.length + this.cardsPerPage - 1) / this.cardsPerPage)
    },
    movieListCardsSliced: function() {
      this.tmp_movieList = JSON.parse(JSON.stringify(this.movieListCards))
      return this.movieListCards.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
    },
    movieListCardsSliced2: function() {
      return this.tmp_movieList.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
    },
  }
};
</script>
