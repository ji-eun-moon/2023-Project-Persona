import axios from 'axios';

const API_URL = 'https://api.themoviedb.org/3/trending/movie'
const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd'

const trendingList = {
  state: {
    dailyTrendingMovies: [],
    weeklyTrendingMovies: [],
  },

  mutations: {
    GET_DAILY_TRENDING_MOVIES(state, movies) {
      state.dailyTrendingMovies = movies;
    },
    GET_WEEKLY_TRENDING_MOVIES(state, movies) {
      state.weeklyTrendingMovies = movies;
    }
  },

  actions: {

    getDailyTrendingMovies(context) {
      return axios.get(`${API_URL}/day?api_key=${API_KEY}&language=ko`)
        .then(response => {
          context.commit('GET_DAILY_TRENDING_MOVIES', response.data.results);
        })
        .catch(error => {
          console.error('Error daily trending movies:', error);
        });
    },

    getWeeklyTrendingMovies(context) {
      return axios.get(`${API_URL}/week?api_key=${API_KEY}&language=ko`)
        .then(response => {
          context.commit('GET_WEEKLY_TRENDING_MOVIES', response.data.results);
        })
        .catch(error => {
          console.error('Error weekly trending movies:', error);
        });
    }
  },

}

export default trendingList