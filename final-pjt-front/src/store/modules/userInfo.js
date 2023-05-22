import axios from 'axios';

const userInfo = {
  state: {
    userProfile: null,
    profileImg: null,
    actorId: null,
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
    setCharacter(state, character) {
      state.character = character;
    }
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
    saveCharacter({commit}, character) {
      commit('setCharacter', character)
    },
  },
}

export default userInfo