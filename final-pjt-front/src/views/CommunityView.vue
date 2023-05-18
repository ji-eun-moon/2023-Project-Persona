<template>
  <div>
    <h1>Community</h1>
    <TopArticles />
    <MovieReviews />
    <FreeTalks />
  </div>
</template>

<script>
import TopArticles from "@/components/community/TopArticles.vue"
import MovieReviews from "@/components/community/MovieReviews.vue"
import FreeTalks from "@/components/community/FreeTalks.vue"

export default {
    name: 'CommunityView',
    components: {
        TopArticles,
        MovieReviews,
        FreeTalks
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