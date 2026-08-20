# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault ([[00-Hub]] and siblings) is built. Nothing else has started.

**Next action:** Begin V0.1 per [[03-Roadmap]]:

1. Explain why the project folder/environment is being set up the way it is.
2. Create `Project/lab/` for the actual application.
3. Set up a Python virtual environment (`python -m venv .venv`) inside it, explained from first principles per [[01-Philosophy]] hard rule 4 — what it is, why isolation matters, activation, `pip`.
4. Verify Python/pip versions.
5. Give the first tiny implementation task: a static AI Research Lab page with Models / Datasets / Experiments sections and one button that changes something on the page — HTML first, taught chunk by chunk per [[01-Philosophy]] hard rule 2, before any CSS or JS.

Do not install FastAPI, a database, Docker, or any framework yet — none of that is justified until a real problem in V0.1+ calls for it (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," and [[05-Concepts]] before ending the session.
