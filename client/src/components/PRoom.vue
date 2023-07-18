<template>
    <div class="pr-container">
      <div class="presenter-video">
        <video ref="presenterVideo" class="video-element" autoplay></video>
      </div>
      <div class="participants-video">
        <!-- 참가자들의 영상 표시 -->
        <!-- 예시: <video class="video-element" v-for="participant in participants" :key="participant.id" :src="participant.videoSrc" autoplay></video> -->
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        presenterStream: null,
        participants: [
          {
            id: 1,
            videoSrc: 'video/participant1-video.mp4' // 참가자 1의 영상 소스
          },
          {
            id: 2,
            videoSrc: 'video/participant2-video.mp4' // 참가자 2의 영상 소스
          },
          // ...
        ]
      };
    },
    mounted() {
      this.getPresenterVideo();
    },
    methods: {
      async getPresenterVideo() {
        try {
          this.presenterStream = await navigator.mediaDevices.getUserMedia({ video: true });
          if (this.$refs.presenterVideo) {
            this.$refs.presenterVideo.srcObject = this.presenterStream;
          }
        } catch (error) {
          console.error('Failed to get presenter video stream:', error);
        }
      }
    },
    beforeUnmount() {
      if (this.presenterStream) {
        this.presenterStream.getTracks().forEach(track => {
          track.stop();
        });
      }
    }
  };
  </script>
  
  <style scoped>
  .pr-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    background-color: #000000;
    color: #eeeeee;
  }
  
  .presenter-video {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #4e4feb;
    max-height: 50vh; /* 변경된 부분: 최대 높이 설정 */
  }
  
  .participants-video {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    background-color: #eeeeee;
    max-height: 50vh; /* 변경된 부분: 최대 높이 설정 */
  }
  
  .video-element {
    width: auto; /* 변경된 부분: 가로 크기 자동 조정 */
    height: 100%;
    object-fit: cover;
  }
  </style>
  