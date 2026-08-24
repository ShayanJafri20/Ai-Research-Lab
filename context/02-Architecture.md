# Architecture — Current State

Living document. Update this every time a layer is added — it should always reflect what's **actually built**, not what's planned (planned lives in [[03-Roadmap]]).

Governed by [[01-Philosophy]] hard rule 7 (one layer below current abstraction) and rule 8 (earn every layer).

## Status: V0.1 + V0.2 complete, core of V0.3 complete

`lab/index.html`: doctype/html/head/title/body/h1 skeleton, three `<section>`s (Models/Datasets/Experiments, each with `<h2>` + an empty `<ul>`) wrapped in a `<div class="sections">`, a `<button>`, and `<script src="script.js">` at the end of `<body>`. `lab/style.css` covers box model, margin collapsing, class/type/pseudo-class selectors, cascade/specificity/inheritance, typography + `rem` units, flexbox (row layout, `gap`, `justify-content`), `position: fixed`, media queries, and hover transitions. `lab/script.js` covers variables/types/arrays/objects, loops, functions with return values, DOM manipulation (`addEventListener`, `.textContent`, `createElement`/`appendChild`, `classList`), the event object + event delegation, and destructuring/spread/rest — each section's list renders from a JS array via one shared `renderList` function, not three duplicated loops. Taught chunk-by-chunk per [[01-Philosophy]] hard rule 2; concepts logged in [[05-Concepts]].

`lab/server.py` (2026-08-24): a raw Python backend using only the standard-library `http.server` module — no frameworks. `Handler(BaseHTTPRequestHandler)` inherits the networking plumbing; `do_GET(self)` is the callback the framework calls automatically per request (same shape as `addEventListener`'s callback, on the server side); the response is built by hand (`send_response`/`send_header`/`end_headers`/`wfile.write(b"...")`); `self.path` drives manual routing (`/models` → 200, everything else → 404). Deliberately not extended to more routes — see [[08-Next-Step]] for why. Runs on `localhost:8000`, verified working in a browser.

## Current stack

| Layer | Technology | Status |
|---|---|---|
| Frontend | static HTML + CSS + JS | V0.1 + V0.2 complete — structure, styling, full interactivity, and DOM/event fundamentals all working. |
| Backend | raw Python `http.server` (`lab/server.py`) | V0.3 core complete — one hand-routed endpoint (`/models`), no framework, no persistence. Next: V0.4 (FastAPI) — see [[08-Next-Step]] |
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
