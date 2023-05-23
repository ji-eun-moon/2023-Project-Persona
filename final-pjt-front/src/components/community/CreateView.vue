<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle" class="article-form">
      <label for="title" class="form-label">제목: </label>
      <input type="text" id="title" v-model.trim="title" class="form-input"  placeholder="제목을 입력하세요"><br>
      <label for="content" class="form-label">내용: </label>
      <textarea id="content" cols="30" rows="10" v-model="content" class="form-textarea"  placeholder="내용을 입력하세요"></textarea><br>
      <input type="submit" id="submit" class="form-submit">
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
  .article-form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 0 auto;
  }
  .form-label {
    font-size: 18px;
    margin-bottom: 10px;
    color: aliceblue;
  }
  .form-input,
  .form-textarea {
    width: 100%;
    padding: 8px;
    font-size: 16px;
    border: 1px solid aliceblue;
    border-radius: 10px;
    margin-bottom: 10px;
  }
  .form-submit {
    padding: 8px 16px;
    font-size: 18px;
    background-color: #4CAF50;
    color: aliceblue;
    border: none;
    border-radius: 10px;
    cursor: pointer;
  }
  .form-submit:hover {
    background-color: #45a049;;
  }
</style>