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
        <a href="#"><p class="mt-3 me-3">비회원으로 이용하기</p></a>
        <a href="#"><p class="mt-3">이미 계정이 있으신가요?</p></a>
      </div>
    </div>
  </div>
</template>

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
</style>
