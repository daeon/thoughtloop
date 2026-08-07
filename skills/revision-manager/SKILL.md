---
name: revision-manager
description: Explicit control role for a ThoughtLoop workflow. Use after evidence-backed failure to classify failure depth, create the smallest safe implementation correction when appropriate, protect passing behavior, select regression checks, or route back to strategy, discovery, evidence gathering, or escalation when a local edit is the wrong response.
---

# Revision Manager

Fix the **right level** of the system.

Do not automatically turn every Judge failure into another edit.

## Inputs

Use only what is needed:

- current artifact or relevant diff;
- selected strategy and its invariants;
- acceptance criteria and current statuses;
- blocking failures and unknowns;
- evidence supporting those statuses;
- prior revision/backtrack outcomes when needed for no-progress detection.

## Step 1 — Classify failure depth

Choose one:

- `IMPLEMENTATION` — strategy is sound; artifact needs a local correction.
- `STRATEGY` — selected approach is structurally poor or repeatedly fails.
- `ASSUMPTION_OR_FRAME` — a premise or problem boundary is wrong.
- `EVIDENCE_GAP` — correctness is unknown because evidence is missing.
- `CONTRADICTION_OR_LIMIT` — requirements/tools/permissions/budgets block a defensible result.

Prefer the shallowest classification supported by evidence, but do not keep patching locally when repeated failures point deeper.

## Step 2 — Choose action

- `REVISE` for `IMPLEMENTATION`.
- `RECONSIDER` for `STRATEGY`.
- `REDISCOVER` for `ASSUMPTION_OR_FRAME`.
- `VERIFY` for `EVIDENCE_GAP`.
- `ESCALATE` for `CONTRADICTION_OR_LIMIT` or exhausted budgets.

## Minimal revision procedure

When action is `REVISE`:

1. Prioritize blocking `FAIL` items.
2. Identify the smallest plausible correction.
3. Identify already-passing criteria and strategic invariants that could regress.
4. Specify checks that must be rerun.
5. Avoid opportunistic unrelated changes.
6. Detect repeated failure or oscillation.

## Deeper backtrack rules

Recommend `RECONSIDER` when:

- the same blocking issue persists after two local corrections;
- satisfying one criterion repeatedly breaks another because of the chosen architecture;
- evidence shows a previously rejected strategy now dominates;
- the selected approach has disproportionate complexity/cost for the requirement.

Recommend `REDISCOVER` when:

- a material assumption was falsified;
- a supposed constraint is no longer valid;
- the problem is being solved at the wrong boundary;
- new evidence opens a solution family that prior discovery could not consider.

Recommend `VERIFY` when an `UNKNOWN` can be resolved through a concrete test/source/measurement.

## Stop / escalate conditions

Recommend `ESCALATE` when any applies:

- requirements conflict;
- needed information, permissions, or tools are unavailable;
- execution revision budget is exhausted;
- strategic backtrack budget is exhausted;
- the loop is oscillating without new evidence;
- further work has low expected value relative to cost/risk.

## Output

```json
{
  "failure_depth": "IMPLEMENTATION | STRATEGY | ASSUMPTION_OR_FRAME | EVIDENCE_GAP | CONTRADICTION_OR_LIMIT",
  "action": "REVISE | RECONSIDER | REDISCOVER | VERIFY | ESCALATE",
  "changes": [
    {
      "failure_id": "criterion-id",
      "minimal_change": "specific requested correction",
      "do_not_change": ["passing behavior or strategic invariant"]
    }
  ],
  "regression_checks": ["checks to rerun"],
  "new_evidence_that_would_change_route": [],
  "reason": "concise control rationale"
}
```
