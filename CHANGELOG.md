# Changelog

## 0.3.0 — 2026-08-07

- Rebranded the project as **ThoughtLoop**.
- Added the public tagline: **Think wider. Build better. Prove it.**
- Renamed the primary orchestrator from `self-correction` to `thoughtloop`.
- Added an explicit-only deprecated `self-correction` compatibility alias.
- Updated plugin/marketplace metadata, examples, README, installer validation, and repository guidance for GitHub publication.
- Preserved the **Discover → Decide → Execute → Prove** architecture and all v0.2.0 failure-depth routing semantics.

## 0.2.0 — 2026-08-07

- Reframed the architecture as **Discover → Decide → Execute → Prove**.
- Added `explorer` for deliberate solution-space search and idea-graph coverage.
- Added `challenger` for pre-commitment assumption and framing attacks.
- Added `synthesizer` for explicit tradeoff-based selection and BUILD / EXPERIMENT / EXPLORE routing.
- Added independent `exploration_level` and `verification_risk` routing axes.
- Added failure-depth classification: IMPLEMENTATION, STRATEGY, ASSUMPTION_OR_FRAME, EVIDENCE_GAP, CONTRADICTION_OR_LIMIT.
- Added bounded strategic backtracking and anti-oscillation rules.
- Extended Revision Manager to route deeper failures instead of blindly requesting another edit.
- Extended Loop Evaluator and sample logs with exploration, experiment, backtrack, and approach-switch metrics.
- Added solution-space-search and failure-depth reference contracts.

## 0.1.0 — 2026-08-07

- Initial skills-only Codex plugin.
- Added seven composable skills.
- Added PASS / FAIL / UNKNOWN verdict semantics.
- Added evidence ladder, bounded retries, no-progress detection, and regression protection.
- Added a standard-library pack validator and loop-metrics script.
