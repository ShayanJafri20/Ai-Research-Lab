# Roadmap — Version Progression

A **direction, not a schedule** (per [[01-Philosophy]]). Versions advance only when the current one is actually understood, not on a timer. Each version should create the reason for the next one's tools — see [[06-Dependencies]].

## Current position

**V0.1 through V0.9 (Load-scoped) all complete.** HTML/CSS/JS foundation solid. V0.3 (2026-08-24) added HTTP fundamentals, a Python venv, and a raw `http.server` backend (`lab/server.py`, kept as a reference). V0.4 (2026-08-25) added FastAPI, decorator-based routing, auto JSON, CORS middleware. V0.5 (2026-08-25 to 2026-08-27) added PostgreSQL — a real `ai_research_lab` database with three tables, all three routes now querying it instead of returning hardcoded lists, secrets handled via a gitignored `.env` from the start. Confirmed working end-to-end (verified with a live-insert test, not just trusted). The previously-deferred `get_connection()` refactor is done (2026-08-27). V0.6 (2026-08-27/28) added version-controlled migrations (`lab/migrations/0001_init.sql`, `0002_add_experiment_foreign_keys.sql`), real foreign keys linking `experiments` to `models`/`datasets`, backfilled and join-verified real data, plus indexes and transactions demonstrated hands-on in the Sandbox (measured `EXPLAIN ANALYZE` speedup, rollback-vs-commit money-transfer demo — see [[07-Sandbox-Log]]) without forcing either onto tables too small to need them yet. V0.7 (2026-08-28) built a real Dataset Explorer: three actual Project Gutenberg texts on disk, a file-backed preview endpoint (path params, parameterized SQL, `os.path.exists`/`try`-`except` error handling), logging/error handling extended to all four routes, and seed data (models + datasets) realigned to match reality and the NLP roadmap track. V0.8 (2026-08-28/29) core loop done: Pandas + matplotlib installed, `lab/eda.py` computes real per-dataset word count/unique words/stopword-filtered top words (cleaned of Gutenberg boilerplate after that inflated every early number), wired into the live app via a new `/datasets/{id}/stats` route and a real frontend stats display — not left as a standalone script. V0.9 (2026-08-29), deliberately scoped to Load only (Extract/Transform skipped — no real trigger yet, see [[09-Ideas-Backlog]]): a new `dataset_stats` table (first `JSONB` column in the project), `lab/load_stats.py` computing and persisting stats once (first real `INSERT`+`commit()` writes in this project), and `/stats` rewritten to a plain `SELECT` instead of recomputing on every request. Next: **V1.0** (RNN — the NLP research track begins) — a genuinely bigger step than anything so far. Live detail in [[08-Next-Step]].

## Progression

| Version | Focus |
|---|---|
| V0.1 | HTML + CSS + JavaScript — static AI Research Lab page (Models / Datasets / Experiments sections, one interactive button) |
| V0.2 | DOM + browser interaction |
| V0.3 | HTTP fundamentals + tiny raw Python HTTP server |
| V0.4 | FastAPI |
| V0.5 | PostgreSQL |
| V0.6 | SQL + migrations + indexes |
| V0.7 | Dataset Explorer |
| V0.8 | Pandas + EDA |
| V0.9 | ETL |
| V1.0 | RNN research lab (NLP track begins) |
| V1.1 | LSTM / GRU |
| V1.2 | Attention |
| V1.3 | Transformer |
| V1.4 | Experiment tracking |
| V1.5 | Reinforcement learning (RLHF-style alignment) |
| V1.6 | Redis / caching |
| V1.7 | Background jobs |
| V1.8 | WebSockets |
| V1.9 | Model registry |
| V2.0 | Inference server |
| V2.1 | Distributed training |
| V2.2 | Docker / CI-CD |
| V2.3 | Cloud deployment |
| V2.4 | Monitoring |
| V2.5 | Multimodal research lab |

## Why this order (each arrow is a "this broke, so we need that" moment, not a schedule)

