<template>
    <div class="main-container">
      <main>
        <div class="content">
          <div class="logo-container">
            <img src="../assets/logo-non-text.png" alt="Logo" class="logo">
          </div>
          <h1>NewEye 화상 통화</h1>
          <p>회의 ID를 입력하세요:</p>
          <input type="text" v-model="meetingId" placeholder="회의 ID">
          <button @click="startMeeting">회의 시작</button>
          
  
        </div>
      </main>
      <footer>
        <p>© 2023 NewEye. All rights reserved.</p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    
  };
  </script>
  
  <style scoped>
  .main-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    background-color: #000000;
    color: #eeeeee;
  }
  
  main {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
  }
  
  .content {
    text-align: center;
  }
  
  .logo-container {
    position: relative;
    animation: floatingLogo 3s infinite ease-in-out;
  }
  
  @keyframes floatingLogo {
    0% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-10px);
    }
    100% {
      transform: translateY(0);
    }
  }
  
  .logo {
    width: 200px;
    margin-bottom: 20px;
  }
  
  h1 {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  input {
    width: 200px;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #4e4feb;
    border: none;
    color: #eeeeee;
    cursor: pointer;
  }
  
  footer {
    padding: 10px;
    text-align: center;
    font-size: 12px;
    color: rgba(238, 238, 238, 0.5);
  }

  
  </style>
  