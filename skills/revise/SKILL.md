---
name: revise
description: Classify evidence-backed failures and route the smallest safe correction to implementation, strategy, assumptions, evidence, or escalation.
---

# Revise

Classify the problem as one of:

- `IMPLEMENTATION`: strategy is sound but the artifact is wrong;
- `STRATEGY`: the approach is structurally poor or uneconomic;
- `ASSUMPTION_OR_FRAME`: a premise or problem boundary was falsified;
- `EVIDENCE_GAP`: correctness is not established;
- `CONTRADICTION_OR_LIMIT`: requirements, tools, authority, or budget conflict.

Route to `builder`, `decide`, `discover`/`investigate`, `verify`, or escalation accordingly. For a local revision, protect passing criteria, state regression checks, and avoid unrelated cleanup. If two local corrections do not resolve a blocker, backtrack instead of repeating the same patch.

Return a `RouteDecision`, not an unrequested implementation.
