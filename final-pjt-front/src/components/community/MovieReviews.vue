<template>
<div class="table-container">
  <h5>MovieReviews</h5> 
  <router-link :to="{ name:'CreateView' }">
  <button>글쓰기</button>
  </router-link>
  
  <div class="table-responsive">
    <table class="table table-dark table-striped table-hover table-sm">
      <thead>
        <tr>
          <th>No.</th>
          <th>제목</th>
          <th>작성자</th>
        </tr>
      </thead>
      <tbody>
        <ArticleListItem 
          v-for="article in articles"
          :key="article.id"
          :article="article" />
      </tbody>
    </table>
  </div>
  
</div>
  <!-- <div>
    <h5>MovieReviews</h5>
    <router-link :to="{ name:'CreateView' }">
      <button>글쓰기</button>
    </router-link>
    <ArticleListItem 
      v-for="article in articles" :key="article.id" :article="article"/>
  </div> -->
</template>

<script>
import ArticleListItem from '@/components/commons/ArticleListItem'
import { mapState } from 'vuex'

export default {
    name: "MovieReviews",
    components: {
      ArticleListItem
    },
    computed: {
      ...mapState ({
        articles: state => state.community.articles,
      })
    }
    
}
</script>

<style scoped>
  table {
    width:100%;
    border-collapse: collapse;
    text-align: center;
  }
  th {
    padding: 10px;
    border: 1px solid #ddd;
    background-color: #f5f5f5;
    text-align: center;
    color: black;
  }
  td {
    padding: 10px;
    border: 1px solid #ddd;
    text-align: center;
  }
  .tr:hover {
    background-color: #f9f9f9;
  }
  .title-link {
    display: inline-block;
    max-width: 200px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    color: white;
    text-decoration: none;
  }
  .table-responsive {
    max-width: 80%;
    margin: 0 auto;
  }
</style>