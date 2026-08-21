# Roadmap — Version Progression

A **direction, not a schedule** (per [[01-Philosophy]]). Versions advance only when the current one is actually understood, not on a timer. Each version should create the reason for the next one's tools — see [[06-Dependencies]].

## Current position

**V0.1 in progress.** HTML structure done (skeleton + Models/Datasets/Experiments sections + button). CSS started: external stylesheet linked, cascade and box model introduced via two real rules, confirmed in DevTools. Live detail in [[08-Next-Step]].

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
