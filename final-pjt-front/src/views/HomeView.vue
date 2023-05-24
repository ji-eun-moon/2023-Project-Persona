<template>
  <div>
    <div class="container">
      <TrendingList class="my-5" @movie-selected="handleMovieSelected"/>
      <NowPlayingList class="my-5" @movie-selected="handleMovieSelected"/>
      <UpcomingList class="my-5" @movie-selected="handleMovieSelected"/>
      <!-- <GenreList @movie-selected="handleMovieSelected" v-if="!showGenres"/>
      <LikeGenreList @movie-selected="handleMovieSelected" v-if="showGenres"/> -->
      <component :is="listComponent" @movie-selected="handleMovieSelected" />
    </div>

   <div class="modal-container" v-if="showModal==true" >
      <div class="modal-content" :style="modalStyle">
        <div class="modal-body">
          <MovieDetail :movieId="selectedMovieId" />
        </div>
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
import LikeGenreList from '@/components/movies/LikeGenreList.vue'
import { mapState } from 'vuex'
import axios from 'axios'

export default {
  
  name: 'HomeView',
  components: {
    NowPlayingList,
    TrendingList,
    UpcomingList,
    GenreList,
    MovieDetail,
    LikeGenreList
  },
  data() {
    return {
      showModal: false,
      selectedMovieId: null,
      genresExist: false,
      genresLoaded: false,
    }
  },
  computed: {
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
    listComponent() {
      return this.genresExist ? 'LikeGenreList' : 'GenreList';
    },

    
  },
  created() {
    if (this.$store.state.token.loggedIn) {
      this.fetchUserGenres();
    } else {
      this.genresLoaded = true;
    }
  },
  methods: {
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
    },
    fetchUserGenres() {
      const username = this.$store.state.token.username;
      const token = this.$store.state.token.token;
      const config = {
        headers: {
          Authorization: `Token ${token}`,
        },
      };
      axios
        .get(`http://127.0.0.1:8000/api/v1/genres/${username}/`, config)
        .then(response => {
          this.genresExist = response.data.genres.length > 0;
        })
        .catch(error => {
          console.error('Failed to fetch user genres:', error);
        })
        .finally(() => {
          this.genresLoaded = true;
        });
    },
  },
}
</script>

<style>
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
  padding: 20px;
}

.modal-content {
  background-color: hsl(210, 7%, 11%);
  padding: 20px;
  text-align: center;
  border-radius: 10px;
  width: 90%;
  overflow-y: auto;
}

.modal-body {
  max-height: 80vh; /* 모달 내용의 최대 높이 설정 */
}


.close-button {
  position: absolute;
  top: 25px;
  right: 30px;
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