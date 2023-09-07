function go_signup(){
    // Get the current pathname, e.g., /path/to/login.html
    let path = location.pathname;

    // Replace 'login.html' with 'signup.html'
    let newPath = path.replace('login.html', 'signup.html');

    // Set the new URL
    location.href = location.origin + newPath;
}


function signup(){
    // 회원가입 로직 돌기
    id = document.getElementById('id').value;
    password = document.getElementById('password').value;
    belong = document.getElementById('belong').value;
    local = document.getElementById('local').value;
    fetch('http://localhost:5000/user/register', {
        method : "POST",
        headers : {
            "Content-Type" : "application/josn"
        },
        body: JSON.stringify(
            {
                "id": id,
                "passwd": password,
                "belong": belong,
                "local": local

            }
        )
    }).then((response) => console.log(response));
    signBool = true;
    if(signBool){
        alert("회원가입 되셨습니다!");
        // Get the current pathname, e.g., /path/to/login.html  
        let path = location.pathname;

        // Replace 'login.html' with 'signup.html'
        let newPath = path.replace('signup.html', 'login.html');

        // Set the new URL
        location.href = location.origin + newPath;
}



}

function login(){
    localStorage.setItem('isLoggedIn', true)
    let path = location.pathname;

    // Replace 'login.html' with 'signup.html'
    let newPath = path.replace('login.html', 'index.html');

    // Set the new URL
    location.href = location.origin + newPath;
}