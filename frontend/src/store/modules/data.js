/* eslint-disable */
import api from '../../api'

// initial state
const state = {
    // shape: [{ id, title, genres, viewCnt, rating }]
    movieSearchList: [],
    temp_movie: [],
    movieSearchList_admin: [],
    movieList_homepage: [],
    movieList_homepage_itembased: [],
    movieList_homepage_userbased: [],
    userSearchList: [],
    userSearchList_admin: [],
    username: '',
    cnt: 10
}

// actions
const actions = {
    async searchMovies({ commit }, params) {
        // document.style.opacity = 0.1
        var preload = document.querySelector('#searching')
            // preload.style.display = 'block'
        const resp = await api.searchMovies(params)
            // preload.style.display = 'none'
        if (!resp.data.length) {
            alert('해당 이름의 영화는 없습니다.')
        }
        const movies = resp.data.map(d => ({
            id: d.id,
            title: d.title,
            genres_array: d.genres_array,
            watch_count: d.watch_count,
            averagerate: d.averagerate,
            score_users: d.score_users,
            plot: d.plot,
            url: d.url,
            director: d.director,
            casting: d.casting
        }))
        commit('setMovieSearchList', movies)
    },
    async searchMovies_admin({ commit }) {
        const resp = await api.searchMovies(params)
        if (!resp.data.length) {
            alert('해당 이름의 영화는 없습니다.')
        }
        const movies = resp.data.map(d => ({
            id: d.id,
            title: d.title,
            genres_array: d.genres_array,
            watch_count: d.watch_count,
            averagerate: d.averagerate,
            score_users: d.score_users,
            plot: d.plot,
            url: d.url,
            director: d.director,
            casting: d.casting
        }))
        commit('setMovieSearchList_admin', movies)
    },
    async getMovies_homepage({ commit }) {
        if (state.movieList_homepage.length !== 0) {
            return
        } else {
            const resp = await api.getMovies_homepage()
            if (!resp.data.length) {
                alert('해당 이름의 영화는 없습니다.')
            }
            const movies = resp.data.map(d => ({
                id: d.id,
                title: d.title,
                genres_array: d.genres_array,
                watch_count: d.watch_count,
                averagerate: d.averagerate,
                score_users: d.score_users,
                plot: d.plot,
                url: d.url,
                director: d.director,
                casting: d.casting
            }))
            commit('setMovieList_homepage', movies)
        }
    },
    async getMovies_subscription_itembased({ commit }, params) {
        var id = params.id
        if (state.movieList_homepage_itembased.length !== 0) {
            return
        } else {
            const resp = await api.getMovies_homepage_itembased(id)
            const movies = resp.data.map(d => ({
                id: d.id,
                title: d.title,
                genres_array: d.genres_array,
                watch_count: d.watch_count,
                averagerate: d.averagerate,
                score_users: d.score_users,
                plot: d.plot,
                url: d.url,
                director: d.director,
                casting: d.casting
            }))
            var data = {
                movies: movies,
                params: params
            }
            commit('setMovieList_homepage_itembased', data)
        }
    },
    async getMovies_subscription_userbased({ commit }, params) {
        var id = params.id
        if (state.movieList_homepage_itembased.length !== 0) {
            // if (params.approval===true) {
            //   console.log(document.querySelector('#item'))
            // }
            return
        } else {
            const resp = await api.getMovies_homepage_userbased(params)
            const movies = resp.data.map(d => ({
                id: d.id,
                title: d.title,
                genres_array: d.genres_array,
                watch_count: d.watch_count,
                averagerate: d.averagerate,
                score_users: d.score_users,
                plot: d.plot,
                url: d.url,
                director: d.director,
                casting: d.casting
            }))
            var data = {
                movies: movies,
                params: params
            }
            commit('setMovieList_homepage_userbased', data)
        }
    },
    async searchGenres({ commit }, params) {
        const resp = await api.searchGenre(params)
        if (!resp.data.length) {
            alert('해당 장르의 영화는 없습니다.')
        }
        const movies = resp.data.map(d => ({
            id: d.id,
            title: d.title,
            genres_array: d.genres_array,
            watch_count: d.watch_count,
            averagerate: d.averagerate,
            score_users: d.score_users,
            plot: d.plot,
            url: d.url,
            director: d.director,
            casting: d.casting
        }))
        commit('setMovieSearchList', movies)
    },
    async searchAges({ commit }, params) {
        const resp = await api.searchAges(params)
        if (!resp.data.length) {
            alert('해당 연령대의 데이터는 없습니다.')
        }
        const movies = resp.data.map(d => ({
            id: d.id,
            title: d.title,
            genres_array: d.genres_array,
            watch_count: d.watch_count,
            averagerate: d.averagerate,
            score_users: d.score_users,
            plot: d.plot,
            url: d.url,
            director: d.director,
            casting: d.casting
        }))
        commit('setMovieSearchList', movies)
    },
    async searchOccupations({ commit }, params) {
        const resp = await api.searchOccupations(params)
        if (!resp.data.length) {
            alert('해당 직업의 데이터는 없습니다.')
        }
        const movies = resp.data.map(d => ({
            id: d.id,
            title: d.title,
            genres_array: d.genres_array,
            watch_count: d.watch_count,
            averagerate: d.averagerate,
            score_users: d.score_users,
            plot: d.plot,
            url: d.url,
            director: d.director,
            casting: d.casting
        }))
        commit('setMovieSearchList', movies)
    },
    async searchGenders({ commit }, params) {
        const resp = await api.searchGenders(params)
        if (!resp.data.length) {
            alert('해당 성별의 데이터는 없습니다.')
        }
        const movies = resp.data.map(d => ({
            id: d.id,
            title: d.title,
            genres_array: d.genres_array,
            watch_count: d.watch_count,
            averagerate: d.averagerate,
            score_users: d.score_users,
            plot: d.plot,
            url: d.url,
            director: d.director,
            casting: d.casting
        }))
        commit('setMovieSearchList', movies)
    },
    resetMovieList({ commit }, params) {
        commit('setMovieSearchList', [])
    },
    async searchUsers({ commit }, params) {
        var preload = document.querySelector('#searching')
        preload.style.display = 'block'
        const resp = await api.searchUsers(params)
        preload.style.display = 'none'
        if (!resp.data.length) {
            alert('해당 이름의 유저는 없습니다.')
        }
        const users = resp.data.map(d => ({
            user_id: d.id,
            username: d.username
        }))
        commit('setUserSearchList', users)
    },
    async searchUsers_admin({ commit }, params) {
        const resp = await api.searchUsers(params)
        const users = resp.data.map(d => ({
            user_id: d.id,
            username: d.username
        }))
        commit('setUserSearchList_admin', users, params.approval)
    },
}

