/* eslint-disable */
import api from '../../api'

// initial state
const state = {
    // shape: [{ id, title, genres, viewCnt, rating }]
    movieSearchList: [],
    movieSearchList_admin: [],
    userSearchList: [],
    userSearchList_admin: [],
    username: ''
}

// actions
const actions = {
    async searchMovies({ commit }, params) {
        // document.style.opacity = 0.1
        var preload = document.querySelector('#searching')
        preload.style.display = 'block'
        const resp = await api.searchMovies(params)
        preload.style.display = 'none'
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
    async searchMovies_admin({ commit }, params) {
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
        commit('setUserSearchList_admin', users)
    },
}

// mutations
const mutations = {
    setMovieSearchList(state, movies) {
        state.movieSearchList = movies.map(m => m)
    },
    setMovieSearchList_admin(state, movies) {
        state.movieSearchList_admin = movies.map(m => m)
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
    }
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