<template>
    <div class="main-container">
      <!-- NAV 시작 (header 역할을 겸함) -->
      <nav class="display-box">
        <router-link to="/"><h1 class="neon-sign-pink title">STUDIE - My profile</h1> </router-link>
      </nav>
      <!-- NAV 끝 -->
  
      <!-- 메인 요소 시작 -->
      <main>
        <div class="content">
  
          <!-- 지역별 보드 시작 -->
          <div class="display-box">
            <h2 class="title neon-sign-sky">
              지역별 랭킹
            </h2>
  
            <ul>
              
              <li  class="first-rank" >  1 : 강원도 </li>
              <li  class="second-rank">  2 : 서울 </li>
              <li  class="third-rank">  3 : 경기도  </li>
              <li>4 : 충청북도</li>
              <li>5 : 경상도</li>
              <li>6 : 충청남도</li>
            </ul>
          </div>
          <!-- 지역별 보드 끝  -->


          <!-- 학교별 보드 시작 -->
          <div class="display-box">
            <h2 class="title neon-sign-sky">
              학교별 랭킹
            </h2>
  
            <ul>
              
              <li  class="first-rank" >  1 : 고려대학교 </li>
              <li  class="second-rank">  2 : 무소속 </li>
              <li  class="third-rank">  3 : 세명컴퓨터고등학교 </li>

            </ul>
          </div>
          <!-- 학교별 보드 끝  -->                    
  

        <!-- 개인 보드 시작 -->
        <div class="display-box">
        <h2 class="title neon-sign-sky">
            개인별 랭킹
        </h2>

        <ul>
            
            <li  class="first-rank" >  1 : 윤현우@YoonHyunWooo </li>
            <li  class="second-rank">  2 : 길은지@Roadun </li>
            <li  class="third-rank">  3 : 기미상궁@kimisang </li>

        </ul>
        </div>
        <!-- 개인 보드 끝  -->   



        
        <!-- 나이별 보드 시작 -->
        <div class="display-box">
            <h2 class="title neon-sign-sky">
                나이별 랭킹
            </h2>
    
            <ul>
                
                <li  class="first-rank" >  1 : 05년생 </li>
                <li  class="second-rank">  2 : 00년생 </li>
                <li  class="third-rank">  3 : 03년생 </li>
    
            </ul>
            </div>
            <!-- 나이별 보드 끝  -->  
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
  
  /* Add custom styling to the first rank */
  .first-rank {
    color: #111111; /* Change the color to whatever you like */
    font-size: 4rem;
    font-weight: bold; /* Add any other styles you want to make it stand out */
    text-shadow: 0 0 4px #ccc, 0 -5px 4px #ff3, 2px -10px 6px #fd3, -2px -15px 11px #f80, 2px -19px 18px #f20
  }

  .second-rank {
    color: white; /* Change the color to whatever you like */
    font-size: 3rem;
    font-weight: bold; /* Add any other styles you want to make it stand out */
  }

  .third-rank {
    color: white; /* Change the color to whatever you like */
    font-size: 2rem;
    font-weight: bold; /* Add any other styles you want to make it stand out */
    
  }
  li{
    font-size: 1.3rem;
  }
  </style>
  