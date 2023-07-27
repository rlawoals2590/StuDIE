<template>
  <div class="main-container">
    <nav class="display-box">
      <router-link to="/"> <h1 class="title">STUDIE - login </h1> </router-link>
    </nav>

    <main>
      <div class="content">

      <div class="display-box login">
          <h2>로그인</h2>
          <input class="apple-like-input" v-model="stid"  placeholder="학번" type="number"  style="color: white;">
          <input class="apple-like-input" v-model="password"  type="password" placeholder="비밀번호">
          <input class="apple-like-input" v-model="name" placeholder="이름">
          <input class="apple-like-input" v-model="belong" placeholder="소속">
          
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
        stid: '',
        password: '',
        name: '',
        belong: ''
      }
    },
    methods: {
      async login() {
        const FormData = require('form-data');
        let data = new FormData();
        data.append('stid', this.stid);
        data.append('passwd', this.password);
        data.append('name', this.name);
        data.append('belong', this.belong);

        let config = {
          method: 'post',
          maxBodyLength: Infinity,
          url: '/user/login/',
          headers: { 
            'Content-Type' :  'multipart/form-data'
          },
          data : data
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
