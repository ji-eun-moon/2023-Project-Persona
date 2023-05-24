<template>
  <div>
      <div class="video-container" v-if="currentTrailerUrl !== ''">
        <iframe :src="currentTrailerUrl" width="100%" height="100%" frameborder="0" allowfullscreen autoplay></iframe>
      </div>
    
    <div class="trending-list">
      <div class="trending-list-header">
        <h1 class="me-2 list-header">What's Trending</h1>
        <div class="button-container">
          <button :class="['btn', 'btn-outline-secondary', { active: showDaily }]" @click="showDailyTrendingMovies" class="me-2">일별</button>
          <button :class="['btn', 'btn-outline-secondary', { active: showWeekly }]" @click="showWeeklyTrendingMovies">주별</button>
        </div>
      </div>
      <div class="card-container" v-if="showDaily">
        <div id="dailyCarousel" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div v-for="(group, index) in dailyTrendingMoviesGrouped" :key="index" :class="['carousel-item', { active: index === 0 }]">
              <ul class="card-list">
                <li v-for="movie in group" :key="movie.id" class="card-item">
                  <MovieCard :movie="movie" @movie-selected="handleMovieSelected" @movie-play="PlayVideo"/>
                </li>
              </ul>
            </div>
          </div>
          <div class="carousel-control-wrapper">
            <button class="carousel-control-prev" type="button" data-bs-target="#dailyCarousel" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#dailyCarousel" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </div>
      </div>
      <div class="card-container" v-if="showWeekly">
        <div id="weeklyCarousel" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div v-for="(group, index) in weeklyTrendingMoviesGrouped" :key="index" :class="['carousel-item', { active: index === 0 }]">
              <ul class="card-list">
                <li v-for="movie in group" :key="movie.id" class="card-item">
                  <MovieCard :movie="movie" @movie-selected="handleMovieSelected" @movie-play="PlayVideo"/>
                </li>
              </ul>
            </div>
          </div>
          <div class="carousel-control-wrapper">
            <button class="carousel-control-prev" type="button" data-bs-target="#weeklyCarousel" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#weeklyCarousel" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </div>
      </div>

    </div>
    </div>

</template>

<script>
import { mapState, mapActions } from 'vuex';
import MovieCard from '@/components/commons/MovieCard.vue';
import axios from 'axios';

export default {
  name: "TrendingList",
  components: {
    MovieCard,
  },
  data() {
    return {
      showDaily: true,
      showWeekly: false,
      currentTrailerUrl: '',
      randomTrailerUrl: '',
    };
  },
  created() {
    this.getDailyTrendingMovies();
    this.getWeeklyTrendingMovies();
  },
  methods: {
    ...mapActions([
      'getDailyTrendingMovies',
      'getWeeklyTrendingMovies'
    ]),
    showDailyTrendingMovies() {
      this.showDaily = true;
      this.showWeekly = false;
    },
    showWeeklyTrendingMovies() {
      this.showDaily = false;
      this.showWeekly = true;
    },
    async PlayVideo(movieId) {
      // 영화 예고편을 가져오는 메서드 호출
      await this.fetchTrailerVideo(movieId);
    },
    handleMovieSelected(movieId) {
      this.$emit('movie-selected', movieId);
    },
    async fetchTrailerVideo(movieId) {
      const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd'
      try {
        const response = await axios.get(`https://api.themoviedb.org/3/movie/${movieId}/videos?api_key=${API_KEY}`);
        const videos = response.data.results;
        const trailer = videos.find(video => video.type === 'Trailer' && video.site === 'YouTube');
        if (trailer) {
          this.currentTrailerUrl = `https://www.youtube.com/embed/?autoplay=1&mute=1&controls=0&playlist=${trailer.key}&loop=1`;
        } else {
          console.log('예고편 동영상이 없습니다.');
        }
      } catch (error) {
        console.error('Failed to fetch trailer video:', error);
      }
    },
    playRandomMovieTrailer() {
      if (this.dailyTrendingMovies.length > 0) {
        const randomIndex = Math.floor(Math.random() * this.dailyTrendingMovies.length);
        const randomMovie = this.dailyTrendingMovies[randomIndex];
        this.fetchTrailerVideo(randomMovie.id);
      }
    },
    setRandomTrailerUrl() {
      if (this.dailyTrendingMovies.length > 0) {
        const randomIndex = Math.floor(Math.random() * this.dailyTrendingMovies.length);
        const randomMovie = this.dailyTrendingMovies[randomIndex];
        this.randomTrailerUrl = `https://www.youtube.com/embed/?autoplay=1&mute=1&controls=0&playlist=${randomMovie.videoKey}&loop=1`;
      }
    },
  },
  computed: {
    ...mapState({
      dailyTrendingMovies: state => state.trendingList.dailyTrendingMovies,
      weeklyTrendingMovies: state => state.trendingList.weeklyTrendingMovies
    }),
    dailyTrendingMoviesGrouped() {
      const groups = [];
      for (let i = 0; i < this.dailyTrendingMovies.length; i += 5) {
        groups.push(this.dailyTrendingMovies.slice(i, i + 5));
      }
      return groups;
    },
    weeklyTrendingMoviesGrouped() {
      const groups = [];
      for (let i = 0; i < this.weeklyTrendingMovies.length; i += 5) {
        groups.push(this.weeklyTrendingMovies.slice(i, i + 5));
      }
      return groups;
    },
  },
};
</script>

<style>
.list-header {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
  color: aliceblue;
  margin-bottom: 20px;
}

.trending-list-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.button-container {
  display: flex;
}


.card-list {
  display: flex;
  padding: 0;
  margin: 0;
  list-style: none;
}

.card-item {
  flex: 0 0 calc(20% - 3px);
  margin-right: 3px;
}

.card-item:last-child {
  margin-right: 0;
}

.card-item .card {
  width: 100%;
}

.card-item .card img {
  max-width: 100%;
  height: auto;
}

.btn.active {
  background-color: #6c757d;
}

.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 비율에 맞게 조정 */
  height: 0;
  overflow: hidden;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

</style>
