import axios from 'axios';
const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd'

const userInfo = {
  state: {
    userProfile: null,
    profileImg: null,
    actorId: null,
    actor: null,
  },
  getters: {
  },
  mutations: {
    setUserProfile(state, userProfile) {
      state.userProfile = userProfile;
      state.actorId = userProfile.character;
    },
    setProfileImg(state, profileImg) {
      state.profileImg = profileImg;
    },
    setActor(state, actor) {
      state.actor = actor;
    },
    },
  actions: {
    async fetchUserProfile({ commit }, username) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/v1/profile/${username}`);
        commit('setUserProfile', response.data);
        commit('setProfileImg', response.data.profile_img)
      } catch (error) {
        console.error('유저 정보를 가져오는 중 오류 발생:', error);
      }
    },
    saveUserProfileImg({commit}, profileImg) {
      commit('setProfileImg', profileImg)
    },
    saveActor({ commit }, actor) {
      commit('setActor', actor);
    },
    async fetchActorDetail({ commit }, actorId) {
      try {
        const response = await axios.get(`https://api.themoviedb.org/3/person/${actorId}?api_key=${API_KEY}`);
        const actorDetail = response.data;
        commit('setActor', actorDetail);
      } catch (error) {
        console.error('배우 세부 정보를 가져오는 중 오류 발생:', error);
      }
    }
  },
}

export default userInfo