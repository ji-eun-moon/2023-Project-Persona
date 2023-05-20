<template>
  <div>
    <h1 class="list-header mt-5">찾고 싶은 영화가 있으신가요?</h1>
    <div class="input-group search">
      <input type="text" v-model="searchQuery" @keydown.enter="searchMovies" class="form-control" placeholder="영화 제목을 입력하세요."/>
      <i @click="searchMovies" class="btn btn-light bi bi-search search-btn"></i>
    </div>

    <div v-if="movies.length > 0" class="container">
      <h3 class="list-header">'{{searchQueryDisplay}}' 검색 결과</h3>
      <div class="movie-list">
        <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" class="movie-card" @movie-selected="handleMovieSelected"/>
      </div>
    </div>

    <div v-else-if="hasSearched" class="container">
      <h5 class="list-header">'{{searchQueryDisplay}}' 검색 결과가 없습니다. 🥲</h5>
    </div>

    <div class="modal-container" v-if="showModal==true" >
      <div class="modal-content" :style="modalStyle">
        <MovieDetail :movieId="selectedMovieId" />
        <button class="close-button" @click="showModal=false"><i class="bi bi-x-circle-fill c-red"></i></button>
      </div>
    </div>
  </div> 
</template>

<script>
import { mapState, mapActions } from 'vuex'
import MovieCard from '@/components/commons/MovieCard.vue';
import MovieDetail from '@/components/movies/MovieDetail.vue'

export default {
  name: 'MovieView',
  data() {
    return {
      searchQuery: '',
      previousSearchQuery: '',
      showModal: false,
      selectedMovieId: null,
      hasSearched: false
    };
  },
  components: {
    MovieCard,
    MovieDetail
  },
  computed: {
    ...mapState({
      movies: state => state.searchmovies.searchResults
    }),
    searchQueryDisplay() {
      return this.previousSearchQuery
    },
    ...mapState({
      movieDetail: state => state.moviedetail.movieDetail,
    }),
    modalStyle() {
      if (this.movieDetail && this.movieDetail.backdrop_path) {
        return {
          backgroundImage: `url('https://image.tmdb.org/t/p/original${this.movieDetail.backdrop_path}')`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
        };
      } else {
        return {};
      }
  },
  },
  methods: {
    ...mapActions(['getMovies']),
    searchMovies() {
     if(this.searchQuery.trim() !== '') {
        this.getMovies(this.searchQuery);
        this.previousSearchQuery = this.searchQuery;
        this.hasSearched = true;
      } else {
        alert("검색어를 입력하세요.");
      }
      this.searchQuery = ''
    },
    handleMovieSelected(movieId) {
      this.selectedMovieId = movieId
      this.showModal = true
      this.$store.dispatch("getMovieDetail", movieId);
    },
    getBackdropImageUrl(backdropPath) {
      if (backdropPath) {
        return `url('https://image.tmdb.org/t/p/original${backdropPath}')`;
      } else {
        return "";
      }
    }
  },
}
</script>

<style>
.search {
  display:flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}

.input-group {
  width: 40%;
  margin: 0 auto;
}

.form-control {
  width: 40%;
  border-radius: 50px;
  text-align: center;
}

.search-btn {
  border-radius: 50px;
  background-color: white;
}

.movie-list {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  margin-top: 20px;
}

.movie-card {
  /* width: 200px;  */
  margin: 10px;
  width: calc(25% - 20px);
}
</style>
