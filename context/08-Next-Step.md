# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. **V0.1 and V0.2 are both complete.** V0.1: full HTML/CSS/JS static page with an interactive button and dynamic array-driven rendering (see prior entry below for detail). V0.2 (2026-08-24): `classList`, the event object (`event.target`), event bubbling/delegation (one listener on `.model-list` handling clicks on dynamically-created `<li>`s), duplicated render loops refactored into one shared `renderList` function using `Array.map`, and destructuring/spread/rest. Full detail in [[05-Concepts]]. The async/Promises/`fetch()` cluster was correctly *not* forced into V0.2 — no real server exists yet to fetch from, so it waits for V0.3 by design, not as debt.

**One loose end, not urgent:** `lab/script.js` still has scratch demo lines at the bottom (the destructuring/spread/rest examples used to learn the concepts, e.g. `console.log(addModels("GPT", "BERT"))`) that aren't part of the app's real logic. Worth a quick delete-not-comment cleanup pass next time, same reasoning as the mid-session cleanup already done once this project (git remembers everything, dead code is just clutter).

**If you're picking this up on the other PC:** clone the repo first (`git clone https://github.com/ShayanJafri20/Ai-Research-Lab.git`), then open the folder in Claude Code — `CLAUDE.md` will point you back to this vault automatically. Run `git pull` before starting work each session, and `git add . && git commit && git push` at the end of one, on whichever machine you used, so the other machine doesn't fall behind. **Note:** history was rewritten on 2026-08-22 to strip an unwanted commit trailer — if a machine hasn't done the one-time `git fetch && git reset --hard origin/main` fixup yet, do that before a normal `git pull`, or it'll try to merge two diverged histories.

**Next action:** Start **V0.3** (HTTP fundamentals + a tiny raw Python HTTP server) per [[03-Roadmap]]. This is the first time the project stops being "just a webpage" and starts talking to an actual backend program. Per hard rule 4, this is also where a Python virtual environment genuinely belongs for the first time (not before — see the 2026-08-20 correction below) — explain *why* isolation matters before creating it, then `python -m venv .venv`. Concept-depth checklist for V0.3 already exists in [[03-Roadmap]]: URL anatomy, DNS, IP, client/server model, request/response anatomy, status code families, HTTP vs HTTPS — much of this got an early informal preview via the DevTools Network tab back in V0.1, so it's reinforcement more than first exposure for some of it.

**Correction (2026-08-20):** a Python virtual environment was previously listed as a V0.1 step — that was wrong and got caught before doing it. V0.1 has zero Python in it (pure static HTML/CSS/JS). A venv isolates Python packages; there's nothing to isolate yet. It belongs at **V0.3**, when a raw Python HTTP server first appears — not before. See [[04-Decisions]].

Do not install FastAPI, a database, Docker, a venv, or any framework yet — none of that is justified until a real problem in V0.1+ calls for it (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," and [[05-Concepts]] before ending the session.
