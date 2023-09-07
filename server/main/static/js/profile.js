function logout(){
    fetch('/user/logout', {
        method : "GET"
    }).then((response) => {
        return response.json();
    }).then(data => {
        
            location.href = "/user/login";

    });
    
}

function loadProfile(){
    fetch('/user/myinfo')
    .then(response => {
        return response.json();
    })
    .then(data => {
        document.getElementById('userId').innerText = "아이디 : " + data.id
        document.getElementById('userLocation').innerText = "지역 : " + data.local
        document.getElementById('userBelong').innerText = "소속 : " + data.belong

        if(data.point == null){
            document.getElementById('userPoint').innerText = "포인트 : 0"
        }else{
            document.getElementById('userPoint').innerText = "포인트 : " + data.point
        }
        
    })
    .catch(error => {
        console.error(error);
    })
}

function editProfile(){
    alert("추후 지원할 예정입니다!")
}


document.addEventListener("DOMContentLoaded", function() {
    loadProfile();  // Initial load
});