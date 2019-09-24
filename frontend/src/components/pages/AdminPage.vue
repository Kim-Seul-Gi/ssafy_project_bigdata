<template>
  <v-flex shrink>
    <span class="display-3 grey--text">Admin page</span>
    <v-flex fluid row style="width:100%;">
      <v-switch v-model="switch1" :label="`movie`" @click="one()" />
      <v-switch v-model="switch2" :label="`user`" @click="two()" />
      <v-switch v-model="switch3" :label="`clustering`" @click="three()" />
      <v-switch v-model="switch4" :label="`subscription`" @click="four()" />
      <v-btn @click="check()">초기화</v-btn>
    </v-flex>
    <v-flex v-if="switch1" xs12>
      <p>movie</p>
      <MovieSearchForm :submit="searchMovies_admin" />
      <v-flex xs4>
        <AdminMovieList :movie-list-cards="movieList" />
      </v-flex>
    </v-flex>
    <v-flex v-if="switch2" xs12>
      <p>user</p>
      <UserSearchForm :submit="searchUsers_admin" />
      <v-flex xs12>
        <AdminUserList :user-list-cards="userList" />
      </v-flex>
    </v-flex>
    <v-flex v-if="switch3" xs12>
      <p>clustering 파라미터 설정하기!</p>
      여기에서 누르면 클러스터링 값이 변경될 것입니다.
      <AdminClustering />
    </v-flex>
    <v-flex v-if="switch4" xs12>
      <p>여기에서 사람들이 구독 신청한 것들을 관리합시다~</p>
      <AdminSubscriptionList />
    </v-flex>
  </v-flex>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieSearchForm from "../searchform/MovieSearchForm";
import AdminMovieList from "../AdminMovieList";
import UserSearchForm from "../searchform/UserSearchForm";
import AdminUserList from "../AdminUserList";
import AdminClustering from "../AdminClustering";
import AdminSubscriptionList from "../AdminSubscriptionList";

export default {
  components: {
    AdminMovieList,
    AdminUserList,
    AdminSubscriptionList,
    
    MovieSearchForm,
    UserSearchForm,

    AdminClustering,

  },
  data: () => ({
    switch1: false,
    switch2: false,
    switch3: false,
    switch4: false,
    movielist:[],
    userlist:[],
  }),
  computed: {
    ...mapState({
      movieList: state => state.data.movieSearchList_admin,
      userList: state => state.data.userSearchList_admin
    })
  },
  methods: {
    ...mapActions("data", ["searchMovies_admin", "searchUsers_admin"]),
    one() {
      this.switch1 = true
      this.switch2 = false
      this.switch3 = false
      this.switch4 = false
    },
    two() {
      this.switch1 = false
      this.switch2 = true
      this.switch3 = false
      this.switch4 = false
    },
    three() {
      this.switch1 = false
      this.switch2 = false
      this.switch3 = true
      this.switch4 = false
    },
    four() {
      this.switch1 = false
      this.switch2 = false
      this.switch3 = false
      this.switch4 = true
    },
    check() {
      this.switch1 = false
      this.switch2 = false
      this.switch3 = false
      this.switch4 = false
    },
  }
}
</script>
