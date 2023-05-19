import MovieView from '../views/MovieView.vue'
import MovieDetail from '../components/movies/MovieDetail'

export default [
  {
    path: '/movies',
    name: 'movies',
    component: MovieView
  },
  {
    path: '/movies/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
]
