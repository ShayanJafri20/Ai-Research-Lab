import os 
import json 
from eda import analyze_dataset, top_words, clean_gutenberg_text 
from main import get_connection 

folder = "datasets"
conn = get_connection() 
cur = conn.cursor() 
cur.execute("SELECT id, filename FROM datasets") 
rows = cur.fetchall() 

for dataset_id, filename in rows: 
    filepath = os.path.join(folder, filename)
    stats = analyze_dataset(filepath) 

    with open(filepath, "r", encoding="utf-8") as f: 
        text = clean_gutenberg_text(f.read()) 
    words = top_words(text, n=10) 

    cur.execute(
        "INSERT INTO dataset_stats (dataset_id, word_count, unique_words, top_words) VALUES (%s, %s, %s, %s)", 
    (dataset_id, stats["word_count"], stats["unique_words"], json.dumps(words))
    )

conn.commit()
conn.close() 
print(f"Loaded stats for {len(rows)} datasets")