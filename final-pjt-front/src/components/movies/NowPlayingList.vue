<template>
  <div>
    <div class="trending-list-header">
      <h1 class="me-2 list-header">현재 상영중인 영화</h1>
    </div>
    <div id="nowPlayingCarousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div v-for="(group, index) in nowPlayingMovieGrouped" :key="index" :class="['carousel-item', { active: index === 0 }]" >
          <ul class="card-list">
            <li v-for="movie in group" :key="movie.id" class="card-item">
              <MovieCard :movie="movie" @movie-selected="handleMovieSelected"/>
            </li>
          </ul>
        </div>
      </div>
      <div class="carousel-control-wrapper">
        <button class="carousel-control-prev" type="button" data-bs-target="#nowPlayingCarousel" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#nowPlayingCarousel" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import MovieCard from '@/components/commons/MovieCard.vue';

export default {
  name: 'NowPlayingList',
  components: {
    MovieCard,
  },
  created() {
    this.getNowPlayingMovies();
  },
  methods: {
    ...mapActions(['getNowPlayingMovies']),
    handleMovieSelected(movieId) {
      this.$emit('movie-selected', movieId);
    },
  },
  computed: {
    ...mapState({
      nowPlayingMovieList: state => state.nowPlayingList.nowplayingMovies,
    }),
    nowPlayingMovieGrouped() {
      const groups = [];
      for (let i = 0; i < this.nowPlayingMovieList.length; i += 5) {
        groups.push(this.nowPlayingMovieList.slice(i, i + 5));
      }
      return groups;
    },
  },
};
</script>

<style>
.carousel-control-wrapper {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  display: flex;
  margin-top: -15px;
  justify-content: space-between;
}

.carousel-control-prev,
.carousel-control-next {
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 50%;
  width: 30px; /* 버튼 너비 */
  height: 30px; /* 버튼 높이 */
  display: flex;
  color: #fff;
  font-size: 20px;
  border: none;
  outline: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}


.carousel-control-prev:hover,
.carousel-control-next:hover {
  background-color: rgba(0, 0, 0, 0.7);
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  width: 15px; /* 아이콘 크기 */
  height: 15px; /* 아이콘 크기 */
}
</style>