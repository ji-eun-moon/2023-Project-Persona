<template>
  <div>
    <h1>Profile</h1>
    <LikeMovies />
  </div>
</template>

<script>
import LikeMovies from "@/components/profile/LikeMovies"

export default {
    name: "ProfileView",
    components: {
        LikeMovies
    }
}
</script>

<style>

</style>