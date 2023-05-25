<template>
  <div class="main-view">
    <!-- <h1 class="movie-title mb-5">Discover Movies as Your Favorite Characters</h1> -->
    <img :src="require('@/assets/persona.png')" class="mb-3" alt="">
    <LoginView v-if="!this.$store.state.token.loggedIn"/>
    <p @click="goHome" class="mt-3 me-3 cursor-pointer movie underline" v-if="!this.$store.state.token.loggedIn">비회원으로 이용하기</p>
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
