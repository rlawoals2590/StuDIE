<template>
    <div class="main-container">
        <nav class="display-box">
            <router-link to="/"> <h1 class="neon-sign-pink title">STUDIE 타임 타이머 ⏰</h1> </router-link>
        </nav>

        <main>
            <div class="content">
                <!-- 타이머 시작 -->
                <div class="box_block display-box">
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
                
        
                <!-- 타이머 끝 -->

                <!-- 설명 시작 -->
                <div class="display-box description-box">
                    <h1 class="title">타임 타이머란? </h1>
                    <p>
                        타임 타이머는 구글에서 인기를 얻어 간편하고 효과적인 시간 관리 도구로 유명해졌습니다. 이 도구는 짧은 시간(60분) 동안 작업에 몰입할 수 있도록 도와주며, 빨간색과 같은 시각적인 효과를 활용하여 눈에 띄게 시간을 줄여가는 기능을 갖추고 있습니다. 이러한 디자인은 마치 데드라인이 점점 다가온다는 느낌을 주며, 사용자에게 깊은 집중을 이끌어내는 데 도움을 줍니다.
                    </p>
                    <p>
                        타임 타이머의 간결하고 직관적인 인터페이스로 인해 누구나 쉽게 활용할 수 있으며, 전문성 있는 시간 관리를 원하는 사용자들에게도 만족스러운 경험을 제공합니다. 이 도구를 사용하면 시간을 효율적으로 활용하여 업무나 공부 등의 목표를 달성하는 데 도움이 될 것입니다. 집중력을 높이고 싶은 모든 분들에게 친근하고 신뢰할 수 있는 시간 관리 도구로서 추천드립니다.
                    </p>
                </div>
                <!-- 설명 끝 -->
            </div>
        </main>

        <footer>
            <p>© 2023 NewEye. All rights reserved.</p>
        </footer>
    </div>
</template>

<style scoped>


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
@import url('../assets/global.css');
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

      }

      
    }, 1000);
    

  },
  },
  beforeDestroy() {
    
      clearInterval(this.intervalId);

  },
};
</script>

