<template>
<div class="table-container">
  <h5>MovieReviews</h5> 
  <div class="create">
    <router-link :to="{ name:'CreateView' }">
    <button class="create-btn">글쓰기</button>
    </router-link>
  </div>
  
  
  <div>
    <table class="table table-dark table-striped table-hover table-sm">
      <thead>
        <tr>
          <th>No.</th>
          <th>제목</th>
          <th>작성자</th>
          <th>작성일</th>
        </tr>
      </thead>
      <tbody>
        <ArticleListItem 
          v-for="(article,index) in articles"
          :key="article.id"
          :article="article"
          :index="index" />
      </tbody>
    </table>
  </div>
</div>
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
  .table-container {
    display: flex;
    flex-direction: column;
  }
  .create {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
  }
  .create-btn {
    padding: 5px 10px;
    background-color: #2196f3;
    color: aliceblue;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
  }
  th {
    padding: 10px;
    border: 1px solid aliceblue;
    background-color: aliceblue;
    text-align: center;
    color: black;
  }
  td {
    padding: 10px;
    border: 1px solid aliceblue;
    text-align: center;
  }
  .tr:hover {
    background-color: aliceblue;
  }

</style>