# Architecture — Current State

Living document. Update this every time a layer is added — it should always reflect what's **actually built**, not what's planned (planned lives in [[03-Roadmap]]).

Governed by [[01-Philosophy]] hard rule 7 (one layer below current abstraction) and rule 8 (earn every layer).

## Status: V0.1 through V0.6 complete

`lab/index.html`: doctype/html/head/title/body/h1 skeleton, three `<section>`s (Models/Datasets/Experiments — not arbitrary, each maps to a later roadmap version, see [[04-Decisions]] 2026-08-27, each with `<h2>` + an empty `<ul>`) wrapped in a `<div class="sections">`, a `<button>`, and `<script src="script.js">` at the end of `<body>`. `lab/style.css` covers box model, margin collapsing, class/type/pseudo-class selectors, cascade/specificity/inheritance, typography + `rem` units, flexbox, `position: fixed`, media queries, hover transitions. `lab/script.js`: variables/types/arrays/objects, loops, functions, DOM manipulation, events/delegation, and now `async`/`await`/`fetch()` — `loadModels()`/`loadDatasets()`/`loadExperiments()` fetch all three sections from the live backend and render via the shared `renderList`. Zero hardcoded frontend data remains. Taught chunk-by-chunk per [[01-Philosophy]] hard rule 2; concepts logged in [[05-Concepts]].

`lab/server.py` (2026-08-24): a raw Python backend using only the standard-library `http.server` module — kept as-is, not deleted, as a deliberate "before" reference to contrast against FastAPI. Not the live backend — superseded by `main.py`.

`lab/main.py` (2026-08-25, refactored 2026-08-27): the live backend. `FastAPI()` app with three decorator-routed endpoints (`/models`, `/datasets`, `/experiments`), each returning a plain dict auto-serialized to JSON. `CORSMiddleware` allowing `http://127.0.0.1:5500` (the Live Server origin `index.html` is served from) to fetch cross-origin. Auto-generated docs at `/docs`. Each route opens a real PostgreSQL connection via a shared `get_connection()` function (extracted 2026-08-27, same pattern as the earlier `renderList` extraction — the previously-deferred cleanup from [[01-Philosophy]] "Refactor timing"), runs a `SELECT`, and returns real rows — no hardcoded data left in any route, no duplicated connection code left either. Verified post-refactor by actually starting the server (venv's `uvicorn.exe` directly, since it isn't on global PATH) and hitting all three routes with `curl`, confirming identical real data to before the change. Run via `uvicorn main:app --reload` on `localhost:8000`.

**PostgreSQL** (2026-08-25, already installed/running as a Windows service before this project needed it): dedicated `ai_research_lab` database, three tables — `models(id SERIAL PRIMARY KEY, name TEXT NOT NULL)`, `datasets(id, filename)`, `experiments(id, description)` — each with a B-tree index auto-created on its primary key. Seeded with the same data that used to be hardcoded in `main.py`. Verified as the real data source (not cached/hardcoded) by inserting a row directly via `psql` while the server was running and confirming it appeared in the API response with zero code changes.

**Migrations** (V0.6, 2026-08-27/28): `lab/migrations/` holds numbered, version-controlled `.sql` files — `0001_init.sql` (the three `CREATE TABLE` statements, reverse-engineered from the live schema via `information_schema` since the tables already existed by hand) and `0002_add_experiment_foreign_keys.sql` (adds `experiments.model_id REFERENCES models(id)` and `experiments.dataset_id REFERENCES datasets(id)`). Both hand-run, no framework yet (raw layer first, per hard rule 7 — Alembic/Flyway only gets introduced once manually tracking "which migration number has already run" becomes genuinely painful). Both tested against a throwaway `migration_test` database before being run for real via `psql.exe -f` against `ai_research_lab`, then verified again by querying `information_schema` directly. Existing experiment rows were backfilled with real `model_id`/`dataset_id` values via `UPDATE`, then a `JOIN` across all three tables confirmed the relationships resolve correctly. Indexes and transactions (the rest of V0.6's concept checklist) were demonstrated in the Sandbox, not added to the real tables — see [[07-Sandbox-Log]] and [[01-Philosophy]] hard rule 3 (no tables here are large enough yet to need an index; no route yet does a multi-step write that would need a transaction).

**Seed data** (2026-08-28): `lab/seed.sql` — plain `INSERT` statements for the same models/datasets/experiments rows every machine has been manually typing so far. Deliberately kept separate from `lab/migrations/` (seed data is a different concern from schema — a migration runner shouldn't auto-replay seed inserts against a real database). Not idempotent, run once via `psql -f seed.sql` on a freshly-migrated empty database. Written after the gap it closes was actually felt twice (once predicted in the vault, once for real setting up the desktop machine) rather than pre-built speculatively.

## Current stack

| Layer | Technology | Status |
|---|---|---|
| Frontend | static HTML + CSS + JS, all three sections `fetch()`ing the backend | V0.1 + V0.2 complete; connected to real, persisted backend data as of V0.5. |
| Backend | FastAPI (`lab/main.py`), raw `http.server` kept as reference (`lab/server.py`) | V0.3-V0.6 complete — three routes, decorator routing, auto JSON, CORS configured, real DB-backed persistence, `get_connection()` refactor done (2026-08-27). Next: V0.7 (Dataset Explorer) — see [[08-Next-Step]] |
| Database | PostgreSQL 17, `ai_research_lab` database, 3 tables + FK relationships | V0.5 + V0.6 complete — real persistence, schema now version-controlled as migrations in `lab/migrations/`, `experiments` has real foreign keys to `models`/`datasets`, backfilled and join-verified. Indexes/transactions understood via Sandbox, not yet needed on real tables. |
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
