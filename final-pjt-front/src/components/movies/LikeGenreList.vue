<template>
  <div>
    <div class="trending-list-header">
      <h1 class="me-1 list-header">{{username}}님을 위한 추천 영화</h1>
    </div>
      <div v-for="(genre, index) in selectedGenres" :key="index">
      <h2 class="me-2 list-header my-3">{{ genre.name }} 영화</h2>
      <div :id="'likeGenreCarousel-' + index" class="carousel slide" data-bs-ride="carousel">
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
          <button class="carousel-control-prev" type="button" :data-bs-target="'#likeGenreCarousel-' + index" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" :data-bs-target="'#likeGenreCarousel-' + index" data-bs-slide="next">
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
  name: 'LikeGenreList',
  components: {
    MovieCard,
  },
  data() {
    return {
      username: this.$store.state.token.username,
      genreMovies: {},
      selectedGenres: [],
      userGenres: [],
    }
  },
  created() {
    this.fetchUserGenres()
  },
  methods:{
    getRandomGenres() {
      const totalGenres = this.userGenres.length;
      const randomIndexes = [];
      while (randomIndexes.length < 3) {
        const randomIndex = Math.floor(Math.random() * totalGenres);
        if (!randomIndexes.includes(randomIndex)) {
          randomIndexes.push(randomIndex);
        }
      }
      this.selectedGenres = randomIndexes.map(index => this.userGenres[index]);
      // console.log(this.selectedGenres)
      this.getMoviesByGenres();
    },
    getMoviesByGenres() {
  const API_KEY = 'ec7cb21d2c86952874cdb3ff92cd1dfd';

  this.selectedGenres.forEach(genre => {
    const url = `https://api.themoviedb.org/3/discover/movie?api_key=${API_KEY}&language=ko&with_genres=${genre.genre_id}&sort_by=popularity.desc`;
    axios.get(url)
      .then(response => {
        // console.log(response.data)
        this.$set(this.genreMovies, genre.genre_id, response.data.results);
      })
      .catch(error => {
        console.error(`Error fetching movies for genre ${genre.name}:`, error);
        this.$set(this.genreMovies, genre.genre_id, []);
      });
  });
},
    fetchUserGenres() {
      const username = this.$store.state.token.username; // 유저 이름 가져오기
      const token = this.$store.state.token.token; // 토큰 가져오기
      const config = {
        headers: {
          Authorization: `Token ${token}`, // 헤더에 토큰 추가
        },
      };
      axios
        .get(`http://127.0.0.1:8000/api/v1/genres/${username}/`, config)
        .then(response => {
          this.userGenres = response.data.genres;
          // console.log(this.userGenres) // 성공
          this.getRandomGenres();
        })
        .catch(error => {
          console.error('Failed to fetch user genres:', error);
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
      const movies = this.genreMovies[genre.genre_id];
      if (movies) {
        const genreGroup = [];
        for (let j = 0; j < movies.length; j += 5) {
          const group = movies.slice(j, j + 5);
          genreGroup.push(group);
        }
        groups.push(genreGroup);
      } else {
        groups.push([]);
      }
    }
    return groups;
  }
}

}
</script>

<style>

</style>