const button = document.querySelector("button")
button.addEventListener("click", () => {
    console.log("button was clicked :)")
    if (button.textContent === "Refresh") {
    button.textContent = "Refreshed!"
    }
    else {
    button.textContent = "Refresh"
    }
})

const models = ["ResNet", "AlexNet", "Transformer"];

function describeModelNames(name) {
    return `Model: ${name}`;
}

const modelList = document.querySelector(".model-list");
for (const model of models){
    const item = document.createElement("li"); 
    item.textContent = describeModelNames(model);
    modelList.appendChild(item);
}

const dataset = ["harrypotter.txt", "apple/oranges.txt", "BeyondGoodandEvil.txt"]
const datasetlist = document.querySelector(".datasets-list")
for (const data of dataset)
{
    const item = document.createElement("li")
    item.textContent = data
    datasetlist.append(item);
}

const experiments = ["Baseline CNN - run 1", "Transformer fine-tune - run 2", "Hyperparameter sweep - run 3"];
const experimentsList = document.querySelector(".experiments-list");
for (const experiment of experiments) {
    const item = document.createElement("li");
    item.textContent = experiment;
    experimentsList.appendChild(item);
}