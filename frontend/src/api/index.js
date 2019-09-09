/* eslint-disable */
import axios from 'axios'

const apiUrl = '/api'

export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params,
    })
  },
  searchGenre(params) {
    // movie search by genre
    return axios.get(`${apiUrl}/genres/`, {
      params,
    })
  },
  searchUsers(params) {
    return axios.get(`${apiUrl}/users/`, {
      params,
    })
  },
  searchAges(params) {
    return axios.get(`${apiUrl}/ages/`, {
      params,
    })
  },
  searchOccupations(params) {
    return axios.get(`${apiUrl}/occupations/`, {
      params,
    })
  },
  searchGenders(params) {
    return axios.get(`${apiUrl}/genders/`, {
      params,
    })
  }
}
