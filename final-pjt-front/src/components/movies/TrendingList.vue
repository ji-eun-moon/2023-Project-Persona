<template>
  <div>
    <div class="trending-list-header">
      <h1 class="me-2 list-header">What's Trending</h1>
      <!-- <h2 class="me-2" v-if="showDaily">What's Daily Trending Movies</h2>
      <h2 class="me-2" v-if="showWeekly">What's This Week Trending Movies</h2> -->
      <div class="button-container">
        <button :class="['btn', 'btn-outline-secondary', { active: showDaily }]" @click="showDailyTrendingMovies">일별</button>
        <button :class="['btn', 'btn-outline-secondary', { active: showWeekly }]" @click="showWeeklyTrendingMovies">주별</button>
      </div>
    </div>
    <div class="card-container" v-if="showDaily">
      <ul class="card-list">
        <li v-for="movie in dailyTrendingMovies" :key="movie.id" class="card-item">
          <MovieCard :movie="movie" />
        </li>
      </ul>
    </div>
    <div class="card-container" v-if="showWeekly">
      <ul class="card-list">
        <li v-for="movie in weeklyTrendingMovies" :key="movie.id" class="card-item">
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
    }
  },
  computed: {
    ...mapState({
      dailyTrendingMovies: state => state.trendingList.dailyTrendingMovies,
      weeklyTrendingMovies: state => state.trendingList.weeklyTrendingMovies
    })
  }
};
</script>

<style>
.list-header {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
  color: aliceblue;
}

.trending-list-header {
  display: flex;
  align-items: center;
}

.button-container {
  display: flex;
}

.button-container button {
  margin-right: 8px;
}

.card-container {
  overflow-x: scroll;
}

.card-list {
  display: flex;
  padding: 0;
  margin: 0;
  list-style: none;
}

.card-item {
  flex: 0 0 calc(20% - 16px);
  margin-right: 16px;
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
