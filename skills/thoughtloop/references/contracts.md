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
| DelegationBrief | ThoughtLoop | Delegated agent | one question, inputs, output contract, authorization, budget, stop condition |
| DelegationResult | Delegated agent | ThoughtLoop | question, inspected evidence, result, uncertainty, edits, checks, decision impact |

Record facts, assumptions, alternatives, decisions, evidence, tests, and concise
rationales only. Never request or store hidden chain-of-thought. An unavailable
check is `UNKNOWN`, not an implicit `PASS`.

## Evidence item shape

Evidence is observable and tied to the artifact or system version being judged.
Use the following fields when available; omit fields that cannot be measured:

```json
{
  "criterion": "C1",
  "command_or_check": "pytest tests/test_retry.py -q",
  "result": "12 passed",
  "exit_code": 0,
  "artifact_revision": "git SHA or file digest",
  "scope": "focused",
  "freshness": "current turn or timestamp",
  "limitations": []
}
```

Focused evidence proves only the behavior it exercises. A delegated report is
an input to verification, not proof by itself; the parent must check material
claims independently. Stale, partial, or unavailable evidence cannot support a
criterion-level `PASS`.

## Delegation contracts

Delegation is optional and bounded. A brief should contain one independently
answerable question, task-relevant artifact paths, the exact output shape, edit
authorization, budget, and a stop condition. A result should identify what was
inspected, what was found, what remains uncertain, which files changed, which
checks ran, and whether the parent decision should change.

The parent remains responsible for synthesis, edits, and final judgment. Do not
paste the entire session history into a delegated prompt, and do not allow
parallel delegates to edit overlapping files.
