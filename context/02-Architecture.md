# Architecture — Current State

Living document. Update this every time a layer is added — it should always reflect what's **actually built**, not what's planned (planned lives in [[03-Roadmap]]).

Governed by [[01-Philosophy]] hard rule 7 (one layer below current abstraction) and rule 8 (earn every layer).

## Status: V0.1 through V0.8's core loop complete

`lab/index.html`: doctype/html/head/title/body/h1 skeleton, three `<section>`s (Models/Datasets/Experiments — not arbitrary, each maps to a later roadmap version, see [[04-Decisions]] 2026-08-27, each with `<h2>` + an empty `<ul>`) wrapped in a `<div class="sections">`, a `<button>`, and `<script src="script.js">` at the end of `<body>`. `lab/style.css` covers box model, margin collapsing, class/type/pseudo-class selectors, cascade/specificity/inheritance, typography + `rem` units, flexbox, `position: fixed`, media queries, hover transitions. `lab/script.js`: variables/types/arrays/objects, loops, functions, DOM manipulation, events/delegation, and now `async`/`await`/`fetch()` — `loadModels()`/`loadDatasets()`/`loadExperiments()` fetch all three sections from the live backend and render via the shared `renderList`. Zero hardcoded frontend data remains. Taught chunk-by-chunk per [[01-Philosophy]] hard rule 2; concepts logged in [[05-Concepts]].

`lab/server.py` (2026-08-24): a raw Python backend using only the standard-library `http.server` module — kept as-is, not deleted, as a deliberate "before" reference to contrast against FastAPI. Not the live backend — superseded by `main.py`.

`lab/main.py` (2026-08-25, refactored 2026-08-27): the live backend. `FastAPI()` app with three decorator-routed endpoints (`/models`, `/datasets`, `/experiments`), each returning a plain dict auto-serialized to JSON. `CORSMiddleware` allowing `http://127.0.0.1:5500` (the Live Server origin `index.html` is served from) to fetch cross-origin. Auto-generated docs at `/docs`. Each route opens a real PostgreSQL connection via a shared `get_connection()` function (extracted 2026-08-27, same pattern as the earlier `renderList` extraction — the previously-deferred cleanup from [[01-Philosophy]] "Refactor timing"), runs a `SELECT`, and returns real rows — no hardcoded data left in any route, no duplicated connection code left either. Verified post-refactor by actually starting the server (venv's `uvicorn.exe` directly, since it isn't on global PATH) and hitting all three routes with `curl`, confirming identical real data to before the change. Run via `uvicorn main:app --reload` on `localhost:8000`.

**PostgreSQL** (2026-08-25, already installed/running as a Windows service before this project needed it): dedicated `ai_research_lab` database, three tables — `models(id SERIAL PRIMARY KEY, name TEXT NOT NULL)`, `datasets(id, filename)`, `experiments(id, description)` — each with a B-tree index auto-created on its primary key. Seeded with the same data that used to be hardcoded in `main.py`. Verified as the real data source (not cached/hardcoded) by inserting a row directly via `psql` while the server was running and confirming it appeared in the API response with zero code changes.

