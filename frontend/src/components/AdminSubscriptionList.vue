<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex >
        <li v-if="subscription.approval==false" v-for="(subscription, index) in this.subscriptions">
          {{subscription.username}}님이 {{subscription.request}}일 구독 신청하였습니다.
          <v-btn @click="approval(subscription, index)">승인</v-btn>

        </li>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    subscriptions : []
  }),
  mounted() {
    this.fecthdata()
  },
  methods : {
    async fecthdata() {
      const apiUrl = '/api'
      var sub = await axios.get(`${apiUrl}/subscription/manager/`)
      this.subscriptions = sub.data
    },
    async approval(subscription, index) {
      const apiUrl = '/api'
      this.subscriptions.splice(index, 1)
      axios.post(`${apiUrl}/subscription/manager/`, {subscription : subscription})
    }
  }

};
</script>
