<template>
<div class="signup-login">
  <div class="buttons-container">
      <button @click="activeForm = 'signup'" :class="{ active: activeForm === 'login' }">Sign Up</button>
      <button @click="activeForm = 'login'" :class="{ active: activeForm === 'signup' }">Log In</button>
  </div>

  <div class="login-container container" v-if="activeForm === 'login'">
    <h4 class="login-header mb-3">Welcome Back !</h4>
    <form @submit.prevent="login">
      <!-- <label for="username">아이디: </label> -->
      <input type="text" id="username-login" v-model="username_login" placeholder="아이디를 입력하세요"><br>

      <!-- <label for="password">비밀번호: </label> -->
      <input type="password" id="password" v-model="password" placeholder="비밀번호를 입력하세요"><br>

      <input type="submit" value="로그인">
    </form>
  </div>

  <div class="signup-container container" v-if="activeForm === 'signup'">
    <h4 class="login-header mb-3">Sign Up For Free</h4>
    <form @submit.prevent="signUp">
      <!-- <label for="username">아이디: </label> -->
      <input type="text" id="username-signup" v-model="username_signup" placeholder="아이디를 입력하세요"><br>

      <!-- <label for="password1">비밀번호: </label> -->
      <input type="password" id="password1" v-model="password1" placeholder="비밀번호를 입력하세요"><br>

      <!-- <label for="password2">비밀번호 재확인: </label> -->
      <input type="password" id="password2" v-model="password2" placeholder="비밀번호를 다시 입력하세요"><br>

      <input type="submit" value="Signup">
    </form>
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
      username_login: '',
      username_signup: '',
      password: '',
      URL: 'http://127.0.0.1:8000/',
      TOKEN: '',
      password1: '',
      password2: '',
      activeForm: 'signup',
    }
  },
  methods: {
    ...mapActions(['saveToken', 'saveUsername']),
    
    async signUp() {
      if (this.password1 !== this.password2) {
        alert('비밀번호가 일치하지 않습니다.')
        return 
      }
      try {
        const response = await axios.post(this.URL + 'accounts/signup/', {
          username: this.username_signup,
          password1: this.password1,
          password2: this.password2,
        })
        console.log(response.data)
        this.TOKEN = response.data.key
        alert(`${this.username_signup}님 회원가입을 축하합니다!`)
        this.username_signup = ''
        this.password1 = ''
        this.password2 = ''
      } catch(error) {
        console.log(error)
      }
    },

    async login() {
        try {
            // console.log(this.username)
            // console.log(this.password)
            const response = await axios.post(this.URL + 'accounts/login/', {
                username: this.username_login,
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
                localStorage.setItem('username', this.username_login)

                // 홈으로 이동
                const currentPageName = this.$route.name;
                if (currentPageName !== 'home') {
                  // Redirect to the home page
                  this.$router.push({ name: 'home' });
                  // this.refresh();
                  window.location.reload();
                }
            } 
        } catch(error) {
            alert('아이디와 비밀번호를 다시 확인해주세요!')
            this.username_login=''
            this.password=''
            console.log(error)
        }
    },
  }
}
</script>

<style scoped>
.login-container{
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f2f2f2;
}

.signup-container{
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f2f2f2;
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
  background-color: #2c3e50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
}

input[type="submit"]:hover {
  background-color: #1c1d1f;
}

.login-header {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 900;
}

.active {
  background-color: #2c3e50; /* Set your active button color here */
  color: white;
}

.buttons-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

button {
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
  transition: background-color 0.3s ease;
  width: 150px;
}

button.active {
  background-color: #2c3e50; /* Set your active button color here */
  color: white;
}

button:hover {
  background-color: #1c1d1f; /* Set your button hover color here */
  color: white;
}
</style>
