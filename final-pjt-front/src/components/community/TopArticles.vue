<template>
  <div>
    <table class="table table-dark table-hover table-sm">
      <thead>
        <tr>
          <th>작성자</th>
          <th>제목</th>
          <th>작성일</th>
          <th>추천수</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in topArticles" :key="article.id" class="article-list-item">
          <td>{{ article.username }}</td>
          <td><router-link :to="{ name:'DetailView', params:{ id:article.id } }" class="title-link">{{ article.title }}</router-link></td>
          <td>{{ formatDateTime(article.created_at) }}</td>
          <td>{{ article.likeCount }}</td>
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
    async created() {
      await this.fetchTopArticles()
    },
    methods: {
      async fetchTopArticles() {
        try {
          const response = await axios.get(`${API_URL}/api/v1/articles/top/`)
          const articles = response.data
          for (const article of articles) {
            await this.getLikeCount(article)
          }
          this.topArticles = articles
          console.log(response)
          
        } catch (error) {
          console.log('Failed to fetch popular articles:', error)
        }
      },
      formatDateTime(dateTime) {
      return moment(dateTime).format('YYYY-MM-DD')
      },
      async getLikeCount(article) {
        try {
          const token = this.$store.state.token.token
          const config = {
            headers: {
              Authorization: `Token ${token}`,
            }
          }
          const response = await axios.get(`${API_URL}/api/v1/articles/${article.id}/like/`, config)
          article.likeCount = response.data.likeCount 
        } catch (error) {
          console.log('Failed to get like count for article ${article.id}: ', error)
        }
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
    width: 40%;
  }
  .article-list-item td:nth-child(3) {
    width: 20%;
  }
  .article-list-item td:last-child {
    width: 20px;
  }
  .title-link {
    text-decoration-line: none;
    color: aliceblue;
  }
  .table {
    width: 100%;
    border-collapse: collapse;
    text-align: center;
    margin-bottom: 20px;
  }
  .table-container {
    display: flex;
    flex-direction: column;
  }

  .table th {
    padding: 10px;
    text-align: center;
    font-size: 15px;
    font-weight: 500;
  }
  .table td {
    padding: 10px;
    text-align: center;
    font-size: 15px;
    font-weight: 300;
  }
  .table thead {
    background-color: #f5f5f5;
  }
  .tr:hover {
    background-color: aliceblue;
  }
</style>