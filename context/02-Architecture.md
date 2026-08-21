# Architecture — Current State

Living document. Update this every time a layer is added — it should always reflect what's **actually built**, not what's planned (planned lives in [[03-Roadmap]]).

Governed by [[01-Philosophy]] hard rule 7 (one layer below current abstraction) and rule 8 (earn every layer).

## Status: V0.1 in progress

`lab/index.html` exists with the minimal required HTML skeleton (doctype, `<html lang="en">`, `<head>`/`<title>`, `<body>`/`<h1>`). Verified working — opened in a browser on both machines, tab and page content matched prediction. No CSS, no JavaScript, no sections/button content yet — those are next within V0.1.

## Current stack

| Layer | Technology | Status |
|---|---|---|
| Frontend | Static HTML (`lab/index.html` — skeleton only) | in progress (V0.1) |
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
