<template>
  <div>
    <h5>TrendingList</h5>
    <button @click="showDailyTrendingMovies">일별</button>
    <button @click="showWeeklyTrendingMovies">주별</button>
    <h2 v-if="showDaily">Daily Trending Movies</h2>
    <div class="card-container" v-if="showDaily">
      <VueSlickCarousel :autoplay="true" :autoplaySpeed="3000">
        <ul class="card-list">
          <li v-for="movie in dailyTrendingMovies" :key="movie.id" class="card-item">
            <MovieCard :movie="movie" />
          </li>
        </ul>
      </VueSlickCarousel>
    </div>
    <h2 v-if="showWeekly">Weekly Trending Movies</h2>
    <div class="card-container" v-if="showWeekly">
      <VueSlickCarousel :autoplay="true" :autoplaySpeed="3000">
        <ul class="card-list">
          <li v-for="movie in weeklyTrendingMovies" :key="movie.id" class="card-item">
            <MovieCard :movie="movie" />
          </li>
        </ul>
      </VueSlickCarousel>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import MovieCard from '@/components/commons/MovieCard.vue';
import VueSlickCarousel from 'vue-slick-carousel';
import 'vue-slick-carousel/dist/vue-slick-carousel.css';

export default {
  name: "TrendingList",
  components: {
    MovieCard,
    VueSlickCarousel
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

/* 추가한 스타일 */
.card-item .card {
  width: 100%;
}

.card-item .card img {
  max-width: 100%;
  height: auto;
}
</style>
