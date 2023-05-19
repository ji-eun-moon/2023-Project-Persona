<template>
  <div>
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
                <MovieCard :movie="movie" @movie-selected="handleMovieSelected"/>
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
                <MovieCard :movie="movie" @movie-selected="handleMovieSelected"/>
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
</template>

<script>
import { mapState, mapActions } from 'vuex';
import MovieCard from '@/components/commons/MovieCard.vue';

export default {
  name: "TrendingList",
  components: {
    MovieCard,
  },
  data() {
    return {
      showDaily: true,
      showWeekly: false
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
    handleMovieSelected(movieId) {
      this.$emit('movie-selected', movieId);
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
</style>
