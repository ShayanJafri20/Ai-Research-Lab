-- Seed data for a freshly-migrated ai_research_lab database.
-- Run once, after both migrations, on an empty database:
--   psql -h localhost -U postgres -d ai_research_lab -f seed.sql
-- Not idempotent (same as the migrations) - running this twice against an
-- already-seeded database will insert duplicate rows, not update existing ones.

-- NLP-track models, matching the roadmap's actual ML sequence (V1.0-V1.3);
-- CNN/vision models don't belong here - that's a separate, later track (see 01-Philosophy).
INSERT INTO models (name) VALUES ('RNN'), ('LSTM'), ('Transformer'), ('GPT');

-- All three are now real files under lab/datasets/, as of V0.7's Dataset Explorer work.
INSERT INTO datasets (filename) VALUES ('peter_rabbit.txt'), ('alice_in_wonderland.txt'), ('wizard_of_oz.txt');

INSERT INTO experiments (description, model_id, dataset_id) VALUES
    ('Baseline RNN - run 1', 1, 2),
    ('Transformer fine-tune - run 2', 3, 1),
    ('Hyperparameter sweep - run 3', 4, 3);
