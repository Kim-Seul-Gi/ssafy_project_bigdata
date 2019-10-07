<!-- eslint-disable -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 by 영화이름-->
      <v-col>
      <v-flex>
        <!-- <div>
          <Subscription
            :user_data="profile_data[0]"
            :now_date="now_date"
            :sub_date="subscription_date"
          />
        </div> -->

        <p style="font-size: 3rem; color: white; font-family: 'Jua', sans-serif;">User Profile</p>
        <p class="profile"><span style="margin-right: 1rem; font-weight: bold;">name</span><span>{{ user.username }}</span></p>
        <p class="profile"><span style="margin-right: 1rem; font-weight: bold;">gender</span><span>{{ user.gender }}</span></p>
        <p class="profile"><span style="margin-right: 1rem; font-weight: bold;">age</span><span>{{ user.age }}</span></p>
        <p class="profile" style="margin-bottom: 3rem;"><span style="margin-right: 1rem; font-weight: bold;">occupation</span><span>{{ user.occupation }}</span></p>
        <v-btn
          color="red lighten-2"
          dark
          @click="dialog=true"
          style="margin-right: 1rem;">
          Edit
        </v-btn>
        <v-btn color="lighten-2" dark
          @click="userMovie(); movie_show=!movie_show">
          내가봤던 영화
        </v-btn>
          <p v-show="movie_show" v-if="movielist.length < 1">보신 영화가 없습니다..</p>
          <v-layout row pa-5 v-show="movie_show" v-if="movielist.length > 1">
            <v-flex>
              <carousel :per-page="pageNum">
                <slide v-for="movie in this.movielist" style="height: 22rem; width: 15rem;">
                  <v-card style="margin:10px; height: 21rem; width: 15rem; border-radius:15px;" color="#424242" dark>
                    <v-img contain :src="movie.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:16rem; width: 15rem;"></v-img>
                    <v-card-text>
                      <div class="movietitle">
                        {{movie.title.substring(0, movie.title.indexOf("("))}}<br>
                        <span class="hovertext">{{movie.title.substring(0, movie.title.indexOf("("))}}</span>
                      </div>
                        <i class="fas fa-star" style="color: #FFB600; margin-right: 0.5rem;"></i><span>평점 </span><span style="font-weight: bold;">{{movie.averagerate}}</span>
                        <v-btn text color="primary" @click="SELECT_MovieDetail(movie)" style="padding-right: 0; margin-left: 2rem; margin-right: 0;">explore</v-btn>
                    </v-card-text>
                  </v-card>
                </slide>
              </carousel>
            </v-flex>
          </v-layout>

        <!-- <div v-show="!profile_data[6]">
          <v-btn @click="NewRate()" v-if="!modal">장르별 평점 등록하기</v-btn>
          <v-btn @click="modal=!modal" v-if="modal">취소</v-btn>
        </div>
        <NewUserRating :modal="modal" v-if="modal"/> -->
      </v-flex>

      <v-flex>
        <div style="margin-top: 3rem;" v-if="typeof(profile_data[1])!='boolean'">
          <p style="font-size: 3rem; color: white; font-family: 'Jua', sans-serif;">Similar Users</p>
          <carousel :per-page="pageNum">
            <slide v-for="person in this.profile_data.slice(1, 6)" style="height: 13rem; width: 15rem;" v-bind:key="person.username">
              <v-card style="margin:10px; border-radius:15px;" color="#424242" dark>
                <v-card-text>
                  <v-container>
                    <p style="color: white; font-size: 1.4rem;">{{ person.username }}</p>
                    {{ person.age }} / {{ person.gender }}<br>
                    {{ person.occupation }}<br>
                    <v-btn text color="primary" @click="SELECT_UserDetail(person.id, person.username)">explore</v-btn>
                  </v-container>
                </v-card-text>
              </v-card>
            </slide>
          </carousel>
        </div>

        <div style="margin-top: 3rem;" v-else>
          <p style="font-size: 3rem; color: white; font-family: 'Jua', sans-serif;">Similar Users</p>
          <p class="profile">
            <span style="margin-right: 1rem; font-weight: bold;">영화 평점을 등록해주세요!</span>
          </p>
          <!-- <carousel :per-page="pageNum">
            <slide v-for="person in this.profile_data.slice(1, 6)" style="height: 13rem; width: 15rem;" v-bind:key="person.username">
              <v-card style="margin:10px; border-radius:15px;" color="#424242" dark>
                <v-card-text>
                  <v-container>
                    <p style="color: white; font-size: 1.4rem;">{{ person.username }}</p>
                    {{ person.age }} / {{ person.gender }}<br>
                    {{ person.occupation }}<br>
                    <v-btn text color="primary" @click="SELECT_UserDetail(person.id, person.username)">explore</v-btn>
                  </v-container>
                </v-card-text>
              </v-card>
            </slide>
          </carousel> -->
        </div>

      </v-flex>

      </v-col>

    </v-layout>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Profile Edit</span>
        </v-card-title>
        <v-card-text>
          <v-container>
          <v-text-field
            v-model="username"
            :counter="10"
            label="Name"
            :rules="nameRules"
            required
          ></v-text-field>
          <v-layout>
            <span style="vertical-align: middle; color: rgba(0, 0, 0, 0.54); padding-left: 0.3rem; padding-right: 2.5rem;">Gender</span>
            <v-radio-group v-model="user.gender" row>
              <v-radio label="Female" value="F"></v-radio>
              <v-radio label="Male" value="M"></v-radio>
            </v-radio-group>
          </v-layout>
          <v-text-field
            v-model="age"
            type="number"
            label="Age"
            required
          ></v-text-field>
          <v-text-field
            v-model="occupation"
            label="Occupation"
            required
          ></v-text-field>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false; edit()">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>

