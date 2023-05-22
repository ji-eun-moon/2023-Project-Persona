<template>
  <div class="login-container container">
    <!-- <h1 class="login-header">로그인</h1> -->
    <form @submit.prevent="login">
      <!-- <label for="username">아이디: </label> -->
      <input type="text" id="username" v-model="username" placeholder="아이디를 입력하세요"><br>

      <!-- <label for="password">비밀번호: </label> -->
      <input type="password" id="password" v-model="password" placeholder="비밀번호를 입력하세요"><br>

      <input type="submit" value="로그인">
    </form>

    <div class="error-message mt-3" v-if="loginError">
      <p>아이디와 비밀번호를 다시 확인해주세요.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex';

export default {
  
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      URL: 'http://127.0.0.1:8000/',
      TOKEN: '',
      loginError: false,
    }
  },
  methods: {
    ...mapActions(['saveToken', 'saveUsername']),
    // async signUp() {
    //   if (this.password1 !== this.password2) {
    //     alert('비밀번호가 일치하지 않습니다.')
    //     return 
    //   }
    //   try {
    //     const response = await axios.post(this.URL + 'accounts/signup/', {
    //       username: this.username,
    //       password1: this.password1,
    //       password2: this.password2,
    //     })
    //     console.log(response.data)
    //     this.TOKEN = response.data.key
    //   } catch(error) {
    //     console.log(error)
    //   }
    // },
    async login() {
        try {
            // console.log(this.username)
            // console.log(this.password)
            const response = await axios.post(this.URL + 'accounts/login/', {
                username: this.username,
                password: this.password,
            })
            if (response.data) {
                // console.log(response.data)
                this.TOKEN = response.data.key

                // 로그인 정보 store에 저장
                this.saveToken(this.TOKEN) // token
                this.$store.commit("setLoggedIn", true); // 로그인 상태
                this.saveUsername(this.username) // username
                console.log('로그인 확인:',this.$store.state.token.username, this.$store.state.token.loggedIn, this.$store.state.token.token)


                // 로컬스토리지에 토큰과 username 저장 - 새로고침해도 로그인 유지
                localStorage.setItem('token', this.TOKEN);
                localStorage.setItem('username', this.username)

                // 홈으로 이동
                const currentPageName = this.$route.name;
                if (currentPageName !== 'home') {
                  // Redirect to the home page
                  this.$router.push({ name: 'home' });
                }
            } 
        } catch(error) {
            this.loginError = true
            console.log(error)
        }
    },
  }
}
</script>

<style scoped>
.login-container {
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 5px;
}

form {
  display: flex;
  flex-direction: column;
}

input[type="text"],
input[type="password"] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

input[type="submit"] {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
}

input[type="submit"]:hover {
  background-color: #45a049;
}
</style>
