import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  state: {
    articles: [],
  },
  mutations: {
    SET_ARTICLES(state, articles) {
      state.articles = articles;
    },
  },
  actions: {
    getArticles({ commit, rootState }) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${rootState.token.token}`,
        },
      })
        .then(res => {
          commit('SET_ARTICLES', res.data);
        })
        .catch(err => {
          console.log(err);
        });
    },
  },
  getters: {
    
  },
};
