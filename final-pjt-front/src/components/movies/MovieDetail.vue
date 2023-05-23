<template>
  <div>
  <div class="movie-container">
    <div class="movie-poster">
      <div class="poster-wrapper">
        <img :src="getMoviePosterUrl(movieDetail.poster_path)" alt="Movie Poster" class="poster-image" />
      </div>
        <div class="d-flex justify-content-center ms-3 mt-4">
          <p style="color:white;" class="me-3 movie mt-1">보고 싶은 영화 담기</p>
          <a class="btn-like" @click="toggleLike(movieId)" :disabled="!isLoggedIn">
          <i class="bi fs-3" :class="isLiked ? 'bi-heart-fill' : 'bi-heart'"></i>
          </a>
        </div>
        <div class="d-flex justify-content-center">
          <p v-if="this.$store.state.token.loggedIn" style="color:white;" class="movie mt-2">이 영화를 담은 사람 : {{likeCount}} 명</p>
        </div>
    </div>
    <div class="movie-info">
      <h1 class="movie-title">{{ movieDetail.title }}</h1>
      <h5 class="movie">{{ movieDetail.original_title }}</h5>
      <div class="movie-content my-3">
        <span class="movie">
          개봉 {{movieDetail.release_date}} | 러닝타임 {{movieDetail.runtime}}분 |
        </span>
        <div class="genres">
          <span class="genre movie" v-for="genre in movieDetail.genres" :key="genre.id"> {{ genre.name }} | </span>
        </div>
        <span class="movie">평점 {{ movieDetail.vote_average }}</span>
      </div>
      <h4 class="movie">{{ movieDetail.tagline }}</h4>
      <h6 class="movie movie-overview">{{ movieDetail.overview }}</h6>
      <h3 class="movie-title mt-5 mb-2">출연진</h3>
      <p class="movie" v-if="isLoggedIn"> 맘에 드는 배우가 있으면 부캐로 골라보세요! </p>
      <p class="movie" v-else>로그인 하고 부캐를 골라보세요!</p>
      <div class="cast-images d-flex justify-content-center">
        <div v-for="(cast, index) in movieCast" :key="index" class="cast-profile">
          <img :src="getProfileImageUrl(cast.profile_path)" :alt="cast.name" class="cast-image cursor-pointer" @click="saveProfileImage(cast)" />
          <span class="cast-name movie-title">{{ cast.name }}</span>
        </div>
      </div>
    </div>
    </div>

    <div class="movie-review-container mt-3 mb-3">
      <div class="movie-review-form">
        <div class="d-flex">
          <h4 class="movie-title mt-5 me-2 my-3">사용자 평점</h4>
          <h4 class="movie-title mt-5 average-rating">{{ average_rating }}</h4>
        </div>
        <star-rating :increment="0.5" :star-size="30" @rating-selected ="setRating" class="movie"
          :border-width="4" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"></star-rating>
        </div>
        <form @submit.prevent="createReview" class="d-flex">
          <textarea id="content" v-model="content" class="expand-textarea" :placeholder="isLoggedIn ? '한줄평 입력' : '한줄평을 남기려면 로그인하세요.'" @click="checkLogin"></textarea>
          <button type="submit" class="btn btn-light btn-sm btn-review" :disabled="!isLoggedIn">한줄평 남기기</button>
        </form>
      <div class="review-list-container mt-5">
        <div v-for="review in reviewList" :key="review.id" class="review-item text-start">
          <p class="review-content movie me-2">
            <span v-for="(i, index) in Math.floor(review.rate)" :key="'fill-' + index" class="bi bi-star-fill c-yellow fs-5"></span>
            <span v-if="review.rate - Math.floor(review.rate) > 0" class="bi bi-star-half c-yellow fs-5"></span>
            <span v-for="(i, index) in 5 - Math.ceil(review.rate)" :key="'empty-' + index" class="bi bi-star c-yellow fs-5"></span>
          </p>
            <p class="review-content movie fs-5">{{ review.content }}</p>
            <div class="review-meta d-flex me-3 mt-3">
              <div class="d-flex me-3">
                <p class="review-username review-content movie me-3">{{ review.username }}</p>
                <p class="movie">{{ formatDateTime(review.created_at) }}</p>
              </div>
              <div class="d-flex justify-content-end" v-if="review.username === username">
                <button class="btn btn-danger btn-sm mb-3 review-del" @click="deleteReview(review.id)" >삭제</button>
              </div>
            </div>
        </div>
      </div>
    </div>

      <div class="modal-container" v-if="showModal && !isLoggedIn">
      <div class="login-modal-content">
        <div class="login-modal-header">
          <i class="bi bi-backspace-fill movie me-2 fs-5" @click="showModal=false"></i>
          <p class="login-close-button mt-1" @click="showModal=false">뒤로가기</p>
        </div>
        <div class="login-modal-body">
          <LoginView />
        </div>
      </div>
    </div>

    
  </div>
