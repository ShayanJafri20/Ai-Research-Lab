-- Seed data for a freshly-migrated ai_research_lab database.
-- Run once, after both migrations, on an empty database:
--   psql -h localhost -U postgres -d ai_research_lab -f seed.sql
-- Not idempotent (same as the migrations) - running this twice against an
-- already-seeded database will insert duplicate rows, not update existing ones.

INSERT INTO models (name) VALUES ('ResNet'), ('AlexNet'), ('Transformer'), ('GPT');

INSERT INTO datasets (filename) VALUES ('harrypotter.txt'), ('apple/oranges.txt'), ('BeyondGoodandEvil.txt');

INSERT INTO experiments (description, model_id, dataset_id) VALUES
    ('Baseline CNN - run 1', 1, 2),
    ('Transformer fine-tune - run 2', 3, 1),
    ('Hyperparameter sweep - run 3', 4, 3);
