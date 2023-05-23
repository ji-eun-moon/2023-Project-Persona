<template>
  <div class="container">
    <h1>Community</h1>
    <TopArticles />
    <MovieReviews />
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
    computed: {
    },
    created() {
      this.getArticles()
    },
    methods: {
      getArticles() {
        this.$store.dispatch('getArticles')
      }
    }
}
</script>

<style>

</style>