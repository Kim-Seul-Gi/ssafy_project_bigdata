<template>
  <v-container>
    <v-layout row wrap>
      <v-flex xs12>



        <!-- <span class="display-3 grey--text">Select menu</span> -->

        <!-- Homepage에서 보여주고자 하는 기능들은 아래와 같습니다. -->
            <!-- (1) 로그인 하셨습니까? -->
            <!-- (2) 구독 관리 -->
            <!-- (3) 단순한 영화 나열(조회수, 인기순) -->
            <!-- (4) 단순한 유사유저 리스트 -->
            <!-- (5) UserBased 영화 추천 -->
            <!-- (6) MovieBased 영화 추천 -->

        <!-- 유저의 상태는 로그인 여부(this.user) / 구독 여부(Subscription) 에서 다룹니다. -->
            <!-- 1. 로그인 X / 보여줄 기능 : (1) -->
            <!-- 2. 로그인 O , 구독 X / 보여줄 기능 : (2), (3), (4) -->
            <!-- 3. 로그인 O , 구독 O / 보여줄 기능 : (2), (3), (4), (5), (6) -->


        <!-- 1. 로그인 여부 -->
        <div v-if="!this.user">
          로그인을 하지 않았습니다!!

          <!-- (1) 로그인 하러가기 -->
          <v-btn>로그인하기</v-btn>

        </div>

        <div v-else>
          저는 {{this.user}}입니다.<br>

          <!-- 2, 3. 구독 여부 에 따른 (2), (5), (6) -->
          <div>
            <Subscription
              :user_data="profile_data[0]"
              :now_date="now_date"
              :sub_date="subscription_date"
              :approval="this.user_data.approval"
            />
          </div>

          <!-- (4) 유사 유저는 여기에서 가져올 수 있네요..?!-->
          <UserCarousel
            :users="profile_data.slice(1)"
          />



          <!-- 이것은 유저들 가져오는 거 구버젼입니다. -->
          <!-- <v-layout row wrap>
          <v-flex v-for="person in this.profile_data.slice(1)" style="margin-bottom: 2rem;" xs12 sm6 md4 lg3 xl2>

              <v-card>
                  <v-card-text>
                    <v-container>
                      <p style="color: black; font-size: 1.4rem;">{{ person.username }}</p>
                      <p>{{ person.age }} / {{ person.gender }}</p>
                      <p>{{ person.occupation }}</p>
                      <v-btn text color="primary" @click="SELECT_UserDetail(person.id, person.username)">explore</v-btn>
                    </v-container>
                  </v-card-text>

              </v-card>
          </v-flex>
          </v-layout> -->


        </div>

        <!-- (3) 단순한 영화 나열(조회수, 인기순) -->


      </v-flex>
    </v-layout row wrap>

  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../../router";
import axios from 'axios'
import Subscription from "../Subscription";
import UserCarousel from "../UserCarousel";


export default {
  components:{
    Subscription,
    UserCarousel
  },
  data() {
    return {
      user:'',
      profile_data:'',
      user_data:'',
      subscription_date:'',
      now_date:'',
    }
  },
  mounted() {
    this.fetchdata()
  },
  methods : {
    async fetchdata() {
      this.user = this.$session.get('id')
      if (this.$session.get('id')=='') {
      } else {
        const apiUrl = '/api';
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
      }

    }
  },

}
</script>

<style>
  .example-slide {
    align-items: center;
    background-color: #666;
    color: #999;
    display: flex;
    font-size: 1.5rem;
    justify-content: center;
    min-height: 10rem;
  }
</style>