</template>

<script>
import { mapState } from 'vuex';
import LoginView from '@/views/LoginView.vue'
import StarRating from 'vue-star-rating'
import moment from 'moment';
import { eventBus } from '@/event-bus';

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "MovieDetail",
  components: {
    LoginView,
    StarRating
  },
  props: {
    movieId: Number,
  },
  data() {
    return {
      isLiked: false,
      likeCount: 0,
      showModal: false,
      rating: 0,
      content: null,
      reviewList: [],
    };
  },
  computed: {
    ...mapState({
      movieDetail: state => state.moviedetail.movieDetail,
      movieCast: state => state.moviedetail.movieCast,
      isLoggedIn: state => state.token.loggedIn
    }),
    posterExists() {
      return this.movieDetail.poster_path !== null;
    },
    average_rating() {
      if (this.reviewList.length > 0) {
        const sum = this.reviewList.reduce((total, review) => {
          if (!isNaN(parseFloat(review.rate))) {
            return total + parseFloat(review.rate);
          } else {
            return total;
          }
        }, 0);
    
      const average = sum / this.reviewList.length;
      return average.toFixed(1);
    } else {
      return 0;
    }
  },
  username() {
    return this.$store.state.token.username
  }
  },
  created() {
    this.$store.dispatch("getMovieDetail", this.movieId);
    this.$store.dispatch("getMovieCast", this.movieId);
    this.saveMovie(this.movieId).then(() => {
    this.checkLikeStatus(this.movieId);
    }).catch(error => {
      console.error('Failed to save movie:', error);
    });
    this.getReviewList()
  },
  methods: {
    setRating: function(rating) {
      this.rating = rating;
    },
    getMoviePosterUrl(posterPath) {
      if (this.posterExists) {
        return "https://image.tmdb.org/t/p/original" + posterPath;
      } else {
        return require("@/assets/default-poster.png");
      }
    },
    getProfileImageUrl(profilePath) {
      if (profilePath) {
        return "https://image.tmdb.org/t/p/w185" + profilePath;
      } else {
        return require("@/assets/default-profile.jpg");
      }
    },
  async toggleLike(movieId) {
      if (!this.isLoggedIn) {
        alert('로그인이 필요한 서비스입니다.');
        this.showModal = true;
        return;
      }
      const previousLiked = this.isLiked;
      this.isLiked = !previousLiked;
      try {
        await this.handleLike(movieId);
        
        this.checkLikeStatus(movieId);
      } catch (error) {
        console.error('Failed to toggle like:', error);
        this.isLiked = previousLiked;
      }
    },

    async checkLikeStatus(movieId) {
      try {
        const token = this.$store.state.token.token; // 토큰 가져오기
        const config = {
          headers: {
            Authorization: `Token ${token}`, // 헤더에 토큰 추가
          },
        };
        const response = await axios.get(`${API_URL}/api/v1/movies/${movieId}/like/`, config);
        this.isLiked = response.data.isLiked; // 좋아요 여부 업데이트
        this.likeCount = response.data.likeCount; // 좋아요 수 업데이트
      } catch (error) {
        console.error('Failed to check like status:', error);
      }
    },
    async handleLike(movieId) {
      try {
        await this.saveMovie(movieId);
        await this.movieLike(movieId);
      } catch (error) {
        console.error('Failed to toggle like:', error);
      }
    },

    async saveMovie(movieId) {
      try {
        const token = this.$store.state.token.token; // 토큰 가져오기
        const config = {
          headers: {
            Authorization: `Token ${token}`, // 헤더에 토큰 추가
          },
        };
        await axios.post(`${API_URL}/api/v1/movies/${movieId}/`, null, config);
      } catch (error) {
        console.error('Failed to save movie:', error);
      }
    },

    async movieLike(movieId) {
      try {
        const token = this.$store.state.token.token; // 토큰 가져오기
        const config = {
          headers: {
            Authorization: `Token ${token}`, // 헤더에 토큰 추가
          },
        };
        await axios.post(`${API_URL}/api/v1/movies/${movieId}/like/`, null, config);
      } catch (error) {
        console.error('Failed to like movie:', error);
      }
    },

    async createReview() {
      try {
        const token = this.$store.state.token.token; // 토큰 가져오기
        const config = {
          headers: {
            Authorization: `Token ${token}`, // 헤더에 토큰 추가
          },
        };
        const data = {
          rate: this.rating,
          content: this.content,
        };
        await axios.post(`${API_URL}/api/v1/movies/${this.movieId}/reviews/`, data, config);
        // 한줄평 작성 후 리뷰 목록을 다시 가져오기
        await this.getReviewList();
      } catch (error) {
        console.error('Failed to create review:', error);
      }
      this.content = null
      this.rating = 0
    },

    async deleteReview(reviewId) {
      try {
        const token = this.$store.state.token.token; // 토큰 가져오기
        const config = {
          headers: {
            Authorization: `Token ${token}`, // 헤더에 토큰 추가
          },
        };
        await axios.delete(`${API_URL}/api/v1/${this.movieId}/reviews/${reviewId}/`, config);
        // 한줄평 삭제 후 리뷰 목록을 다시 가져오기
        await this.getReviewList();
      } catch (error) {
        console.error('Failed to delete review:', error);
      }
    },

    async getReviewList() {
      try {
        const response = await axios.get(`${API_URL}/api/v1/movies/${this.movieId}/reviews/`);
        this.reviewList = response.data; // 서버에서 받아온 리뷰 목록을 저장
        console.log(this.reviewList)
      } catch (error) {
        console.error('Failed to get review list:', error);
      }
    },

    formatDateTime(dateTime) {
      return moment(dateTime).format('YYYY-MM-DD HH:mm:ss');
    },

    checkLogin(){
      if (this.isLoggedIn === false) {
        alert('로그인이 필요한 서비스입니다.')
        this.showModal = true
      } 
    },
    async saveProfileImage(actor) {
      if (!this.isLoggedIn) {
        alert('로그인이 필요한 서비스입니다.');
        this.showModal = true;
        return;
      }
      try {
        const token = this.$store.state.token.token
        const username = this.$store.state.token.username
        const response = await axios.put(`http://127.0.0.1:8000/api/v1/upload_image/${username}/`, 
        { profile_img: actor.profile_path,
          character:  actor.id },
        {
          headers: {
          Authorization: `Token ${token}`} // 헤더에 토큰 추가
        });

        console.log(response.data); // 서버 응답 확인

        // 상태 정보에 저장된 프로필 사진 업데이트 - 바로 이미지 바꾸기 위해서!
        this.$store.dispatch('saveUserProfileImg', response.data.profile_img)
        // 부캐 정보를 상태 정보에 저장
        this.$store.dispatch('saveActor', actor);
        eventBus.$emit('refresh-app');
        alert(`나의 부캐가 '${actor.name}'으로 저장되었습니다!`)
      } catch (error) {
        console.error('이미지 업로드 중 오류 발생:', error);
      }
    }
  },
};
</script>

