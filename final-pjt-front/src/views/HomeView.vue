<template>
  <div>
    <h1>Home</h1>
    <NowPlayingList />
    <TrendingList />
    <UpcomingList />
    <GenreList />
  </div>
</template>

<script>
import NowPlayingList from "@/components/movies/NowPlayingList.vue"
import TrendingList from "@/components/movies/TrendingList.vue"
import UpcomingList from "@/components/movies/UpcomingList.vue"
import GenreList from "@/components/movies/GenreList.vue"

export default {
  name: 'HomeView',
  components: {
    NowPlayingList,
    TrendingList,
    UpcomingList,
    GenreList,
  }
}
</script>
