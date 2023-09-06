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