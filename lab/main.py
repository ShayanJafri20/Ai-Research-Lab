import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from dotenv import load_dotenv
import psycopg

load_dotenv()

app = FastAPI()

def get_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

@app.get("/models")
def get_models():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM models")
    rows = cur.fetchall()
    conn.close()
    return {"models": [row[0] for row in rows]}

@app.get("/datasets")
def get_datasets():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT filename FROM datasets")
    rows = cur.fetchall()
    conn.close()
    return {"datasets": [row[0] for row in rows]}

@app.get("/experiments")
def get_experiments():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT description FROM experiments")
    rows = cur.fetchall()
    conn.close()
    return {"experiments": [row[0] for row in rows]}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)   