<template>
    <div class="main-container">
        <div class="box_block">
            <div class="STUDIE-TIME-TIMER">STUDIE TIME TIMER</div>
            <div class="time">
              <input type="number" min="0" v-model="timeInput" placeholder="분을 입력하세요" />
            </div>
            <div class="time-timer-normal-red"></div>
            <svg class="time-timer-red" viewBox="0 0 100 100">
              <path :d="pathD" fill="#fb534b" />
            </svg>
            <div class="time-timer-white"></div>
            <div class="time-timer-border"></div>
            <div class="time-timer-back"></div>
            <div class="fold_button"></div>
            <div class="inside_fold_button" @click="startTimer"></div>
        </div>
    </div>
</template>

<style scoped>
.main-container {
    display: flex;
    height: 100vh;
    background-color: #C3D2D8;
    display: flex;
    justify-content: center;
}

.box_block {
    position : relative;
    width: 45vh;
    height: 75vh;
    border-radius: 5vh;
    margin: 0 auto;
    box-shadow: 1.35vh 1.61vh 0 0 rgba(0, 0, 0, 0.1);
    background-color: #357994;
    display: grid;
    place-items: center;
}

.STUDIE-TIME-TIMER {
    margin-top : -5vh;
    font-family: HeadlineR-HM;
    font-size: 2vh;
    font-weight: normal;
    font-stretch: normal;
    font-weight : bold;
    color: #fad9d2;
    z-index : 300;
}

.time{
    position : absolute;
    margin-top : -50vh;
    font-family: HeadlineR-HM;
    font-size: 2vh;
    font-weight: bold;
    color: #000;
    z-index : 10;
}

.time-timer-normal-red{
  position : absolute;
  width: 20vh;
  height: 20vh;
  margin-top : -25vh;
  border-radius: 150px;
  background-color: #fb534b;
  z-index : 5;
}

.time-timer-red{
    position: absolute;
    width: 20vh;
    height: 20vh;
    margin-top : -25vh;
    z-index : 5;
}

.time-timer-white{
    position : absolute;
    width: 5vh;
    height: 5vh;
    margin-top : -25vh;
    border-radius: 150px;
    border: solid 1px #454851;
    background-color: #fff;
    z-index : 7;
}

.time-timer-back {
    position : absolute;
    margin-top : -26vh;
    width: 30.5vh;
    height: 30.5vh;
    border-radius: 50px;
    border: solid 30px #f0f0f0;
    background-color: #fff;
}

.time-timer-border {
    position : absolute;
    margin-top : -26vh;
    width: 34vh;
    height: 34vh;
    border-radius: 50px;
    border: solid 15px #454851;
    z-index : 2;
}

.fold_button{
    width: 20vh;
    height: 20vh;
    margin-top : 30vh;
    box-shadow: inset 8.4px 10px 0 0 #28657c;
    border: solid 5px #1f5565;
    border-radius : 150px;
    background-color: #317089;
}
  
.inside_fold_button{
    position : absolute;
    width: 10vh;
    height: 10vh;
    margin-top : 42vh;
    border: solid 2px #1f5565;
    border-radius : 150px;
    background-color: #317089;
}
</style>

<script>
const WIDTH = 100;
const HEIGHT = 100;
const RADIUS = 50;
const CX = WIDTH / 2;
const CY = HEIGHT / 2;

export default {
  data() {
    return {
      time: 0,  // 초기화
      timeInput: '',
      intervalId: null,
      pathD: '',
    };
  },
  mounted() {
    this.updatePathD();
  },
  methods: {
  updatePathD() {
    const fraction = this.time / (this.timeInput * 60);
    const endX = CX + RADIUS * Math.sin(Math.PI * 2 * fraction);
    const endY = CY - RADIUS * Math.cos(Math.PI * 2 * fraction);
    const largeArcFlag = fraction <= 0.5 ? 0 : 1;
    this.pathD = `
      M ${CX} ${CY}
      L ${CX} 0
      A ${RADIUS} ${RADIUS} 0 ${largeArcFlag} 1 ${endX} ${endY}
      Z
    `;
  },
  startTimer() {
    // 분을 초로 변환
    this.time = this.timeInput * 60;
    const startTime = Date.now();
    const element = document.querySelector(".time-timer-normal-red");
    // 타이머 시작
    this.updatePathD();
    if (element) {
      element.style.display = "none";
    }
    this.intervalId = setInterval(() => {
      const elapsedTime = Math.round((Date.now() - startTime) / 1000);
      this.time = Math.max(this.timeInput * 60 - elapsedTime, 0);
      this.updatePathD();
      if (this.time === 0) {
        clearInterval(this.intervalId);
        if (element) {
          element.style.display = "block";
        }
        setInterval(()=>{
          var snd = new Audio("data:audio/wav;base64,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qJrx4KOQjahZxWbcZgztj2c49nKmkId44S71j0c8eV9yDK6uPRzx5X18eDvjvQ6yKo9ZSS6l//8elePK/Lf//IInrOF/FvDoADYAGBMGb7FtErm5MXMlmPAJQVgWta7Zx2go+8xJ0UiCb8LHHdftWyLJE0QIAIsI+UbXu67dZMjmgDGCGl1H+vpF4NSDckSIkk7Vd+sxEhBQMRU8j/12UIRhzSaUdQ+rQU5kGeFxm+hb1oh6pWWmv3uvmReDl0UnvtapVaIzo1jZbf/pD6ElLqSX+rUmOQNpJFa/r+sa4e/pBlAABoAAAAA3CUgShLdGIxsY7AUABPRrgCABdDuQ5GC7DqPQCgbbJUAoRSUj+NIEig0YfyWUho1VBBBA//uQZB4ABZx5zfMakeAAAAmwAAAAF5F3P0w9GtAAACfAAAAAwLhMDmAYWMgVEG1U0FIGCBgXBXAtfMH10000EEEEEECUBYln03TTTdNBDZopopYvrTTdNa325mImNg3TTPV9q3pmY0xoO6bv3r00y+IDGid/9aaaZTGMuj9mpu9Mpio1dXrr5HERTZSmqU36A3CumzN/9Robv/Xx4v9ijkSRSNLQhAWumap82WRSBUqXStV/YcS+XVLnSS+WLDroqArFkMEsAS+eWmrUzrO0oEmE40RlMZ5+ODIkAyKAGUwZ3mVKmcamcJnMW26MRPgUw6j+LkhyHGVGYjSUUKNpuJUQoOIAyDvEyG8S5yfK6dhZc0Tx1KI/gviKL6qvvFs1+bWtaz58uUNnryq6kt5RzOCkPWlVqVX2a/EEBUdU1KrXLf40GoiiFXK///qpoiDXrOgqDR38JB0bw7SoL+ZB9o1RCkQjQ2CBYZKd/+VJxZRRZlqSkKiws0WFxUyCwsKiMy7hUVFhIaCrNQsKkTIsLivwKKigsj8XYlwt/WKi2N4d//uQRCSAAjURNIHpMZBGYiaQPSYyAAABLAAAAAAAACWAAAAApUF/Mg+0aohSIRobBAsMlO//Kk4soosy1JSFRYWaLC4qZBYWFRGZdwqKiwkNBVmoWFSJkWFxX4FFRQWR+LsS4W/rFRb/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////VEFHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAU291bmRib3kuZGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjAwNGh0dHA6Ly93d3cuc291bmRib3kuZGUAAAAAAAAAACU=");
          snd.play(); 
        }, 1000)
        alert("Time is over")
      }
    }, 1000);
  },
  },
  beforeDestroy() {
    clearInterval(this.intervalId);
  },
};
</script>

