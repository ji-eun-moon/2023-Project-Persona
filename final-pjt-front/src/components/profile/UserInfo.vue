<template>
<div>
  <div class="profile-item mb-2">
    <div class="d-flex user-info align-items-between justify-content-center">
      <div class="d-flex justify-content-center">
        <div class="mb-5 me-5">
          <h2 class="profile-item-header mb-3">{{ isMyProfile ? "나의" : username + "'s" }} 부캐</h2>
          <div>
            <img :src="getActorImageURL(userInfo?.profile_img)" alt="userInfo.username" class="profile-image mb-5">
          </div>
          <div class="mb-5 fs-5 font-weight-bold">
            <p>{{ actorDetail?.name }}</p>
            <p>{{ actorDetail?.birthday}}</p>
            <p>{{ actorDetail?.place_of_birth}}</p>
          </div>
          <div>
            <button v-if="isMyProfile" @click="handleClickActor" class="btn btn-secondary random-btn">부캐 랜덤 추천 받기</button>
          </div>
        </div>
      </div>

      <div class="d-flex row info-item">
        <div v-if="userInfo && userInfo.character" class="character-info">
          <h2 class="profile-item-header">부캐 주요 작품</h2>
          
          <div class="character-movie">
            <div v-for="movie in limitedMovies" :key="movie.id" class="mb-3">
              <h5> {{ movie.title }} </h5>
            </div>
          </div>

        </div>
        <div v-else class="no-character1">
          <h5>아직 부캐가 설정되지 않은 사용자 입니다.</h5>
        </div>
  
        <div class="like-genres">
          <h2 class="profile-item-header mb-4">{{$route.params.username}}님이 좋아하는 장르</h2>
            <div v-if="userGenres.length > 0">
              <ul class="genre-list">
                <li v-for="genre in userGenres" :key="genre.id" class="genre-list-item mb-2">
                  <i class="bi bi-camera-reels-fill"></i> {{ genre.name }}
                </li>
              </ul>
            </div>
            <div v-else>
              선택한 장르가 아직 없습니다.
            </div>
        </div>
      </div>
    </div>

    <div class="pagination">
      <span class="spacer"></span>
      <button v-if="isMyProfile" @click="handleClickGenre" class="btn btn-secondary random-btn">좋아하는 장르 고르기</button>
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
    <h5 v-else class="no-character2">아직 부캐가 설정되지 않은 사용자 입니다.</h5>
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
      
      userGenres:[],

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
	},
  created() {
    this.getUserProfile(this.$route.params.username);
    this.fetchUserGenres()
  },
  methods: {
    getActorImageURL(imagePath) {
      if (imagePath) {
        return "https://image.tmdb.org/t/p/w185" + imagePath;
      } else {
        return require("@/assets/default-profile.jpg");
      }
    },
    async getUserProfile(username) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/v1/profile/${username}`);
        this.profileImg = response.data.profile_img
        this.userInfo = response.data
        if (this.userInfo.character){
          this.getActorDetail(this.userInfo.character)
          this.getMoviesByActor(this.userInfo.character)
        }
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
    handleClickActor(){
      this.$emit('select-actor');
    },
    handleClickGenre(){
      this.$emit('select-genre');
    },
    handleMovieSelected(movieId) {
      this.$emit('movie-selected', movieId);
    },

    // 선택한 장르 가져오기
    fetchUserGenres() {
      const username = this.$route.params.username; // 유저 이름 가져오기
      const token = this.$store.state.token.token; // 토큰 가져오기
      const config = {
        headers: {
          Authorization: `Token ${token}`, // 헤더에 토큰 추가
        },
      };
      axios
        .get(`http://127.0.0.1:8000/api/v1/genres/${username}/`, config)
        .then(response => {
          console.log(response.data)
          this.userGenres = response.data.genres;
        })
        .catch(error => {
          console.error('Failed to fetch user genres:', error);
        });
    }
  }
}
</script>

<style>
.profile-image {
  width: 180px;
  object-fit: cover;
  border-radius: 40%;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
}

.random-btn {
  background-color: #2c3e50;
  border-radius: 20px;
}

.no-character1{
  /* margin-left: 10px; */
  margin-bottom: 20px;
  /* text-align: left; */
}
.no-character2{
  margin-left: 20px;
  margin-bottom: 20px;
  /* text-align: left; */
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

.genre-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.genre-list-item {
  display: inline-block;
  margin-right: 10px;
  background-color: #2c3e50;
  color: white;
  padding: 6px 10px;
  border-radius: 4px;
  font-weight: 400px;
}

.user-info {
  font-size: 15px;
  font-weight: 400;
  margin-top: 30px;
}

.character-movie {
  margin-top : 40px;
  background-color: #2c3e50;
  color:aliceblue;
  padding: 10px;
  border-radius: 20px;
}

.character-info {
  display: flex;
  flex-direction: column;
}

.info-item{
  margin-left: 70px;
}
</style>