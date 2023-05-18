import Vue from 'vue'
import Vuex from 'vuex'
import trendingList from './modules/trendingList'
import nowPlayingList from './modules/nowPlayingList'
import upcomingList from './modules/upcomingList'

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
    upcomingList
  }
})
