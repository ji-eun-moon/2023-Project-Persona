<template>
  <div>
    <div class="trending-list-header">
      <h1 class="me-2 list-header">개봉 예정 영화</h1>
    </div>
    <div class="card-container">
      <ul class="card-list">
        <li v-for="movie in upcomingMovieList" :key="movie.id" class="card-item">
          <MovieCard :movie="movie"/>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import MovieCard from '@/components/commons/MovieCard.vue'

export default {
    name: "UpcomingList",
    components: {
      MovieCard
    },

    created() {
      this.getUpcomingMovies()
    },
    methods: {
      ...mapActions([
        'getUpcomingMovies'
      ])
    },
    computed: {
      ...mapState({
        upcomingMovieList: state => state.upcomingList.upcomingMovies
      })
    }
}
</script>

<style>

</style>