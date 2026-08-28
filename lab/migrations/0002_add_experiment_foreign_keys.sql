ALTER TABLE experiments ADD COLUMN model_id INTEGER REFERENCES models(id);
ALTER TABLE experiments ADD dataset_id INTEGER REFERENCES datasets(id);