// mutations
const mutations = {
    setMovieSearchList(state, movies) {
        console.log(movies)
        state.temp_movie = movies.map(m => m)
        movies.forEach(element => {
                state.movieSearchList.push(element)
            })
            // state.movieSearchList = state.movieSearchList.concat(movies.map(m => m))
            // console.log(state.movieSearchList)
            // state.movieSearchList = movies.map(m => m)
    },
    setMovieSearchList_admin(state, movies) {
        state.movieSearchList_admin = movies.map(m => m)
    },
    setMovieList_homepage(state, movies) {
        state.movieList_homepage = movies.map(m => m)
    },
    setUserSearchList(state, users) {
        state.userSearchList = users.map(function(m) {
            return m
        })
    },
    setUserSearchList_admin(state, users) {
        state.userSearchList_admin = users.map(function(m) {
            return m
        })
    },
    setUser(state, username) {
        state.username = username
    },
    setMovieList_homepage_itembased(state, data) {
        if (data.params.approval) {
            // document.querySelector('#item').style.display = 'block';
        }
        // console.log(data)
        state.movieList_homepage_itembased = data.movies.map(m => m)
    },
    setMovieList_homepage_userbased(state, data) {
        if (data.params.approval) {
            // document.querySelector('#user').style.display = 'block';
        }
        state.movieList_homepage_userbased = data.movies.map(m => m)
    },
}

// getters
const getters = {
    username: state => state.username
}

export default {
    namespaced: true,
    state,
    actions,
    mutations
}