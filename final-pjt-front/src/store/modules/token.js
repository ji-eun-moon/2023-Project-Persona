const token = {
    state: {
      token: null,
      loggedIn: false,
      username: ''
    },
    getters: {
    },
    mutations: {
      setToken(state, token) {
        state.token = token;
        // console.log('token:', state.token);
      },
      setLoggedIn(state, value) {
        state.loggedIn = value;
      },
      setUsername(state, username) {
        state.username = username;
      },
      removeLoggedIn(state) {
        state.token = '',
        state.loggedIn = false,
        state.username = ''
      }
    },
    actions: {
      saveToken({ commit }, token) {
        // 로그인 액션: 토큰을 받아와 스토어의 토큰 상태를 업데이트
        commit('setToken', token);
      },
      saveUsername({ commit }, username) {
        commit('setUsername', username);
      },
      removeLoggedIn({ commit }) {
        commit('removeLoggedIn');
      }
    }
}

export default token