import axios from 'axios';

const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd'

const searchmovies = {
  state: {
    searchResults: [],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.searchResults = movies
    }
  },
  actions: {
    getMovies(context, searchQuery){
      return axios.get(`https://api.themoviedb.org/3/search/movie?api_key=${API_KEY}&query=${encodeURIComponent(searchQuery)}&language=ko-KR`)
        .then(response => {
          // console.log(response.data.results)
          context.commit('GET_MOVIES', response.data.results)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },

}

export default searchmovies