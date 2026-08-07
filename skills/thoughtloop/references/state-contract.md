# Suggested state contract

Use explicit state for complex tasks. Keep it compact and observable.

```json
{
  "objective": "string",
  "hard_constraints": [],
  "soft_constraints": [],
  "important_unknowns": [],
  "exploration_level": 2,
  "verification_risk": "medium",
  "discovery_pass": 1,
  "max_discovery_passes": 2,
  "strategic_backtracks": 0,
  "max_strategic_backtracks": 2,
  "selected_approach": "approach-id-or-null",
  "rejected_approaches": [],
  "revision": 0,
  "max_execution_revisions": 3,
  "criteria": [
    {
      "id": "string",
      "requirement": "string",
      "blocking": true,
      "status": "PENDING | PASS | FAIL | UNKNOWN"
    }
  ],
  "latest_failure_depth": "IMPLEMENTATION | STRATEGY | ASSUMPTION_OR_FRAME | EVIDENCE_GAP | CONTRADICTION_OR_LIMIT | null",
  "latest_failures": [],
  "regression_checks": [],
  "unresolved_unknowns": []
}
```

Do not store hidden chain-of-thought. Store alternatives, assumptions, task state, observable evidence, decisions, and concise rationales only.
