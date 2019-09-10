<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 by 영화이름-->
      <v-flex xs6>
        <div>
          <Subscription
            :user_data="profile_data[0]"
            :now_date="now_date"
            :sub_date="subscription_date"
          />
        </div>

        <div class="display-2 pa-10">아직 만들지 않은 페이지입니다.</div>
        현재 로그인 한 유저 : {{this.user}} <br>
        내가 좋아하는 장르들 : 나중에 가져올게요! <br>
        나와 같은 집단에 속하는 사람들 :
        <li v-for="person in this.profile_data.slice(1)">
          <div>{{person}}
              <v-btn @click="SELECT_UserDetail(person.id, person.username)">놀러가기~</v-btn>
          </div>
        </li>
        <!-- {{this.profile_data.slice(1)}}<br> -->
      </v-flex>

      <!-- 검색 결과 -->
      <!-- <v-flex xs7>
        <MovieList :movie-list-cards="movieList" />
      </v-flex> -->

    </v-layout>
  </v-container>

</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../../router";
import axios from 'axios'
import Subscription from "../Subscription";
// import MovieSearchForm from "../searchform/MovieSearchForm";
// import MovieList from "../MovieList";


export default {
  components: {
    // MovieSearchForm,
    // MovieList,
    Subscription
  },
  data: () => ({
    user: '',
    profile_data:'',
    user_data:'',
    subscription_date:'',
    now_date:''
    // movielist:[],
  }),
  created() {
    this.fetchdata();
  },
  computed: {
    // ...mapState({
      // movieList: state => state.data.movieSearchList
    // })
  },
  methods: {
    // ...mapActions("data", ["searchMovies"]),
    async fetchdata() {
      this.user = this.$session.get('id')
      const apiUrl = '/api'
      const id = this.$session.get('id_number')
      var profile = await axios.get(`${apiUrl}/users/${id}`)
      this.profile_data = profile.data

      // 구독 날짜 확인하기,
      // 오늘 날짜 : this.now_date , ex) 20190910
      // 회원의 구독 날짜 : this.subscription_date, ex) 20190801
      this.user_data = this.profile_data[0]
      this.subscription_date = this.user_data.subscription.substring(0, 10).replace(/-/g,'')
      var now = new Date()
      var year = now.getFullYear()
      var month = now.getMonth() + 1
      var date = now.getDate()
      if ( month < 10 ) {
        month = '0' + String(month)
      } else {
        month = String(month)
      }
      if ( date < 10) {
        date = '0' + String(date)
      } else {
        date = String(date)
      }
      this.now_date = String(year)+month+date
    },

    SELECT_UserDetail(id, username) {
      var user_data = {'id':id, 'username':username}
      router.push({name:'user-detail', params : {'id':user_data.id, 'user_data':user_data}})
    }
  }
}
</script>
