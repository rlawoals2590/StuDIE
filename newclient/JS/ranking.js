document.addEventListener("DOMContentLoaded", function() {
    loadRankingByCategory();  // Initial load
});

function loadRankingByCategory() {
    const category = document.getElementById("category").value;
    const recordList = document.getElementById("recordList");
    recordList.innerHTML = "";  // Clear the current list

    // Sample data for demonstration. You'd replace this with actual data or fetch from an API.
    const rankings = {
        general: [
            {name: "이지은", points: 100},
            {name: "이성현", points: 90},
            {name: "윤현우", points: 85},
            {name: "김민성", points: 70},
            {name: "박민성", points: 60},
            {name: "이정범", points: 55},
            {name: "김재민", points: 40}
        ],
        sports: [
            {name: "세명컴고", points: 100},
            {name: "한국디미고", points: 90},
            {name: "선린인고", points: 85},
            {name: "미림소마고", points: 70},

        ],
        arts: [
            {name: "서울특별시", points: 100},
            {name: "경기도", points: 90},
            {name: "강원도", points: 85},
            {name: "경상북도", points: 70},
            {name: "경상남도", points: 60},
        ],
    };

    const currentRankings = rankings[category];

    currentRankings.forEach((record, index) => {
        const li = document.createElement("li");
        li.textContent = `${index + 1}. ${record.name} - ${record.points} points`;

        // Add special class for top 3
        if(index === 0) li.classList.add("top1");
        else if(index === 1) li.classList.add("top2");
        else if(index === 2) li.classList.add("top3");

        recordList.appendChild(li);
    });
}
