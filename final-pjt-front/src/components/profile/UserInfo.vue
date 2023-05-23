<template>
<div class="profile-item">
	<h2 class="profile-item-header fs-1">INFO</h2>

  <div class="d-flex">
    <div class="d-flex">
      <div class="ms-3 mb-5 me-5">
        <img :src="getActorImageURL(userInfo?.profile_img)" alt="userInfo.username" class="profile-image mb-3">
        <p>{{ userInfo?.username }}</p>

        <button v-if="isMyProfile" @click="handleClick" class="btn btn-secondary ms-4">부캐 랜덤 추천 받기</button>
        
      </div>
    </div>
  
    <div v-if="userInfo && userInfo.character">
        <h3>{{ actorDetail?.name }}</h3>
    </div>
    <div v-else>
      <h5>아직 부캐가 설정되지 않은 사용자 입니다.</h5>
    </div>

  </div>

</div>
</template>

<script>
import axios from 'axios';
const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd'

export default {
	name : 'UserInfo',
	props :{
		username : String
	},
  components: {
  },
  data() {
    return {
      profileImg: null,
      userInfo: null,
      actorDetail: null,
    }
  },
	computed: {
		isMyProfile() {
      return this.$route.params.username === this.$store.state.token.username;
    },
    // userInfo() {
    //   return this.$store.state.userInfo.userProfile;
    // },
    // profileImg() {
    //   return this.$store.state.userInfo.profileImg;
    // },
    // actor() {
    //   return this.$store.state.userInfo.actor;
    // }
	},
  created() {
    // this.getUserInfo();
    this.getUserProfile(this.$route.params.username);
  },
  methods: {
    getActorImageURL(imagePath) {
      if (imagePath) {
        return "https://image.tmdb.org/t/p/w185" + imagePath;
      } else {
        return require("@/assets/default-profile.jpg");
      }
    },
    // getUserInfo() {
    //   this.$store.dispatch('fetchUserProfile', this.username)
    //     .then(() => {
    //       const user = this.$store.state.userInfo.userProfile;
    //       if (user && user.character) {
    //         this.$store.dispatch('fetchActorDetail', user.character);
    //       }
    //     })
    //     .catch(error => {
    //       console.error('유저 정보를 가져오는 중 오류 발생:', error);
    //     });
    // },
    async getUserProfile(username) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/v1/profile/${username}`);
        this.profileImg = response.data.profile_img
        this.userInfo = response.data
        if (this.userInfo.character){
          this.getActorDetail(this.userInfo.character)
        }
        // commit('setProfileImg', response.data.profile_img)
      } catch (error) {
        console.error('유저 정보를 가져오는 중 오류 발생:', error);
      }
    },
    async getActorDetail(actorId) {
      try {
        const response = await axios.get(`https://api.themoviedb.org/3/person/${actorId}?api_key=${API_KEY}`);
        this.actorDetail = response.data;
      } catch (error) {
        console.error('배우 세부 정보를 가져오는 중 오류 발생:', error);
      }
    },
    handleClick(){
      this.$emit('select-actor');
    }
  }
}
</script>

<style>
.profile-image {
  margin-left: 30px;
  width: 180px;
  object-fit: cover;
  border-radius: 40%;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
}
</style>