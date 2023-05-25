<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <div class="container">

        <!-- <router-link class="navbar-brand" :to="{ name: 'home' }">logo</router-link> -->
        <a :href="homeLink">
          <img :src="require('@/assets/eye-mask.png')" class="logo-img cursor-pointer" alt="">
          <img :src="require('@/assets/persona.png')" class="logo me-2 cursor-pointer" alt="">
        </a>
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
              <div class="dropdown-menu dropdown-menu-end justify-content-center" aria-labelledby="dropdownMenuButton1">
                <div class="d-flex align-items-center mypage-items">
                    <div>
                      <img :src="getProfileImageURL(userInfo)" alt="userInfo.username" class="my-profile-image mb-3">
                    </div>
                    <!-- <router-link class="nav-link c-yellow" :to="{ name: 'LoginView' }" v-if="!$store.state.token.loggedIn">login</router-link> -->
                    <div>
                      <button @click="loginShow=true" class="btn btn-outline-dark" v-if="!$store.state.token.loggedIn">LOGIN</button>
                    </div>
                    <div v-if="$store.state.token.loggedIn">
                      <h3 class="mb-3 hello">Hello, {{this.$store.state.token.username}}</h3>
                    </div>

                      <h5 class="mt-2" v-if="this.$store.state.token.loggedIn">선호 장르</h5>
                      <div v-if="userGenres.length > 0 && $store.state.token.loggedIn" class="d-flex ms-5">
                        <ul class="genre-list">
                          <li v-for="genre in userGenres" :key="genre.id" class="genre-list-item mb-2">
                            <i class="bi bi-camera-reels-fill"></i> {{ genre.name }}
                          </li>
                        </ul>
                      </div>
                      <div v-else-if="this.$store.state.token.loggedIn">
                        <p>선택한 장르가 없습니다.</p>
                      </div>

                    <div class="mt-2" v-if="this.$store.state.token.loggedIn">
                      <a class="profile-link cursor-pointer" :href="profileLink">나의 프로필 보기</a>
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

    <div class="fs-3 text-center footer">
      <div class="d-flex justify-content-center align-items-center" style="height: 100px">
        <div class="">
          <div><a href="https://github.com/mjieun0956/2023-Project-Persona"><i class="bi bi-github" style="color:aliceblue;"></i></a></div>
          <div style="font-size: 10px;">MADE BY</div>
          <div class="d-flex">
            <div style="font-size: 15px; margin-right: 10px;">Jieun Moon</div>
            <div style="font-size: 15px; margin-left: 10px;">Jisoo Choi</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script> 
import { mapActions } from 'vuex';
import { eventBus } from './event-bus';
import LoginView from '@/views/LoginView.vue'
import axios from 'axios'

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
      this.fetchUserGenres();
      console.log('로그인 유지 확인:',this.$store.state.token.username, this.$store.state.token.loggedIn, this.$store.state.token.token)
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo.userProfile;
    },
    profileLink() {
      const username = this.$store.state.token.username;
      return `http://localhost:8080/profile/${username}/`;
    },
	},
  data() {
    return {
      loginShow: false,
      userGenres:[],
      homeLink: "http://localhost:8080/home/"
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
    fetchUserGenres() {
      const username = this.$store.state.token.username; // 유저 이름 가져오기
      const token = this.$store.state.token.token; // 토큰 가져오기
      const config = {
        headers: {
          Authorization: `Token ${token}`, // 헤더에 토큰 추가
        },
      };
      axios
        .get(`http://127.0.0.1:8000/api/v1/genres/${username}/`, config)
        .then(response => {
          console.log(response.data)
          this.userGenres = response.data.genres;
        })
        .catch(error => {
          console.error('Failed to fetch user genres:', error);
        });
    },
  },

}
</script>

<style>
.footer {
  background-color: #24292f;
  font-family: 'Noto Sans KR',  sans-serif;
  font-weight: 300;
  color: aliceblue;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 9999;
}

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
  /* min-height: 100%; */
  position: relative;
  padding-bottom: 170px;
  min-height: 100vh;
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
  width: 400px;
}

.my-profile-image {
  width: 180px;
  object-fit: cover;
  border-radius: 40%;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
  background-color: aliceblue;
}

.mypage-items {
  flex-direction: column;
}

.logo-img{
 width: 50px;
}
.logo {
  width: 100px;
}

.hello {
  font-weight: 600;
}
</style>
