# Decisions Log

Append-only. Newest entry at the top. Each entry: date, decision, why, alternatives considered. Referenced from [[00-Hub]].

---

### 2026-08-27 — Made explicit: Models/Datasets/Experiments sections map directly onto later roadmap versions

**Decision:** Documented, rather than left implicit in the roadmap table, that the three V0.1 sections were never arbitrary placeholder content — each is a deliberate stand-in for what a specific later version fills in for real:
- **Datasets** → V0.7 (Dataset Explorer), V0.8 (Pandas/EDA), V0.9 (ETL) — real dataset files/metadata replace `harrypotter.txt`-style stand-ins.
- **Models** → V1.9 (Model registry), V2.0 (Inference server) — real trained checkpoints from the V1.0-V1.3 RNN→LSTM→Attention→Transformer track replace `ResNet`/`GPT`-style stand-ins.
- **Experiments** → V1.4 (Experiment tracking) — real run logs/hyperparameter comparisons replace `Baseline CNN - run 1`-style stand-ins.

**Why:** User asked why the app looks so basic (three sections, placeholder rows) if later versions supposedly move on to real ML work — reasonable to wonder whether the current shape gets discarded. It doesn't: the row *shape* (name/filename/description) was chosen to match what real data will eventually look like, populated early only because [[01-Philosophy]] hard rule 8 requires earning the DB/API layer before building the real feature on top of it. User's framing of the underlying principle: **"everything we do should have a purpose"** — already the substance of hard rules 3/8/9, but worth stating as a direct quote here since it's the reasoning the user reached for unprompted, not just a rule imposed on them.

**Alternatives considered:** Leaving the mapping only implicit in [[03-Roadmap]]'s version list (rejected — user specifically asked for it to be made explicit, and an implied connection across 25 versions is easy to lose track of in a long multi-session project).

---

### 2026-08-27 — Defer refactoring until the feature works end-to-end (new standing rule)

**Decision:** When duplication is spotted mid-build (here: `psycopg.connect(...)` repeated across all three FastAPI routes), flag it and propose the fix, but don't push to do it immediately — default to finishing the working version first, refactor after. Logged as [[01-Philosophy]]'s new "Refactor timing" rule.

**Why:** User explicitly declined an offered `get_connection()` extraction mid-V0.5 with the reasoning that generalizing/cleaning up while still learning the underlying feature is too much cognitive load at once — better to get the full round trip (Postgres → FastAPI → frontend) actually working, then clean up once it's proven. This is a legitimate engineering sequencing principle ("make it work, then make it right"), not corner-cutting, and the same underlying instinct as the earlier "don't skip basics" and "explain before installing" preferences: don't compress multiple new things into one moment.

