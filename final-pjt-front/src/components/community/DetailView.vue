<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호: {{ article?.id }}</p>
    <p>제목: {{ article?.title }}</p>
    <p>내용: {{ article?.content }}</p>
    <p>작성시간: {{ formatDateTime(article.created_at) }}</p>
    <p>수정시간: {{ formatDateTime(article.updated_at) }}</p>

    <button @click="updateArticleBtn">수정</button>
    <button @click="deleteArticle">삭제</button>

    <br>
    <hr>
    <form @submit.prevent="createComment">

      <label for="content">댓글 내용: </label>
      <textarea id="content" cols="30" rows="5" v-model="commentContent"></textarea><br>

      <button type="submit">댓글 작성</button>
    </form>

    <div v-for="comment in commentList" :key="comment.id" >
      <p>{{ comment.username }}</p>
      <p>{{ comment.content }}</p>
      <p>{{ formatDateTime(comment.created_at) }}</p>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
      commentContent: '',
      commentList: []
    }
  },
  created() {
    this.getArticleDetail()
    this.getCommentList()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`
      })
      .then((res) => {
        // console.log(res)
        this.article = res.data
      })
      .catch(err => console.log(err))
    },
    deleteArticle() {
      axios({
        method:'delete',
        url: `${API_URL}/api/v1/articles/${this.article.id}/`,
      })
      .then(() => {
        this.$router.push({ name:'community' })
      })
      .catch(err => console.log(err))
    },
    updateArticleBtn() {
      this.$router.push({ name:'UpdateView',parmas:{id:this.article.id}})
    },
    async createComment() {
      try {
        const token = this.$store.state.token.token
        const config = {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
        const data = {
          content: this.commentContent,
        }
        await axios.post(`${API_URL}/api/v1/articles/${this.article.id}/comments/`,data,config)
        await this.getCommentList()
      } catch (error) {
        console.error('Failed to create comment:', error)
      }
      this.commentContent = ''
    },
    async getCommentList() {
      try {
        const token = this.$store.state.token.token
        const config = {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
        const response = await axios.get(`${API_URL}/api/v1/articles/${this.article.id}/comments/`,config)
        this.commentList = response.data
        console.log(this.commentList)
      } catch (error) {
        console.log('Failed to get comment list:', error)
      }
    },
    formatDateTime(dateTime) {
      return moment(dateTime).format('YYYY-MM-DD HH:mm:ss')
    }
  }
}
</script>

<style>

</style>