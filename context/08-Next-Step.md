# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault ([[00-Hub]] and siblings) is built and pushed to a private GitHub repo (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. Nothing else has started.

**If you're picking this up on the other PC:** clone the repo first (`git clone https://github.com/ShayanJafri20/Ai-Research-Lab.git`), then open the folder in Claude Code — `CLAUDE.md` will point you back to this vault automatically. Run `git pull` before starting work each session, and `git add . && git commit && git push` at the end of one, on whichever machine you used, so the other machine doesn't fall behind.

**Next action:** Begin V0.1 per [[03-Roadmap]]:

1. Explain why the project folder is being set up the way it is.
2. Create `Project/lab/` for the actual application.
3. Give the first tiny implementation task: a static AI Research Lab page with Models / Datasets / Experiments sections and one button that changes something on the page — HTML first, taught chunk by chunk per [[01-Philosophy]] hard rule 2, before any CSS or JS.

**Correction (2026-08-20):** a Python virtual environment was previously listed as a V0.1 step — that was wrong and got caught before doing it. V0.1 has zero Python in it (pure static HTML/CSS/JS). A venv isolates Python packages; there's nothing to isolate yet. It belongs at **V0.3**, when a raw Python HTTP server first appears — not before. See [[04-Decisions]].

Do not install FastAPI, a database, Docker, a venv, or any framework yet — none of that is justified until a real problem in V0.1+ calls for it (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," and [[05-Concepts]] before ending the session.