</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../../router";
import axios from 'axios'
import Subscription from "../Subscription";
import NewUserRating from "../NewUserRating";
import { Carousel, Slide } from 'vue-carousel';

// import MovieSearchForm from "../searchform/MovieSearchForm";
// import MovieList from "../MovieList";


export default {
  components: {
    // MovieSearchForm,
    // MovieList,
    Subscription,
    NewUserRating,
    Carousel,
    Slide
  },
  data: () => ({
    user: null,
    username: null,
    age: null,
    gender: null,
    occupation: null,
    profile_data:'',
    dialog: false,
    modal: false,
    checkCSV: false,
    movie_show: false,
    pageNum: 4,
    nameRules: [
      v => !!v || 'Name is required',
      v => (v && v.length <= 10) || 'Name must be less than 10 characters'
    ],
    user_data:'',
    subscription_date:'',
    now_date:'',
    movielist:[],
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
      console.log(profile, 123123)
      this.profile_data = profile.data
      console.log(this.profile_data[6])

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

      this.user = this.profile_data[0]
      this.username = this.user.username
      this.age = this.user.age
      this.gender = this.user.gender
      this.occupation = this.user.occupation
    },

    SELECT_UserDetail(id, username) {
      var user_data = {'id':id, 'username':username}
      router.push({name:'user-detail', params : {'id':user_data.id, 'user_data':user_data}})
    },

    userMovie() {
      const apiUrl = '/api'
      let user_pk = this.$session.get('id_number')
      axios.post(`${apiUrl}/user/${user_pk}/movies/`).then(res => {
        this.movielist = res.data
      })
    },

    NewRate() {
      const apiUrl = '/api'
      axios.post(`${apiUrl}/KNN/checkCSV/`,{
        pk:this.$session.get('id_number')
      }).then(res => {
        console.log(res.data)
        if(res.data==false)
          this.modal = !(this.modal)
        else
          // alert("이미 등록하신 평점이 있습니다!")
          Swal.fire({
            text: '이미 등록한 평점이 있어요.'
          })
      })
    },

    async edit() {
      let __this = this;
      const id = this.$session.get('id_number');
      const apiUrl = '/api';
      let tmp = await axios.post(`${apiUrl}/users/${id}`, {
        username: __this.username,
        gender: __this.gender,
        age: __this.age,
        occupation: __this.occupation
      }).then(async res => {
        var profile = await axios.get(`${apiUrl}/users/${id}`)
        this.profile_data = profile.data
        this.user = this.profile_data[0]
      })
    }
  }
}
</script>
<style scoped>
  .profile {
    color:  rgba(255, 255, 255, 0.7);
    font-size: 2rem;
  }
</style>
