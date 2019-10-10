<template>
  <div>
    <v-form
      ref="form"
      v-model="valid"
      lazy-validation
    >
      <v-text-field
        v-model="title"
        :counter="30"
        :rules="titleRules"
        label="Title"
        required
        dark
      />
      <v-select
        v-model="genres"
        :items="items"
        :rules="[v => !!v || 'Item is required']"
        label="Genre"
        multiple
        required
        dark
      />
      <v-text-field
        v-model="url"
        label="ImageURL"
        required
        dark
      />
      <v-text-field
        v-model="director"
        :rules="titleRules"
        label="Director"
        required
        dark
      />
      <v-combobox
        v-model="casting"
        label="Casting"
        hint="Maximum of 5 tags"
        persistent-hint
        small-chips
        multiple
        required
        dark
      />
      <v-textarea
        v-model="plot"
        solo
        :counter="500"
        label="Plot"
        required
      />
      <v-btn :disabled="!valid" color="success" class="mr-4" @click="validate">Validate</v-btn>
      <v-btn color="error" class="mr-4" @click="reset">Reset Form</v-btn>
    </v-form>
    <v-dialog v-model="dialog" persistent max-width="700">
      <template v-slot:activator="{ on }">
        <v-btn dark v-on="on">등록하기</v-btn>
      </template>
      <v-card>
        <v-card-title class="headline">{{ title }}</v-card-title>
        <v-card-text>장르: {{ genres }}</v-card-text>
        <v-card-text>이미지url: {{ url }}</v-card-text>
        <v-card-text>감독: {{ director }}</v-card-text>
        <v-card-text>배우: {{ casting }}</v-card-text>
        <v-card-text>줄거리: {{ plot }}</v-card-text>
        <v-card-actions>
          <v-btn color="green darken-1" text @click="createMovie();dialog=false">OK</v-btn>
          <v-btn color="green darken-1" text @click="dialog=false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  components: {

  },
  data: () => ({
    valid: true,
    dialog: false,
    title:'',
    genres:[],
    plot:'',
    url:'',
    director:'',
    casting:[],
    items: ['Action', 'Adventure', 'Animation', 'Comedy',
    'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
    'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western', "Children's"],
    titleRules: [
      v => !!v || 'This is required',
      v => (v && v.length <= 30) || 'Name must be less than 30 characters',
    ]
  }),
  watch: {
    casting (val) {
      if (val.length > 5) {
        this.$nextTick(() => this.casting.pop())
      }
    },
  },
  methods: {
    validate () {
      if (this.$refs.form.validate()) {
        this.snackbar = true
      }
    },
    reset () {
      this.$refs.form.reset()
    },
    createMovie: function() {
      const apiUrl = '/api'
      var preload = document.querySelector('#check1')
      preload.style.display = 'block'

      axios.post(`${apiUrl}/KNN/movie/`, {
        title:this.title,
        genres:this.genres,
        plot:this.plot,
        url:this.url,
        director:this.director,
        casting:this.casting
      }).then(() => {
        preload.style.display = 'none'
        alert("영화가 등록되었습니다!")
        this.$refs.form.reset()
      })
    }
  }
}
</script>