```
V0.1 Static HTML/CSS/JS
     -> page is fake: nothing changes, nothing persists, nothing computes
     v  problem: a button that does nothing isn't an app

V0.2 DOM + browser interaction (JavaScript)
     -> button can change the page, but only using data typed into the HTML/JS itself
     v  problem: nothing lives anywhere outside the browser tab

V0.3 HTTP + tiny raw Python server
     -> page can talk to a program outside itself, but a hand-written server gets
        messy fast (manual parsing, no routing conventions)
     v  problem: real APIs need structure a raw socket server doesn't give you

V0.4 FastAPI
     -> clean routes/validation, but every value lives in a Python variable and
        vanishes on restart
     v  problem: no persistence

V0.5 PostgreSQL
     -> data survives a restart, but growing data needs real query/schema tooling
     v  problem: raw SQL without indexes/migrations doesn't scale or evolve safely

V0.6 SQL, migrations, indexes -> data layer solid; this is where real research
     content can start, because there's finally somewhere to put it

V0.7-V0.9 Dataset Explorer -> Pandas/EDA -> ETL
     -> need to actually look at and clean data before training on it
     -> right after V0.9: connect Power BI Desktop AND Metabase (a free,
        browser-based BI tool) to the now-clean, loaded `ai_research_lab`
        data and build real charts on it - both firmly planned (2026-08-28/29),
        not opportunistic, covering two different display contexts
        (a separate app vs. a browser page) - see [[01-Philosophy]]

V1.0-V1.3 RNN -> LSTM/GRU -> Attention -> Transformer
     -> each architecture is introduced because the previous one has a specific,
        teachable failure mode (RNNs forget long sequences -> gating fixes that ->
        sequential processing is slow/still bottlenecked -> attention looks at
        everything at once -> generalizing that gives a Transformer)
     -> tokenization (and later BPE, once word-level vocab/OOV problems show up)
        is forced in immediately, since none of the above can accept raw text;
        PyTorch is introduced only once manual/NumPy backprop gets genuinely
        painful, not before -> autograd + GPU acceleration become the earned reason

V1.4 Experiment tracking
     -> once several architectures/hyperparams are tried, eyeballing results stops
        working -> this is also where config files replace hardcoded hyperparameters

V1.5 Reinforcement learning (RLHF-style alignment)
     -> a Transformer trained purely on next-token prediction reflects the
        statistics of its training data, not necessarily what you actually want
        it to do
     v  problem: supervised training alone has no way to express "preference" -
        it can only imitate, not optimize for a judged outcome

V1.6-V1.8 Redis/caching -> Background jobs -> WebSockets
     -> training takes real time: can't block an HTTP request for minutes (-> jobs),
        want live progress instead of refreshing (-> WebSockets); caching shows up
        wherever something slow gets asked for repeatedly

V1.9-V2.0 Model registry -> Inference server
     -> trained models pile up unorganized -> need to store/version them, then serve
        predictions from one -> this is also the natural home for generation-time
        concerns like top-k/top-p sampling and KV caching, once "serving fast,
        repeated predictions" is the actual problem instead of "training once"

V2.1 Distributed training -> a single GPU becomes the bottleneck for bigger models/datasets

V2.2 Docker/CI-CD -> "works on my machine" becomes a real problem the moment more
     than one environment is involved (same root issue as syncing this project
     across two PCs, but for the runtime instead of files)

V2.3-V2.5 Cloud -> Monitoring -> Multimodal research lab
     -> local hardware runs out of room -> running services need observability ->
        the research itself expands past text into vision/audio
```

If a version turns out to need something unexpected, the chain adjusts right there rather than forcing the next box on the list — see [[09-Ideas-Backlog]] for concepts flagged along the way that don't have a trigger yet.

## Concept depth checklists (added 2026-08-21)

User goal is full understanding of what's happening underneath, not just shipping features — see [[04-Decisions]] "Gap-check against external web-dev roadmap." These expand the one-line roadmap rows above into sub-concepts so nothing gets silently skipped across a many-session project. Track actual coverage in [[05-Concepts]], not here — this is the checklist, not the log.

