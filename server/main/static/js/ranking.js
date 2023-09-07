document.addEventListener("DOMContentLoaded", function() {
    loadRankingByCategory();  // Initial load
});

function loadRankingByCategory() {
    const category = document.getElementById("category").value;
    const recordList = document.getElementById("recordList");

    recordList.innerHTML = "";  // Clear the current list

    // Using Promise.all to wait for all fetch requests to complete
    Promise.all([
        fetch('/rank/belong').then(response => response.json()),
        fetch('/rank/local').then(response => response.json()),
        fetch('/rank/personal').then(response => response.json())
    ]).then(([belongData, localData, personalData]) => {
        const rankings = {
            "belong": belongData,
            "local": localData,
            "general": personalData
        };

        const currentRankings = rankings[category];

        currentRankings.forEach((record, index) => {
            const li = document.createElement("li");
            if(record.name === undefined){
                li.textContent = `${index + 1}. ${record.id} - ${record.ranking}st` ;
            }else{
                li.textContent = `${index + 1}. ${record.name} - ${record.ranking} st`;
            }


            // Add special class for top 3
            if(index === 0) li.classList.add("top1");
            else if(index === 1) li.classList.add("top2");
            else if(index === 2) li.classList.add("top3");

            recordList.appendChild(li);
        });
    });
}