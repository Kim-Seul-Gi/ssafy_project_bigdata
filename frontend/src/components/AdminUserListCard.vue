<template>
  <div>
    <v-hover v-slot:default="{ hover }">
      <v-card :elevation="hover ? 8 : 2">
        <v-layout align-center py-4 pl-4>
          <v-flex text-center>
            <v-container grid-list-lg pa-0>
              <div style="cursor: pointer; display: inline-block" @click="SELECT_UserDetail()">{{ id }} | {{ username }}</div>
              <div>
                <v-btn @click="profile_detail(id); dialog=true">수정</v-btn>
                <v-btn @click="profile_delete(id)">삭제</v-btn>
              </div>
            </v-container>
          </v-flex>
        </v-layout>
      </v-card>
    </v-hover>
    <v-dialog v-model="dialog" width="500">
      <v-card flat class="text-xs-center ma-3" min-width="500">
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-card-text>
            <v-text-field
              id="username"
              v-model="username"
              hint="이름을 변경할 수 있습니다."
              name="username"
              label="Username"
              clearable
            />
            <v-text-field
              id="gender"
              v-model="gender"
              hint="성별을 변경할 수 있습니다."
              name="gender"
              label="Gender"
              clearable
            />
            <v-text-field
              id="age"
              v-model="age"
              hint="나이를 변경할 수 있습니다."
              name="age"
              label="Age"
              clearable
            />
            <v-select
              id="occupation"
              v-model="occupation"
              hint="직업을 변경할 수 있습니다."
              name="occupation"
              label="Occupation"
              :items="occupations"
              attach
              occupation
            />
          </v-card-text>
        </v-form>
        <v-btn color="primary" text @click="profile_update(id); dialog=false">
          수정하기
        </v-btn>
        <v-btn color="primary" text @click="dialog=false">
          닫기
        </v-btn>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import router from "../router";
import axios from "axios"
export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    username: {
      type: String,
      default: ""
    }
  },
  data:() => ({
    dialog: false,
    valid: true,
    occupations: ["other","academic/educator","artist","clerical/admin","college/grad student",
    "customer service","doctor/health care","executive/managerial","farmer","homemaker",
    "K-12 student","lawyer","programmer","retired","sales/marketing","scientist",
    "self-employed","technician/engineer","tradesman/craftsman","unemployed","writer"],
    gender:'',
    age:'',
    occupation:''
  }),
  methods: {
    SELECT_UserDetail() {
      var user_data = {'id':this.id, 'username':this.username, 'occupation':this.occupation}
      router.push({name:'user-detail', params : {'id':user_data.id, 'user_data':user_data}})
    },
    profile_detail: async function(id) {
      const apiUrl = '/api'
      var profile = await axios.get(`${apiUrl}/users/${id}`)
      this.gender = profile.data[0].gender
      this.age = profile.data[0].age
      this.occupation = profile.data[0].occupation
    },
    profile_delete: function(id) {
      const apiUrl = '/api'
      let chk = confirm("정말 삭제하시겠습니까?")
      if (chk == true) {
        axios.delete(`${apiUrl}/profile/${id}/delete/`, {id})
        window.location.reload()
      }
    },
    profile_update: function(id) {
      const apiUrl = '/api'
      let chk = confirm("수정하시겠습니까?")
      if (chk == true) {
        axios.put(`${apiUrl}/profile/${id}/update/`, {
          username:this.username,
          gender:this.gender,
          age:this.age,
          occupation:this.occupation
        })
      }
    }
  }
}
</script>