# Shared graph contracts

The graph passes compact, observable state between skills. These are behavioral
contracts, not a required serialization format.

| Contract | Producer | Consumers | Minimum content |
|---|---|---|---|
| TaskContract | ThoughtLoop or Gapfinder | Every node | objective, constraints, criteria, risk, budget |
| DiscoveryBrief | Gapfinder | Discover, Investigate, Decide | unknowns, assumptions, falsifiers, probes |
| OptionSet | Discover | Decide | options, tradeoffs, tests, unresolved questions |
| InvestigationReport | Investigate | Decide, Verify | scope, facts, hypotheses, evidence, gaps |
| DecisionRecord | Decide | Builder | selected approach, rationale, criteria |
| ChangeSet | Builder | Verify, Review | changed artifacts, intended behavior, tests |
| EvidenceSet | Verify | Judge, Revise | criterion, check, result, provenance, limits |
| Verdict | Judge or Review | Revise, Handoff | PASS, FAIL, or UNKNOWN by criterion |
| RouteDecision | Revise | Discover, Decide, Builder, Verify | failure depth, owner, correction, regressions |
| HandoffRecord | Handoff | Future session or agent | state, evidence, risks, next action |

## State rules

- Record facts, assumptions, alternatives, decisions, evidence, tests, and
  concise rationales. Never request or store hidden chain-of-thought.
- An unavailable check is UNKNOWN; it is not an implicit PASS.
- Graph state is disposable task context unless the user explicitly asks for a
  handoff or another artifact.
