# Next Step

The single current action. Overwrite this at the end of every session — it should always answer "what do we do the moment this reconvenes." Linked from [[00-Hub]].

## Right now

The context vault is on GitHub (`https://github.com/ShayanJafri20/Ai-Research-Lab`, branch `main`) — see [[04-Decisions]] and [[06-Dependencies]]. V0.1 HTML structure is done: `lab/index.html` has the doctype/html/head/title/body/h1 skeleton, three `<section>`s (Models/Datasets/Experiments) wrapped in a `<div class="sections">`, and one `<button>`. CSS (`lab/style.css`) now covers: `h1` color, `section` box model (margin/padding/background-color), two class-selector overrides (`.Models`, `.Datasets`), `body { font-family }` with a proper fallback stack, and `.sections { display: flex; gap: 30px; }` laying the three sections out in a row instead of stacked. Concepts covered this session: margin collapsing (including the asymmetric case), class selectors vs. type selectors, cascade vs. specificity vs. inheritance (three distinct things, now clearly separated for the user), `display: block` default, flexbox basics, and why collapsing stops applying to flex items. Full detail in [[05-Concepts]].

**If you're picking this up on the other PC:** clone the repo first (`git clone https://github.com/ShayanJafri20/Ai-Research-Lab.git`), then open the folder in Claude Code — `CLAUDE.md` will point you back to this vault automatically. Run `git pull` before starting work each session, and `git add . && git commit && git push` at the end of one, on whichever machine you used, so the other machine doesn't fall behind. **Note:** history was rewritten on 2026-08-22 to strip an unwanted commit trailer — if a machine hasn't done the one-time `git fetch && git reset --hard origin/main` fixup yet, do that before a normal `git pull`, or it'll try to merge two diverged histories.

**Next action:** Continue building on flexbox in `lab/style.css` — natural next small steps (pick one, don't dump all at once):
1. `justify-content` / `align-items` on `.sections` — control how the row of boxes is distributed/aligned, now that there's extra empty space to the right of "Experiments."
2. Style the `<button>` (still fully unstyled, plain browser default) — either a new `button { }` type-selector rule, or fold it into the flex layout too.
3. Revisit the CSS depth checklist in [[03-Roadmap]] for what's still untouched: specificity as a formal point system (only used informally so far), units beyond `px` (em/rem/%), position, media queries/responsive design.

Keep the same rhythm: one property/concept at a time, predict → change → refresh → inspect in DevTools.

**Correction (2026-08-20):** a Python virtual environment was previously listed as a V0.1 step — that was wrong and got caught before doing it. V0.1 has zero Python in it (pure static HTML/CSS/JS). A venv isolates Python packages; there's nothing to isolate yet. It belongs at **V0.3**, when a raw Python HTTP server first appears — not before. See [[04-Decisions]].

Do not install FastAPI, a database, Docker, a venv, or any framework yet — none of that is justified until a real problem in V0.1+ calls for it (hard rule 3).

## After that

Update this file, [[02-Architecture]], [[03-Roadmap]] "current position," and [[05-Concepts]] before ending the session.
