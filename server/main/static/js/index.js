document.querySelector('button').addEventListener('click', function() {
    var description = document.getElementById('visionDescription');
    description.style.display = "block"
    if (description.style.maxHeight === "0px" || description.style.maxHeight === "") {
        description.style.maxHeight = description.scrollHeight + "px";
    } else {
        description.style.maxHeight = "0px";
    }
});

// transitionend 이벤트 리스너 추가
document.getElementById('visionDescription').addEventListener('transitionend', function() {
    var description = document.getElementById('visionDescription');
    
    // 애니메이션이 끝나면 display 속성을 변경
    if (description.style.maxHeight === "0px") {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
        description.style.display = 'none';

        

    } else {
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
        description.style.display = 'block';

    }
});
