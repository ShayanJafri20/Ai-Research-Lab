# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. **V0.1 through V0.6 are all complete and confirmed working end-to-end.** The app is a real, if small, full stack: static HTML/CSS/JS frontend → `fetch()` → FastAPI backend → PostgreSQL, all three sections (Models/Datasets/Experiments) reading from real database tables, now with real relationships between them.

**V0.6 summary (2026-08-27 to 2026-08-28):** Version-controlled migrations added at `lab/migrations/` (`0001_init.sql`, `0002_add_experiment_foreign_keys.sql`), hand-run via `psql -f` (no framework yet — raw layer first). `experiments` now has real `model_id`/`dataset_id` foreign keys to `models`/`datasets`, enforced (proven with a rejected bad insert) and backfilled with real data, verified via a `JOIN` query. Indexes (measured `EXPLAIN ANALYZE`: 357ms → 0.15ms on a throwaway 2M-row table) and transactions (rollback-vs-commit money-transfer demo) were covered hands-on in the Sandbox rather than forced onto the real tables, which are still too small (3-4 rows) to need either — see [[07-Sandbox-Log]]. Full detail in [[02-Architecture]], [[05-Concepts]].

Also resolved this session: the previously-deferred `get_connection()` refactor is done — `lab/main.py`'s three routes share one connection function. And a real architectural question got documented: why the Models/Datasets/Experiments sections aren't arbitrary placeholder content — each maps directly onto a specific later roadmap version (Datasets→V0.7-0.9, Models→V1.9-2.0, Experiments→V1.4) — see [[04-Decisions]] 2026-08-27.

**Noted gap, not yet acted on:** terminal/CLI basics (opening a terminal, cmd vs PowerShell syntax differences, running a program with a full path) were a real sticking point this session, distinct from the SQL/concept understanding itself, which was solid. Worth being more explicit/basic about terminal steps going forward rather than assuming familiarity — see [[05-Concepts]] 2026-08-27/28 entry.

**Next action: start V0.7 — Dataset Explorer.** Not yet scoped in detail — per hard rule 3, start by identifying the actual problem this version solves before picking any tool. Likely direction (confirm with user first): right now "datasets" are just filenames in a table with no way to actually look inside them — V0.7 is presumably about being able to browse/preview real dataset content from the app, which is also the natural setup for V0.8 (Pandas/EDA). Ask the user what "Dataset Explorer" should concretely mean before building anything.

**If picking this up on a different PC:** clone the repo, set git identity there, `python -m venv .venv` inside `lab/` then `pip install -r requirements.txt`. PostgreSQL 17 must be installed separately there too (not a `pip` package — a real server install). The `ai_research_lab` database now has a repeatable build path: create the empty database, then run `lab/migrations/0001_init.sql` and `0002_add_experiment_foreign_keys.sql` in order via `psql -f` (see [[02-Architecture]] for the exact command). `lab/.env` needs creating locally from `lab/.env.example` with that machine's own DB password. `git pull` before starting, `git add . && git commit && git push` at the end.

**Done for real, 2026-08-28 — desktop machine now matches the laptop:** Python 3.14.7 (via `winget install Python.Python.3.14`) and PostgreSQL 17 installed fresh, venv created, dependencies installed, schema built from both migrations, and all three API routes verified returning correct live data (confirmed via the `experiments` JOIN query matching the laptop's rows exactly, plus a running server hit with `curl`). One real environment gotcha hit and worth remembering: a long-running terminal tool session can hold a *stale* copy of `PATH` from before an installer updates it — Python was genuinely on PATH at the OS level immediately after install, but that session needed the new directories prepended manually (or the full `python.exe` path used directly) until a fresh terminal was opened. Not a sign anything installed wrong.

**The predicted seed-data gap is now closed:** `lab/seed.sql` exists — plain `INSERT` statements, run once via `psql -f seed.sql` on a freshly-migrated empty database, kept deliberately separate from `lab/migrations/` (seed data is a different concern from schema — you wouldn't want a migration runner auto-replaying it against a real database). Not idempotent, same as the migrations. Deliberately **not** run against the desktop's already-seeded database (would create duplicates) — this is for the next fresh machine.

Do not install Docker or Redis yet — not justified until a real problem calls for them (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," [[06-Dependencies]], and [[05-Concepts]] before ending the session.
