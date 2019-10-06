<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 by 영화이름-->
      <v-flex xs6 v-if="bymoviename">

        <div class="display-2 pa-10">영화 검색</div>

        <v-btn @click="changesearch1()">다른 검색</v-btn>

        <div>
          <MovieSearchForm :submit="before_searchMovies" />
        </div>
      </v-flex>

      <!-- 검색 폼 by 장르이름 -->
      <v-flex xs6 v-if="!bymoviename">
        <v-btn @click="changesearch1()">영화 이름으로 검색하기</v-btn><br>

        <v-btn @click="changesearch2()">장르 기준</v-btn>
        <v-btn @click="changesearch3()">연령대 기준</v-btn>
        <v-btn @click="changesearch4()">직업 기준</v-btn>
        <v-btn @click="changesearch5()">성별 기준</v-btn>

        <div v-if="bygenre" class="display-2 pa-10">장르 검색
          <GenreSearchForm :submit="searchGenres" />
        </div>

        <div v-if="byage" class="display-2 pa-10">연령대 검색
          <AgeSearchForm :submit="searchAges" />
        </div>

        <div v-if="byoccupation" class="display-2 pa-10">직업 검색
          <OccupationSearchForm :submit="searchOccupations" />
        </div>

        <div v-if="bygender" class="display-2 pa-10">성별 검색
          <GenderSearchForm :submit="searchGenders" />
        </div>
      </v-flex>

      <!-- 검색 결과 -->
      <v-flex xs12>
        <MovieList :movie-list-cards="movieList" :reset="reset"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieSearchForm from "../searchform/MovieSearchForm";
import GenreSearchForm from "../searchform/GenreSearchForm";
import AgeSearchForm from "../searchform/AgeSearchForm";
import OccupationSearchForm from "../searchform/OccupationSearchForm";
import GenderSearchForm from "../searchform/GenderSearchForm";
import MovieList from "../MovieList";
export default {
  components: {
    MovieList,
    MovieSearchForm,
    GenreSearchForm,
    AgeSearchForm,
    OccupationSearchForm,
    GenderSearchForm
  },
  data: () => ({
    movielist:[],
    bymoviename:true,
    bygenre:false,
    byage:false,
    byoccupation:false,
    bygender:false,
    reset : true,
  }),
  computed: {
    ...mapState({
      movieList: state => state.data.movieSearchList
    })
  },
  mounted() {
    // this.resetMovieList()
  },
  methods: {
    ...mapActions("data", ["searchMovies", "searchGenres", "searchAges", "searchOccupations", "searchGenders", "resetMovieList"]),
    before_searchMovies(params) {
      this.reset = !this.reset
      this.searchMovies(params)
    },
    changesearch1() {
      this.bymoviename = !this.bymoviename
      this.bygenre = false
      this.byage = false
      this.byoccupation = false
      this.bygender = false
    },
    changesearch2() {
      // 장르별 하기 위함
      this.bygenre = true
      this.byage = false
      this.byoccupation = false
      this.bygender = false
    },
    changesearch3() {
      // 나이별 하기 위함
      this.bygenre = false
      this.byage = true
      this.byoccupation = false
      this.bygender = false
    },
    changesearch4() {
      // 직업별 하기 위함
      this.bygenre = false
      this.byage = false
      this.byoccupation = true
      this.bygender = false
    },
    changesearch5() {
      // 나이별 하기 위함
      this.bygenre = false
      this.byage = false
      this.byoccupation = false
      this.bygender = true
    },
  }
};
</script>
