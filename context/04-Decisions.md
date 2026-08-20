# Decisions Log

Append-only. Newest entry at the top. Each entry: date, decision, why, alternatives considered. Referenced from [[00-Hub]].

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
