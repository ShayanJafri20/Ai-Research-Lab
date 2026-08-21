# Architecture — Current State

Living document. Update this every time a layer is added — it should always reflect what's **actually built**, not what's planned (planned lives in [[03-Roadmap]]).

Governed by [[01-Philosophy]] hard rule 7 (one layer below current abstraction) and rule 8 (earn every layer).

## Status: V0.1 in progress

`lab/index.html`: full V0.1 HTML structure — doctype/html/head/title/body/h1, plus three `<section>`s (Models/Datasets/Experiments, each with `<h2>`) and one `<button>`. `lab/style.css` exists, linked via `<link rel="stylesheet">`, with two rules (`h1` color, `section` margin-bottom) — first real CSS chunk (cascade + box model) in progress. No JS yet. Taught chunk-by-chunk per [[01-Philosophy]] hard rule 2; concepts logged in [[05-Concepts]].

## Current stack

| Layer | Technology | Status |
|---|---|---|
| Frontend | static HTML + CSS | HTML structure done; CSS started (cascade, box model) — see [[08-Next-Step]] for next CSS chunk |
| Backend | none yet | not started |
| Database | none yet | not started |
| Cache | none yet | not started |
| Queue / Workers | none yet | not started |
| Training / Inference | none yet | not started |
| DevOps / Deployment | none yet | not started |

See [[06-Dependencies]] for the installed-package record once it starts filling in.

## Planned folder layout (created when V0.1 starts, not before)

```
Project/
  context/     <- this vault (already exists)
  lab/         <- AI Research Lab application code
  sandbox/     <- Learning Sandbox experiments (see [[07-Sandbox-Log]])
```

## Diagram (target end-state, from [[01-Philosophy]] success criterion)

```
Browser → DOM → JavaScript → HTTP → Backend → Database → Cache → Queue → Worker → GPU → Model
```

Each arrow above becomes real (and gets its own section here) as the corresponding roadmap version in [[03-Roadmap]] is reached.
