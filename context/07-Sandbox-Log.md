# Sandbox Log

Index of small, disposable experiments used to unblock a confusing concept encountered in the main project, per [[01-Philosophy]] ("main project vs sandbox"). Code lives under `sandbox/` (created on first use); this file just indexes what was explored and what it resolved.

| Date | Concept explored | Triggered by (main project context) | Resolved? |
|---|---|---|---|
| 2026-08-28 | Indexes/B-trees, measured directly: `EXPLAIN ANALYZE` on a throwaway 2M-row table, same `WHERE tag = ...` query before and after `CREATE INDEX` | V0.6 concept checklist — real project's tables (3-4 rows) are too small for an index to show any real effect, so the mechanism was demonstrated on synthetic scale instead of forced onto tiny real tables (hard rule 3) | Yes — measured 357ms (sequential scan) vs 0.15ms (bitmap index scan), ~2,400x. Table dropped after; no index added to the real project tables since none is justified yet. |
| 2026-08-28 | Transactions/atomicity: classic two-account money-transfer example, `rollback()` vs `commit()` on a throwaway table | V0.6 concept checklist — no real project route yet performs a multi-step write that would need transaction wrapping (all three routes are still read-only `SELECT`s), so demonstrated standalone rather than in `main.py` | Yes — showed a partially-applied update fully undone by `rollback()`, and the same two updates landing together after `commit()`. Noted for later: `main.py` routes should wrap multi-step writes in a transaction once any route actually does more than one write. |
