<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <router-link class="navbar-brand" :to="{ name: 'home' }">logo</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'home' }">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'movies' }">Movies</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'community' }">Community</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'SignUpView' }">Sign Up</router-link>
            </li>
          </ul>
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'profile' }">Profile</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'LoginView' }">login</router-link>
            </li>
            <button @click="logout">logout</button>
          </ul>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  components: {
  },
  created() {
    const token = localStorage.getItem('token');
    if (token) {
      this.$store.commit('setToken', token);
    }
  },
  methods : {
    ...mapActions(['removeLoggedIn']),
    logout() {
      this.removeLoggedIn(); // Vuex에서 로그인 정보 제거
      localStorage.removeItem('token'); // 로컬 스토리지에서 토큰 제거
      console.log('false 이면 로그아웃 성공! :', this.$store.state.token.loggedIn)
    },
  }
}
</script>

<style>
body {
  background-color: #1c1d1f;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
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
  color: #42b983 !important;
}
</style>