**Alternatives considered:** Refactoring immediately since the duplication was already identified and the fix was small (rejected — that's what the user pushed back on); doing it silently without asking (rejected — same reasoning as hard rule 6, the user should be consulted on scope, not have decisions like this made unilaterally).

---

### 2026-08-23 — Added Reinforcement Learning as a real roadmap version (V1.5); renumbered V1.5-V2.4 to V1.6-V2.5

**Decision:** User asked whether tokenization/BPE/lemmatization, PyTorch, config-driven training, top-k sampling, KV caching, and LoRA/QLoRA would be covered, plus reinforcement learning. Verdict, itemized:
- Tokenization, BPE, lemmatization, PyTorch (introduced only after a hand-rolled/NumPy pass, per hard rule 3/7), and config files all fit naturally into the *existing* V1.0-V1.4 track — added to that section's concept-depth checklist in [[03-Roadmap]], no roadmap restructuring needed.
- top-k/top-p sampling and KV caching fit naturally into V1.9-V2.0 (Model registry/Inference server, renumbered from V1.8-V1.9) — also just a checklist addition.
- LoRA/QLoRA has no current trigger (no large pretrained model exists yet to need efficient fine-tuning) — logged to [[09-Ideas-Backlog]] instead of forced into the roadmap now.
- **Reinforcement learning (RLHF-style alignment) is different** — it's a genuinely separate subfield from the supervised RNN→LSTM→Attention→Transformer track (different training loop, different math), not a bolt-on extension of it. User explicitly chose to add it as a real, dedicated roadmap version rather than defer it.

**Placement:** inserted as the new **V1.5**, directly after V1.4 (Experiment tracking) and before the systems/infra stretch (Redis/jobs/WebSockets). Reasoning: RL needs a working trained model (V1.0-V1.3) and ideally already-solid experiment tracking (V1.4, since RL training is notoriously unstable and benefits enormously from tracked runs) before it makes sense to attempt. Everything from the old V1.5 onward shifted up by one version number (old V1.5-V2.4 → new V1.6-V2.5). The roadmap table, the causal "why this order" narrative, and the concept-depth checklists in [[03-Roadmap]] were all updated to match — this is a renumbering of labels only, no version's actual content changed.

**Why renumber instead of using a fractional label like "V1.45":** the project's version numbers are direction markers, not semver — a clean sequential renumber keeps the roadmap and its own causal narrative readable for future sessions, and nothing outside [[03-Roadmap]] referenced the old V1.5+ numbers specifically (checked [[08-Next-Step]], [[05-Concepts]], [[09-Ideas-Backlog]] before renumbering).

**Alternatives considered:** folding RL into V1.3 (Transformer) or V1.4 (Experiment tracking) as a sub-topic (rejected — user and this session agreed it's substantial enough to warrant its own dedicated version, not a footnote); leaving it on the Ideas Backlog (the other option offered, not chosen — user picked the dedicated-version path).

---

### 2026-08-21 — Gap-check against external web-dev roadmap; kept plan, added concept-depth checklists

**Decision:** User brought in a generic web-dev learning roadmap (browser fundamentals → HTML → CSS → JS → HTTP → Node.js → databases → React → TypeScript → Tailwind → Next.js → production) from a separate ChatGPT conversation and asked whether it changes our plan. Verdict: the *sequencing philosophy* independently matches what [[01-Philosophy]] already enforces (rules 3, 7, 8) — no change needed there. Two real forks were surfaced and resolved:
1. **Backend runtime stays Python** (V0.3 raw HTTP server → V0.4 FastAPI, not Node.js/Express) — matches existing ML/Python fluency, avoids a second unfamiliar server-side language, and the rest of the roadmap (Postgres, Pandas/ETL, RNN research track) is already built around it.
2. **No dedicated React/TypeScript/Tailwind/Next.js phase added** — stays deferred per hard rule 3, only introduced if a real problem in the project calls for it, not pre-planned.

What *did* change: the user clarified the actual goal is full underlying understanding of both frontend and backend, not just shipping features, and asked for a genuine gap-check rather than a stack switch. Cross-referencing GPT's more granular concept lists against [[03-Roadmap]] found real granularity gaps (not direction gaps) — CSS and JS were each flattened into a single roadmap line with no sub-concept breakdown, HTTP fundamentals weren't unpacked, and auth/cookies/sessions/CORS didn't appear anywhere. Added explicit "Concept depth checklists" to [[03-Roadmap]] and candidate sandbox drills (Counter/Todo/fetch-app) to [[01-Philosophy]] so these don't get silently skipped across a long multi-session project, without changing the version sequence or pulling anything in early.

**Why:** Hard rule 3 says don't install/introduce tools without a real problem — but concept *tracking* is different from tool *installation*; leaving CSS/JS/HTTP as one-line roadmap items risked skipping sub-topics not because a problem never arose, but because nobody was watching for them across sessions.

**Alternatives considered:** Adopting GPT's roadmap wholesale, including Node.js/Express and a React/Next.js phase (rejected — abandons the Python-leverage rationale already decided, and pre-plans a frontend framework before any real need, violating hard rule 3); making no changes at all (rejected — the granularity gaps were real, even though the direction wasn't wrong).

---

### 2026-08-20 — Removed premature venv step from V0.1

**Decision:** Moved "set up a Python virtual environment" out of the V0.1 next-step list. V0.1 is pure static HTML/CSS/JS — no Python code exists yet to isolate. Venv setup now correctly waits for V0.3 (first raw Python HTTP server).

**Why:** Caught while about to execute [[08-Next-Step]] as originally written — it had been drafted speculatively when the vault was first built, before re-checking it against [[01-Philosophy]] hard rule 3 (no tool without a real, current problem) and hard rule 8 (earn every layer). A venv with nothing to isolate is exactly the kind of unexplained setup the project is trying to avoid.

**Alternatives considered:** Setting it up anyway "since we'll need it eventually" (rejected — that's precisely the preemptive-installation pattern hard rule 3 exists to prevent).

---

### 2026-08-20 — Git + private GitHub repo chosen for multi-machine work

**Decision:** The whole project (`context/` vault and future `lab/`/`sandbox/` code) lives in one private GitHub repo — `https://github.com/ShayanJafri20/Ai-Research-Lab` — synced via plain `git push`/`git pull` between machines. `context/` is tracked in the same repo as the code, not gitignored or split out. `context/.obsidian/workspace.json` is gitignored (pure local UI state, not privacy-related — see `.gitignore`).

**Why:** User needs to code from a second PC. Considered and rejected: USB/copy-paste and cloud-sync folders (both risk silent overwrites, no real conflict resolution — see [[01-Philosophy]] hard rule 3, problem-first reasoning); gitignoring `context/` and shuttling it manually (rejected — reintroduces the exact sync problem git solves, and breaks the `CLAUDE.md` → `context/00-Hub.md` auto-discovery design meant to give any new Claude session full context automatically); making the repo public now (rejected — `context/` is a raw, un-curated learning journal including self-reported weaknesses in [[05-Concepts]], not portfolio material; private→public is a free toggle any time, public→regretted-it is not, since anything exposed while public can already be cloned/cached/indexed). Deleting `context/` and then going public was also considered and rejected as a false fix — deleting a folder in a new commit doesn't remove it from git history, so it would remain fully visible once public; a genuinely public share later should be a brand-new repo built for that purpose, not a rewrite of this one's history.

**Branches/merges/PRs:** deliberately not used yet — nothing has diverged (one commit, one branch). Per hard rule 3, these get introduced hands-on the first time work actually diverges across the two machines, not as a preemptive lesson.

---

### 2026-08-20 — Folder/file structure must always be explained (hard rule 9)

**Decision:** Every file, folder, and config that appears in the project needs a stated reason at the time it's created — extends [[01-Philosophy]] hard rule 3 (no tools installed without justification) to project structure itself, including boilerplate a framework/CLI would normally scaffold silently.

**Why:** User doesn't want files/config "randomly appearing" without understanding why they exist — same first-principles-over-convenience stance as hard rule 3, applied one level up to structure rather than just dependencies.

**Alternatives considered:** Leaving scaffolded/generated files unexplained as "just how the framework does it" (rejected — defeats the goal of a fully explainable project).

---

### 2026-08-20 — "Understood" ML concepts get full coverage, not skipped (amended same day)

**Decision:** "Understood (prior background)" in [[05-Concepts]] does not mean skip anything — it only changes pacing. Basics still get covered (faster, as a refresher) and depth (math, tensor shapes, implementation) still gets taught, even on AI/ML concepts the user has used before (CNNs, attention, etc.).

**Why:** User pushed back twice on the same day: first that reinforcing known ML material via AI-guided teaching strengthens understanding rather than being redundant (so depth shouldn't be skipped), then clarified further that basics shouldn't be skipped either — "it's better to look at everything." The project isn't only a vehicle for net-new software-engineering content.

**Alternatives considered:** Skipping re-explanation of basics while still teaching depth (this session's first attempt, superseded — user said they don't mind basics either); leaving "understood" topics as pure fast-forward/context-only mentions (rejected first, for the same underlying reason).

---

### 2026-08-20 — Context vault built before any project code

**Decision:** Create the full cross-session context structure ([[00-Hub]] and siblings) as an Obsidian vault before writing V0.1 of the AI Research Lab.

**Why:** User explicitly wants any future Claude session (or human) to be able to pick up full context without re-deriving the philosophy, architecture, or progress. Chose graph-linked markdown nodes over a single flat doc so relationships (philosophy → decisions → architecture) are navigable and visualizable.

**Alternatives considered:** Notion (rejected for now — requires OAuth the user hasn't set up, and this session can't complete that flow); single flat `PROJECT_STATE.md` (rejected — user specifically asked for "nodes or graph," which flat files don't give).

---

### 2026-08-20 — Obsidian chosen over Notion or plain markdown

**Decision:** Vault format is Obsidian-style markdown with `[[wikilinks]]` in a `context/` folder.

**Why:** Zero setup (just open the folder in Obsidian), wikilinks render as a graph natively, files remain plain markdown so they're readable/portable even without Obsidian installed.

**Alternatives considered:** Notion (needs connector auth, not available in this session); tool-agnostic plain markdown (loses automatic graph visualization for no real benefit since Obsidian was available as an option).
