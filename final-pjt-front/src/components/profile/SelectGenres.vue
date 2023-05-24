<template>
  <div class="profile-item">
    <h2 class="genre-title mb-4">좋아하는 장르를 선택하세요!</h2>
    <div class="genre-container mb-3">
      <label v-for="genre in genres" :key="genre.id" class="genre-item fs-5 cursor-pointer">
        <input type="checkbox" :value="genre" v-model="selectedGenres">
        <span class="checkmark"></span>
        {{ genre.name }}
      </label>
    </div>
    <button @click="saveGenres" class="btn btn-dark me-1">저장하기</button>
    <button @click="uncheckCheckboxes" class="btn btn-outline-dark">초기화</button>
  </div>
</template>

<script>
import axios from 'axios'
import { eventBus } from '@/event-bus';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'SelectGenres',
  data() {
    return {
      genres: [{ id: 28, name: "액션" }, { id: 12, name: "모험" }, { id: 16, name: "애니메이션" }, 
              { id: 35, name: "코미디" }, { id: 80, name: "범죄" }, { id: 99, name: "다큐멘터리" }, 
              { id: 18, name: "드라마" }, { id: 10751, name: "가족" }, { id: 14, name: "판타지" }, 
              { id: 36, name: "역사" }, { id: 27, name: "공포" }, { id: 10402, name: "음악" }, 
              { id: 9648, name: "미스터리" }, { id: 10749, name: "로맨스" }, { id: 878, name: "SF" }, 
              { id: 10770, name: "TV" }, { id: 53, name: "스릴러" }, { id: 10752, name: "전쟁" }, 
              { id: 37, name: "서부" }],
      selectedGenres: [],
    };
  },
  computed: {
    groupedGenres() {
      // genres 배열을 4개씩 나누어서 그룹화
      const groups = [];
      for (let i = 0; i < this.genres.length; i += 4) {
        groups.push(this.genres.slice(i, i + 4));
      }
      return groups;
    },
  },
  methods: {
    async saveGenres() {
      try {
        if (this.selectedGenres.length < 3) {
          alert('장르를 3개 이상 선택해야 합니다.');
          return;
        }
        const token = this.$store.state.token.token; // 토큰 가져오기
        const config = {
          headers: {
            Authorization: `Token ${token}`, // 헤더에 토큰 추가
          },
        };
        const username = this.$store.state.token.username;
        const genre_ids = this.selectedGenres.map(genre => genre.id); // 선택한 장르의 ID들을 추출하여 배열로 만듦
        await axios.post(`${API_URL}/api/v1/genres/${username}/`, { genre_ids }, config);
        eventBus.$emit('refresh-app');
      } catch (error) {
        console.error('Failed to save genres:', error);
      }
    },
    uncheckCheckboxes() {
      const checkboxes = document.querySelectorAll('.genre-item input[type="checkbox"]');
      checkboxes.forEach((checkbox) => {
        checkbox.checked = false;
      });
    },
  }
}
</script>

<style>
.genre-container {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start; /* 위쪽 정렬 */
  justify-content: flex-start; /* 왼쪽 정렬 */
}

.genre-item {
  flex-basis: 25%;
  margin-bottom: 10px;
  font-weight: 500;
}

.genre-item input[type="checkbox"] {
  display: none;
}

/* 체크박스 커스텀 스타일 */
.genre-item .checkmark {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid #ccc;
  border-radius: 50%;
  margin-right: 8px;
  position: relative;
  top: 4px;
}

/* 체크박스 체크 시 스타일 변경 */
.genre-item input[type="checkbox"]:checked + .checkmark {
  background-color: #2196F3;
  border-color: #2196F3;
}

/* 체크박스 체크 아이콘 */
.genre-item .checkmark::after {
  content: "";
  display: block;
  width: 6px;
  height: 12px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
  position: absolute;
  top: 2px;
  left: 5px;
}

.genre-title {
  font-weight: 700;
}
</style>