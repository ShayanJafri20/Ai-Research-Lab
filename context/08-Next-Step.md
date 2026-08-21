# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. V0.1 HTML structure is done: `lab/index.html` has the doctype/html/head/title/body/h1 skeleton plus three `<section>`s (Models/Datasets/Experiments, each with an `<h2>`) and one `<button>`. CSS has started: `lab/style.css` exists and is linked via `<link rel="stylesheet">`, with two rules so far — `h1 { color: orange; }` and `section { margin-bottom: 40px; }`. Confirmed working via DevTools (Elements → Computed/Layout box-model diagram matched the CSS exactly). See [[05-Concepts]] for the full concept log from this session (cascade, box model, DevTools Network tab, HTTP status codes/caching preview).

**If you're picking this up on the other PC:** clone the repo first (`git clone https://github.com/ShayanJafri20/Ai-Research-Lab.git`), then open the folder in Claude Code — `CLAUDE.md` will point you back to this vault automatically. Run `git pull` before starting work each session, and `git add . && git commit && git push` at the end of one, on whichever machine you used, so the other machine doesn't fall behind.

**Next action:** Continue the CSS chunk on `lab/style.css` (box model / cascade already introduced, keep building on them):

1. Fix the gap noted but left unaddressed: there's no space between `<h1>` and the first `<section>` (only `margin-bottom` was used, nothing above). Add `margin-top` somewhere (on `h1`, or on `section`) to fix it — let the user attempt this first per hard rule 6.
2. From there, natural next small steps (pick one, don't dump all at once): `padding` on the sections (text currently sits flush against the page edge), or a `background-color`/`border` to visually distinguish each section, or basic `font-family`/typography on `body`.
3. Keep it one property/concept at a time, predict → change → refresh → inspect in DevTools, same rhythm as this session.

**Correction (2026-08-20):** a Python virtual environment was previously listed as a V0.1 step — that was wrong and got caught before doing it. V0.1 has zero Python in it (pure static HTML/CSS/JS). A venv isolates Python packages; there's nothing to isolate yet. It belongs at **V0.3**, when a raw Python HTTP server first appears — not before. See [[04-Decisions]].

Do not install FastAPI, a database, Docker, a venv, or any framework yet — none of that is justified until a real problem in V0.1+ calls for it (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," and [[05-Concepts]] before ending the session.
