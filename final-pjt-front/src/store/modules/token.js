const token ={
    state: {
      token: null,
      loggedIn: false,
    },
    getters: {
    },
    mutations: {
      setToken(state, token) {
        state.token = token;
        console.log('token:', state.token);
      },
      setLoggedIn(state, value) {
        state.loggedIn = value;
      },
    },
    actions: {
      saveToken({ commit }, token) {
        // 로그인 액션: 토큰을 받아와 스토어의 토큰 상태를 업데이트
        commit('setToken', token);
      },
    }
}

export default token