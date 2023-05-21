<template>
  <div>
    <div class="video-container">
      <video autoplay muted loop class="main-video">
        <source src="../assets/main-video.mp4" type="video/mp4" />
      </video>
    </div>
    <div class="intro-text-container">
      <h1 class="m-4">회원 가입 유도글 적기</h1>
      <button class="btn sign-btn">가입하고 영화 추천받기</button>
      <div class="d-flex justify-content-center">
        <p @click="goHome" class="mt-3 me-3 cursor-pointer">비회원으로 이용하기</p>
        <p @click="loginShow=true" class="mt-3 cursor-pointer">이미 계정이 있으신가요?</p>
      </div>
    </div>

    <div class="modal-container" v-if="loginShow">
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
.video-container {
  width: 100%;
  height: 0;
  padding-bottom: 56.25%;
  position: relative;
  overflow: hidden;
}

.main-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.intro-text-container {
  font-family: 'Noto Sans KR', sans-serif;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(20%, -90%);
  text-align: center;
}

.sign-btn {
  background-color: brown;
  color: aliceblue;
}

.cursor-pointer{
  cursor: pointer;
}
</style>
