<template>
  <div class="container">
    <h1>Community</h1>
    <button @click="showTopArticles">TopArticles</button>
    <button @click="showMovieReviews">MovieReviews</button>
    <div v-if="displayTopArticles">
      <TopArticles />
    </div>
    <div v-if="displayMovieReviews">
      <MovieReviews />
    </div>
  </div>
</template>

<script>
import TopArticles from "@/components/community/TopArticles.vue"
import MovieReviews from "@/components/community/MovieReviews.vue"

export default {
    name: 'CommunityView',
    components: {
        TopArticles,
        MovieReviews,
    },
    data() {
      return {
        displayTopArticles: false,
        displayMovieReviews: false,
      }
    },
    computed: {
    },
    created() {
      this.getArticles()
    },
    methods: {
      getArticles() {
        this.$store.dispatch('getArticles')
      },
      showTopArticles() {
        this.displayTopArticles = true 
        this.displayMovieReviews = false
      },
      showMovieReviews() {
        this.displayTopArticles = false
        this.displayMovieReviews = true
      }
    }
}
</script>

<style>

</style>