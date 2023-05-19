<template>
  <div>
    <div class="container">
      <TrendingList class="my-5" @movie-selected="handleMovieSelected"/>
      <NowPlayingList class="my-5" @movie-selected="handleMovieSelected"/>
      <UpcomingList class="my-5" @movie-selected="handleMovieSelected"/>
      <GenreList @movie-selected="handleMovieSelected"/>
    </div>

  <div class="modal-container" v-if="showModal==true">
    <div class="modal-content">
      <MovieDetail :movieId="selectedMovieId" />
      <button class="close-button" @click="showModal=false"><i class="bi bi-x-circle-fill c-red"></i></button>
    </div>
  </div>
  </div>
</template>

<script>
import NowPlayingList from "@/components/movies/NowPlayingList.vue"
import TrendingList from "@/components/movies/TrendingList.vue"
import UpcomingList from "@/components/movies/UpcomingList.vue"
import GenreList from "@/components/movies/GenreList.vue"
import MovieDetail from '@/components/movies/MovieDetail.vue'

export default {
  name: 'HomeView',
  components: {
    NowPlayingList,
    TrendingList,
    UpcomingList,
    GenreList,
    MovieDetail
  },
  data() {
    return {
      showModal: false,
      selectedMovieId: null
    }
  },
  methods: {
    handleMovieSelected(movieId) {
      this.selectedMovieId = movieId
      this.showModal = true
    },
  },
}
</script>

<style scoped>
.modal-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
  
}

.modal-content {
  background-color: hsl(210, 7%, 11%);
  padding: 20px;
  max-width: 600px;
  text-align: center;
  border-radius: 10px;
}


.close-button {
  position: absolute;
  top: 10px;
  right: 20px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: none;
  font-size: 25px;
  cursor: pointer;
  background-color: transparent;
}

.c-red {
  color: #c51b1b;
}
</style>