# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. **V0.1 is complete.** `lab/index.html`/`style.css`/`script.js` together implement the full original goal: three sections (Models/Datasets/Experiments) plus an interactive button, styled with real CSS (box model, flexbox, media queries, hover/transitions) and made genuinely dynamic with JS — each section's list renders from a JS array via a loop + `createElement`/`appendChild`, not hardcoded HTML. Full concept log for this (long, dense) session in [[05-Concepts]], including three real bugs hit and understood, not just fixed: a `button :hover` space bug, a `textContent` assignment placed outside its callback, and a duplicate-function-name mixup.

**If you're picking this up on the other PC:** clone the repo first (`git clone https://github.com/ShayanJafri20/Ai-Research-Lab.git`), then open the folder in Claude Code — `CLAUDE.md` will point you back to this vault automatically. Run `git pull` before starting work each session, and `git add . && git commit && git push` at the end of one, on whichever machine you used, so the other machine doesn't fall behind. **Note:** history was rewritten on 2026-08-22 to strip an unwanted commit trailer — if a machine hasn't done the one-time `git fetch && git reset --hard origin/main` fixup yet, do that before a normal `git pull`, or it'll try to merge two diverged histories.

**Next action:** Start **V0.2** (deeper DOM + browser interaction) per [[03-Roadmap]]. A lot of V0.2 territory got touched organically during V0.1's JS work already (querySelector, addEventListener, textContent, createElement/appendChild) — so this isn't starting from zero. Genuine remaining gaps to reach for, driven by a real next problem rather than dumped all at once:
1. More event types beyond `click` (e.g. keyboard/input events), and the **event object** itself (`event.target`, etc.) — not touched yet.
2. `classList.add`/`.remove`/`.toggle` — using JS to toggle a CSS *class* instead of directly overwriting inline styles/text, a cleaner pattern than what the button's toggle currently does by comparing `textContent` strings.
3. Remaining JS language fundamentals never exercised: destructuring, spread/rest, `async`/`await`, `fetch()` (this one's real trigger is more V0.3/V0.9-shaped — pulling data from an actual server instead of a hardcoded array — don't force it early).
4. CSS Grid and `inline`/`inline-block` are deliberately still deferred — see [[09-Ideas-Backlog]].

Keep the same rhythm: one property/concept at a time, predict → change → refresh → inspect in DevTools, let the user attempt before handing over code (hard rule 6) — though today showed it's fine to write something directly when explicitly asked, as happened with the Experiments section.

**Correction (2026-08-20):** a Python virtual environment was previously listed as a V0.1 step — that was wrong and got caught before doing it. V0.1 has zero Python in it (pure static HTML/CSS/JS). A venv isolates Python packages; there's nothing to isolate yet. It belongs at **V0.3**, when a raw Python HTTP server first appears — not before. See [[04-Decisions]].

Do not install FastAPI, a database, Docker, a venv, or any framework yet — none of that is justified until a real problem in V0.1+ calls for it (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," and [[05-Concepts]] before ending the session.
