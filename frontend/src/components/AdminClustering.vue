<template>
  <v-form ref="form">
    <div>
      <p style="font-size: 1rem; font-family: 'Jua', sans-serif;"
                >Cluster 알고리즘 설정하기:</p>
      <div v-for="way in ways" style="display:inline-block;">
        <input type="radio" :value="way" v-model="picked_way">
        <label style="font-size:10px; ">{{way}}</label> &nbsp;
      </div>
      <br><br>
      <p style="font-size: 1rem; font-family: 'Jua', sans-serif;"
                >Cluster 개수 설정하기:</p>
      <div v-for="n_component in n_components" style="display:inline-block;">
        <input type="radio" :value="n_component" v-model="picked_n">
        <label style="font-size:10px;">{{n_component}}개</label> &nbsp;
      </div>
      <br> 
    </div>
    <br>
    <v-btn v-if="this.saved_n!=this.picked_n || this.saved_way!=this.picked_way" large color="indigo white--text" @click="change()">변경하기</v-btn>
    <v-btn v-if="this.saved_n!=this.picked_n || this.saved_way!=this.picked_way" large color="indigo white--text" @click="cancel()">취소하기</v-btn>

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
    n_components : ['3','4', '5', '6', '7'],
    ways : ['K', 'H', 'EM', 'MF'],
    saved_n:'',
    saved_way : '',
    picked_n:'',
    picked_way:'',
  }),
  mounted() {
    this.getCluster()
  },
  methods: {
    async getCluster() {
      const apiUrl = '/api'
      var cluster = await axios.get(`${apiUrl}/cluster/`)
      // console.log(cluster.data, '갓다왓냐?')
      this.picked_n = cluster.data.n_component
      this.saved_n = cluster.data.n_component
      this.picked_way = cluster.data.way
      this.saved_way = cluster.data.way
    },
    change: function() {
      const apiUrl = '/api'
      var result = axios.post(`${apiUrl}/cluster/`, {
        n_component : this.picked_n,
        way : this.picked_way
      }).then(res => {
        this.saved_n = this.picked_n
        this.saved_way = this.picked_way
        // console.log('성공했습니다.')
      })
    },
    cancel() {
      this.picked_n = this.saved_n
      this.picked_way = this.saved_way
    }

  }
};
</script>
