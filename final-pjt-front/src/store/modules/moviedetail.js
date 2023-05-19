import axios from 'axios';

const API_URL = 'https://api.themoviedb.org/3/movie'
const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd'

const moviedetail = {
  state: {
    movieDetail : []
  },
  getters: {
  },
  mutations: {
    GET_MOVIE_DETAIL(state, details) {
      state.movieDetail = details
    }
  },
  actions: {
    getMovieDetail(context, movieId){
      return axios.get(`${API_URL}/${movieId}?api_key=${API_KEY}&language=ko`)
        .then(response => {
          // console.log(response.data)
          context.commit('GET_MOVIE_DETAIL', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    } 
  }
}

export default moviedetail