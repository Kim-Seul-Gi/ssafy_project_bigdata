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
    <v-card v-if="check">
      평점 등록 및 클러스터링이 진행 중입니다!
      잠시만 기다려주세요!
    </v-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    modal:false,
    check:false,
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
      const apiUrl = '/api'
      this.check = true;
      axios.post(`${apiUrl}/KNN/user/`, {
        scores:this.scores,
        pk:this.$session.get('id_number')
      }).then(res => {
        this.check = false;
        alert('평점을 등록했습니다!')
      })
      // console.log(this.$session.getAll())
    }
  }
}
</script>