<template>
  <v-app id="app">
    <v-navigation-drawer v-model="drawer" app permanent dark floating fixed color="#000">
      <v-list dense dark color="#000">
        <div style="margin-left: 1.5rem; margin-top: 2rem; margin-bottom: 1.7rem;">
        <router-link to="/" style="text-decoration:none;"><img src="../public/img/popcorn.png" style="height: 4rem; width: 4rem; margin-right: 0.9rem; margin-bottom: -1.2rem;"/><span style="font-size: 2rem; height: 4rem; line-height: 4rem; vertical-align: middle; font-family: 'Raleway', sans-serif; color: white;">Fluid</span></router-link>
        </div>
        <template v-for="(choice, i) in choices">
          <v-list-item
            :key="i"
            v-if="choice.auth!==false"
            @click="() => {
              if (choice.path) {
                goTo(choice.path)
              } else {
                logout()
              }
            }"
          >
            <v-list-item-action>
              <v-icon>{{ choice.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 white--text">{{ choice.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-content>
      <v-container fluid fill-height style="background-color: #303030; padding: 0;">
        <v-layout align-center>
          <div style="width:100%; height:100%; position:absolute;
          z-index:10; display:none; background-color:#a6a6a6; opacity:.6;" id="searching">

              <div style="width:100%;height:100%" class="lds-wedges">
                <div><div><div></div></div><div><div></div></div><div><div></div></div>
                <div><div></div></div></div></div>

          </div>
          <div style="width:100%; height:100%; position:absolute;
          z-index:10; display:none; background-color:#a6a6a6; opacity:.6;" id="check1">
              <v-card class="d-flex justify-center" ><p style="font-size:30px">영화 등록 중입니다!
                <br>잠시만 기다려주세요!</p></v-card>
            <div style="width:100%;height:50%" class="lds-wedges">
              <div style="width:100%;height:50%" class="lds-wedges">
              <div><div><div></div></div><div><div></div></div><div><div></div></div>
              <div><div></div></div></div></div>
            </div>
          </div>
          <div style="width:100%; height:100%; position:absolute;
          z-index:10; display:none; background-color:#a6a6a6; opacity:.6;" id="check2">
              <v-card class="d-flex justify-center" ><p style="font-size:30px">평점 등록 중입니다!
                <br>잠시만 기다려주세요!</p></v-card>
            <div style="width:100%;height:50%" class="lds-wedges">
              <div style="width:100%;height:50%" class="lds-wedges">
              <div><div><div></div></div><div><div></div></div><div><div></div></div>
              <div><div></div></div></div></div>
            </div>
          </div>
          <!-- each pages will be placed here -->
          <router-view />
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import router from "./router";
import axios from 'axios';

export default {
  data: () => ({
    drawer: true,
    choices: [
      {
        icon: "mdi-account-circle",
        text: "로그인",
        path: "sign-in"
      },
      {
        icon: "mdi-movie",
        text: "영화 검색",
        path: "movie-search"
      },
      {
        icon: "fa-search",
        text: "유저 검색",
        path: "user-search"
      },
      {
        icon: "mdi-account",
        text: "My 페이지",
        path: "my-page",
        auth: false,
      },
      {
        icon: "mdi-wrench",
        text: "관리자 페이지",
        path: "admin-page",
        auth: false,
      }
    ],
    user: '',
    user2: "",
  }),
  mounted() {
    this.setUser();
  },
  watch: {
    user: function () {
      if (this.user == '') {
        this.choices[0] = {icon: "mdi-account-circle", text: "로그인", path: "sign-in"}
      } else {
        this.choices[0] = {icon: "mdi-account-circle", text: "로그아웃", path: ""}
      }
    }
  },
  methods: {
    goTo: function(path) {
      router.push({ name: path });
    },
    homepage() {
      router.push({name:'home'})
    },
    setUser() {

      // 이건 계속 axios를 보내야하는데, 초기에 session 값에 로그인 정보가 저장되어 있다면 이것은 사용할 필요가 사실상 없어집니다.
      // 즉 axios를 보내지 않고 session 을 확인하는 것으로도 기능을 수행할 수 있게 됩니다.
      // let __this = this;
      // let tmp = axios.get('/api/auth/userState').then(res => {
      //   if (res.data.user != '') {
      //     __this.user = res.data.user
      //   }
      //   if (__this.user == '') {
      //     __this.choices[0] = {icon: "mdi-account-circle", text: "로그인", path: "sign-in"}
      //   } else {
      //     __this.choices[0] = {icon: "mdi-account-circle", text: "로그아웃", path: ""}
      //   }
      // })

      if (this.$session.get('id')==undefined || this.$session.get('id')=="" ) {
        // console.log('로그인 안 한 상태입니다.')
        this.$session.set('id', '')
        this.$session.set('id_number', '')
        this.$session.set('admin', false)
        this.choices[0] = {icon: "mdi-account-circle", text: "로그인", path: "sign-in"}
      } else {
        // console.log(this.$session.get('id'))
        // console.log(this.$session.get('admin'))
        this.choices[0] = {icon: "mdi-account-circle", text: "로그아웃", path: ""}
        this.choices[3].auth = true
        if (this.$session.get('admin')==true) {
          this.choices[4].auth = true
        }
      }
    },
    logout() {
      // let __this = this
      let tmp = axios.get('/api/auth/logout').then(res => {
        // console.log(res)
      })
      this.choices[3].auth = false
      this.choices[4].auth = false
      this.user = ''
      this.$session.set('id', '')
      this.$session.set('id_number', '')
      this.$session.set('admin', false)
      router.push({name:'home'})
      window.location.reload()
      // router.push('/')
    },

    // get_array() {
    // movie를 장르로 나눠서 csv 만들때 사용한 코드입니다.
    //   const apiUrl = '/api'
    //   axios.get(`${apiUrl}/movies/getarray`)
    // }
  }
};
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none;
}
@keyframes lds-wedges {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-webkit-keyframes lds-wedges {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
.lds-wedges {
  position: relative;
}
.lds-wedges > div > div {
  -webkit-transform-origin: 100px 100px;
  transform-origin: 100px 100px;
  -webkit-animation: lds-wedges 3s linear infinite;
  animation: lds-wedges 3s linear infinite;
  opacity: 0.8;
}
.lds-wedges > div > div > div {
  position: absolute;
  left: 30px;
  top: 30px;
  width: 70px;
  height: 70px;
  border-radius: 70px 0 0 0;
  -webkit-transform-origin: 100px 100px;
  transform-origin: 100px 100px;
}
.lds-wedges > div div:nth-child(1) > div {
  background: #51CACC;
  -webkit-transform: rotate(0deg);
  transform: rotate(0deg);
}
.lds-wedges > div div:nth-child(1) {
  -webkit-animation-duration: 0.75s;
  animation-duration: 0.75s;
}
.lds-wedges > div div:nth-child(2) > div {
  background: #9DF871;
  -webkit-transform: rotate(0deg);
  transform: rotate(0deg);
}
.lds-wedges > div div:nth-child(2) {
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
}
.lds-wedges > div div:nth-child(3) > div {
  background: #E0FF77;
  -webkit-transform: rotate(0deg);
  transform: rotate(0deg);
}
.lds-wedges > div div:nth-child(3) {
  -webkit-animation-duration: 1.5s;
  animation-duration: 1.5s;
}
.lds-wedges > div div:nth-child(4) > div {
  background: #DE9DD6;
  -webkit-transform: rotate(0deg);
  transform: rotate(0deg);
}
.lds-wedges > div div:nth-child(4) {
  -webkit-animation-duration: 3s;
  animation-duration: 3s;
}
.lds-wedges {
  width: 90% !important;
  height: 80% !important;
  display: flex;
  align-items: center;
  justify-content: center;
  -webkit-transform: translate(-100px, -100px) scale(1) translate(100px, 100px);
  transform: translate(-100px, -100px) scale(1) translate(100px, 100px);
}
</style>
