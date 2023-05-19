<template>
  <div>
    <div class="trending-list-header">
      <h1 class="me-1 list-header">이런 장르는 어때요?</h1>
    </div>

    <div v-for="(genre, index) in selectedGenres" :key="index">
      <h2 class="me-2 list-header my-3">{{ genre.name }} 영화</h2>
      <div :id="'genreCarousel-' + index" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div v-for="(group, groupIndex) in GenreMoviesGroup[index]" :key="groupIndex" :class="['carousel-item', { active: groupIndex === 0 }]">
            <ul class="card-list">
              <li v-for="movie in group" :key="movie.id" class="card-item">
                <MovieCard :movie="movie" @movie-selected="handleMovieSelected"/>
              </li>
            </ul>
          </div>
        </div>
        <div class="carousel-control-wrapper">
          <button class="carousel-control-prev" type="button" :data-bs-target="'#genreCarousel-' + index" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" :data-bs-target="'#genreCarousel-' + index" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/commons/MovieCard.vue';

export default {
  name: 'GenreList',
  components: {
    MovieCard,
  },
  data() {
    return {
      genres: [{ id: 28, name: "액션" }, { id: 12, name: "모험" }, { id: 16, name: "애니메이션" }, 
              { id: 35, name: "코미디" }, { id: 80, name: "범죄" }, { id: 99, name: "다큐멘터리" }, 
              { id: 18, name: "드라마" }, { id: 10751, name: "가족" }, { id: 14, name: "판타지" }, 
              { id: 36, name: "역사" }, { id: 27, name: "공포" }, { id: 10402, name: "음악" }, 
              { id: 9648, name: "미스터리" }, { id: 10749, name: "로맨스" }, { id: 878, name: "SF" }, 
              { id: 10770, name: "TV" }, { id: 53, name: "스릴러" }, { id: 10752, name: "전쟁" }, 
              { id: 37, name: "서부" }],
      selectedGenres: [],
      genreMovies: {},
    };
  },
  created() {
    this.getRandomGenres();
  },
  methods: {
    getRandomGenres() {
      const totalGenres = this.genres.length;
      const randomIndexes = [];
      while (randomIndexes.length < 3) {
        const randomIndex = Math.floor(Math.random() * totalGenres);
        if (!randomIndexes.includes(randomIndex)) {
          randomIndexes.push(randomIndex);
        }
      }
      this.selectedGenres = randomIndexes.map(index => this.genres[index]);
      this.getMoviesByGenres();
    },
    getMoviesByGenres() {
      const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd';

      this.selectedGenres.forEach(genre => {
        const url = `https://api.themoviedb.org/3/discover/movie?api_key=${API_KEY}&language=ko&with_genres=${genre.id}&sort_by=popularity.desc`;
        axios.get(url)
          .then(response => {
            console.log(response.data)
            this.$set(this.genreMovies, genre.id, response.data.results);
          })
          .catch(error => {
            console.error(`Error fetching movies for genre ${genre.name}:`, error);
            this.$set(this.genreMovies, genre.id, []);
          });
      });
    },
    handleMovieSelected(movieId) {
      this.$emit('movie-selected', movieId);
    },
  },

computed: {
  GenreMoviesGroup() {
    const groups = [];
    for (let i = 0; i < this.selectedGenres.length; i++) {
      const genre = this.selectedGenres[i];
      const movies = this.genreMovies[genre.id];
      if (movies) {
        const genreGroup = [];
        for (let j = 0; j < movies.length; j += 5) {
          const group = movies.slice(j, j + 5);
          genreGroup.push(group);
        }
        groups.push(genreGroup);
      }
    }
    return groups;
  }
}


};
</script>
