<template>
  <v-card>
    <v-card-text>
    <p style="text-align: center; font-size: 2.5rem; padding-bottom: 3rem; padding-top: 3rem;">Sign up</p>
    <form>
    <v-text-field
    v-model="username"
    :counter="10"
    label="Name"
    :rules="nameRules"
    required
    style="margin-left: 5rem; margin-right: 5rem;"
    ></v-text-field>
    <v-text-field
    v-model="password"
    label="Password"
    :counter="20"
    :rules="passwordRules"
    type="password"
    style="margin-left: 5rem; margin-right: 5rem;"
    required
    ></v-text-field>
    <v-layout style="margin-left: 5rem; margin-right: 5rem;">
    <span style="vertical-align: middle; color: rgba(0, 0, 0, 0.54); padding-left: 0.3rem; padding-right: 2.5rem;">Gender</span>
    <v-radio-group v-model="gender" row>
    <v-radio label="Female" value="F"></v-radio>
    <v-radio label="Male" value="M"></v-radio>
    </v-radio-group>
    </v-layout>
    <v-text-field
    v-model="age"
    type="number"
    label="Age"
    style="margin-left: 5rem; margin-right: 5rem;"
    required
    ></v-text-field>
    <v-text-field
    v-model="occupation"
    label="Occupation"
    style="margin-left: 5rem; margin-right: 5rem;"
    required
    ></v-text-field>

    <v-btn @click="submit" style="margin-top: 2rem; margin-bottom: 1rem;">Sign up</v-btn>
    </form>
    <div style="padding-top: 1.5rem; padding-top: 3rem;">
    <router-link to="signin">로그인하러 가기</router-link>
    </div>
    </v-card-text>
  </v-card>
</template>

<script>
import axios from 'axios';

export default {
  components: {
  },
  data() {
    return {
      username: '',
      password: '',
      gender: 'F',
      age: null,
      occupation: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters'
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 6) || 'Name must be more than 6 characters'
      ],
    }
  },
  methods: {
    async submit() {
      const apiUrl = '/api'   
      let __this = this;
      await axios.post(`${apiUrl}/auth/signup/`, {
        username: __this.username,
        password: __this.password,
        gender: __this.gender,
        age: __this.age,
        occupation: __this.occupation
      }).then(res => {
        if (res.status == 201) {
          this.$router.push('/users/signin');
        }
      })
    }
  }
};
</script>