<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="login">
      <label for="username">아이디: </label>
      <input type="text" id="username" v-model="username" placeholder="아이디를 입력하세요"><br>

      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="password" placeholder="비밀번호를 입력하세요"><br>

      <input type="submit" value="login">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      URL: 'http://127.0.0.1:8000/',
      TOKEN: '',
    }
  },
  methods: {
    async signUp() {
      if (this.password1 !== this.password2) {
        alert('비밀번호가 일치하지 않습니다.')
        return 
      }
      try {
        const response = await axios.post(this.URL + 'accounts/signup/', {
          username: this.username,
          password1: this.password1,
          password2: this.password2,
        })
        console.log(response.data)
        this.TOKEN = response.data.key
      } catch(error) {
        console.log(error)
      }
    },
    async login() {
        try {
            console.log(this.username)
            console.log(this.password)
            const response = await axios.post(this.URL + 'accounts/login/', {
                username: this.username,
                password: this.password,
            })
            if (response.data) {
                console.log(response.data)
                this.TOKEN = response.data.key 
            } 

        } catch(error) {
            console.log(error)
        }
    },
  }
}
</script>

<style>

</style>