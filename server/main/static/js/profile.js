function logout(){
    fetch('/user/logout', {
        method : "GET"
    }).then((response) => {
        return response.json();
    }).then(data => {
        
            location.href = "/user/login";
            
    });
    
}

function editProfile(){
    alert("추후 지원할 예정입니다!")
}