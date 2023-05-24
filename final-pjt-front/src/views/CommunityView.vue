<template>
  <div class="container">
    <div class="button-group mt-5">
      <button @click="showTopArticles" :class="{ 'active': displayTopArticles }" class="button">👑TopArticles</button>
      <button @click="showMovieReviews" :class="{ 'active': displayMovieReviews }" class="button">MovieReviews</button>
    </div>

    <div v-if="displayTopArticles" class="content">
      <TopArticles />
    </div>
    <div v-if="displayMovieReviews" class="content">
      <MovieReviews />
    </div>
  </div>
</template>

<script>
import TopArticles from "@/components/community/TopArticles.vue"
import MovieReviews from "@/components/community/MovieReviews.vue"
import { eventBus } from '@/event-bus'

export default {
    name: 'CommunityView',
    components: {
        TopArticles,
        MovieReviews,
    },
    data() {
      return {
        displayTopArticles: true,
        displayMovieReviews: false,
      }
    },
    computed: {
    },
    created() {
      this.getArticles()
      eventBus.$on('articleCreated', this.handleArticleCreated)
    },
    // destroyed() {
    //   eventBus.$off('articleCreated', this.handleArticleCreated)
    // },
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
      },
      handleArticleCreated() {
        this.displayTopArticles = false
        this.displayMovieReviews = true
      }
    }
}
</script>

<style>
  .container {
    text-align: center;
  }
  .button-group {
    margin-top: 5rem;
    margin-bottom: 20px;
    display: flex;
    justify-content: center;
  }
  .button {
    padding: 10px 20px;
    background-color: darkgray;
    color: aliceblue;
    border: none;
    font-size: 16px;
    cursor: pointer;
    width: 30%;
  }
  .button.active {
    background-color:cornflowerblue;
  }
  .content {
    margin-top: 30px;
  }

</style>