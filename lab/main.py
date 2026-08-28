import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from dotenv import load_dotenv
import psycopg
import logging 

logging.basicConfig(level=logging.INFO)

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
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT name FROM models")
        rows = cur.fetchall()
        conn.close()
        logging.info(f"Served {len(rows)} models")
        return {"models": [row[0] for row in rows]}
    except Exception as e:
        logging.error(f"Failed to fetch models: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch models")

@app.get("/datasets")
def get_datasets():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, filename FROM datasets")
        rows = cur.fetchall()
        conn.close()
        logging.info(f"Served {len(rows)} datasets")
        return {"datasets": [{"id": row[0], "filename": row[1]} for row in rows]}
    except Exception as e:
        logging.error(f"Failed to fetch datasets: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch datasets")

@app.get("/datasets/{dataset_id}/preview")
def get_dataset_preview(dataset_id: int):
    conn = get_connection() 
    cur = conn.cursor() 
    cur.execute("SELECT filename FROM datasets WHERE id = %s", (dataset_id,))
    row = cur.fetchone() 
    conn.close() 

    filepath = os.path.join("datasets", row[0])

    if not os.path.exists(filepath):
        logging.warning(f"Dataset file not found: {filepath}")
        raise HTTPException(status_code=404, detail="Dataset file not found")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        logging.info(f"Served preview for dataset {dataset_id} ({row[0]})")
    except Exception as e:
        logging.error(f"Failed to read {filepath}: {e}")
        raise HTTPException(status_code=500, detail="Could not read dataset file")

    words = text.split()
    preview = " ".join(words[:300])
    return {"filename": row[0], "preview": preview}

@app.get("/datasets/{dataset_id}/stats")
def get_dataset_stats(dataset_id: int):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT word_count, unique_words, top_words FROM dataset_stats WHERE dataset_id = %s", (dataset_id,))
        row = cur.fetchone()
        conn.close()
        if row is None:
            raise HTTPException(status_code=404, detail="No stats found for this dataset")
        logging.info(f"Served stored stats for dataset {dataset_id}")
        return {"word_count": row[0], "unique_words": row[1], "top_words": row[2]}
    except Exception as e:
        logging.error(f"Failed to fetch stats for dataset {dataset_id}: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch dataset stats")
    
@app.get("/experiments")
def get_experiments():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT description FROM experiments")
        rows = cur.fetchall()
        conn.close()
        logging.info(f"Served {len(rows)} experiments")
        return {"experiments": [row[0] for row in rows]}
    except Exception as e:
        logging.error(f"Failed to fetch experiments: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch experiments")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)   