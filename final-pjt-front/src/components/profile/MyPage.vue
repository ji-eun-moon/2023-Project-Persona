<template>
  <div>
    <h1 class="mypage-title">MyPage</h1>
    <img class="profile-img" src="@/assets/default-profile.jpg" alt="">
    <br>
    <button class="mt-3 btn btn-secondary">로그인 하세요</button>
  </div>
</template>

<script>
export default {
  name: 'MyPage'
}
</script>

<style>
.mypage-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
}
.profile-img {
  border-radius: 50%;
  width: 100px;
  margin: 20px;
}
</style>