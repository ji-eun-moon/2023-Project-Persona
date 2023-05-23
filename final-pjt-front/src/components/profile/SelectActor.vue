<template>
  <div class="select-actor">
    <div class="d-flex cast-images justify-content-center">
      <div v-for="actor in randomActors" :key="actor.id" class="me-5">
        <img :src="getActorImageURL(actor.profile_path)" :alt="actor.name" class="cast-image cursor-pointer" 
              @click="saveProfileImage(actor)"/>
        <p class="movie">{{ actor.name }}</p>
      </div>
    </div>
      <button @click="getRandomActors" class="btn btn-secondary">다시 불러오기</button>
  </div>
</template>


<script>
import axios from 'axios'
const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd';

export default {
  name: 'SelectActor',
  data() {
    return {
      randomActors: [],
      actorImages: {}
    }
  },
  created() {
    this.getRandomActors()
  },
  methods: {
    async getRandomActors() {
      try {
        const timeWindow = 'day'; // 시간 범위 ('day', 'week')

        const response = await axios.get(`https://api.themoviedb.org/3/trending/person/${timeWindow}`, {
          params: {
            api_key: API_KEY,
            language: 'ko'
          }
        });
        const actors = response.data.results; // 모든 배우 정보 가져오기
        const filteredActors = actors.filter(actor => actor.known_for_department === 'Acting'); // 배우인지 확인하기
        const shuffledActors = filteredActors.sort(() => 0.5 - Math.random()); // 결과를 랜덤하게 섞기
        this.randomActors = shuffledActors.slice(0, 5)
        // console.log(this.randomActors)
      } catch (error) {
        console.error('유명한 배우 정보를 가져오는 중 오류 발생:', error);
        throw error;
      }
    },
    getActorImageURL(imagePath) {
      if (imagePath) {
        return "https://image.tmdb.org/t/p/w185" + imagePath;
      } else {
        return require("@/assets/default-profile.jpg"); // 기본 이미지
      }
    },
    async saveProfileImage(actor) {
      try {
        const token = this.$store.state.token.token
        const response = await axios.put(`http://127.0.0.1:8000/api/v1/upload_image/${this.$route.params.username}/`, 
        { profile_img: actor.profile_path,
          character:  actor.id },
        {
          headers: {
          Authorization: `Token ${token}`} // 헤더에 토큰 추가
        });

        // console.log(response.data); // 서버 응답 확인

        // 상태 정보에 저장된 프로필 사진 업데이트 - 바로 이미지 바꾸기 위해서!
        this.$store.dispatch('saveUserProfileImg', response.data.profile_img)

        // 부캐 정보를 상태 정보에 저장
        this.$store.dispatch('saveActor', actor);
        alert(`나의 부캐가 '${actor.name}'으로 저장되었습니다!`)
        console.log(this.$store.state.userInfo.actor)
      } catch (error) {
        console.error('이미지 업로드 중 오류 발생:', error);
      }
    }
  }
}
</script>

<style>
</style>