<template>
  <v-form ref="form">
    <div>
      <br>
      <div v-for="occupation in occupations" style="display:inline-block;">
        <input type="radio" :value="occupation" v-model="picked">
        <label style="font-size:10px;">{{occupation}}</label> &nbsp;
      </div>
    </div>
    <br>
    <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
    <!-- *  0:  "other" or not specified
  	*  1:  "academic/educator"
  	*  2:  "artist"
  	*  3:  "clerical/admin"
  	*  4:  "college/grad student"
  	*  5:  "customer service"
  	*  6:  "doctor/health care"
  	*  7:  "executive/managerial"
  	*  8:  "farmer"
  	*  9:  "homemaker"
  	* 10:  "K-12 student"
  	* 11:  "lawyer"
  	* 12:  "programmer"
  	* 13:  "retired"
  	* 14:  "sales/marketing"
  	* 15:  "scientist"
  	* 16:  "self-employed"
  	* 17:  "technician/engineer"
  	* 18:  "tradesman/craftsman"
  	* 19:  "unemployed"
  	* 20:  "writer" -->
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
    title: "",
    occupations : ['전체보기','academic/educator', 'artist', 'clerical/admin', 'college/grad student', 'customer service', 'doctor/health care', 'executive/managerial',
                  'farmer', "homemaker", "K-12 student", "lawyer", "programmer", "retired", "sales/marketing", "scientist", "self-employed", "technician/engineer",
                  "tradesman/craftsman", "unemployed", "writer"],
    picked:'',
  }),
  methods: {
    onSubmit: function() {
      if (this.picked == '전체보기') {
        const params = {
          occupation: '',
        };
        this.submit(params);
      } else {
        // console.log(this.picked, 123123)
        const params = {
          occupation: this.picked,
        };
        this.submit(params);
      }

    },

  }
};
</script>
