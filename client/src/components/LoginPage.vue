<template>
  <div class="main-container">
    <nav class="display-box">
      <router-link to="/"> <h1 class="title">STUDIE - login </h1> </router-link>
    </nav>

    <main>
      <div class="content">

      <div class="display-box login">
          <h2>로그인</h2>
          <input class="apple-like-input" v-model="id"  placeholder="아이디" type="text"  style="color: white;">
          <input class="apple-like-input" v-model="password"  type="password" placeholder="비밀번호">

          
          <button class="apple-like-button" @click="login">로그인</button>

          <router-link to="/signup" > 회원가입 </router-link>
        </div>

      </div>
    </main>

    <footer>
      <p>© 2023 NewEye. All rights reserved.</p>
    </footer>
  </div>
</template> 

<script>
import axios from 'axios';

export default {
  data() {
    return {
      id: '',
      password: '',
    }
  },
  methods: {
    async login() {
      // We're sending JSON data, so we use a JavaScript object
      let data = {
        id: this.id,
        passwd: this.password
      };

      let config = {
        method: 'post',
        url: '/user/login/',
        headers: { 
          'Content-Type' :  'application/json' // The content type should be application/json for JSON data
        },
        data: data
      };

      axios.request(config)
      .then((response) => {
        location.href = 'http://localhost:8081/'
      })
      .catch((error) => {
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>
  @import url('../assets/global.css');

  ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
    color: white;
    opacity: 1; /* Firefox */
  }
  
  .login{
    display: flex;
    flex-direction: column;
  }

  a[href='/signup']{
    color: #666666;
    text-align: center;
  }

  .login input, .login button{
    padding: 10px;
    margin: 10px;
    border-radius: 10px;
    background-color: #111111;
    border:  1px solid #666666;
    color: white;
  }
  
  
</style>
