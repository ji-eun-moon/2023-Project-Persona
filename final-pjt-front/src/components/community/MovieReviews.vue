<template>
  <div>
    <h5>MovieReviews</h5>
    <router-link :to="{ name:'CreateView' }">
      <button>글쓰기</button>
    </router-link>
    <ArticleListItem 
      v-for="article in articles" :key="article.id" :article="article"/>
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

<style>

</style>