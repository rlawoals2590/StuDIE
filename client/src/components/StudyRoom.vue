  <template>
    <div class="main-container">

      <!-- NAV 시작 (header 역할을 겸함) -->
      <nav class="display-box">
        <router-link to="/"> <h1 class="neon-sign-pink title">스터다이 AI 공부방</h1> </router-link>
      </nav>
      <!-- NAV 끝 -->

      <!-- 메인 요소 시작 -->
      <main>
        <div class="content">

          <!-- 내 영상 시작 -->
          <div class="display-box">
            <h1 class="neon-sign-sky title"> My Video 👨‍🎓 </h1>
            <video autoplay="true" ref="videoElement" id="videoElement"></video>
          </div>
          <!-- 내 영상 끝  -->

          <!-- 집중도 시작 -->
          <div class="display-box">
            <h1 class="neon-sign-sky title"> 집중도 </h1>
            <div id="myProgress">
              <div :style="{ width: progress + '%' }" id="myBar">{{ progress }}%</div>
            </div>
          </div>
          <!-- 집중도 끝  -->

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
    
    methods:{

      
    
      
      captureImage() {
  const video = this.$refs.videoElement;
  if (!video) {
    console.log('Video element not found');
    return; // Return early if the video element is not found
  }
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  const imageData = canvas.toDataURL('image/jpeg');
  this.sendImageToServer(imageData);
},

      sendImageToServer(imageData) {
        fetch('/room/upload', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ image: imageData }),
        }).then((response) => {
          // 응답 처리
        });
      },
    },
    data() {
      return {
        progress: 50,
      };
    },
    mounted() {
      

      this.interval1 = setInterval(() => {

        fetch('/room/score/', {
          method : 'GET'
        }).then((response) => {
          return response.json();
        }).then((data) => {
          

          this.progress = data.score;
          
          
        }) 
      }, 1000);
      if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
          .then((stream) => {
            const video = this.$refs.videoElement;
            video.srcObject = stream;
          })
          .catch((error) => {
            console.log("Something went wrong:", error);
          });
      }

      this.interval2 = setInterval(() => {
        

        this.captureImage()
      }, 1000);


    },  beforeDestroy() {
      clearInterval(this.interval1);
      clearInterval(this.interval2);
    }
    
  };

  </script>

  <style scoped>
  @import url('../assets/global.css');

  #videoElement {
    width: 80vh;
    height: 60vh;
    transform: scaleX(-1); /* 좌우 반전 */
    background-color: #111111;
  }

  #myProgress {
    width: 100%;
    background-color: grey;
    margin-bottom: 20px;
    margin-top: 20px;
  }

  #myBar {
    width: 50%;
    height: 30px;
    background-color: #6626A6;
    font-family: 'Arial', sans-serif;
    text-align: center; /* To center it horizontally (if you want) */
    line-height: 30px; /* To center it vertically */
    color: white;
  }
  </style>
