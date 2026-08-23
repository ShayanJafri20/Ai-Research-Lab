# Ideas Backlog

Concepts/tools the user flagged as wanting to learn eventually, but that don't have a current problem triggering them yet (per [[01-Philosophy]] hard rule 3). Checked whenever a new roadmap version is being planned, in case one of these now has a real reason to slot in. Referenced from [[00-Hub]].

| Date added | Idea | Why it's not "now" | Resolved (roadmap version / sandbox / dropped) |
|---|---|---|---|
| 2026-08-23 | CSS Grid (2D layout — rows and columns together) | Flexbox already solved the only layout problem this page had (three sections in a row); no real 2D-layout need exists yet to justify it | *(open)* |
| 2026-08-23 | `display: inline` / `inline-block` | No current element needs inline flow with box-model control; noted conceptually, not exercised hands-on | *(open)* |
| 2026-08-23 | LoRA / QLoRA (parameter-efficient fine-tuning) | Solves "fine-tune a large pretrained model without the compute to fully retrain it" — no large pretrained model exists yet to have this problem with. Real trigger: once past V1.3/V1.5, working with a model big enough that full fine-tuning is actually expensive. | *(open)* |
| 2026-08-23 | Apache Airflow (pipeline orchestration) | ETL (V0.9) will start as a manually-run script — no scheduling/multi-step-dependency/retry problem exists yet. Real trigger: wanting the pipeline to run automatically, or needing to see which of several dependent steps failed and why. Plausible around V0.9-V1.6 (post-renumber). | *(open)* |
| 2026-08-23 | Hadoop (HDFS/MapReduce) | Solves "data too large for one machine." Honest assessment, not just deferred: this project's actual data scale (personal research lab, own models/datasets/experiments) is very unlikely to ever organically need it — unlike the other rows here, this may never get a real trigger. If genuinely wanted, better suited to a standalone sandbox exploration than waiting for a need that likely won't arrive. Spark is the more realistic modern angle if distributed data processing ever becomes relevant. | *(open — likely permanent, see note)* |
