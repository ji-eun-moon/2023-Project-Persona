<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용: </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    async createArticle() {
      // const title = this.title
      // const content = this.content

      try {
        const token = this.$store.state.token.token 
        const config = {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
        const data = {
          title: this.title,
          content: this.content,
        }
        await axios.post(`${API_URL}/api/v1/articles/`, data, config)
        await this.$router.push({name:'community'})
      } catch (error) {
        console.log('Failed to create article list: ', error)
      }

      if (!this.title) {
        alert('제목을 입력해 주세요')
        return 
      }
      else if (!this.content) {
        alert('내용을 입력해 주세요')
        return 
      }
      // axios({
      //   method: 'post',
      //   url: `${API_URL}/api/v1/articles/`,
      //   data: {title,content},
      //   headers: {
      //     Authorization: `Token ${this.$store.state.token.token}`,
      //   },
      // })
      // .then(()=> {
      //   // console.log(res)
      //   this.$router.push({name:'community'})
      // })
      // .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>