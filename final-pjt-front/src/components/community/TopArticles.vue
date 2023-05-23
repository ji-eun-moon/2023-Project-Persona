<template>
  <div>
    <table class="table table-dark table-striped table-hover table-sm">
      <thead>
        <tr>
          <th>작성자</th>
          <th>제목</th>
          <th>작성일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in topArticles" :key="article.id" class="article-list-item">
          <td>{{ article.username }}</td>
          <td><router-link :to="{ name:'DetailView', params:{ id:article.id } }" class="title-link">{{ article.title }}</router-link></td>
          <td>{{ formatDateTime(article.created_at) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: "TopArticles",
    data() {
      return {
        topArticles: [],
      }
    },
    created() {
      this.fetchTopArticles()
    },
    methods: {
      async fetchTopArticles() {
        try {
          const response = await axios.get(`${API_URL}/api/v1/articles/top/`)
          this.topArticles = response.data
        } catch (error) {
          console.log('Failed to fetch popular articles:', error)
        }
      },
      formatDateTime(dateTime) {
      return moment(dateTime).format('YYYY-MM-DD')
      }
    }
  }
</script>

<style>
  .article-list-item {
    border-bottom: 1px solid #ccc;
  }
  .article-list-item td {
    padding: 10px;
  }
  .article-list-item td:first-child {
    width: 20%;
  }
  .article-list-item td:nth-child(2) {
    width: 60%;
  }
  .article-list-item td:last-child {
    width: 10px;
  }
  .title-link {
    text-decoration-line: none;
    color: aliceblue;
  }
  /* table {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
  } */
  /* th,td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid aliceblue;
  } */
</style>