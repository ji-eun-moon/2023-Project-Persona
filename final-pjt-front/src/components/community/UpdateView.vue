<template>
  <div>
    <h1>글 수정</h1>
    <form @submit.prevent="updateArticle">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용: </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" value="수정">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method:'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`
      })
      .then((res) => {
        this.title = res.data.title
        this.content = res.data.content
      })
      .catch(err => console.log(err))
    },
    updateArticle() {
      axios({
        method:'put',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        data: {
          title: this.title,
          content: this.content
        }
      })
      .then(() => {
        this.$router.push({ name: 'DetailView', params: {id: this.$route.params.id } })
      })
    }
  }
}
</script>

<style>

</style>