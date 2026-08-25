from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()
@app.get("/models")
def get_models():
    return {"models": ["ResNet","AlexNet","Transformer"]}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)   