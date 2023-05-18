import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

const community = {
  state: {
    articles: []
  },
  getters: {

  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
      .then(res =>
        // console.log(res,context)
        context.commit('GET_ARTICLES',res.data)
      )
      .catch(err => console.log(err))
    }
  }
}

export default community