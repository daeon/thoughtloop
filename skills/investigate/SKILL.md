---
name: investigate
description: Perform read-only repository, debugging, log, or performance investigation with evidence, hypotheses, and next probes before implementation.
---

# Investigate

This is the shared investigation engine. Select one mode:

- `repository`: map entry points, components, owners, call paths, contracts, side effects, tests, and risks;
- `debugging`: reconstruct expected versus observed behavior, failure paths, hypotheses, counter-evidence, and falsifying probes;
- `logs`: normalize events into a timeline, correlate signals, redact secrets, and identify gaps;
- `performance`: define metric, workload, baseline, variance, hot path, resource boundary, and measurement plan before suggesting optimization.

Read-only is the default. Do not edit source, tests, configuration, or runtime state unless the user explicitly changes the task to implementation. Treat logs as sensitive and summarize high-volume data.

Return an `InvestigationReport` with scope, facts, evidence and provenance, hypotheses, ruled-out causes, unknowns, confidence limits, and next probes. Label implementation ideas as recommendations, not findings. In a graph, pass the report to `decide`, `verify`, or `builder` only after the relevant gate.
