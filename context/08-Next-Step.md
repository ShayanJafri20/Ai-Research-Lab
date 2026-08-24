# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. **V0.1, V0.2, and the core of V0.3 are complete.**

**V0.3 (2026-08-24):** HTTP fundamentals covered conceptually first (client/server model, URL anatomy, DNS/IP, request anatomy, response anatomy, status code families 2xx/3xx/4xx/5xx, HTTP vs HTTPS), then `lab/.venv` created (first genuinely justified venv — see [[06-Dependencies]]), then `lab/server.py` built using only the standard-library `http.server` module: a `Handler` class inheriting `BaseHTTPRequestHandler`, a `do_GET` method building a response by hand (`send_response`/`send_header`/`end_headers`/`wfile.write`), and manual path-based routing (`if self.path == "/models"` → 200, `else` → 404) — verified working in a browser on both `/models` and a non-matching path. First build attempt moved too fast (built the whole file in one pass without the user writing any of it); redone slower, one piece at a time, with the user typing every line themselves — see [[05-Concepts]].

**Deliberately not done:** routing wasn't extended to `/datasets`/`/experiments` — user chose to stop after proving the concept with `/models` rather than hand-write repetitive routing branches, specifically to feel the tedium that motivates V0.4 (FastAPI) rather than build it out further by hand. This was a deliberate choice, not something skipped by accident.

**Still-open loose end from V0.2, not urgent:** `lab/script.js` still has scratch demo lines at the bottom (destructuring/spread/rest practice, e.g. `console.log(addModels("GPT", "BERT"))`) that aren't part of the app's real logic — still needs a delete-not-comment cleanup pass.

**If you're picking this up on the other PC:** clone the repo first (`git clone https://github.com/ShayanJafri20/Ai-Research-Lab.git`), then open the folder in Claude Code — `CLAUDE.md` will point you back to this vault automatically. Set git identity there, `python -m venv .venv` inside `lab/` (the venv itself is gitignored, machine-specific — see [[06-Dependencies]]). Run `git pull` before starting work each session, `git add . && git commit && git push` at the end of one.

**Next action:** Start **V0.4 (FastAPI)** per [[03-Roadmap]]. Frame it explicitly against the pain just felt in V0.3: no automatic routing (had to hand-write `if self.path == ...`), no automatic JSON handling, no request validation, every response byte written manually. Explain what FastAPI actually removes before writing any FastAPI code, install it (`pip install fastapi uvicorn` — first real `pip install`, so this is also where `lab/requirements.txt` starts existing for real, per [[01-Philosophy]] hard rule 3), verify, smallest possible example, then rebuild the `/models` route in FastAPI so the contrast with the hand-written version is direct and felt, not abstract.

Do not install a database, Docker, or anything beyond FastAPI/uvicorn yet — none of that is justified until a real problem in V0.4 calls for it (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," and [[05-Concepts]] before ending the session.
