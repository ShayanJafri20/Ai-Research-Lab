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

function describeModelNames(name) {
    return `Model: ${name}`;
}

const modelList = document.querySelector(".model-list");
modelList.addEventListener("click", (event) => {
  console.log("You clicked:", event.target.textContent);
});

const dataset = ["harrypotter.txt", "apple/oranges.txt", "BeyondGoodandEvil.txt"]
const datasetlist = document.querySelector(".datasets-list")

const experiments = ["Baseline CNN - run 1", "Transformer fine-tune - run 2", "Hyperparameter sweep - run 3"];
const experimentsList = document.querySelector(".experiments-list");

function renderList(items, container) { 
    for (const item of items) { 
        const li = document.createElement("li"); 
        li.textContent = item; 
        container.appendChild(li)
    }
}

loadModels();
renderList(dataset, datasetlist)
renderList(experiments, experimentsList)