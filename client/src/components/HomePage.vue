<template>
  <div class="main-container">
    <!-- NAV 시작 (header 역할을 겸함) -->
    <nav class="display-box">
      <h1 class="neon-sign-pink title">STUDIE</h1>
      <h1 class="neon-sign-purple title">STUDY 📖 OR DIE 💀</h1>

    </nav>
    <!-- NAV 끝 -->

    <!-- 메인 요소 시작 -->
    <main>
      <div class="content">
        <!-- 프로필 바로가기 시작 -->
        <div class="display-box">
          <router-link to="/profilePage">
            <h1 class="neon-sign-sky title"> Profile 👨‍🎓 </h1>
          </router-link>
          <h2> 이름 : 윤현우 </h2>
          <h2> 성별 : 남자 </h2>
          <h2 > 나이 : 만 17세 </h2>
          <h2 > 직업 : 고3 </h2>
          <h2 > 목표 : 수능 </h2>
          <h2 > 거주지 : 경기도  </h2>
          <h2 > 라이벌 : 없음  </h2>
        </div>
        <!-- 프로필 바로가기 끝  -->

        <!-- 공부방 바로가기 시작 -->
        <div class="display-box">
          <router-link to="/StudyRoom">
            <h1 class="neon-sign-sky title"> AI 공부방 👀 </h1>
          </router-link>
          <h3> 인공지능이 당신을 감시중입니다.. 🤖 </h3>
        </div>
        <!-- 공부방 바로가기 끝  -->

        <!-- 공부 타이머 바로가기 시작 -->
        <div class="display-box">
          <router-link to="/StudyTimer">
            <h1 class="neon-sign-sky title"> 공부 타이머 ⏱ </h1>
          </router-link>
          <h3> 타이머로 순공 시간을 측정해보세요! </h3>
        </div>
        <!-- 공부 타이머 바로가기 끝  -->

        <!-- 랭킹 바로가기 시작 -->
        <div class="display-box">
          <router-link to="/RankingBoard">
            <h1 class="neon-sign-sky title"> 랭킹 보드 🥇</h1>
          </router-link>
          <h3> 우리 지역/학교는 몆등일까? </h3>
        </div>
        <!-- 랭킹 바로가기 끝  -->
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

}
</script>

<style scoped>
@import url('../assets/global.css');

.main-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #000000;
  color: #eeeeee;
}

.main {
  flex: 1;
  display: flex;
  justify-content: center;
  padding: 20px;
  background-color: #000000;
}

.content {
  text-align: center;
  background-color: #000000;
}


.profile-img {
  height: 40px;
  width: 40px;
  border-radius: 50%;
  cursor: pointer;
  transition: 0.3s ease-in-out;
}

.profile-img:hover {
  transform: scale(1.1);
}

.profile-dropdown {
  position: absolute;
  top: 50px;
  right: 0;
  background-color: #111111;
  color: #eeeeee;
  padding: 10px;
  border-radius: 10px;
  text-align: left;
  transition: 0.3s ease-in-out;
  min-width: 200px;
  display: none;
}

.profile-container:hover .profile-dropdown {
  display: block;
}

.profile-dropdown h2 {
  margin: 5px 0;
}

/* other styles */
</style>
