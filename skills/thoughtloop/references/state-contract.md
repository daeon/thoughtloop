# State-contract reference

For complex or delegated work, keep compact observable state such as:

```json
{
  "objective": "string",
  "constraints": [],
  "criteria": [{"id": "string", "status": "PENDING"}],
  "unknowns": [],
  "selected_approach": null,
  "rejected_approaches": [],
  "delegation": {"mode": "off | subagents", "budget": "light | balanced | deep", "used": 0, "follow_up_rounds": 0, "max_follow_up_rounds": 1},
  "latest_failure_depth": null,
  "revisions": 0,
  "evidence": [],
  "next_action": "string"
}
```

This is a suggestion, not a mandatory serialization format. Store alternatives,
assumptions, decisions, evidence, tests, and concise rationales. Never store
hidden chain-of-thought. State is disposable task context unless the user asks
for a handoff.
