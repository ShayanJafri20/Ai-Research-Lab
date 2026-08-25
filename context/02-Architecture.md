# Architecture — Current State

Living document. Update this every time a layer is added — it should always reflect what's **actually built**, not what's planned (planned lives in [[03-Roadmap]]).

Governed by [[01-Philosophy]] hard rule 7 (one layer below current abstraction) and rule 8 (earn every layer).

## Status: V0.1 + V0.2 complete, V0.3 + V0.4 core complete

`lab/index.html`: doctype/html/head/title/body/h1 skeleton, three `<section>`s (Models/Datasets/Experiments, each with `<h2>` + an empty `<ul>`) wrapped in a `<div class="sections">`, a `<button>`, and `<script src="script.js">` at the end of `<body>`. `lab/style.css` covers box model, margin collapsing, class/type/pseudo-class selectors, cascade/specificity/inheritance, typography + `rem` units, flexbox (row layout, `gap`, `justify-content`), `position: fixed`, media queries, and hover transitions. `lab/script.js` covers variables/types/arrays/objects, loops, functions with return values, DOM manipulation, events/delegation, and now `async`/`await`/`fetch()` — `loadModels()` fetches `/models` from the live backend and renders it via the existing `renderList`; Datasets/Experiments still render from hardcoded arrays (not yet converted, see [[08-Next-Step]]). Taught chunk-by-chunk per [[01-Philosophy]] hard rule 2; concepts logged in [[05-Concepts]].

`lab/server.py` (2026-08-24): a raw Python backend using only the standard-library `http.server` module — kept as-is, not deleted, as a deliberate "before" reference to contrast against FastAPI. `Handler(BaseHTTPRequestHandler)`, `do_GET(self)` building a response by hand, manual `self.path` routing (`/models` → 200, else → 404). Not the live backend anymore — superseded by `main.py` below.

`lab/main.py` (2026-08-25): the live backend. `FastAPI()` app, `@app.get("/models")` decorator-based routing returning a plain dict auto-serialized to JSON, `CORSMiddleware` allowing `http://127.0.0.1:5500` (the Live Server origin `index.html` is actually served from) to fetch cross-origin. Auto-generated docs at `/docs`. `fastapi`+`uvicorn` pinned in `lab/requirements.txt`. No persistence — `/models` data is still a hardcoded Python list inside the route function, same underlying gap as `server.py` had, just prettier. Run via `uvicorn main:app --reload` on `localhost:8000`.

## Current stack

| Layer | Technology | Status |
|---|---|---|
| Frontend | static HTML + CSS + JS, now with a live `fetch()` to the backend | V0.1 + V0.2 complete; V0.4 connected `/models` to real data over the network for the first time. |
| Backend | FastAPI (`lab/main.py`), raw `http.server` kept as reference (`lab/server.py`) | V0.3 + V0.4 core complete — one real endpoint (`/models`), decorator routing, auto JSON, CORS configured, no persistence yet. Next: extend routes or V0.5 (PostgreSQL) — see [[08-Next-Step]] |
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