- **V0.1 — HTML:** elements/tags/attributes, nesting, document structure, semantic HTML, forms, inputs, buttons, links, images, tables, lists, **accessibility basics** (tie this to whenever semantic HTML/forms are introduced — it rarely breaks loudly enough to force itself in via hard rule 3, so it needs to be deliberate), HTML parsing → DOM.
- **V0.1 — CSS** (previously just "add CSS," no breakdown): selectors, cascade, specificity, inheritance, box model (content/padding/border/margin), `display` (block/inline/inline-block/flex/grid), position, flexbox, grid, colors, fonts, units, responsive design, media queries, animations/transitions.
- **V0.1/V0.2 — JavaScript, split into two layers** (previously flattened into one line):
  - Language fundamentals: variables (`let`/`const`/`var`), types, operators, conditionals, loops, functions, scope, closures, objects, arrays, destructuring, spread/rest, modules, classes.
  - Browser API layer (V0.2): DOM methods (`querySelector`, `createElement`, `textContent`, `classList`), events, event loop, call stack, Web APIs, Promises, `async`/`await`, `fetch()`.
- **V0.3 — HTTP fundamentals**, unpacked: URL anatomy, DNS, IP, client/server model, request anatomy (method/headers/body), response anatomy (status code/headers/body), the status code families (2xx/3xx/4xx/5xx), HTTP vs HTTPS.
- **V0.4+ — Auth/sessions**: cookies, sessions, tokens. Still deliberately deferred — this single-user app has no login yet, so hard rule 3 has nothing to justify it. Likely real trigger: V0.9 ETL pulling an external dataset API that needs a key/token. Revisit then, not before.
- **CORS — prediction correction (2026-08-25):** this was grouped with auth above and predicted to first trigger at V0.9. Wrong — it triggered at **V0.4**, the moment the frontend (served on `127.0.0.1:5500` via Live Server) fetched the backend (`127.0.0.1:8000`) for the first time; different ports alone are enough to make these different origins under the Same-Origin Policy, no login/auth needed to hit it. Fixed via `CORSMiddleware` in `main.py`. Noted here as a reminder that these "likely trigger" predictions are best guesses, not commitments — see [[04-Decisions]].
- **V0.5-V0.6 — PostgreSQL/SQL**, unpacked (added 2026-08-25, before starting V0.5): what a relational database actually is (a separate server process, not a `pip` package — explicit contrast to draw before installing), tables/rows/columns, primary keys/foreign keys/relationships, normalization, SQL itself (SELECT/INSERT/UPDATE/DELETE, `WHERE`, joins), transactions, constraints, indexes (and *why* — B-trees, query planning), migrations (schema changes over time, not just initial setup), connection pooling. Driver/ORM choice (raw `psycopg` vs. SQLAlchemy or similar) deliberately not pre-decided — treat that choice itself with the same problem-first reasoning once actually connecting from FastAPI, not before.
- **V1.0-V1.3 — NLP/tokenization** (added 2026-08-23): tokenization (forced immediately — models take numbers, not text), BPE/subword tokenization (once word-level vocab/out-of-vocabulary limits show up, expect around V1.2-V1.3), lemmatization (cover conceptually — what it is, why classical NLP needed it, why subword tokenization mostly displaced that need — not a deep implementation focus). Framework: hand-rolled/NumPy math first for the simplest case, PyTorch introduced only once manual backprop is genuinely painful (hard rule 3/7), not preemptively.
- **V1.4 — Config-driven training**: hyperparameters move out of hardcoded scripts into config files once multiple runs need comparing — same session that introduces experiment tracking.
- **V1.5 — RL/RLHF**: added 2026-08-23 as a genuine new version (not a bolt-on) — see [[04-Decisions]] for why it's separate from the supervised RNN→Transformer track.
- **V1.9-V2.0 — Generation/serving**: top-k/top-p sampling (text generation quality/diversity), KV caching (inference-speed optimization for Transformers) — both fit once there's a working model to generate from or serve, not before.

## Notes

- CNN architectures (AlexNet, ResNet) are already used in practice per user background, but still get **full coverage** (basics as a fast refresher, then depth — math, tensor shapes, implementation) when the vision track resumes; reinforcement of known ML material is explicitly wanted, not just net-new SWE content. See [[05-Concepts]].
- Later stages (MongoDB comparison, Power BI dashboards, DSA, Kubernetes) are woven in opportunistically per [[01-Philosophy]], not as separate standalone versions — see that file's data engineering, Power BI, and DSA sections for how each gets introduced.
- A dedicated frontend-framework track (React/TypeScript/Tailwind/Next.js) was considered on 2026-08-21 and explicitly **not** added — decided later, per hard rule 3, only if a real problem in the project ever calls for it. See [[04-Decisions]].
- Update the "Current position" section above at the end of every session that changes it.
