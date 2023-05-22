<template>
  <div class="profile-item">
    <div class="d-flex">
      <h2 class="profile-item-header ms-3">{{ isMyProfile ? "내가" : username + "'s" }} 담은 영화</h2>
      <button class="like-toggle-button btn btn-secondary ms-auto" @click="toggleMovieList">
        {{ showMovieList ? "접기" : "보기" }}
      </button>
    </div>
    <div class="movie-list justify-content-center" v-show="showMovieList">
      <MovieCard v-for="movie in likedMovies" :key="movie.id" :movie="movie" class="like-movie-card" @movie-selected="handleMovieSelected"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import MovieCard from '@/components/commons/MovieCard.vue';

export default {
  name : 'LikeMovies',
  props : {
    username : String
  },
  data() {
    return {
      likedMovies: [],
      showMovieList: false
    }
  },
  components: {
    MovieCard,
  },
  computed: {
    isMyProfile() {
      return this.username === this.$store.state.token.username;
    },
  },
  created() {
    this.getLikedMovies();
  },
  methods: {
    async getLikedMovies() {
      try {
        const response = await axios.get(`${API_URL}/api/v1/profile/${this.username}/`);  // 좋아요한 영화의 id 받아오고
        console.log(response.data)
        const movieIds = response.data.liked_movies.map(movie => movie.movie_id);
        await Promise.all(movieIds.map(async (movieId) => {
          const movie = await this.$store.dispatch("getMovieDetail", movieId);  // 그 영화의 상세정보 불러오기
          this.likedMovies.push(movie);
        }));
      } catch (error) {
        console.error("Failed to fetch liked movies:", error);
      }
    },
    handleMovieSelected(movieId) {
      this.$emit('movie-selected', movieId);
    },
    toggleMovieList() {
      this.showMovieList = !this.showMovieList;
    }
  }
  
}
</script>

<style>
.profile-item{
  background-color: hwb(0 88% 10% / 0.932);
  border-radius: 20px;
  padding: 20px;
}

.like-movie-card {
  flex-basis: 200px;
  margin: 10px;
}

.profile-item-header{
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 600;
}

.like-toggle-button{
  border-radius: 20px;
}
</style>