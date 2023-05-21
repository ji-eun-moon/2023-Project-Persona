const token ={
    state: {
      token: null
    },
    getters: {
    },
    mutations: {
      setToken(state, token) {
        state.token = token;
        console.log('token:', state.token);
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