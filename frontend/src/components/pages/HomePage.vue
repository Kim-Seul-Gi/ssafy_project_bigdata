<template>
  <v-flex shrink>
    <!-- <span class="display-3 grey--text">Select menu</span> -->

    <!-- 따져아 할 상태 : 로그인and구독 / 로그인and구독X / 로그인X -->

    <!--  -->

    <!--  -->

    <!--  -->


  </v-flex>
</template>

<script>
export default {
  components:{

  },
  data() {
    return {

    }
  },
  mounted() {
    this.usercheck()
  },
  methods : {
    usercheck() {
      console.log(this.$session.get('id'))


    }
  },

}
</script>
