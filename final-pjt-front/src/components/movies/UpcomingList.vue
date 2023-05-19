<template>
  <div>
    <div class="trending-list-header">
      <h1 class="me-2 list-header">개봉 예정 영화</h1>
    </div>
    <div id="upcomingCarousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div v-for="(group, index) in upcomingMovieGrouped" :key="index" :class="['carousel-item', { active: index === 0 }]">
          <ul class="card-list">
            <li v-for="movie in group" :key="movie.id" class="card-item">
              <MovieCard :movie="movie" @movie-selected="handleMovieSelected"/>
            </li>
          </ul>
        </div>
      </div>
      <div class="carousel-control-wrapper">
        <button class="carousel-control-prev" type="button" data-bs-target="#upcomingCarousel" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#upcomingCarousel" data-bs-slide="next">
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
  name: 'UpcomingList',
  components: {
    MovieCard,
  },
  created() {
    this.getUpcomingMovies();
  },
  methods: {
    ...mapActions(['getUpcomingMovies']),
      handleMovieSelected(movieId) {
      this.$emit('movie-selected', movieId);
    },
  },
  computed: {
    ...mapState({
      upcomingMovieList: state => state.upcomingList.upcomingMovies,
    }),
    upcomingMovieGrouped() {
      const groups = [];
      for (let i = 0; i < this.upcomingMovieList.length; i += 5) {
        groups.push(this.upcomingMovieList.slice(i, i + 5));
      }
      return groups;
    },
  },
};
</script>

<style>

</style>