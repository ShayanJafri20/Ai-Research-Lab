# Architecture — Current State

Living document. Update this every time a layer is added — it should always reflect what's **actually built**, not what's planned (planned lives in [[03-Roadmap]]).

Governed by [[01-Philosophy]] hard rule 7 (one layer below current abstraction) and rule 8 (earn every layer).

## Status: V0.1 through V0.4 complete

`lab/index.html`: doctype/html/head/title/body/h1 skeleton, three `<section>`s (Models/Datasets/Experiments, each with `<h2>` + an empty `<ul>`) wrapped in a `<div class="sections">`, a `<button>`, and `<script src="script.js">` at the end of `<body>`. `lab/style.css` covers box model, margin collapsing, class/type/pseudo-class selectors, cascade/specificity/inheritance, typography + `rem` units, flexbox, `position: fixed`, media queries, hover transitions. `lab/script.js`: variables/types/arrays/objects, loops, functions, DOM manipulation, events/delegation, and now `async`/`await`/`fetch()` — `loadModels()`/`loadDatasets()`/`loadExperiments()` fetch all three sections from the live backend and render via the shared `renderList`. Zero hardcoded frontend data remains. Taught chunk-by-chunk per [[01-Philosophy]] hard rule 2; concepts logged in [[05-Concepts]].

`lab/server.py` (2026-08-24): a raw Python backend using only the standard-library `http.server` module — kept as-is, not deleted, as a deliberate "before" reference to contrast against FastAPI. Not the live backend — superseded by `main.py`.

`lab/main.py` (2026-08-25): the live backend. `FastAPI()` app with three decorator-routed endpoints (`/models`, `/datasets`, `/experiments`), each returning a plain dict auto-serialized to JSON. `CORSMiddleware` allowing `http://127.0.0.1:5500` (the Live Server origin `index.html` is served from) to fetch cross-origin. Auto-generated docs at `/docs`. `fastapi`+`uvicorn` pinned in `lab/requirements.txt`. **No persistence** — all three routes return hardcoded Python lists baked into the function bodies; this is the exact gap V0.5 exists to close. Run via `uvicorn main:app --reload` on `localhost:8000`.

## Current stack

| Layer | Technology | Status |
|---|---|---|
| Frontend | static HTML + CSS + JS, all three sections `fetch()`ing the backend | V0.1 + V0.2 complete; V0.4 connected the full page to real (if not yet persisted) backend data. |
| Backend | FastAPI (`lab/main.py`), raw `http.server` kept as reference (`lab/server.py`) | V0.3 + V0.4 complete — three routes, decorator routing, auto JSON, CORS configured, no persistence yet. Next: V0.5 (PostgreSQL) — see [[08-Next-Step]] |
| Database | none yet | not started |
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
