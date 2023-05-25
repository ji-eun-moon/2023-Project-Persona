<template>
  <div>
    <h1 style="margin-top:30px; color:aliceblue; margin-bottom:30px; font-weight:bold;"><i class="bi bi-pencil-fill me-2"></i>Write Your Story</h1>
    <div class="create-form">
      <form @submit.prevent="createArticle" class="article-form">
        <label for="title" class="title-label"></label>
        <input type="text" id="title" v-model.trim="title" class="title-input"  placeholder="제목을 입력하세요"><br>
        <label for="content" class="textarea-label"></label>
        <textarea id="content" cols="30" rows="10" v-model="content" class="textarea-input"  placeholder="내용을 입력하세요"></textarea><br>
        <input type="submit" id="submit" class="form-submit" value="등록">
      </form>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import { eventBus } from '@/event-bus'
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
        eventBus.$emit('articleCreated')
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
    }
  }
}
</script>

<style>
  .article-form {
    display: flex;
    flex-direction: column;
    max-width: 500px;
    margin: 0 auto;
    
  }
  .create-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  .title-input {
    width: 100%;
    padding: 8px;
    font-size: 16px;
    border: 1px solid aliceblue;
    border-radius: 10px;
    margin-top: 30px;
  }
  .textarea-input {
    width: 100%;
    padding: 8px;
    font-size: 16px;
    border: 1px solid aliceblue;
    border-radius: 10px;
    margin-top: 10px;
  }
  .form-submit {
    padding: 8px 16px;
    font-size: 18px;
    background-color: darkgray;
    color: aliceblue;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    margin-bottom: 25px;
  }
  .form-submit:hover {
    background-color: rgb(127, 166, 239);
  }
</style>