<style>
.movie-container {
  display: flex;
  background: rgba(0, 0, 0, 0.7);
  border-radius: 10px;
  flex-direction: row;
}

.movie-review-container{
  background: rgba(0, 0, 0, 0.7);
  border-radius: 10px;
  padding-left: 20px;
  padding-right: 20px;
  margin-bottom: 20px;
  padding-bottom: 20px;
}

.movie-poster {
  flex: 0 0 300px; /* 원하는 고정 너비 설정 */
  margin: 20px;
  display: flex;
  flex-direction: column;
}

.poster-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden; /* 이미지를 넘어갈 경우 자르기 */
}

.poster-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover; /* 이미지 비율 유지하면서 채우기 */
  border-radius: 10px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
}

.movie-title {
  color: aliceblue;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
}

.movie {
  font-family: 'Noto Sans KR', sans-serif;
  color: aliceblue;
  font-weight: 400;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
}

.movie-info {
  margin: 20px;
  overflow: hidden;
  flex: 1;
}

.genres {
  display: inline;
}

.cast-profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-right: 20px;
}

.cast-image {
  width: 100px;
  height: 160px;
  object-fit: cover;
  border-radius: 40%;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
}

.cast-name {
  color: aliceblue;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  margin-top: 10px;
}

.btn-like {
  color: crimson;
  cursor: pointer;
}

.login-modal-content {
  position: relative;
  background-color: hsl(210, 7%, 11%);
  padding: 20px;
  text-align: center;
  border-radius: 10px;
  width: 400px;
}

.login-modal-header {
  display: flex;
  justify-content: flex-start;
}

.login-close-button {
  cursor: pointer;
  color:aliceblue;
}

.login-modal-body {
  max-height: 450px; 
  overflow-y: auto;
  margin-bottom: 30px;
}

.movie-review {
  background-color: 0px 5px 10px rgba(0, 0, 0, 0.869);
  border-radius: 10px;
  padding: 5px, 10px, 10px, 10px;

}

.average-rating {
  color: orange;
}

.expand-textarea {
  flex: 1;
  resize: none;
  height: auto;
  min-height: 50px;
  padding: 5px;
  padding-left:10px;
  margin-right: 10px;
  border-radius :10px;
  margin-top: 10px;
}

.btn-review {
  height: 60px;
  padding: 0 10px;
  margin-top: 10px;
  border-radius: 10px;
}

.review-username {
  font-weight: 700;
  color: antiquewhite
}

.review-item{
  background-color: rgba(195, 195, 195, 0.3);
  border-radius: 10px;
  margin : 4px;
  padding: 10px;
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.review-content {
  margin-bottom: 5px; /* 원하는 간격으로 조정 */
}

.review-meta {
  display: flex;
  margin-left: auto;
  text-align: right;
}

.review-del {
  border-radius: 15px;
}
</style>