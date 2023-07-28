<template>
  <div class="main-container">
    <!-- NAV 시작 (header 역할을 겸함) -->
    <nav class="display-box">
      <a href="/"> <h1 class="neon-sign-pink title">STUDIE - My profile </h1> </a>
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
          <h2> 윤현우 </h2>
          <ul>
            <li> 라이벌 : 홍박사 </li>
            <li> 포인트 : 196000 </li>

            <li> 남성 </li>
          </ul>
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
          <p> 경기도</p>
        </div>
        <!-- 지역 끝 -->

          <!-- 소속 시작 -->
          <div class="display-box">
            <h2> 소속 학교 </h2>
            <p> 세명컴퓨터고등학교</p>
          </div>
          <!-- 소속 끝 -->
        
        <!-- 직업 시작 -->
        <div class="display-box">
          <h2> 직업 </h2>
          <p> 고등학생 3학년</p>
        </div>
        <!-- 직업 끝 -->

        <!-- 목표 시작 -->
        <div class="display-box">
          <h2> 목표 </h2>
          <ul>
            <li> 정보처리산업기사 </li>
            <li> 수능 </li>
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
export default {

};

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
