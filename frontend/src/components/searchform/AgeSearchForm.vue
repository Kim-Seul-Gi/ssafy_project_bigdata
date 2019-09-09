<template>
  <v-form ref="form">
    <div>
      <br>
      <div v-for="age in ages" style="display:inline-block;">
        <input type="radio" :value="age" v-model="picked">
        <label style="font-size:10px;">{{age}}</label> &nbsp;
      </div>
    </div>
    <br>
    <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
    <!-- 	*  1:  "Under 18"
    	* 18:  "18-24"
    	* 25:  "25-34"
    	* 35:  "35-44"
    	* 45:  "45-49"
    	* 50:  "50-55"
    	* 56:  "56+" -->
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
    ages : ['전체보기','Under 18', '18-24', '25-34', '35-44', '45-49', '50-55', '56+'],
    picked:'',
  }),
  methods: {
    onSubmit: function() {
      if (this.picked == '전체보기') {
        const params = {
          age: '',
        };
        this.submit(params);
      } else {
        const params = {
          age: this.picked,
        };
        this.submit(params);
      }

    },

  }
};
</script>
