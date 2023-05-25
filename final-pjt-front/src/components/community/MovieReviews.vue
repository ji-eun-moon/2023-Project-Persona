<template>
  <div class="table-container">
    <div>
      <table class="table table-dark table-hover table-sm">
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
            v-for="(article, index) in displayedArticles"
            :key="article.id"
            :article="article"
            :index="getArticleNumber(index)"
          />
        </tbody>
      </table>
    </div>

    <div class="create">
      <router-link :to="{ name:'CreateView' }">
        <button class="create-btn">글쓰기</button>
      </router-link>
    </div>

    <nav aria-label="Page navigation example" class="pagination-wrapper">
      <ul class="pagination">
        <li class="page-item" :class="{ disabled: currentPage === 1 }">
          <a class="page-link" href="#" aria-label="Previous" @click="prevPage">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li class="page-item" v-for="pageNumber in totalPages" :key="pageNumber" :class="{ active: currentPage === pageNumber }">
          <a class="page-link" href="#" @click="setCurrentPage(pageNumber)">{{ pageNumber }}</a>
        </li>
        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
          <a class="page-link" href="#" aria-label="Next" @click="nextPage">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
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
  data() {
    return {
      currentPage: 1,
      itemsPerPage: 10
    };
  },
  computed: {
    ...mapState({
      articles: (state) => state.community.articles
    }),
    displayedArticles() {
      const sortedArticles = this.articles.slice().sort((a,b) => {
        return new Date(b.created_at) - new Date(a.created_at)
      })
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return sortedArticles.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.articles.length / this.itemsPerPage);
    }
  },
  methods: {
    setCurrentPage(pageNumber) {
      this.currentPage = pageNumber;
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    getArticleNumber(index) {
      return (this.currentPage - 1) * this.itemsPerPage + index + 1
    }
  }
};
</script>

<style scoped>

.table-container {
  margin-bottom: 20px;
}
.create {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 20px;
}
.create-btn {
  padding: 5px 10px;
  background-color: rgb(127, 166, 239);
  color: aliceblue;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}
.table th {
  padding: 10px;
  text-align: center;
  font-size: 15px;
  font-weight: 500;
}
td {
  padding: 10px;
  border: 1px solid aliceblue;
  text-align: center;
  font-size: 15px;
}
.tr:hover {
  background-color: aliceblue;
}
.pagination-wrapper {
  display: flex;
  justify-content: center;
}
.pagination {
  margin-top: 10px;
}
.pagination li {
  display: inline-block;
}
.pagination li a {
  padding: 5px 10px;
  text-decoration: none;
  color: rgb(127, 166, 239);
}
.pagination li.active a {
  background-color: rgb(127, 166, 239);
  color: aliceblue;
}
.pagination li.disabled a {
  pointer-events: none;
  opacity: 0.6;
}
</style>
