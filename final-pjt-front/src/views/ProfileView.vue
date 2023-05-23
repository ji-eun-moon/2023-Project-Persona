<template>
  <div class="container">
    <h1 class="movie-title m-4">{{ isMyProfile ? "나의 프로필" : $route.params.username + "'s 프로필" }}</h1>
    <UserInfo :username="$route.params.username" class="mb-4" @select-actor="handleActorSelect" @movie-selected="handleMovieSelected"/>
    <LikeMovies :username="$route.params.username" @movie-selected="handleMovieSelected"/>

    <div class="modal-container" v-if="showModal==true" >
      <div class="modal-content" :style="modalStyle">
        <div class="modal-body">
          <MovieDetail :movieId="selectedMovieId" />
        </div>
        <button class="close-button" @click="showModal=false"><i class="bi bi-x-circle-fill c-red"></i></button>
      </div>
    </div>

    <div class="modal-container" v-if="SelectActorModal==true" >
      <div class="modal-content">
        <div class="modal-body">
          <SelectActor/>
        </div>
        <button class="close-button" @click="SelectActorModal=false"><i class="bi bi-x-circle-fill c-red"></i></button>
      </div>
    </div>

  </div>
</template>

<script>
import { mapState } from 'vuex'
import LikeMovies from "@/components/profile/LikeMovies"
import UserInfo from "@/components/profile/UserInfo"
import MovieDetail from '@/components/movies/MovieDetail.vue'
import SelectActor from '@/components/profile/SelectActor'

export default {
    name: "ProfileView",
    components: {
        LikeMovies,
        MovieDetail,
        UserInfo,
        SelectActor
    },
    data() {
      return {
        showModal: false,
        selectedMovieId: null,
        SelectActorModal: false,
      }
   },
  computed: {
    ...mapState({
      movieDetail: state => state.moviedetail.movieDetail,
    }),
    isMyProfile() {
      return this.$route.params.username === this.$store.state.token.username;
    },
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
    handleMovieSelected(movieId) {
      this.selectedMovieId = movieId
      this.showModal = true
      this.$store.dispatch("getMovieDetail", movieId);
    },
    handleActorSelect() {
      this.SelectActorModal = true
    }
  }
}
</script>

<style>

</style>