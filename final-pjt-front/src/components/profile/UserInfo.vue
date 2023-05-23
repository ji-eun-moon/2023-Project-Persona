<template>
<div>
  <div class="profile-item mb-2">
    <h2 class="profile-item-header fs-1">INFO</h2>

    <div class="d-flex user-info align-items-center">
      <div class="d-flex">
        <div class="ms-3 mb-5 me-5">
          <img :src="getActorImageURL(userInfo?.profile_img)" alt="userInfo.username" class="profile-image mb-3">
          <p>{{ actorDetail?.name }}</p>
          <p>{{ actorDetail?.birthday}}</p>
          <p>{{ actorDetail?.place_of_birth}}</p>
          <!-- <h5 class="user-info-item">{{ userInfo?.username }}</h5> -->
        </div>
      </div>
    
      <div v-if="userInfo && userInfo.character" class="character-info">
          <h3 class="profile-item-header">{{ userInfo?.username }}의 부캐 {{ actorDetail?.name }}</h3>
          <h4>주요 작품</h4>
        <ul>
          <li v-for="movie in limitedMovies" :key="movie.id">
            {{ movie.title }}
          </li>
        </ul>
        <p>여기에 뭘 적으면 좋을까?</p>
        <p>좋아요한 글?</p>
      </div>
      <div v-else class="no-character">
        <h5>아직 부캐가 설정되지 않은 사용자 입니다.</h5>
      </div>

      <div class="random-btn-container">
        <button v-if="isMyProfile" @click="handleClick" class="btn btn-secondary random-btn">부캐 랜덤 추천 받기</button>
      </div>
  </div>
  </div>

  <div class="profile-item">
    <h2 class="profile-item-header ms-3">{{ isMyProfile ? "나의" : username + "'s" }} 부캐가 나온 영화</h2>
    <div v-if="userInfo && userInfo.character">
      <div class="movie-list justify-content-center">
          <MovieCard v-for="movie in displayedMovies" :key="movie.id" :movie="movie" class="like-movie-card" @movie-selected="handleMovieSelected"/>
      </div>
      <div class="pagination">
        <a class="fs-2 cursor-pointer" @click="loadPreviousMovies" v-if="currentPage > 1">
          <i class="bi bi-arrow-left-circle-fill next-btn"></i>
        </a>
        <span class="spacer"></span>
        <a class="fs-2 cursor-pointer" @click="loadMoreMovies" v-if="currentPage < movieChunks.length">
          <i class="bi bi-arrow-right-circle-fill next-btn"></i>
        </a>
      </div>
    </div>
    <h5 v-else class="no-character">아직 부캐가 설정되지 않은 사용자 입니다.</h5>
  </div>

</div>
</template>

<script>
import _ from 'lodash';
import axios from 'axios';
import MovieCard from '@/components/commons/MovieCard.vue';
const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd'

export default {
	name : 'UserInfo',
	props :{
		username : String
	},
  components: {
    MovieCard,
  },
  data() {
    return {
      profileImg: null,
      userInfo: null,
      actorDetail: null,
      movies: [],

      movieChunks: [],
      displayedMovies: [],
      moviesPerPage: 4,
      currentPage: 0,
    }
  },  
	computed: {
		isMyProfile() {
      return this.$route.params.username === this.$store.state.token.username;
    },
    limitedMovies() {
      return this.movies.slice(0, 5);
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
          this.getMoviesByActor(this.userInfo.character)
        }
        // commit('setProfileImg', response.data.profile_img)
      } catch (error) {
        console.error('유저 정보를 가져오는 중 오류 발생:', error);
      }
    },
    async getActorDetail(actorId) {
      try {
        const response = await axios.get(`https://api.themoviedb.org/3/person/${actorId}?api_key=${API_KEY}&language=ko`);
        this.actorDetail = response.data;
        console.log(this.actorDetail)
      } catch (error) {
        console.error('배우 세부 정보를 가져오는 중 오류 발생:', error);
      }
    },
    getMoviesByActor(actorId) {

      axios.get('https://api.themoviedb.org/3/discover/movie', {
        params: {
          api_key: API_KEY,
          with_cast: actorId,
          language: 'ko-KR',
        },
      })
      .then(response => {
        this.movies = response.data.results;
        this.movieChunks = _.chunk(this.movies, this.moviesPerPage);
        this.loadMoreMovies();
        console.log(this.movies)
      })
      .catch(error => {
        console.error('영화 데이터 가져오기 실패:', error);
      });
    },
    loadMoreMovies() {
      if (this.currentPage < this.movieChunks.length) {
        this.currentPage++;
        this.displayedMovies = this.movieChunks[this.currentPage - 1];
      } else {
        this.currentPage = 1;
        this.displayedMovies = this.movieChunks[this.currentPage - 1];
      }
    },

    loadPreviousMovies() {
      if (this.currentPage > 1) {
        this.currentPage--;
        this.displayedMovies = this.movieChunks[this.currentPage - 1];
      } else {
        this.currentPage = this.movieChunks.length;
        this.displayedMovies = this.movieChunks[this.currentPage - 1];
      }
    },
    handleClick(){
      this.$emit('select-actor');
    },
    handleMovieSelected(movieId) {
      this.$emit('movie-selected', movieId);
    },
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

.random-btn {
  background-color: #2c3e50;
  border-radius: 20px;
}

.no-character{
  margin-left: 100px;
  margin-bottom: 20px
}

.user-info-item{
  font-weight: 600;
}

.random-btn-container {
  margin-left: auto;
  margin-top: auto;
}

.next-btn {
  color: #2c3e50;
}

.pagination {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-top: 10px;
}

.pagination .next-btn {
  margin-right: auto;
}

.spacer {
  flex-grow: 1;
}
</style>