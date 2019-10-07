<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <div>
        <p style="color: white; font-size: 1.4rem; font-family: 'Jua', sans-serif;">10개 이상 평점을 매겨주세요. 더 많이 평점을 줄수록 정확한 추천을 드립니다 :)</p>
        <v-btn color="red lighten-2" dark style="margin-bottom: 1rem;" @click="save()">평가 완료</v-btn>
    </div>
    <v-layout justify-center wrap>
        <!-- 처음에 보여주는 것 : 조회수 순 -->
      <v-flex v-for="(card,i) in movielist" :key="i" xs12 sm6 md4 lg3 xl2 style="height: 26rem; width: 28rem;">
        <v-card style="margin:10px; height: 25rem; width: 15rem; border-radius:15px;" color="#424242" dark>
            <v-img :src="card.url || 'https://cdn.samsung.com/etc/designs/smg/global/imgs/support/cont/NO_IMG_600x600.png'" style="height:16rem; width: 15rem;"></v-img>
            <v-card-text>
                <p style="font-size: 1rem;">{{ card.title }}</p>
                <div class="text-center mt-1" @click="plus(card.id, card.rating)">
                    <v-rating
                        v-model="card.rating"
                        color="yellow darken-3"
                        background-color="grey darken-1"
                        half-increments
                        hover
                    ></v-rating>
                </div>
            </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-btn @click="before_plusMovies()" style="margin-top: 1.5rem; margin-bottom: 2rem;" fab><v-icon dark>mdi-plus</v-icon></v-btn>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import axios from 'axios';

export default {
  mounted() {
      this.onSubmit();
  },
  data: () => ({
    movielist:[],
    bymoviename:true,
    bygenre:false,
    byage:false,
    byoccupation:false,
    bygender:false,
    reset : true,
    num:1,
    rating: 0,
    rating_box:{}
  }),
  watch: {

  },
  methods: {
    ...mapActions("data", ["searchMovies", "plusMovies"]),
    onSubmit: function() {
        const apiUrl = '/api'
        const params = {
            title: ''
            // cnt: this.cnt
        }
        axios.get(`${apiUrl}/movies`, {
            params
        }).then(res => {
            // console.log(res.data)
            let tmp = []
            res.data[0].forEach(ele => {
                ele['rating'] = 0
                tmp.push(ele)
            })
            this.movielist = tmp
        })
    },
    before_plusMovies() {
      const params = {'title':'', 'num':this.num}
      const apiUrl = '/api'
      this.num += 1
      axios.get(`${apiUrl}/movies`, {
            params
        }).then(res => {
            let tmp = []
            res.data[0].forEach(ele => {
                ele['rating'] = 0
                tmp.push(ele)
            })
            this.movielist = this.movielist.concat(res.data[0])
        })
    },
    save() {
        const apiUrl = '/api'
        axios.post(`${apiUrl}/signup/new_cluster/`, {
            user_pk:this.$session.get("id_number"),
            movies:this.rating_box,
        }).then(res => {

        })
    },
    plus(id, rating) {
      this.rating_box[id]=rating
      console.log(this.rating_box)
    }
  }
}
</script>
