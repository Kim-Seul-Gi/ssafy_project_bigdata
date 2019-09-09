<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>

            <v-layout column @click="SELECT_UserDetail()">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">
                    ID : {{ id }}, username : {{ username }}

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
                  <!-- <v-icon color="black">mdi-eye</v-icon> -->
                  <!-- <div class="grey--text ml-4">{{ viewCnt }}</div> -->
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
    username: {
      type: String,
      default : ''
    }
  },
  computed: {
    // genresStr: function() {
    //   return this.genres.join(" / ");
    // },
  },
  methods: {
    SELECT_UserDetail() {
      var user_data = {'id':this.id, 'username':this.username}
      router.push({name:'user-detail', params : {'id':user_data.id, 'user_data':user_data}})
    }
  }

};
</script>
