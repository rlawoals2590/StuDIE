<template>
  <div class="main-container">
    <!-- NAV 시작 (header 역할을 겸함) -->
    <nav class="display-box">
      <router-link to="/"> <h1 class="neon-sign-pink title">STUDIE - My profile </h1> </router-link>
    </nav>
    <!-- NAV 끝 -->

    <!-- 메인 요소 시작 -->
    <main>
      <div class="content">
        <!-- 간략 프로필 시작 -->
        <div class="display-box">
          <!-- 동그라미 모양으로 크롭된 프로필 사진 -->
          <div class="profile-picture">
            <img src="../assets/logo-non-text.png" alt="Profile Picture">
          </div>
          <h2> {{ profile.name }} </h2>
          <ul>
            <li> 라이벌 : {{ profile.rival_id }} </li>
            <li> 포인트 : {{ profile.point }} </li>

            <li> {{ profile.gender }} </li>
          </ul>

          <button @click="logout">Logout</button>
        </div>
        <!-- 간략 프로필 끝 -->

        <div class="display-box">
          <h2 > 프로필 카드 </h2>
          <div class="profile-card">
          <img src="../assets/exampleCard.png">

        </div>
        
        </div>
        
        <!-- 지역 시작 -->
        <div class="display-box">
          <h2> 지역 </h2>
          <p> {{ profile.local }}</p>
        </div>
        <!-- 지역 끝 -->

          <!-- 소속 시작 -->
          <div class="display-box">
            <h2> 소속 학교 </h2>
            <p> {{ profile.belong }}</p>
          </div>
          <!-- 소속 끝 -->
        

        <!-- 목표 시작 -->
        <div class="display-box">
          <h2> 목표 </h2>
          <ul>
            <li> {{ profile.goal }} </li>
          </ul>
        </div>
        <!-- 목표 끝 -->
      </div>
    </main>
    <!-- 메인 요소 끝 -->

    <!-- footer 시작 -->
    <footer>
      <p>© 2023 NewEye. All rights reserved.</p>
    </footer>
    <!-- footer 끝 -->
  </div>
</template>

<script>
import axios from 'axios'


export default {
  methods: {
    logout() {
      
        axios.get('/user/logout/');
        this.$cookies.remove('user_access_token')
        this.$cookies.remove('session')
        this.$router.push('/')

        
        
    },

  
      
    },
  mounted() {

    axios.get('/user/get_users/').then((response) => {
      this.profile = response.data
    })

  },
  data(){
    return{
    profile : {}
    }
  }
  }

</script>

<style scoped>
@import url('../assets/global.css');

/* CSS for the circular cropped profile picture */
.profile-picture {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto;
}

.profile-picture img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  

}

.profile-card{
  text-align: center;
  align-items: center;
}
/* Add the background image to the main container */


</style>
