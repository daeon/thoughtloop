# Changelog

## 1.0.0 — 2026-08-07

- Consolidated the pack around one adaptive graph and shared observable contracts.
- Added canonical `gapfinder`, `discover`, `investigate`, `decide`, `verify`, `review`, `revise`, `handoff`, `evaluate`, and `standard-english` nodes.
- Removed duplicate capability names and made the canonical nodes the only supported public surface.
- Added graph examples, budget policy, and graph validation.
- Refreshed the README around a popular GitHub README structure with clearer positioning, navigation, architecture, quick start, subagent budgets, and project links.
- Added repository contribution and security guidance.
- Added a GitHub Actions validation workflow for pushes and pull requests.
- Removed duplicate marketplace metadata and the obsolete one-time deployment guide.
- Removed the deprecated legacy entry-point alias and all references to the old orchestrator name.
- Bumped the plugin version to `1.0.0` for the cohesive graph and removed duplicate entry points.

## 0.4.0 — 2026-08-07

- Simplified every skill while preserving role boundaries, evidence rules, and failure-depth routing.
- Added explicit, budget-aware ThoughtLoop subagent mode with narrow fresh-context delegation.
- Simplified orchestration references and made the state contract optional guidance rather than a required schema.
- Updated the README, plugin metadata, and validation expectations.

## 0.3.0 — 2026-08-07

- Rebranded the project as **ThoughtLoop**.
- Added the public tagline: **Think wider. Build better. Prove it.**
- Renamed the original primary orchestrator to `thoughtloop`.
- Updated plugin/marketplace metadata, examples, README, installer validation, and repository guidance for GitHub publication.
- Preserved the **Discover → Decide → Execute → Prove** architecture and all v0.2.0 failure-depth routing semantics.

## 0.2.0 — 2026-08-07

- Reframed the architecture as **Discover → Decide → Execute → Prove**.
- Added deliberate solution-space search, framing challenge, and evidence-backed selection within the owning graph nodes.
- Added independent `exploration_level` and `verification_risk` routing axes.
- Added failure-depth classification: IMPLEMENTATION, STRATEGY, ASSUMPTION_OR_FRAME, EVIDENCE_GAP, CONTRADICTION_OR_LIMIT.
- Added bounded strategic backtracking and anti-oscillation rules.
- Extended failure routing to distinguish deeper failures instead of blindly requesting another edit.
- Extended loop metrics and sample logs with exploration, experiment, backtrack, and approach-switch signals.
- Added solution-space-search and failure-depth reference contracts.

## 0.1.0 — 2026-08-07

- Initial skills-only Codex plugin.
- Added seven composable skills.
- Added PASS / FAIL / UNKNOWN verdict semantics.
- Added evidence ladder, bounded retries, no-progress detection, and regression protection.
- Added a standard-library pack validator and loop-metrics script.
