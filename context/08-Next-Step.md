# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. **V0.1 through the core of V0.4 are complete — the first real frontend-to-backend round trip is working.**

**V0.3 (2026-08-24):** HTTP fundamentals covered conceptually, `lab/.venv` created, `lab/server.py` built with the standard-library `http.server` module — `Handler(BaseHTTPRequestHandler)`, `do_GET` building a response by hand, manual `self.path` routing (`/models` → 200, else → 404). First build attempt moved too fast (built solo); redone slower, user typing every line — see [[05-Concepts]]. Deliberately not extended past one route, to feel the tedium motivating V0.4.

**V0.4 (2026-08-25):** `fastapi` + `uvicorn` installed into `lab/.venv`, pinned into `lab/requirements.txt` via `pip freeze` (first real dependency file — see [[06-Dependencies]]). `lab/main.py` built: `app = FastAPI()`, `@app.get("/models")` decorator-based routing (contrasted directly against `server.py`'s manual `if self.path == ...`), returning a plain dict that FastAPI auto-serializes to JSON with the correct `Content-Type` header — no manual `send_response`/`send_header`/`wfile.write`. Auto-generated interactive docs at `/docs` (OpenAPI/Swagger UI) shown and explained as a dev tool, not user-facing. `lab/script.js` then rewired: `loadModels()` (an `async` function using `fetch()`/`await`/`response.json()`) replaces the hardcoded `models` array entirely — the Models section now renders from a live network call to the FastAPI backend, not static JS data. This also **finally closed the V0.2 loose end**: the destructuring/spread/rest scratch block at the bottom of `script.js` (which referenced `models`) was deleted as part of removing the hardcoded array, not left as separate cleanup debt.

**Real CORS trigger, earlier than predicted:** [[03-Roadmap]]'s concept checklist predicted CORS would first become necessary at V0.9 (an external dataset API). It actually surfaced right here at V0.4 — the frontend (served via VS Code Live Server on `127.0.0.1:5500`) and the backend (`127.0.0.1:8000`) are different origins purely due to port, which is enough to trigger the browser's Same-Origin Policy. Taught from first principles (origin = protocol+host+port, same-origin policy as a security boundary, CORS as the server's explicit opt-in via `Access-Control-Allow-Origin`), then fixed with `CORSMiddleware` in `main.py`, `allow_origins` scoped to the Live Server origin specifically. **Correction to make in [[03-Roadmap]]'s concept checklist:** the "V0.9" prediction for CORS's trigger was wrong; note it triggered at V0.4 instead, as a reminder that these predictions are best guesses, not commitments.

**Still open, not urgent:** Datasets and Experiments sections still render from hardcoded JS arrays, not fetched from the backend — only `/models` was converted, deliberately (same "prove the concept once, don't repeat by hand" pattern as V0.3's routing). No FastAPI endpoints exist yet for datasets/experiments either. Decide next session whether to extend this now or move on to V0.5 (PostgreSQL) first, since real persistence is arguably the more urgent gap (the "models" list still isn't stored anywhere — restarting the FastAPI server loses nothing today only because it's hardcoded in `main.py`, which is itself the next problem V0.5 solves).

**If you're picking this up on the other PC:** clone the repo, set git identity there, `python -m venv .venv` inside `lab/` then `pip install -r requirements.txt` (this is the first session where `requirements.txt` actually matters — see [[06-Dependencies]]). `git pull` before starting, `git add . && git commit && git push` at the end.

**Next action:** Decide and start one of: (a) extend `/datasets` and `/experiments` the same way `/models` was done, for full-stack consistency before moving on, or (b) move to **V0.5 (PostgreSQL)** per [[03-Roadmap]] — the real next problem, since `main.py`'s data is still hardcoded in Python, not persisted. Either is reasonable; ask the user which they'd rather do first next session rather than assuming.

Do not install a database, Docker, or anything beyond FastAPI/uvicorn yet — wait for the user's call on (a) vs (b) above before installing PostgreSQL (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," and [[05-Concepts]] before ending the session.
