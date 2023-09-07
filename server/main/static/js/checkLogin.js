if (window.location.pathname !== '/user/login' && window.location.pathname !== '/') {
    fetch('/user/', {
        method : "GET"
    }).then((response) => {
        return response.json();
    }).then(data => {
        if (data.status === "Authentication failed") {
            location.href = "/user/login";
        } else {
            
                }
    });
}
