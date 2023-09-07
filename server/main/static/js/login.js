function go_signup(){
    // 회원가입 버튼
    location.href = "/user/register"
}


function signup(){
    // 회원가입 로직
    id = document.getElementById('id').value;
    password = document.getElementById('password').value;
    belong = document.getElementById('belong').value;
    local = document.getElementById('local').value;
    fetch('/user/register', {
        method : "POST",
        headers : {
            "Content-Type" : "application/json"
        },
        body: JSON.stringify(
            {
                "id": id,
                "passwd": password,
                "belong": belong,
                "local": local

            }
        )
    })  .then(response => {
        // 서버 응답을 JSON 형식으로 파싱
        return response.json();
    })
    .then(data => {
        // 파싱된 데이터를 사용

    })
    .catch(error => {
        // 오류 처리
        console.error('오류 발생:', error);
    });
    
    alert("회원가입이 완료되었습니다");
        location.href = "/user/login"    
    
    



}

function login(){
    // 로그인 로직
    id = document.getElementById('id').value;
    password = document.getElementById('password').value;
    
    const requestData = {
    id: id,
    passwd: password
    };

    fetch('/user/login/', {
    method: 'POST',
    headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestData)
    })
    .then(response => {
    if (!response.ok) {
        throw new Error('서버 응답 오류');
    }
    return response.json();
    })
    .then(data => {
    if(data.status === "Success"){
        location.href="/"
        }else{
            
            alert("아이디 혹은 비밀번호가 틀렸습니다!")
            document.getElementById('id').value = ""
            document.getElementById('password').value = ""
        }
    console.log('응답 데이터:' +  data.status);
    console.log();
    
    })
    .catch(error => {
    console.error('오류 발생:', error);
    });
    
    
}