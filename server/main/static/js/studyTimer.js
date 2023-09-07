

let interval;
let isRunning = false;
let minutes = 0;
let seconds = 0;

function startTimer() {
    if (!isRunning) {
        isRunning = true;
        interval = setInterval(function() {
            seconds++;
            if (seconds == 60) {
                minutes++;
                seconds = 0;
            }
            document.getElementById("seconds").innerText = seconds < 10 ? "0" + seconds : seconds;
            document.getElementById("minutes").innerText = minutes < 10 ? "0" + minutes : minutes;
        }, 1000);
    }
}

function resetTimer() {
    clearInterval(interval);
    isRunning = false;
    minutes = 0;
    seconds = 0;
    document.getElementById("seconds").innerText = "00";
    document.getElementById("minutes").innerText = "00";
}


function saveRecord() {
    if (minutes > 0 || seconds > 0) {
        const now = new Date();
        const year = now.getFullYear();
        const month = now.getMonth() + 1; // 월은 0부터 시작하므로 1을 더해줍니다.
        const day = now.getDate();
        
        const currentDate = `${year}년 ${month < 10 ? "0" + month : month}월 ${day < 10 ? "0" + day : day}일`;
        const currentRecord = `${currentDate} - ${minutes < 10 ? "0" + minutes : minutes}분 ${seconds < 10 ? "0" + seconds : seconds}초만큼 순공 했습니다`;
        let records = JSON.parse(localStorage.getItem('studyRecords')) || [];
        records.push(currentRecord);
        localStorage.setItem('studyRecords', JSON.stringify(records));

        // 기록을 ul 요소에 추가
        addRecordToList(currentRecord);

        alert("기록이 저장되었습니다!");
        resetTimer();
    } else {
        alert("타이머에 기록된 시간이 없습니다.");
    }
}

// 새로운 기록을 ul 요소에 추가하는 함수
function addRecordToList(record) {
    const recordList = document.getElementById('recordList');
    const li = document.createElement('li');
    li.textContent = record;
    recordList.appendChild(li);
}

// 페이지 로딩 시 저장된 기록들을 불러오는 함수
function loadRecords() {
    let records = JSON.parse(localStorage.getItem('studyRecords')) || [];
    records.forEach(record => addRecordToList(record));
}

// 페이지 로딩 시 기록을 불러오도록 함수 호출
window.onload = loadRecords;
