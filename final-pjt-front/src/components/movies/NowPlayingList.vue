<template>
  <div>
    <div class="trending-list-header">
      <h1 class="me-2 list-header">현재 상영중인 영화</h1>
    </div>
    <div class="card-container">
      <ul class="card-list">
        <li v-for="movie in nowPlayingMovieList" :key="movie.id" class="card-item">
          <MovieCard :movie="movie" />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import MovieCard from '@/components/commons/MovieCard.vue'

export default {
    name: 'NowPlayingList',
    components: {
      MovieCard,
    },

    created() {
      this.getNowPlayingMovies()
    },
    methods: {
      ...mapActions([
        'getNowPlayingMovies'
      ])
    },
    computed: {
      ...mapState({
        nowPlayingMovieList: state => state.nowPlayingList.nowplayingMovies
      })
    }

}
</script>

<style>

</style>