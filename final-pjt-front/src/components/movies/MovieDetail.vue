<template>
  <div class="movie-container">
    <div class="movie-poster">
      <div class="poster-wrapper">
        <img :src="getMoviePosterUrl(movieDetail.poster_path)" alt="Movie Poster" class="poster-image" />
      </div>
    </div>
    <div class="movie-info">
      <h1 class="movie-title">{{ movieDetail.title }}</h1>
      <h5 class="movie">{{ movieDetail.original_title }}</h5>
      <div class="movie-content my-3">
        <span class="movie">
          개봉 {{movieDetail.release_date}} | 러닝타임 {{movieDetail.runtime}}분 |
        </span>
        <div class="genres">
          <span class="genre movie" v-for="genre in movieDetail.genres" :key="genre.id"> {{ genre.name }} | </span>
        </div>
        <span class="movie">평점 {{ movieDetail.vote_average }}</span>
      </div>
      <h4 class="movie">{{ movieDetail.tagline }}</h4>
      <h6 class="movie movie-overview">{{ movieDetail.overview }}</h6>
      <h3 class="movie-title mt-5 mb-4">출연진</h3>
      <div class="cast-images d-flex justify-content-center">
        <div v-for="(cast, index) in movieCast" :key="index" class="cast-profile">
          <img :src="getProfileImageUrl(cast.profile_path)" :alt="cast.name" class="cast-image" />
          <span class="cast-name movie-title">{{ cast.name }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: "MovieDetail",
  props: {
    movieId: Number
  },
  computed: {
    ...mapState({
      movieDetail: state => state.moviedetail.movieDetail,
      movieCast: state => state.moviedetail.movieCast
    }),
    posterExists() {
      return this.movieDetail.poster_path !== null;
    },
  },
  created() {
    this.$store.dispatch("getMovieDetail", this.movieId);
    this.$store.dispatch("getMovieCast", this.movieId);
  },
  methods: {
    getMoviePosterUrl(posterPath) {
      if (this.posterExists) {
        return "https://image.tmdb.org/t/p/original" + posterPath;
      } else {
        return require("@/assets/default-poster.png");
      }
    },
    getProfileImageUrl(profilePath) {
      if (profilePath) {
        return "https://image.tmdb.org/t/p/w185" + profilePath;
      } else {
        return require("@/assets/default-profile.jpg");
      }
    },
  }
};
</script>

<style>
.movie-container {
  display: flex;
  background: rgba(0, 0, 0, 0.7);
  border-radius: 10px;
}

.movie-poster {
  flex: 0 0 300px; /* 원하는 고정 너비 설정 */
  margin: 40px;
}

.poster-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden; /* 이미지를 넘어갈 경우 자르기 */
}

.poster-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover; /* 이미지 비율 유지하면서 채우기 */
  border-radius: 10px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
}

.movie-title {
  color: aliceblue;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 900;
}

.movie {
  font-family: 'Noto Sans KR', sans-serif;
  color: aliceblue;
  font-size: 100;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
}

.movie-info {
  margin: 20px;
  overflow: hidden
}

.genres {
  display: inline;
}

.cast-profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-right: 20px;
}

.cast-image {
  width: 100px;
  height: 160px;
  object-fit: cover;
  border-radius: 40%;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
}

.cast-name {
  color: aliceblue;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  margin-top: 10px;
}

</style>