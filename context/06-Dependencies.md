# Dependencies — Installed Tools & Why

Every tool/package gets a row **only after** it's been justified per [[01-Philosophy]] hard rule 3 (explain the problem → explain the tool → install → verify → smallest example → integrate) and actually installed. Nothing goes here speculatively. Referenced from [[00-Hub]] and [[02-Architecture]].

| Tool / Package | Version | Purpose | Introduced (roadmap version) | Date | Why (link to [[04-Decisions]] entry if applicable) |
|---|---|---|---|---|---|
| Git | 2.55 | Version control — sync the whole project (context vault + future code) between two machines with real history and conflict resolution, instead of manually copying files | pre-V0.1 (infrastructure, not a roadmap version) | 2026-08-20 | [[04-Decisions]] "Git + private GitHub repo chosen for multi-machine work" |
| Obsidian | (installed by user) | Renders the `context/` vault's `[[wikilinks]]` as a navigable graph | pre-V0.1 (infrastructure) | 2026-08-20 | [[04-Decisions]] "Obsidian chosen over Notion or plain markdown" |
| Python venv (`lab/.venv`) | Python 3.14.6 | Isolates this project's future `pip install`s from the system Python and any other project — created empty, no packages installed yet beyond bundled `pip` | V0.3 (first Python code — the raw HTTP server) | 2026-08-24 | Genuinely justified now per hard rule 4; previously removed from V0.1 for being premature, see [[04-Decisions]] "Removed premature venv step from V0.1" |
