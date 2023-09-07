document.addEventListener("DOMContentLoaded", function() {
    const videoElement = document.getElementById("webcam");
    const loadingElement = document.getElementById("loading");

    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                videoElement.srcObject = stream;
                loadingElement.style.display = 'none'; // 웹캠이 로딩되면 로딩 표시를 숨깁니다.
            })
            .catch(function(err) {
                console.error("웹캠에 접근할 수 없습니다:", err);
                loadingElement.textContent = '웹캠에 접근할 수 없습니다.'; // 에러 메시지를 변경
            });
    } else {
        alert("이 브라우저는 웹캠을 지원하지 않습니다.");
    }
});