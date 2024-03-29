<template>
  <div class="card h-100 shadow" @click="handleClick" @mouseover="handleMouseOver" @mouseleave="handleMouseLeave">
    <div class="image-wrapper">
      <img :src="getPosterPath()" :alt="movie.title" class="card-image">
      <div class="card-info" :class="{ 'hovered': hover }">
        <h5 class="card-title text-center" v-show="hover">{{ movie.title }}</h5>
        <div class="icon-text justify-content-end" v-show="hover">
          <i class="bi bi-star-fill c-yellow me-2"></i>
          <p class="vote-average c-yellow">{{ movie.vote_average }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  data() {
    return {
      hover: false,
    };
  },
  computed: {
    posterExists() {
      return this.movie.poster_path !== null;
    },
  },
  methods: {
    getPosterPath() {
      if (this.posterExists) {
        return "https://image.tmdb.org/t/p/original" + this.movie.poster_path;
      } else {
        // 기본 이미지 파일 경로
        return require("@/assets/default-poster.png");
      }
    },
    handleClick() {
      // 클릭된 카드의 movie id를 사용하여 디테일 페이지로 이동
      this.$emit("movie-selected", this.movie.id);
    },
    handleMouseOver() {
      this.hover = true;
      this.$emit("movie-play", this.movie.id);
    },
    handleMouseLeave() {
      this.hover = false;
    },
  },
};
</script>


<style>
.card {
  position: relative;
  cursor: pointer;
  z-index: 1;
  border: 1px solid black;
  transition: border-color 0.3s ease;
}

.card:hover {
  border-color: #FBBF24;
}

.image-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
}

.card-info {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  color: #fff;
  padding: 10px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.card-info.hovered {
  opacity: 1;
}

.card-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
  margin: 0;
  text-align: center;
}

.vote-average {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 600;
  margin: 0;
}

.icon-text {
  display: flex;
}

.c-yellow {
  color: #FBBF24;
}

.card-image {
  border-radius: 5px;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>