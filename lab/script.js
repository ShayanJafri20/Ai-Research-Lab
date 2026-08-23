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


const models = ["ResNet", "AlexNet", "Transformer"];

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

renderList(models.map(describeModelNames), modelList) 
renderList(dataset, datasetlist) 
renderList(experiments, experimentsList)

const [first, second, third] = models;
console.log(first); // "ResNet"

const model = { name: "ResNet", accuracy: 0.92 };
const { name, accuracy } = model;
console.log(name, accuracy);

const newModels = [...models, "GPT"];
console.log(newModels); // ["ResNet", "AlexNet", "Transformer", "GPT"]
console.log(models);    // still just the original 3 - untouched

function addModels(...newOnes) {
  return [...models, ...newOnes];
}
console.log(addModels("GPT", "BERT"));