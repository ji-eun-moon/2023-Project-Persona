import axios from 'axios';

const API_URL = 'https://api.themoviedb.org/3/movie';
const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd';

const moviedetail = {
  state: {
    movieDetail: [],
    movieCast: [],
    castProfileImages: [],
    castNames: [],
  },
  mutations: {
    GET_MOVIE_DETAIL(state, details) {
      state.movieDetail = details;
    },
    GET_MOVIE_CAST(state, cast) {
      state.movieCast = cast;
    },
    GET_CAST_PROFILE_IMAGES(state, profiles) {
      state.castProfileImages = profiles;
    },
    GET_CAST_NAMES(state, names) {
      state.castNames = names;
    },
  },
  actions: {
    getMovieDetail(context, movieId) {
      return axios.get(`${API_URL}/${movieId}?api_key=${API_KEY}&language=ko`)
        .then(response => {
          context.commit('GET_MOVIE_DETAIL', response.data);
          return response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getMovieCast(context, movieId) {
      return axios.get(`${API_URL}/${movieId}/credits?api_key=${API_KEY}&language=ko`)
        .then(response => {
          const mainCast = response.data.cast.filter(member => member.known_for_department === 'Acting');
          const topFiveCast = mainCast.slice(0, 6);
          context.commit('GET_MOVIE_CAST', topFiveCast);
          const profilePromises = topFiveCast.map(member => axios.get(`https://api.themoviedb.org/3/person/${member.id}?api_key=${API_KEY}&language=ko`));
          const namePromises = topFiveCast.map(member => axios.get(`https://api.themoviedb.org/3/person/${member.id}?api_key=${API_KEY}&language=ko`));
          return Promise.all([Promise.all(profilePromises), Promise.all(namePromises)]);
        })
        .then(([profileResponses, nameResponses]) => {
          const castProfileImages = profileResponses.map(response => response.data.profile_path);
          context.commit('GET_CAST_PROFILE_IMAGES', castProfileImages);

          const castNames = nameResponses.map(response => response.data.name);
          context.commit('GET_CAST_NAMES', castNames);
          return castProfileImages;
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
};

export default moviedetail;
