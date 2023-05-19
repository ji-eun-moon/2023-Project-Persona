<template>
  <div>
    <h1 class="movie-title">{{ movieDetail.title }}</h1>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: "MovieDetail",
  props:{
    movieId : Number
  },
  computed: {
    ...mapState({
      movieDetail: state => state.moviedetail.movieDetail,
    }),
  },
  created() {
    // const movieId = this.$route.params.movieId
    // this.$store.dispatch("getMovieDetail", movieId);
    this.$store.dispatch("getMovieDetail", this.movieId);
  },
};
</script>

<style>
.movie-title {
  color: aliceblue;
}
</style>