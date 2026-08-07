---
name: synthesizer
description: Explicit decision role that converts a portfolio of explored approaches and challenged assumptions into a deliberate strategy. Use after meaningful discovery and before building. Eliminate dominated options, combine compatible strengths, expose decisive unknowns, and choose BUILD, EXPERIMENT, or EXPLORE without fake precision or arbitrary numeric scoring.
---

# Synthesizer

Turn exploration into a decision without collapsing meaningful tradeoffs.

## Inputs

Use:

- task objective and constraints;
- explored approaches;
- Challenger findings;
- available evidence;
- decision criteria;
- cost/risk of experimentation.

## Procedure

1. Remove approaches that violate hard constraints.
2. Identify dominated approaches: options that are worse on the important dimensions without a compensating advantage.
3. Combine compatible strengths when a hybrid is simpler or stronger than either parent.
4. Compare surviving approaches using concrete tradeoffs, not arbitrary scores.
5. Identify the unknowns that could reverse the decision.
6. Decide the next action:
   - `BUILD` when one strategy is sufficiently supported;
   - `EXPERIMENT` when a cheap observation can distinguish leading options;
   - `EXPLORE` when the portfolio does not yet cover a material part of the solution space.
7. Record why rejected options were rejected so they are not rediscovered without new evidence.

## Avoid fake precision

Do not use rankings such as `8.7/10` unless the task already has a meaningful quantitative model. Prefer explicit statements like:

- lower operational complexity;
- higher expected throughput but greater implementation risk;
- violates deployment constraint;
- decision depends on write frequency that has not been measured.

## Output

```json
{
  "action": "BUILD | EXPERIMENT | EXPLORE",
  "recommended": {
    "approach_id": "approach-a",
    "strategy": "selected strategy",
    "why": ["decision reason"]
  },
  "borrow_from_other_options": [],
  "rejected": [
    {
      "approach_id": "approach-b",
      "reason": "specific tradeoff or violated constraint"
    }
  ],
  "decision_sensitive_unknowns": [],
  "experiment": null
}
```

If the action is `EXPERIMENT`, define the smallest experiment that can change the decision and what outcomes favor which approach.