**Migrations** (V0.6, 2026-08-27/28): `lab/migrations/` holds numbered, version-controlled `.sql` files — `0001_init.sql` (the three `CREATE TABLE` statements, reverse-engineered from the live schema via `information_schema` since the tables already existed by hand) and `0002_add_experiment_foreign_keys.sql` (adds `experiments.model_id REFERENCES models(id)` and `experiments.dataset_id REFERENCES datasets(id)`). Both hand-run, no framework yet (raw layer first, per hard rule 7 — Alembic/Flyway only gets introduced once manually tracking "which migration number has already run" becomes genuinely painful). Both tested against a throwaway `migration_test` database before being run for real via `psql.exe -f` against `ai_research_lab`, then verified again by querying `information_schema` directly. Existing experiment rows were backfilled with real `model_id`/`dataset_id` values via `UPDATE`, then a `JOIN` across all three tables confirmed the relationships resolve correctly. Indexes and transactions (the rest of V0.6's concept checklist) were demonstrated in the Sandbox, not added to the real tables — see [[07-Sandbox-Log]] and [[01-Philosophy]] hard rule 3 (no tables here are large enough yet to need an index; no route yet does a multi-step write that would need a transaction).

**Seed data** (2026-08-28): `lab/seed.sql` — plain `INSERT` statements for the models/datasets/experiments rows every machine has been manually typing so far. Deliberately kept separate from `lab/migrations/` (seed data is a different concern from schema — a migration runner shouldn't auto-replay seed inserts against a real database). Not idempotent, run once via `psql -f seed.sql` on a freshly-migrated empty database. Written after the gap it closes was actually felt twice (once predicted in the vault, once for real setting up the desktop machine) rather than pre-built speculatively. Kept in sync with the real seed data as it changed (dataset filenames, then model names) rather than left to drift.

**V0.7 — Dataset Explorer** (2026-08-28): `lab/datasets/` holds three real public-domain texts — `peter_rabbit.txt`, `alice_in_wonderland.txt`, `wizard_of_oz.txt` — downloaded from Project Gutenberg, license headers intact, committed to the repo (not gitignored — this is real app data, not a machine-specific secret). `datasets` rows updated to point to them (was `harrypotter.txt`-style placeholders). New route `GET /datasets/{dataset_id}/preview` in `lab/main.py`: path parameter → `SELECT filename FROM datasets WHERE id = %s` (parameterized, never raw string interpolation) → `os.path.exists` check (`404` if missing) → `open()`/`.read()` wrapped in `try`/`except` (`500` on unexpected read failure) → first 300 words joined back into a string. `logging` (`info`/`warning`/`error`) plus `try`/`except` → clean error responses were extended to **all four** routes, not just the new one, once the underlying DB-failure risk was recognized as universal, not preview-specific. `/datasets` itself changed shape — now returns `{id, filename}` objects instead of bare filename strings, since the frontend needs the `id` to know which dataset was clicked. Frontend (`lab/script.js`): a new `renderDatasetList` (kept separate from the shared `renderList`, which stayed string-only for Models/Experiments after briefly breaking them by overloading the shared function), each rendered `<li>` carrying `data-id`; one delegated click listener on `.datasets-list` reads `event.target.dataset.id`, fetches the preview, and writes it into a new `<div class="preview">` in `index.html`. `models` seed data was also realigned from CNN names (`ResNet`/`AlexNet`) to the actual NLP roadmap track (`RNN`/`LSTM`/`Transformer`/`GPT`) — see [[04-Decisions]]. Known, deliberately deferred gap: no `conn.close()`-on-exception fix yet (a connection leak on the error path) — see [[09-Ideas-Backlog]].

**V0.8 — Pandas + EDA** (2026-08-28/29): `lab/eda.py` — `analyze_dataset(filepath)` returns `{filename, word_count, unique_words}` (`os.path.basename`, `.split()`, `len(set(...))`); `top_words(text, n=10)` uses `re.findall(r"\b\w+\b", text.lower())` + `collections.Counter` to get frequency-ranked words, case/punctuation-normalized; `clean_gutenberg_text(text)` uses `str.find()` + slicing to strip Gutenberg's license header/footer before any analysis runs — added after discovering the raw boilerplate was inflating every stat. All script-level demo code (the 3-file comparison loop, both `plt.show()` calls) lives inside `if __name__ == "__main__":`, so importing this module doesn't execute any of it. New route `GET /datasets/{dataset_id}/stats` in `main.py`: `from eda import analyze_dataset, top_words, clean_gutenberg_text` (first local-module import in this project, not just installed packages), same DB-lookup/error-handling shape as `/preview`, returns `{filename, word_count, unique_words, top_words}` as JSON. Frontend: new `<div class="stats">`, the existing dataset click handler extended to fetch and display both `/preview` and `/stats` together. Dependencies: `pandas`, `matplotlib`, and their transitive packages — see [[06-Dependencies]].

## Current stack

| Layer | Technology | Status |
|---|---|---|
| Frontend | static HTML + CSS + JS, all three sections `fetch()`ing the backend, dataset previews + stats on click | V0.1 + V0.2 complete; connected to real, persisted backend data as of V0.5; real per-dataset preview UI as of V0.7; real EDA stats display as of V0.8. |
| Backend | FastAPI (`lab/main.py`), raw `http.server` kept as reference (`lab/server.py`) | V0.3-V0.8 complete — five routes (incl. file-backed preview and Pandas-backed stats), decorator routing, auto JSON, CORS configured, real DB-backed persistence, logging + error handling across all routes. Next: V0.9 (ETL) or continue polishing V0.8 — see [[08-Next-Step]] |
| Database | PostgreSQL 17, `ai_research_lab` database, 3 tables + FK relationships | V0.5 + V0.6 complete — real persistence, schema now version-controlled as migrations in `lab/migrations/`, `experiments` has real foreign keys to `models`/`datasets`, backfilled and join-verified. Indexes/transactions understood via Sandbox, not yet needed on real tables. Seed data (models/datasets) realigned to real files and the NLP roadmap track as of V0.7. |
| Data analysis | Pandas + matplotlib (`lab/eda.py`) | V0.8 core complete — per-dataset word count/unique words/top words, cleaned of Gutenberg boilerplate, importable as a module (not just a standalone script), wired into a real API route. |
| Cache | none yet | not started |
| Queue / Workers | none yet | not started |
| Training / Inference | none yet | not started |
| DevOps / Deployment | none yet | not started |

See [[06-Dependencies]] for the installed-package record once it starts filling in.

## Planned folder layout (created when V0.1 starts, not before)

```
Project/
  context/     <- this vault (already exists)
  lab/         <- AI Research Lab application code
  sandbox/     <- Learning Sandbox experiments (see [[07-Sandbox-Log]])
```

## Diagram (target end-state, from [[01-Philosophy]] success criterion)

```
Browser → DOM → JavaScript → HTTP → Backend → Database → Cache → Queue → Worker → GPU → Model
```

Each arrow above becomes real (and gets its own section here) as the corresponding roadmap version in [[03-Roadmap]] is reached.
