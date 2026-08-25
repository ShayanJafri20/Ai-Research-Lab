const button = document.querySelector("button")
button.addEventListener("click", (event) => {
    console.log("button was clicked :)")
    if (button.textContent === "Refresh") {
    button.textContent = "Refreshed!"
    }
    else {
    button.textContent = "Refresh"
    }

    
    button.classList.toggle("clicked")  
})

async function loadModels() {
    const response = await fetch("http://127.0.0.1:8000/models")
    const data = await response.json();
    renderList(data.models.map(describeModelNames), modelList);
}

async function loadDatasets() {
    const response = await fetch("http://127.0.0.1:8000/datasets");
    const data = await response.json();
    renderList(data.datasets, datasetlist);
}

async function loadExperiments() {
    const response = await fetch("http://127.0.0.1:8000/experiments");
    const data = await response.json();
    renderList(data.experiments, experimentsList);
}

function describeModelNames(name) {
    return `Model: ${name}`;
}

const modelList = document.querySelector(".model-list");
modelList.addEventListener("click", (event) => {
  console.log("You clicked:", event.target.textContent);
});

const datasetlist = document.querySelector(".datasets-list")
const experimentsList = document.querySelector(".experiments-list");

function renderList(items, container) { 
    for (const item of items) { 
        const li = document.createElement("li"); 
        li.textContent = item; 
        container.appendChild(li)
    }
}

loadModels();
loadDatasets();
loadExperiments();