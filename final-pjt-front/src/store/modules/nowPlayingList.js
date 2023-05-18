import axios from 'axios';

const API_URL = 'https://api.themoviedb.org/3/movie/now_playing'
const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd'

const nowPlayingList = {
  state: {
    nowplayingMovies: []
  },
  getters: {
  },
  mutations: {
    GET_NOW_PLAYING_MOVIES(state, movies) {
      state.nowplayingMovies = movies
    }
  },
  actions: {
    getNowPlayingMovies(context){
      return axios.get(`${API_URL}?api_key=${API_KEY}&language=ko&page=1&region=KR`)
        .then(response => {
          // console.log(response.data.results)
          context.commit('GET_NOW_PLAYING_MOVIES', response.data.results)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },

}

export default nowPlayingList