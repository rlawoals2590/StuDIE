<template>
    <div class="main-container">
        <nav class="display-box">
            <a href="/"> <h1 class="neon-sign-pink title">스터다이 타임 타이머 ⏰</h1> </a>
        </nav>

        <main>
            <div class="content">
                <!-- 타이머 시작 -->
                <div class="display-box">
                    <h1 class="title"> 타임 타이머 </h1>
                    <div id="timer">
                        <svg class="progress-ring" width="30vw" height="30vw">
                            <circle class="progress-ring__circle"
                                    stroke="red"
                                    stroke-width="10"
                                    fill="transparent"
                                    r="14vw"
                                    cx="15vw"
                                    cy="15vw"
                                    :style="circleStyle"
                            ></circle>

                        </svg>
                        <div id="timer-display">
                            <span>{{ minutes }} 분 {{ seconds }} 초 남았습니다!</span>
                        </div>
                        <div id="timer-controls">
                            <div id="input-container">
                                <input type="number" id="minutes" v-model="inputMinutes" @input="setTime" :disabled="isTimerRunning" :class="{ disabled: isTimerRunning }">
                                <label for="minutes">분</label>
                            </div>
                            <div class="button-div">
                            <button @click="startTimer">시작</button>
                            <button @click="resetTimer">리셋</button>
                            </div>
                        </div>
                    </div>
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

<script>
export default{
    data() {
        return {
            totalSeconds: 0,
            seconds: 0,
            minutes: 0,
            timer: null,
            inputMinutes: 0,
            strokeDashoffset: 0,
            strokeDasharray: 0,
            radius: 0,
            isTimerRunning: false,
        }
    },
    mounted() {
        this.radius = window.innerWidth * 0.14;
        this.strokeDasharray = 2 * Math.PI * this.radius;
    },
    computed: {
        circleStyle() {
            return {
                strokeDasharray: this.strokeDasharray,
                strokeDashoffset: this.strokeDashoffset
            }
        }
    },
    methods: {
        setTime() {
            this.totalSeconds = this.inputMinutes * 60;
            this.minutes = this.padTime(Math.floor(this.totalSeconds / 60));
            this.seconds = this.padTime(this.totalSeconds % 60);
        },
        startTimer() {
            this.isTimerRunning = true;
            this.runTimer();
        },
        resetTimer() {
            this.isTimerRunning = false;
            this.inputMinutes = 0;
            this.totalSeconds = 0;
            this.minutes = 0;
            this.seconds = 0;
            this.strokeDashoffset = 0;
            clearInterval(this.timer);
        },
        runTimer() {
            this.setTime();
            this.strokeDashoffset = 0;
            clearInterval(this.timer);
            this.timer = setInterval(() => {
                this.totalSeconds--;
                this.minutes = this.padTime(Math.floor(this.totalSeconds / 60));
                this.seconds = this.padTime(this.totalSeconds % 60);
                this.strokeDashoffset = this.strokeDasharray * (1 - this.totalSeconds / (this.inputMinutes * 60));
                if (this.totalSeconds <= 0) {
                    this.isTimerRunning = false;
                    clearInterval(this.timer);
                    alert('시간이 다 되었습니다!');
                }
            }, 1000);
        },
        padTime(time) {
            return (time < 10 ? '0' : '') + time;
        }
    }
}
</script>

<style scoped>
@import url('../assets/global.css');

#timer {
    position: relative;
    width: 30vw;
    height: 30vw;
    margin-bottom: 15vh;
}
.progress-ring {
    position: absolute;
    top: 0;
    left: 0;
    transform: rotate(-90deg);
}

#timer-display {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 30px;
}
.description-box {
    width: 30vw;
}
#timer-controls {
    position: absolute;
    bottom: -13vh;
    left: 50%;
    transform: translate(-50%, 0);
    width: 80%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

#input-container {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

input {
    width: 100%;
    height: 30px;
    border: none;
    font-size: 30px;
    border-radius: 10px;
    padding: 10px;
    outline: none;
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
    color: #eeeeee;
    background-color: #111111;
    border: 1px solid #eeeeee;

}

input.disabled {
    color: #aaa;
}

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

input[type=number] {
    -moz-appearance: textfield;
}

button {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    
    background-color: #111111;
    
    border: 1px solid #eeeeee;
    margin-top: 0.5rem;
    padding: 0.5rem 1rem;
    
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 25px;
    font-weight: 400;
    text-align: center;
    text-decoration: none;
    
    border-radius: 4px;
    color: #eeeeee;
    width: 10rem;
    margin: 30px;
    cursor: pointer;
    transition: all 0.2s;
}

button:hover {
    background-color: #eeeeee;
    color: #111111;
}

label{
    font-size: 30px;

}
p{
    font-size: 20px;
}
</style>
