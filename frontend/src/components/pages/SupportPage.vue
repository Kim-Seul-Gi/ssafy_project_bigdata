<template>
<div>
  <p style="font-size: 3rem; color: white; font-family: 'Jua', sans-serif;">
          여러분의 작은 후원이 모이면 큰 희망이 됩니다</p>
  <p style="font-size: 1.5rem; color: orange;">고맙습니다.</p>
  <p style="font-size: 2.5rem; color: red;">감사합니다.</p>
  <v-row>
  <v-col v-for="(user, i) in this.users" 
        v-bind:key=i
        cols="3">
      <v-card
        class="mx-auto my-12"
        max-width="374"
      >
        <v-img
          :src="user.url"
          height="250"
        ></v-img>

        <v-card-title>{{user.name}}</v-card-title>
        <v-card-text>

          <div>{{user.title}}</div>
        </v-card-text>

        <v-card-text>
          <div class="title text--primary">Availability</div>
          <v-chip-group
            active-class="deep-purple accent-4 white--text"
            column
          >
            <v-chip v-for="(skill, i) in user.skills" v-bind:key=i>{{skill}}</v-chip>
          </v-chip-group>
        </v-card-text>

        <v-card-actions>
          <v-btn
            :href="user.bank"
            color="deep-purple accent-4"
            text
          >
            {{user.AccountNumber}}
          </v-btn>
        </v-card-actions>
          <v-btn @click="support(i)">
            후원하기
          </v-btn>
          {{user.cnt}}
      </v-card>
  </v-col>
  </v-row>
</div>
</template>
<script>
export default {
  components: {

  },
  data: () => ({
    users:[
      {
        url:"https://avatars0.githubusercontent.com/u/43327544?s=460&v=4",
        name:"Hwang yeojin",
        title:"즐",
        skills:[
          "Python",
          "Java",
          "Vue.js",
          "Firebase",
          "Sqlite3",
          "Pilates",
          "Neck slice"
        ],
        AccountNumber:"95739122258,(국민은행)",
        bank:"https://obank.kbstar.com/quics?page=C055027&QSL=F#loading",
        cnt:0
      },
      {
        url:"http://edu.ssafy.com/edu/comm/imgDownload.do?userId=Z%2B13nx9qVOUU0%2B%2BMS1BMEQ%3D%3D",
        name:"Kim seoung hoon",
        title:"인간의 수면 욕구는 어디까지인가",
        skills:[
          "Python",
          "Vue.js",
          "Sqlite3",
          "Greedy Algorithm",
          "Sudoku",
          "Sleep",
          "Cocomong"
        ],
        AccountNumber:"453067-56-026707,(NH농협)",
        bank:"https://branch.nonghyup.com/servlet/IPAR0011I.view",
        cnt:0
      },
      {
        url:"http://edu.ssafy.com/edu/comm/imgDownload.do?userId=2aqyWVSrd2GKXlkYag2L%2FQ%3D%3D",
        name:"Kim seul gi",
        title:"잘하자",
        skills:[
          "Python",
          "Vue.js",
          "Sqlite3",
          "Firebase",
          "Oracle",
          "SQL",
          "정보처리기사",
        ],
        AccountNumber:"1002047639579,(우리은행)",
        bank:"https://spib.wooribank.com/pib/Dream?withyou=PSTRS0008",
        cnt:0
      },
      {
        url:"https://avatars1.githubusercontent.com/u/44271206?s=460&v=4",
        name:"Lee Heon gyu",
        title:"배고파",
        skills:[
          "Python",
          "Java",
          "Sqlite3",
          "MariaDB",
          "Vue.js",
          "Poppin",
          "Hiphop"
        ],
        AccountNumber:"130047-52-145675,(NH농협)",
        bank:"https://branch.nonghyup.com/servlet/IPAR0011I.view",
        cnt:0
      }
    ],
  }),
  methods: {
    support(id) {
      this.users[id].cnt += 1;
      Swal.fire({
        text: '1000원 후원에 성공하셨습니다!',
        type: 'success'
      })
    }
  }
}
</script>