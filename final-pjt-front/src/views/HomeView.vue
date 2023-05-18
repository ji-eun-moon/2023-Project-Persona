<template>
  <div>
    <div class="container">
      <TrendingList class="my-5"/>
      <NowPlayingList class="my-5"/>
      <UpcomingList class="my-5"/>
      <GenreList />
    </div>
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
