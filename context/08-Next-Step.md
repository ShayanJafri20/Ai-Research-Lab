# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. **V0.1 through V0.4 complete; V0.5 (PostgreSQL) core work done, pending final confirmation.**

**V0.5 (2026-08-25 to 2026-08-27):** PostgreSQL 17 was already installed and running locally (Windows service) — no fresh install needed, just connection. Created a dedicated `ai_research_lab` database (separate from an unrelated pre-existing `hospital_db`). Taught relational concepts by hand in pgAdmin/psql before any Python: `CREATE TABLE models (id SERIAL PRIMARY KEY, name TEXT NOT NULL)` (noted the auto-created B-tree index on the primary key), `INSERT INTO ... VALUES`, `SELECT`. Same pattern repeated for `datasets` (column `filename`) and `experiments` (column `description`), all seeded with the same data previously hardcoded in `main.py`.

**Secrets handled correctly from the start:** before writing any DB password into a file, installed `python-dotenv`, created `lab/.env` (real password, gitignored) and `lab/.env.example` (template, no real value, committed) — explicitly reasoned as "don't let the secret into git in the first place" rather than fixing it after, callback to the earlier history-rewrite pain.

**Driver choice:** `psycopg[binary]` chosen over an ORM (SQLAlchemy), explicitly reasoned the same way as raw `http.server` before FastAPI — understand the raw SQL/connection layer first, ORM is a later decision if a real problem justifies it.

**All three routes converted**, each following the same shape: `psycopg.connect(...)` using `os.getenv(...)` for credentials → cursor → `execute()` → `fetchall()` → list comprehension to flatten tuples → close connection. `/models` was built first, chunk-by-chunk, user typing every line. Verified with a real proof, not just trusting it: inserted a 4th row (`'GPT'`) directly via `psql` with the server already running, refreshed, and the new row appeared with zero code changes — confirms the route is genuinely reading from Postgres, not returning cached/hardcoded data. `/datasets` and `/experiments` were then converted the same way, done directly (not chunk-by-chunk) since it's pure repetition of an already-proven pattern, matching how the V0.4 route extension was handled.

**Not yet confirmed:** user hadn't yet verified `/datasets` and `/experiments` actually return correct data through the browser/frontend after the conversion — confirm this before considering V0.5 fully done.

**Deliberately deferred (2026-08-27):** the three routes now duplicate the same `psycopg.connect(...)` block. A shared `get_connection()` helper was proposed (same shape as the `renderList` refactor from V0.2) and the user explicitly chose to defer it — reasoning: "generalizing everything will be too much [while] learning, we will do after everything is working." This is a real, sound preference to remember: **prioritize getting a full round trip working end-to-end before refactoring/DRYing it up**, even when the duplication is spotted early. Don't push cleanup passes before functional confirmation next time either — see [[04-Decisions]] and [[01-Philosophy]] if this should become a durable rule.

**If you're picking this up on the other PC:** clone the repo, set git identity there, `python -m venv .venv` inside `lab/` then `pip install -r requirements.txt`. **New for V0.5:** PostgreSQL 17 must be installed there too (separately — it's not something `pip`/`requirements.txt` can provide, it's a real server install), the `ai_research_lab` database and its three tables need creating fresh (no automatic schema sync between machines yet — that's what migrations, V0.6, will properly solve), and `lab/.env` needs creating locally from `lab/.env.example` with that machine's own DB password. `git pull` before starting, `git add . && git commit && git push` at the end.

**Next action:** Get the user's confirmation that `/datasets` and `/experiments` work correctly end-to-end (browser test). Once confirmed: V0.5's core goal is met — do the vault wrap-up (this file, [[02-Architecture]], [[03-Roadmap]] position, [[06-Dependencies]], [[05-Concepts]]) and decide with the user whether to do the deferred `get_connection()` refactor now or move to **V0.6** (SQL + migrations + indexes) per [[03-Roadmap]] — ask, don't assume, per the preference logged above.

Do not install Docker or Redis yet — not justified until a real problem calls for them (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," [[06-Dependencies]], and [[05-Concepts]] before ending the session.
