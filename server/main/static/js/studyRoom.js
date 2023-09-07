totalScore = 0;
document.addEventListener("DOMContentLoaded", function() {
    const videoElement = document.getElementById("webcam");
    const loadingElement = document.getElementById("loading");

    function captureImage() {
        const canvas = document.createElement('canvas');
        canvas.width = videoElement.videoWidth;
        canvas.height = videoElement.videoHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
        const imageData = canvas.toDataURL('image/jpeg');
        sendImageToServer(imageData);
    }

    function getScore(){
        fetch('/room/score/', {
            method : 'GET'
            }).then((response) => {
            return response.json();
            }).then(data => {
                
                document.getElementsByClassName('score')[0].innerText = `현재 : ${data.score}점`
                
                fetch('/room/save/' +  `${data.score - totalScore}`);
                totalScore = data.score
            }).catch(error => {
                console.log(error);
            })

            }

function sendImageToServer(imageData) {
    fetch('/room/upload', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: imageData }),
    }).then((response) => {
        return response.json()
    }).then(data => {
        // console.log(data);
    }).catch(error => {
        // console.err(error);
    });
}

    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                videoElement.srcObject = stream;
                loadingElement.style.display = 'none'; // 웹캠이 로딩되면 로딩 표시를 숨깁니다.

                // 웹캠 스트림이 준비되면, 1초마다 이미지를 캡처하여 서버로 전송
                captureImage();
                setInterval(() => {
                    getScore();
                    captureImage();
                    
                }, 5000);
                
            })
            .catch(function(err) {
                console.error("웹캠에 접근할 수 없습니다:", err);
                loadingElement.textContent = '웹캠에 접근할 수 없습니다.'; // 에러 메시지를 변경
            });
    } else {
        alert("이 브라우저는 웹캠을 지원하지 않습니다.");
    }
});


function saveDB(){
    
}
    
