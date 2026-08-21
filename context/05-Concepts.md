# Concepts — Knowledge State Tracker

Update this whenever a session reveals what the user does/doesn't understand. Drives how deep explanations in [[01-Philosophy]] hard rule 2 need to go. Referenced from [[00-Hub]].

## Understood (prior background — cover it anyway, just move faster)

- Python, NumPy, Pandas, scikit-learn, PyTorch basics
- Core ML/DL concepts, model training loop
- CNN architectures: AlexNet, ResNet
- NLP/Transformer concepts, attention (conceptual level — depth to confirm when V1.0–V1.3 is reached)

**Note (2026-08-20, updated 2026-08-20):** "Understood" does not mean skip. User wants full coverage — basics included — for AI/ML topics when the roadmap reaches them, not just software engineering content; reinforcing known material strengthens understanding rather than wasting time ("it's better to look at everything"). The only thing "understood" changes is pacing: basics move faster as a refresher instead of a first exposure, and depth (math, tensor shapes, implementation) still gets covered even on architectures already used in practice. Treat the depth side the same as [[01-Philosophy]] hard rule 7 (one layer below the current abstraction).

## Partially understood

*(none logged yet)*

## Struggling / weak — treat as new even if previously exposed

- General software engineering fluency (self-reported): writing moderately complex code without heavy debugging, problem decomposition, reading unfamiliar code, software architecture
- Standard programming constructs not yet confirmed: decorators, classes/inheritance, generators/iterators, context managers, modules/packages, virtual envs, async/await, closures, type hints, HTTP, processes/threads, event loops — see [[01-Philosophy]] hard rule 1

## Log

| Date | Concept | Status | Notes |
|---|---|---|---|
| 2026-08-21 | HTML skeleton (doctype, `<html>`, `<head>`/`<title>`, `<body>`) | Partially understood | Couldn't write it unassisted on first try ("I don't know the code") — built together line by line with explanation per line. Predict-run-inspect succeeded afterward (correctly matched tab vs. page content on both machines). Re-attempt writing structure unassisted next time a similar skeleton is needed, before calling this fully understood. |
| 2026-08-20 | Git core mechanics (working directory / staging / repo, `add`/`commit`/`push`/`pull`, `.gitignore`) | Understood | Confirmed after a from-scratch walkthrough — first pass moved too fast (jumped straight to commands without the mental model), second pass slowed down and it landed. Branches/merges/PRs still unconfirmed — see [[01-Philosophy]] hard rule 3, deferred to first real multi-machine divergence. |
| 2026-08-21 | Git merge conflicts (real, not staged) | Resolved, not yet taught | Two parallel Claude Code sessions (this one and one on the other PC) both independently pushed vault edits without either pulling first, causing a genuine divergence in `02-Architecture.md`/`03-Roadmap.md`. Resolved by fetching, merging, hand-resolving the conflict markers (both sides' content was complementary, kept both), and pushing the merge commit — but this was done *for* the user, not explained step-by-step yet. Owe a proper walkthrough of what a conflict marker means and why it happens next time it's relevant. Practical takeaway to state explicitly: avoid running two Claude Code sessions on this project across machines without a pull in between. |
| 2026-08-20 | (vault created, no teaching session yet) | — | — |
| 2026-08-21 | HTML basics: `<!DOCTYPE html>`, `<html lang>`, `<head>`, `<title>`, `<body>`, `<h1>` | Taught, re-explained | Skeleton was built in a prior session but not retained by the next one ("forgot about this html code") — re-taught chunk by chunk with MDN links. Watch for retention on a third pass before marking fully Understood. |
| 2026-08-21 | `<section>`/`<h2>`/`<button>` added to `lab/index.html`; user attempted the skeleton but wasn't confident writing it blind, so it was written directly and explained chunk by chunk (hard rule 6 escalation) | Taught | |
| 2026-08-21 | Misconception caught and corrected: "HTML does nothing without CSS/JS." Rendered page in browser and saw default bold/bordered styling with zero authored CSS — corrected via the user-agent stylesheet concept (browser ships default CSS for every tag) and the distinction between browser-default vs. custom behavior for JS. Good sign: user is reasoning from what they actually observe in the browser (hard rule 5), not just accepting explanations. | Corrected | Natural lead-in to the CSS phase — the real problem CSS solves is overriding these generic defaults, not "adding style from nothing." |
| 2026-08-21 | External stylesheet linking: `<link rel="stylesheet" href="...">`, three ways to attach CSS (inline/internal/external) | Attempted solo, correct | User wrote the `<link>` tag and created the empty `lab/style.css` file themselves without help — first fully independent edit this project (hard rule 6 ratio moving the right direction). |
| 2026-08-21 | DevTools Network tab; HTTP status codes preview (`200` vs `304 Not Modified`, browser caching) | Introduced, live example seen | Predicted `200`, actually saw `304` on a repeat refresh — used as a real predict/observe/explain moment (hard rule 5) rather than a mismatch to gloss over. Early preview of concepts formally scheduled for V0.3 in [[03-Roadmap]]'s HTTP checklist; revisit there for full depth (headers, request/response anatomy, status code families). |
