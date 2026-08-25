# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. **V0.1 through V0.4 are fully complete** — all three sections (Models/Datasets/Experiments) render from live `fetch()` calls to a real FastAPI backend, no hardcoded frontend data remains anywhere in `lab/`.

**V0.4 wrap-up (2026-08-25):** After `/models` proved the FastAPI + `fetch()` pattern (see prior entries below for the full first-principles walkthrough of FastAPI, Promises/async/await, and the real CORS trigger), `/datasets` and `/experiments` were added to `lab/main.py` and `loadDatasets()`/`loadExperiments()` added to `lab/script.js`, mirroring `loadModels()` exactly. User explicitly asked for this extension to be done directly/mechanically rather than taught chunk-by-chunk — reasonable, since it's pure repetition of an already-proven pattern with no new concept in it, unlike V0.3's routing (which was deliberately left unextended specifically to feel new tedium). Verified working in browser, all three sections populate, no console errors.

**Where persistence actually stands:** every route in `main.py` still returns a hardcoded Python list baked into the function. Nothing survives a server restart because nothing was ever real to begin with — this is the exact gap V0.5 exists to close.

**If you're picking this up on the other PC:** clone the repo, set git identity there, `python -m venv .venv` inside `lab/` then `pip install -r requirements.txt`. `git pull` before starting, `git add . && git commit && git push` at the end.

**Next action:** Start **V0.5 — PostgreSQL** per [[03-Roadmap]]. Frame it against the concrete gap above: three `/models`/`/datasets`/`/experiments` lists that only exist as long as the Python process is alive. Per hard rule 3: explain what a relational database actually is and what problem it solves before installing anything, then install PostgreSQL itself (this is a genuinely new kind of install — not a `pip` package, a whole database *server* running as its own process — explain that distinction explicitly), create the database, then introduce whichever Python driver/ORM is needed to connect from FastAPI (don't pre-decide raw `psycopg` vs. an ORM like SQLAlchemy — that choice itself deserves the same problem-first treatment once we're actually there). Concept-depth checklist for the DB track already exists in [[03-Roadmap]] if one was written — check there first; if not, build one the same way V0.3's HTTP checklist was built, not just "add a database" as one line.

Do not install Docker, Redis, or anything beyond PostgreSQL + its Python driver yet — none of that is justified until V0.5 itself creates a reason (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," and [[05-Concepts]] before ending the session.
