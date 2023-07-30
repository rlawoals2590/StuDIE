<template>
  <div class="main-container">
    <nav class="display-box">
      <router-link to="/"> <h1 class="title">STUDIE - login </h1> </router-link>
    </nav>

    <main>
      <div class="content">

      <div class="display-box sign-up">
          <h2>회원 가입</h2>
          <input class="apple-like-input" v-model="id"  placeholder="아이디" type="text"  style="color: white;" required>

          <input class="apple-like-input" v-model="passwd"  type="password" placeholder="비밀번호">
          <input class="apple-like-input" v-model="name" placeholder="이름">
          <input class="apple-like-input" v-model="birth" placeholder="생일">
          <select v-model="gender " class="apple-like-input" placeholder="태어난 해" >
            <option value="" disabled selected>성별</option>
            <option value="0"> 남성 </option>            
            <option value="1"> 여성 </option>
          </select>
          
          
          <input class="apple-like-input" v-model="belong" placeholder="소속">
          <input class="apple-like-input" v-model="local" placeholder="지역">
          <input class="apple-like-input" v-model="vision" placeholder="목표">

          
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
        vision : ''
      }
    },
    methods: {
      async signUp() {
      if (!this.id || !this.passwd || !this.name || !this.birth || !this.gender || !this.vision) {
        alert('모든 필드를 채워주세요!')
        return;
      }
        let data = {
          id: this.id,
        passwd:this.passwd,
        name: this.name,
        birth: this.birth,
        gender: this.gender,
        belong:this.belong,
        local: this.local,
        vision : this.vision
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
          location.href = '/'
          
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

  .sign-up input, .sign-up button, .sign-up select{
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
  