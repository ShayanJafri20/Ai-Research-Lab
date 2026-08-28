CREATE TABLE dataset_stats(
    id SERIAL PRIMARY KEY, 
    dataset_id INTEGER REFERENCES datasets(id), 
    word_count INTEGER NOT NULL, 
    unique_words INTEGER NOT NULL, 
    top_words JSONB
)