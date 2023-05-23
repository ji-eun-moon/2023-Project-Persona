<template>
  <tr class="article-list-item">
    <td>{{ index+1 }}</td>
    <td><router-link :to="{ name:'DetailView', params:{ id:article.id } }" class="title-link">{{ article.title }}</router-link></td>
    <td>{{ article.username }}</td>
    <!-- <td>{{ article.created_at }}</td> -->
    <td>{{ formatDateTime(article.created_at) }}</td>
  </tr>
</template>

<script>
import moment from 'moment'

export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
    index: Number,
  },
  methods: {
    formatDateTime(dateTime) {
      return moment(dateTime).format('YYYY-MM-DD')
    }
  }
}
</script>

<style scoped>
  .article-list-item {
    border-bottom: 1px solid #ccc;
  }
  .article-list-item td {
    padding: 10px;
  }
  .article-list-item td:first-child {
    width: 10%;
  }
  .article-list-item td:nth-child(2) {
    width: 50%;
  }
  .article-list-item td:nth-child(3) {
    width: 10%;
  }
  .article-list-item td:last-child {
    width: 20px;
  }
  .title-link {
    text-decoration-line: none;
    color: aliceblue;
  }
</style>