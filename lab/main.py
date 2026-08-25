from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()
@app.get("/models")
def get_models():
    return {"models": ["ResNet","AlexNet","Transformer"]}

@app.get("/datasets")
def get_datasets():
    return {"datasets": ["harrypotter.txt", "apple/oranges.txt", "BeyondGoodandEvil.txt"]}

@app.get("/experiments")
def get_experiments():
    return {"experiments": ["Baseline CNN - run 1", "Transformer fine-tune - run 2", "Hyperparameter sweep - run 3"]}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)   