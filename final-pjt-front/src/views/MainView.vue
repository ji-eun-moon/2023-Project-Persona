<template>
  <div class="main-view">
    <!-- <h1 class="movie-title mb-5">Where Movies Come to Life</h1> -->
    <img :src="require('@/assets/persona.png')" class="mb-3" alt="">
    <LoginView v-if="!this.$store.state.token.loggedIn"/>
    <p @click="goHome" class="mt-3 me-3 cursor-pointer movie underline" v-if="!this.$store.state.token.loggedIn">비회원으로 이용하기</p>
  </div>
</template>

<script>
import LoginView from '@/views/LoginView.vue'

export default {
  name :'MainView',
  components: {
    LoginView
  },
  data() {
    return {
      loginShow: false
    };
  },
  methods: {
    goHome() {
      this.$router.push({name: 'home'});
    }
  }
}
</script>

<style>

.cursor-pointer{
  cursor: pointer;
}

.underline {
   text-decoration: underline;
}
.main-view {
  margin: 100px;
}
</style>
