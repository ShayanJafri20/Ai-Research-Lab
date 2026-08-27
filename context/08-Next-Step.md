# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. **V0.1 through V0.5 are all complete and confirmed working end-to-end.** The app is a real, if small, full stack: static HTML/CSS/JS frontend → `fetch()` → FastAPI backend → PostgreSQL, all three sections (Models/Datasets/Experiments) reading from real database tables. No hardcoded data remains anywhere in `lab/`.

**V0.5 summary (2026-08-25 to 2026-08-27):** PostgreSQL 17 was already installed/running locally before this project needed it — just connected, no fresh install. Created `ai_research_lab` database, three tables (`models`, `datasets`, `experiments`), each taught by hand in pgAdmin/psql (`CREATE TABLE`/`INSERT`/`SELECT`) before touching Python — noted the auto-created B-tree index on each primary key. Secrets handled correctly from the start via `python-dotenv` + gitignored `lab/.env` + committed `lab/.env.example` template, specifically to avoid repeating the earlier git-history-rewrite pain. Driver chosen: `psycopg[binary]` over an ORM, same "raw layer first" reasoning as `http.server` before FastAPI. All three FastAPI routes rewritten to query Postgres via `psycopg.connect()` → cursor → `execute()` → `fetchall()`. **Verified as genuinely real** (not just trusted) by inserting a row directly via `psql` while the server ran and confirming it appeared through the API with zero code changes. `/datasets`/`/experiments` conversion done directly (pattern already proven via `/models`), and the user **confirmed all three sections work correctly** through the actual frontend as the final check. Full detail in [[02-Architecture]], [[06-Dependencies]], [[05-Concepts]].

**Open, unresolved question — ask the user, don't assume:** the three routes in `lab/main.py` still duplicate the same `psycopg.connect(...)` block. A `get_connection()` refactor was proposed and the user explicitly deferred it until "everything is working" — which is now true. At the end of the last session the user was asked to choose between (a) doing that refactor now, or (b) moving straight to **V0.6 — SQL + migrations + indexes**, and the session ended before they answered (context ran out, moving to a fresh session). **This is the literal first thing to ask when this reconvenes.**

**If picking this up on a different PC:** clone the repo, set git identity there, `python -m venv .venv` inside `lab/` then `pip install -r requirements.txt`. PostgreSQL 17 must be installed separately there too (not a `pip` package — a real server install), the `ai_research_lab` database and its three tables need creating fresh by hand (no migrations yet — that's what V0.6 will properly solve), and `lab/.env` needs creating locally from `lab/.env.example` with that machine's own DB password. `git pull` before starting, `git add . && git commit && git push` at the end.

**Next action:** Ask the user: refactor `get_connection()` now, or start V0.6? Once that's picked:
- **If V0.6**: frame it against the real gap — the schema (`CREATE TABLE` statements) currently exists only as commands typed once into pgAdmin, not as version-controlled code. If the database were dropped or recreated on another machine, there's no repeatable script to rebuild it. That's what migrations solve. Also cover indexes/query planning in more depth per [[03-Roadmap]]'s V0.5-V0.6 concept checklist (normalization, joins, transactions, constraints beyond what's been touched already).
- **If the refactor**: same pattern as `renderList` — extract `get_connection()`, have the user attempt replacing the three duplicated blocks themselves (hard rule 6), since this is genuinely learnable, not just busywork.

Do not install Docker or Redis yet — not justified until a real problem calls for them (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," [[06-Dependencies]], and [[05-Concepts]] before ending the session.
