<template>
  <div>
    <h1 style="color:aliceblue; font-weight:bold; font-size:36px; margin-top:30px;"><i class="bi bi-pencil-fill me-2"></i>Update Your Content</h1>
    <div class="update-form">
      <form @submit.prevent="updateArticle" class="form">
        <label for="title" class="label"></label>
        <input type="text" id="title" v-model.trim="title" class="input"><br>
        <label for="content" class="label"></label>
        <textarea id="content" cols="30" rows="10" v-model="content" class="textarea"></textarea><br>
        <input type="submit" value="수정" class="submit-btn">
      </form>
    </div>
    
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

<style scoped>
.update-form {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 40px;
}

h1 {
  font-size: 24px;
  text-align: center;
  margin-bottom: 20px;
}

.form {
  display: flex;
  flex-direction: column;
}

.label {
  font-size: 18px;
  margin-bottom: 5px;
}

.input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid aliceblue;
  border-radius: 10px;
  margin-bottom: 10px;
  margin-top: 25px;
}
.textarea {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid aliceblue;
  border-radius: 10px;
  margin-bottom: 10px;
}

.submit-btn {
  padding: 10px 20px;
  font-size: 16px;
  background-color:rgb(127, 166, 239);
  color: #fff;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  margin-bottom: 25px;
}

.submit-btn:hover {
  background-color: rgb(127, 166, 239);
}

</style>