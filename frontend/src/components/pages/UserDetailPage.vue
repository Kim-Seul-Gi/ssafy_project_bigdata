<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 by 영화이름-->
      <v-flex xs12>

        <div class="display-2 pa-10">
        유저 상세 내용<br>

        <p>{{profile_data[0]['is_username']}}</p>
        <div v-if="profile_data[0]['gender'] == 'F'">성별 : 여</div>
        <div v-else-if="profile_data[0]['gender'] == 'M'">성별 : 남</div>
        <p>직업 : {{profile_data[0]['occupation']}}</p>
        <div v-if="profile_data[0]['age'] == '1'">연령대 : 18세이하</div>
        <div v-else-if="profile_data[0]['age'] == '18'">연령대 : 18-24세</div>
        <div v-else-if="profile_data[0]['age'] == '25'">연령대 : 25-34세</div>
        <div v-else-if="profile_data[0]['age'] == '35'">연령대 : 35-44세</div>
        <div v-else-if="profile_data[0]['age'] == '45'">연령대 : 45-49세</div>
        <div v-else-if="profile_data[0]['age'] == '50'">연령대 : 50-55세</div>
        <div v-else-if="profile_data[0]['age'] == '56'">연령대 : 56세이상</div>


        <br>

        <v-flex v-for="(person,idx) in profile_data.slice(1)" :key='idx' pa-2>

        <v-hover v-slot:default="{ hover }">

          <v-card :elevation="hover ? 8 : 2">
            <v-layout align-center py-4 pl-4>
              <v-flex text-center>
                <v-container grid-list-lg pa-0>

                  <v-layout column @click="SELECT_UserDetail(person.id, person.username)">
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title class="headline">
                          {{person.id}}
                          
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

        <br>
        <v-btn @click="search()">검색으로 이동</v-btn>
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
    // user_data : {type:Object}
  },
  data: () => ({
    profile_data:[
      {'id':''},
      {"approval":''},
      {"gender":''},
      {"age":''},
      {"is_staff":''},
      {"occupation":''},
      {"subscription":''},
      {"username":''}],
  }),
  mounted() {
    this.fetchdata()
  },
  methods: {
    async fetchdata() {
      const apiUrl = '/api'
      const id = this.$route.params.id
      var profile = await axios.get(`${apiUrl}/users/${id}`)
      this.profile_data = profile.data
      // console.log(profile)
    },
    search() {
      router.push({name:'user-search'})
    },

    SELECT_UserDetail(id, username) {
      var user_data = {'id':id, 'username':username}
      router.push({name:'user-detail', params : {'id':user_data.id, 'user_data':user_data}})
      window.location.reload()
    }

  }
};
</script>
