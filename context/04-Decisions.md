# Decisions Log

Append-only. Newest entry at the top. Each entry: date, decision, why, alternatives considered. Referenced from [[00-Hub]].

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
