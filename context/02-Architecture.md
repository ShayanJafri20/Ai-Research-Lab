# Architecture — Current State

Living document. Update this every time a layer is added — it should always reflect what's **actually built**, not what's planned (planned lives in [[03-Roadmap]]).

Governed by [[01-Philosophy]] hard rule 7 (one layer below current abstraction) and rule 8 (earn every layer).

## Status: V0.1 through V0.5 complete

`lab/index.html`: doctype/html/head/title/body/h1 skeleton, three `<section>`s (Models/Datasets/Experiments, each with `<h2>` + an empty `<ul>`) wrapped in a `<div class="sections">`, a `<button>`, and `<script src="script.js">` at the end of `<body>`. `lab/style.css` covers box model, margin collapsing, class/type/pseudo-class selectors, cascade/specificity/inheritance, typography + `rem` units, flexbox, `position: fixed`, media queries, hover transitions. `lab/script.js`: variables/types/arrays/objects, loops, functions, DOM manipulation, events/delegation, and now `async`/`await`/`fetch()` — `loadModels()`/`loadDatasets()`/`loadExperiments()` fetch all three sections from the live backend and render via the shared `renderList`. Zero hardcoded frontend data remains. Taught chunk-by-chunk per [[01-Philosophy]] hard rule 2; concepts logged in [[05-Concepts]].

`lab/server.py` (2026-08-24): a raw Python backend using only the standard-library `http.server` module — kept as-is, not deleted, as a deliberate "before" reference to contrast against FastAPI. Not the live backend — superseded by `main.py`.

`lab/main.py` (2026-08-25): the live backend. `FastAPI()` app with three decorator-routed endpoints (`/models`, `/datasets`, `/experiments`), each returning a plain dict auto-serialized to JSON. `CORSMiddleware` allowing `http://127.0.0.1:5500` (the Live Server origin `index.html` is served from) to fetch cross-origin. Auto-generated docs at `/docs`. Each route now opens a real PostgreSQL connection (`psycopg.connect(...)` using credentials from `os.getenv(...)`, populated via `load_dotenv()` reading `lab/.env`), runs a `SELECT`, and returns real rows — no hardcoded data left in any route. Connection code is currently duplicated three times; a `get_connection()` refactor was proposed and **deliberately deferred** by the user until after everything works (now confirmed working) — see [[01-Philosophy]] "Refactor timing" and [[08-Next-Step]] for whether/when to revisit. Run via `uvicorn main:app --reload` on `localhost:8000`.

**PostgreSQL** (2026-08-25, already installed/running as a Windows service before this project needed it): dedicated `ai_research_lab` database, three tables — `models(id SERIAL PRIMARY KEY, name TEXT NOT NULL)`, `datasets(id, filename)`, `experiments(id, description)` — each with a B-tree index auto-created on its primary key. Seeded with the same data that used to be hardcoded in `main.py`. Verified as the real data source (not cached/hardcoded) by inserting a row directly via `psql` while the server was running and confirming it appeared in the API response with zero code changes.

## Current stack

| Layer | Technology | Status |
|---|---|---|
| Frontend | static HTML + CSS + JS, all three sections `fetch()`ing the backend | V0.1 + V0.2 complete; connected to real, persisted backend data as of V0.5. |
| Backend | FastAPI (`lab/main.py`), raw `http.server` kept as reference (`lab/server.py`) | V0.3-V0.5 complete — three routes, decorator routing, auto JSON, CORS configured, real DB-backed persistence. Next: V0.6 (SQL/migrations/indexes) or the deferred `get_connection()` refactor — see [[08-Next-Step]] |
| Database | PostgreSQL 17, `ai_research_lab` database, 3 tables | V0.5 complete — real persistence confirmed working end-to-end. No migrations yet (V0.6), schema created by hand once, not version-controlled as code. |
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
