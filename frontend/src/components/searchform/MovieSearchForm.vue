<template>
  <v-form ref="form">
    <v-text-field v-model="title" @keyup.enter="onSubmit" background-color="#424242" label="영화 제목" />

    <!-- enter 치면 리렌더링 방지용 -->
    <v-text-field v-show="false"/>

    <v-layout justify-center pa-5>
      <!-- <v-btn v-show="cnt<=10" large color="indigo white--text" @click="onSubmit">Search</v-btn> -->
      <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
    </v-layout>
    <!-- <v-btn v-show="cnt>10" large color="indigo white--text" @click="onSubmit">더보기</v-btn> -->
  </v-form>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    title: "",
    // cnt: 10,
    movielist:[]
  }),
  methods: {
    onSubmit: function() {
      const apiUrl = '/api'
      const params = {
        title: this.title,
        // cnt: this.cnt
      };
      this.submit(params);
      // this.cnt=this.cnt + 10
    },
  }
};
</script>
