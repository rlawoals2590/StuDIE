<template>
  <div class="main-container">
    <nav class="display-box">
      <router-link to="/"> <h1 class="title">STUDIE - login </h1> </router-link>
    </nav>

    <main>
      <div class="content">

      <div class="display-box sign-up">
          <h2>회원 가입</h2>
          <input class="apple-like-input" v-model="id"  placeholder="아이디" type="number"  style="color: white;">
          <input class="apple-like-input" v-model="passwd"  type="password" placeholder="비밀번호">
          <input class="apple-like-input" v-model="name" placeholder="이름">
          <input class="apple-like-input" v-model="birth" placeholder="생일">
          <input class="apple-like-input" v-model="gender" placeholder="성별" type="number">
          <input class="apple-like-input" v-model="belong" placeholder="소속">
          <input class="apple-like-input" v-model="local" placeholder="지역">
          
          <button class="apple-like-button" @click="signUp">가입하기</button>
          <router-link to="/loginpage" > 로그인 </router-link>
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
        passwd: '',
        name: '',
        birth : '',
        gender: '',
        belong: '',
        local: '',
      }
    },
    methods: {
      async signUp() {

        let data = {
          id: this.id,
        passwd:this.passwd,
        name: this.name,
        birth: this.birth,
        gender: this.gender,
        belong:this.belong,
        local: this.local,
      };
        let config = {
          method: 'post',
          url: '/user/register/',
          headers: { 
            'Content-Type' :  'application/json' // The content type should be application/json for JSON data
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
  
  .sign-up{
    display: flex;
    flex-direction: column;
    
  }

  .sign-up input, .sign-up button{
    padding: 10px;
    margin: 10px;
    border-radius: 10px;
    background-color: #111111;
    border:  1px solid #666666;
    color: white;
    
  }


  a[href='/loginpage']{
    color: #666666;
    text-align: center;
  }
  
  </style>
  