# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. **V0.1 through V0.7 are all complete.** The app is a real full stack: static HTML/CSS/JS frontend → `fetch()` → FastAPI backend → PostgreSQL + real files on disk, with a genuine Dataset Explorer feature working end-to-end.

**V0.7 summary (2026-08-28) — Dataset Explorer, done for real:** all three `datasets` rows now point to real public-domain texts (`peter_rabbit.txt`, `alice_in_wonderland.txt`, `wizard_of_oz.txt` — all under `lab/datasets/`, downloaded from Project Gutenberg with license headers intact). New route `GET /datasets/{dataset_id}/preview`: path parameter → parameterized SQL lookup (`WHERE id = %s`, never raw string interpolation) → `os.path.exists` check → `open()`/`.read()` inside `try`/`except` → first 300 words returned as JSON. Frontend: `/datasets` now returns `{id, filename}` objects (not bare strings), rendered via a new `renderDatasetList` (kept separate from the shared `renderList`, which stayed string-only for Models/Experiments), each `<li>` carrying a `data-id`; one delegated click listener on `.datasets-list` fetches and displays the real preview in a new `.preview` div. `logging` (info/warning/error) plus `try`/`except` → clean `404`/`500` responses added across **all four** routes, not just the new one, since the underlying DB-failure risk applies equally to `/models`/`/datasets`/`/experiments` — extending an already-justified pattern for consistency, not new speculative complexity. A known, deliberately-deferred gap: `conn.close()` still doesn't run if `cur.execute()` throws (a connection leak on the error path) — noted, not fixed, see [[09-Ideas-Backlog]].

Also fixed this session: `models` used to mix CNN (`ResNet`, `AlexNet`) and NLP (`Transformer`, `GPT`) names, mismatching the actual roadmap (V1.0-V1.5 is all NLP). Realigned to `RNN`/`LSTM`/`Transformer`/`GPT`, with the one dependent `experiments` description fixed to match — both the live DB and `seed.sql` updated. See [[04-Decisions]] for both this and the earlier dataset-filename decision.

**Three real bugs hit and fixed this session, each a genuine debugging moment, not hand-holding:** a `500` from `/datasets` (SQL only selected `filename` but the return statement assumed `row[1]` existed too — fixed by selecting `id, filename`); a missing-backtick bug (`${id}` inside double quotes instead of a template literal, so it fetched a literal `${id}` in the URL); and a shared-function collision (editing `renderList` to expect `{id, filename}` objects broke Models/Experiments, which still pass plain strings — fixed by splitting into two functions). Also mid-session: user explicitly pushed back on the AI writing too much backend code directly (logging/error handling included) — a real hard-rule-6 course correction, not just frontend/CSS anymore. Full detail in [[05-Concepts]].

**Noted gap, not yet acted on:** terminal/CLI basics were a real sticking point in the V0.6 session, distinct from SQL/concept understanding, which was solid — still worth being explicit about terminal steps rather than assuming familiarity.

**Next action: start V0.8 — Pandas + EDA.** Real trigger already sitting there: V0.7 can show raw text, but "explore this dataset" should mean more than reading prose — word counts, word-frequency distributions, basic stats, ideally with matplotlib/seaborn visualization, per [[01-Philosophy]]'s dashboarding-layers note. This is also the step that turns text into structured numbers, which is the actual prerequisite for the now-firmly-planned Power BI step right after V0.9.

**If picking this up on a different PC:** clone the repo, set git identity there, `python -m venv .venv` inside `lab/` then `pip install -r requirements.txt`. PostgreSQL 17 must be installed separately (a real server install, not `pip`). Build the DB: create it empty, run both migrations via `psql -f`, then `psql -f seed.sql` for real starting data (all three dataset rows now seed with real filenames — the actual `.txt` files under `lab/datasets/` are committed to the repo, so nothing extra needs downloading). `lab/.env` needs creating locally from `lab/.env.example` with that machine's own DB password. `git pull` before starting, `git add . && git commit && git push` at the end.

Do not install Docker or Redis yet — not justified until a real problem calls for them (hard rule 3). Don't reach for matplotlib/seaborn/Pandas either until V0.8 actually starts.

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," [[06-Dependencies]], and [[05-Concepts]] before ending the session.
