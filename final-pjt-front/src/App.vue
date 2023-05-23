<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <div class="container">

        <!-- <router-link class="navbar-brand" :to="{ name: 'home' }">logo</router-link> -->
          <i class="navbar-brand bi bi-camera-reels-fill"></i>
          <ul class="navbar-nav movie-title">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'home' }">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'movies' }">Movies</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'community' }" v-if="$store.state.token.loggedIn">Community</router-link>
              <a class="nav-link cursor-pointer" @click="openLoginModal" v-else>Community</a>
            </li>
          </ul>


          <ul class="navbar-nav ms-auto movie-title align-items-center">
            <div class="dropdown">
              <button class="btn btn-dark dropdown-toggle movie-title" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                MyPage
              </button>
              <div class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton1">
                <img :src="getProfileImageURL(userInfo)" alt="userInfo.username" class="my-profile-image mb-3">
                  <div class="d-flex align-items-center mypage-items">
                    <!-- <router-link class="nav-link c-yellow" :to="{ name: 'LoginView' }" v-if="!$store.state.token.loggedIn">login</router-link> -->
                    <div>
                      <button @click="loginShow=true" class="btn btn-outline-dark" v-if="!$store.state.token.loggedIn">LOGIN</button>
                    </div>
                    <div v-if="$store.state.token.loggedIn">
                      <h3 class="mb-3">Hello, {{this.$store.state.token.username}}</h3>
                    </div>
                    <div>
                      <router-link class="profile-link" :to="{ name: 'profile', params: { username: $store.state.token.username }}" v-if="$store.state.token.loggedIn">나의 프로필 보기</router-link>
                    </div>
                    <button @click="logout" v-if="$store.state.token.loggedIn" class="btn btn-outline-danger mt-3">LOGOUT</button>
                  </div>
              </div>
            </div>
          </ul>

        </div>
    </nav>


    <div class="modal-container" v-if="loginShow && !this.$store.state.token.loggedIn">
      <div class="login-modal-content">
        <div class="login-modal-header">
          <i class="bi bi-backspace-fill movie me-2 fs-5" @click="loginShow=false"></i>
          <p class="login-close-button mt-1" @click="loginShow=false">뒤로가기</p>
        </div>
        <div class="login-modal-body">
          <LoginView />
        </div>
      </div>
    </div>

    <router-view/>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import { eventBus } from './event-bus';
import LoginView from '@/views/LoginView.vue'

export default {
  name : 'App',
  components: {
    LoginView
  },
  created() {
    eventBus.$on('refresh-app', this.refresh)
    const token = localStorage.getItem('token');
    const username = localStorage.getItem('username');
    if (token) {
      // 로컬스토리지에 토큰이 존재한다면 - 스토어에 토큰, 로그인상태, username 저장
      this.$store.commit('setToken', token);
      this.$store.commit("setLoggedIn", true);
      this.$store.dispatch('saveUsername', username)
      this.$store.dispatch('fetchUserProfile', username)
      console.log('로그인 유지 확인:',this.$store.state.token.username, this.$store.state.token.loggedIn, this.$store.state.token.token)
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo.userProfile;
    },
	},
  data() {
    return {
      loginShow: false,
    }
  },
  methods : {
    ...mapActions(['removeLoggedIn']),
    logout() {
      this.removeLoggedIn(); // Vuex에서 로그인 정보 제거
      localStorage.removeItem('token'); // 로컬 스토리지에서 토큰 제거
      localStorage.removeItem('username'); // 로컬 스토리지에서 username 제거
      this.loginShow = false
      this.$router.push({name:'main'})
      this.refresh();
      console.log('로그아웃 확인:', this.$store.state.token.loggedIn, this.$store.state.token.username, this.$store.state.token.token)
    },
    getProfileImageURL(userInfo) {
      if (userInfo && userInfo.profile_img ) {
        return "https://image.tmdb.org/t/p/w185" + userInfo.profile_img;
      } else {
        return require("@/assets/default-profile.jpg");
      }
    },
    refresh() {
      window.location.reload();
    },
    openLoginModal() {
      alert('로그인이 필요한 서비스입니다.')
      this.loginShow = true;
    },
  },

}
</script>

<style>
body {
  background-color: #1c1d1f;
}
#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #1c1d1f;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: aliceblue !important;
}

.dropdown-menu {
  padding: 30px;
  border-radius: 20px;
}

.my-profile-image {
  width: 180px;
  object-fit: cover;
  border-radius: 40%;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
}

.mypage-items {
  flex-direction: column;
}
</style>
