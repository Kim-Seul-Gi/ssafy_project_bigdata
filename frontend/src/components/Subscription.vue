<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex>
        <h1>구독 관련</h1>

        <div v-if="user_data.approval">
          회원님의 구독 유효 기간은 {{sub_date}} 입니다.

          <div v-if="before_extend">
            <div v-for="amount in amounts" style="display:inline-block;">
              <input type="radio" :value="amount" v-model="picked_amount">
              <label style="font-size:10px;">{{amount}}</label> &nbsp;
            </div>
            <v-btn @click="extend_subscription()">구독 연장</v-btn>
          </div>

          <div v-else>
            연장 신청을 하였습니다.
          </div>

        </div>

        <div v-else>
          회원님은 구독 서비스를 이용한 적이 없어요~
          <div v-if="before_create">
            <div v-for="amount in amounts" style="display:inline-block;">
              <input type="radio" :value="amount" v-model="picked_amount">
              <label style="font-size:10px;">{{amount}}</label> &nbsp;
            </div>
            <v-btn @click="create_subscription()">구독 신청</v-btn>
          </div>
          <div v-else>
            구독 신청을 하였습니다.
          </div>
        </div>

      </v-flex>


    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    amounts: [30, 90],
    picked_amount:'',
    before_create : true,
    before_extend : true
  }),
  props : {
    user_data : {
      type : Object,
    },
    now_date : { type : String },
    sub_date : { type : String }
  },
  mounted() {
  },
  methods : {
    async create_subscription() {
      const apiUrl = '/api'
      var subscription = await axios.post(`${apiUrl}/subscription/create/`, {user : this.$session.get('id'), request:this.picked_amount})
      // console.log(subscription, 123)
      if (subscription.data) {
        alert(subscription.data.message)
      }
      this.before_create = false
    },
    async extend_subscription() {
      const apiUrl = '/api'
      var subscription = await axios.post(`${apiUrl}/subscription/create/`, {user : this.$session.get('id'), request:this.picked_amount})
      // console.log(subscription, 456)
      this.before_extend = false
    },
  }
};
</script>
