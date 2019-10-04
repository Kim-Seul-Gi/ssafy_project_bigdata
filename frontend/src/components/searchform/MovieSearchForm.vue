<template>
  <v-form ref="form">
    <v-text-field v-model="title" @keyup.enter="onSubmit" background-color="#424242" label="영화 제목" />

    <!-- enter 치면 리렌더링 방지용 -->
    <v-text-field v-show="false"/>

    <v-layout justify-center pa-10>
      <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
    </v-layout>
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    title: ""
  }),
  methods: {
    onSubmit: function() {
      const params = {
        title: this.title,
      };
      this.submit(params);
    }
  }
};
</script>
