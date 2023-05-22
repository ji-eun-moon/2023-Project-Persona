<template>
  <tr class="article-list-item">
    <td>{{ article.id }}</td>
    <td><router-link :to="{ name:'DetailView', params:{ id:article.id } }">{{ article.title }}</router-link></td>
    <td>{{ article.username }}</td>
  </tr>
  <!-- <div>
    <h5>{{ article.id }}</h5>
    <router-link :to="{ name: 'DetailView', params: {id: article.id } }">{{ article.title }}</router-link>
    <p>{{ article.username }}</p>
    <hr>
  </div> -->
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
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
    width: 70%;
  }
  .article-list-item td:last-child {
    width: 20px;
  }
</style>