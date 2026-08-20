# Roadmap — Version Progression

A **direction, not a schedule** (per [[01-Philosophy]]). Versions advance only when the current one is actually understood, not on a timer. Each version should create the reason for the next one's tools — see [[06-Dependencies]].

## Current position

**Not started.** Next: V0.1. Live detail in [[08-Next-Step]].

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

## Notes

- CNN architectures (AlexNet, ResNet) are already used in practice per user background, but still get **full coverage** (basics as a fast refresher, then depth — math, tensor shapes, implementation) when the vision track resumes; reinforcement of known ML material is explicitly wanted, not just net-new SWE content. See [[05-Concepts]].
- Later stages (MongoDB comparison, Power BI dashboards, DSA, Kubernetes) are woven in opportunistically per [[01-Philosophy]], not as separate standalone versions — see that file's data engineering, Power BI, and DSA sections for how each gets introduced.
- Update the "Current position" section above at the end of every session that changes it.
