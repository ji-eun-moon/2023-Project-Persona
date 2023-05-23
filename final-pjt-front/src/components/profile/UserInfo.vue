<template>
<div class="profile-item">
	<h2 class="profile-item-header fs-1">INFO</h2>

  <div class="d-flex">
    <div class="d-flex">
      <div class="ms-3 mb-5 me-5">
        <img :src="getActorImageURL(profileImg)" alt="userInfo.username" class="profile-image mb-3">
        <p>{{ userInfo.username }}</p>
        <div class="follow-btn">
          <button v-if="!isMyProfile">팔로우</button>
          <button v-if="!isMyProfile">언팔로우</button>
        </div>
        <button v-if="isMyProfile" @click="handleClick" class="btn btn-secondary ms-4">부캐 랜덤 추천 받기</button>
        
      </div>
    </div>
  
    <div>
      <h3>{{ actor.name }}</h3>
    </div>
  </div>

</div>
</template>

<script>

export default {
	name : 'UserInfo',
	props :{
		username : String
	},
  components: {
  },
	computed: {
		isMyProfile() {
      return this.$route.params.username === this.$store.state.token.username;
    },
    userInfo() {
      return this.$store.state.userInfo.userProfile;
    },
    profileImg() {
      return this.$store.state.userInfo.profileImg;
    },
    actor() {
      return this.$store.state.userInfo.actor;
    }
	},
  created() {
    this.getUserInfo();
  },
  methods: {
    getActorImageURL(imagePath) {
      if (imagePath) {
        return "https://image.tmdb.org/t/p/w185" + imagePath;
      } else {
        return require("@/assets/default-profile.jpg");
      }
    },
    getUserInfo() {
      this.$store.dispatch('fetchUserProfile', this.username)
        .then(() => {
          const user = this.$store.state.userInfo.userProfile;
          if (user && user.character) {
            this.$store.dispatch('fetchActorDetail', user.character);
          }
        })
        .catch(error => {
          console.error('유저 정보를 가져오는 중 오류 발생:', error);
        });
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