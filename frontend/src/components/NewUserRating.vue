<template>
  <div>
    <v-row justify="center">
      <v-dialog v-model="modal" persistent max-width="600">
        <template v-slot:activator="{ on }">
          <v-btn color="primary" dark v-on="on">Let's get it!!</v-btn>
        </template>
        <v-card>
          <v-form v-for="i in 18">
            <div>
              <p>{{ items[i-1] }}</p>
              <v-text-field
                  v-model="scores[i-1]"
                  label="score"
                  :rules="scoreRules"
                  type="number"
                  required>
              </v-text-field>
            </div>
          </v-form>
          <v-btn @click="modal=!modal, createScore()">register</v-btn>
          <v-btn @click="modal=!modal">cancel</v-btn>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    modal:false,
    items: ["Action","Adventure","Animation","Children's",
                "Comedy","Crime","Documentary","Drama","Fantasy",
                "Film-Noir","Horror","Musical","Mystery","Romance",
                "Sci-Fi","Thriller","War","Western"],
    scores:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    scoreRules: [
      v => !!v || 'This is required',
      v => (v < 6) || 'score is maximum of 5',
    ],
  }),
  methods: {
    createScore() {
      console.log(111)
      // 시작
      var preload = document.querySelector('#check2')
      preload.style.display = 'block'
      const apiUrl = '/api'
      axios.post(`${apiUrl}/KNN/user/`, {
        scores:this.scores,
        pk:this.$session.get('id_number')
      }).then(res => {
        // 끝
        preload.style.display = 'none'
        alert('평점을 등록했습니다!')
      })
      // console.log(this.$session.getAll())
    }
  }
}
</script>