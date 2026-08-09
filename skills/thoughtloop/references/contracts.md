# Shared graph contracts

The graph passes compact, observable state between public nodes and internal
operations. These are behavioral contracts, not a required serialization
format.

| Contract | Producer | Consumers | Minimum content |
|---|---|---|---|
| TaskContract | ThoughtLoop or Gapfinder | Every stage | objective, constraints, criteria, risk, budget |
| DiscoveryBrief | Gapfinder | Discover, Investigate, Decide | unknowns, assumptions, falsifiers, probes |
| OptionSet | Discover | Decide | options, tradeoffs, tests, unresolved questions |
| InvestigationReport | Investigate | Decide, Verify | scope, facts, hypotheses, evidence, gaps |
| DecisionRecord | Decide | Execute | selected approach, rationale, criteria |
| ChangeSet | Execute | Verify, Review | changed artifacts, intended behavior, tests |
| EvidenceSet | Verify | Final judgment, Review, Correct | criterion, check, result, provenance, limits |
| ReviewReport | Review | Final judgment, Correct | findings, counterexamples, coverage gaps, severity |
| FinalOutcome | Final judgment | Correct, Handoff, user | PASS, FAIL, or UNKNOWN by criterion |
| RouteDecision | Correct | Discover, Investigate, Decide, Execute, Verify | failure depth, owner, correction, regressions |
| HandoffRecord | Handoff | Future session or agent | state, evidence, risks, next action |

Record facts, assumptions, alternatives, decisions, evidence, tests, and concise
rationales only. Never request or store hidden chain-of-thought. An unavailable
check is `UNKNOWN`, not an implicit `PASS`.
