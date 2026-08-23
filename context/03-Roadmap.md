# Roadmap — Version Progression

A **direction, not a schedule** (per [[01-Philosophy]]). Versions advance only when the current one is actually understood, not on a timer. Each version should create the reason for the next one's tools — see [[06-Dependencies]].

## Current position

**V0.1 complete.** HTML structure, full CSS (box model, flexbox, media queries, transitions), and a real JS foundation (variables/arrays/objects/loops/functions/DOM manipulation) all working together — the button is interactive and all three sections render from JS arrays. Next: **V0.2** (deeper DOM/browser interaction). Live detail in [[08-Next-Step]].

## Progression

| Version | Focus |
|---|---|
| V0.1 | HTML + CSS + JavaScript — static AI Research Lab page (Models / Datasets / Experiments sections, one interactive button) |
| V0.2 | DOM + browser interaction |
| V0.3 | HTTP fundamentals + tiny raw Python HTTP server |
| V0.4 | FastAPI |
| V0.5 | PostgreSQL |
| V0.6 | SQL + migrations + indexes |
| V0.7 | Dataset Explorer |
| V0.8 | Pandas + EDA |
| V0.9 | ETL |
| V1.0 | RNN research lab (NLP track begins) |
| V1.1 | LSTM / GRU |
| V1.2 | Attention |
| V1.3 | Transformer |
| V1.4 | Experiment tracking |
| V1.5 | Redis / caching |
| V1.6 | Background jobs |
| V1.7 | WebSockets |
| V1.8 | Model registry |
| V1.9 | Inference server |
| V2.0 | Distributed training |
| V2.1 | Docker / CI-CD |
| V2.2 | Cloud deployment |
| V2.3 | Monitoring |
| V2.4 | Multimodal research lab |

## Why this order (each arrow is a "this broke, so we need that" moment, not a schedule)

```
V0.1 Static HTML/CSS/JS
     -> page is fake: nothing changes, nothing persists, nothing computes
     v  problem: a button that does nothing isn't an app

V0.2 DOM + browser interaction (JavaScript)
     -> button can change the page, but only using data typed into the HTML/JS itself
     v  problem: nothing lives anywhere outside the browser tab

V0.3 HTTP + tiny raw Python server
     -> page can talk to a program outside itself, but a hand-written server gets
        messy fast (manual parsing, no routing conventions)
     v  problem: real APIs need structure a raw socket server doesn't give you

V0.4 FastAPI
     -> clean routes/validation, but every value lives in a Python variable and
        vanishes on restart
     v  problem: no persistence

V0.5 PostgreSQL
     -> data survives a restart, but growing data needs real query/schema tooling
     v  problem: raw SQL without indexes/migrations doesn't scale or evolve safely

V0.6 SQL, migrations, indexes -> data layer solid; this is where real research
     content can start, because there's finally somewhere to put it

V0.7-V0.9 Dataset Explorer -> Pandas/EDA -> ETL
     -> need to actually look at and clean data before training on it

V1.0-V1.3 RNN -> LSTM/GRU -> Attention -> Transformer
     -> each architecture is introduced because the previous one has a specific,
        teachable failure mode (RNNs forget long sequences -> gating fixes that ->
        sequential processing is slow/still bottlenecked -> attention looks at
        everything at once -> generalizing that gives a Transformer)

V1.4 Experiment tracking
     -> once several architectures/hyperparams are tried, eyeballing results stops working

V1.5-V1.7 Redis/caching -> Background jobs -> WebSockets
     -> training takes real time: can't block an HTTP request for minutes (-> jobs),
        want live progress instead of refreshing (-> WebSockets); caching shows up
        wherever something slow gets asked for repeatedly

V1.8-V1.9 Model registry -> Inference server
     -> trained models pile up unorganized -> need to store/version them, then serve
        predictions from one

V2.0 Distributed training -> a single GPU becomes the bottleneck for bigger models/datasets

V2.1 Docker/CI-CD -> "works on my machine" becomes a real problem the moment more
     than one environment is involved (same root issue as syncing this project
     across two PCs, but for the runtime instead of files)

V2.2-V2.4 Cloud -> Monitoring -> Multimodal research lab
     -> local hardware runs out of room -> running services need observability ->
        the research itself expands past text into vision/audio
```

If a version turns out to need something unexpected, the chain adjusts right there rather than forcing the next box on the list — see [[09-Ideas-Backlog]] for concepts flagged along the way that don't have a trigger yet.

## Concept depth checklists (added 2026-08-21)

User goal is full understanding of what's happening underneath, not just shipping features — see [[04-Decisions]] "Gap-check against external web-dev roadmap." These expand the one-line roadmap rows above into sub-concepts so nothing gets silently skipped across a many-session project. Track actual coverage in [[05-Concepts]], not here — this is the checklist, not the log.

- **V0.1 — HTML:** elements/tags/attributes, nesting, document structure, semantic HTML, forms, inputs, buttons, links, images, tables, lists, **accessibility basics** (tie this to whenever semantic HTML/forms are introduced — it rarely breaks loudly enough to force itself in via hard rule 3, so it needs to be deliberate), HTML parsing → DOM.
- **V0.1 — CSS** (previously just "add CSS," no breakdown): selectors, cascade, specificity, inheritance, box model (content/padding/border/margin), `display` (block/inline/inline-block/flex/grid), position, flexbox, grid, colors, fonts, units, responsive design, media queries, animations/transitions.
- **V0.1/V0.2 — JavaScript, split into two layers** (previously flattened into one line):
  - Language fundamentals: variables (`let`/`const`/`var`), types, operators, conditionals, loops, functions, scope, closures, objects, arrays, destructuring, spread/rest, modules, classes.
  - Browser API layer (V0.2): DOM methods (`querySelector`, `createElement`, `textContent`, `classList`), events, event loop, call stack, Web APIs, Promises, `async`/`await`, `fetch()`.
- **V0.3 — HTTP fundamentals**, unpacked: URL anatomy, DNS, IP, client/server model, request anatomy (method/headers/body), response anatomy (status code/headers/body), the status code families (2xx/3xx/4xx/5xx), HTTP vs HTTPS.
- **V0.4+ — Auth/sessions** (not currently anywhere in the roadmap): cookies, sessions, tokens, CORS. Deliberately deferred, not forgotten — this single-user app has no login yet, so hard rule 3 has nothing to justify it. Likely real trigger: V0.9 ETL pulling an external dataset API that needs a key/token. Revisit then, not before.

## Notes

- CNN architectures (AlexNet, ResNet) are already used in practice per user background, but still get **full coverage** (basics as a fast refresher, then depth — math, tensor shapes, implementation) when the vision track resumes; reinforcement of known ML material is explicitly wanted, not just net-new SWE content. See [[05-Concepts]].
- Later stages (MongoDB comparison, Power BI dashboards, DSA, Kubernetes) are woven in opportunistically per [[01-Philosophy]], not as separate standalone versions — see that file's data engineering, Power BI, and DSA sections for how each gets introduced.
- A dedicated frontend-framework track (React/TypeScript/Tailwind/Next.js) was considered on 2026-08-21 and explicitly **not** added — decided later, per hard rule 3, only if a real problem in the project ever calls for it. See [[04-Decisions]].
- Update the "Current position" section above at the end of every session that changes it.
