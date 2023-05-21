import Vue from 'vue'
import Vuex from 'vuex'
import trendingList from './modules/trendingList'
import nowPlayingList from './modules/nowPlayingList'
import upcomingList from './modules/upcomingList'
import community from './modules/community'
import moviedetail from './modules/moviedetail'
import searchmovies from './modules/searchmovies'
import token from './modules/token'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    trendingList,
    nowPlayingList,
    upcomingList,
    community,
    moviedetail,
    searchmovies,
    token
  }
})
