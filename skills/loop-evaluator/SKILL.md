---
name: loop-evaluator
description: Explicit meta-evaluation role for the Discover-Decide-Execute-Prove system. Use to analyze run logs, benchmark solution-space coverage, decision quality, verification reliability, false passes/failures, regressions, repeated failures, strategic backtracks, excessive ideation or retries, and recommend changes to the problem-solving loop itself rather than the artifact.
---

# Loop Evaluator

Evaluate the **problem-solving system**, not the artifact it produced.

The system has two coupled loops:

- outer loop: Discover -> Decide -> strategic backtrack;
- inner loop: Execute -> Prove -> implementation correction.

Do not optimize one loop while ignoring failure in the other.

## Useful metrics

Track when labels are available:

### Discovery / decision

- `exploration_used_rate`;
- `average_approach_count`;
- `near_duplicate_idea_rate`;
- `experiment_before_commit_rate`;
- `strategic_backtrack_rate`;
- `assumption_backtrack_rate`;
- `approach_switch_success_rate`;
- `premature_convergence_rate` when human labels exist.

### Execution / proof

- `first_pass_success_rate`;
- `average_revisions_to_success`;
- `escalation_rate`;
- `false_pass_rate`;
- `false_fail_rate`;
- `unknown_rate`;
- `regressions_introduced`;
- `repeated_failure_rate`;
- `verification_cost`;
- `tokens_or_runtime_per_success`.

## Correction yield

A useful directional metric is whether revisions resolve more blocking failures than they introduce regressions. Do not force a single universal formula when costs are incomparable; track at least:

- blocking failures resolved;
- regressions introduced;
- cost/tokens/runtime spent.

## Diagnostic questions

1. Did discovery produce genuinely different solution families or cosmetic variants?
2. Did the system challenge inherited assumptions when warranted?
3. Did Synthesizer commit before decision-sensitive unknowns were measured?
4. Are empirical questions being answered with more brainstorming instead of experiments?
5. Are failures usually implementation-level, strategic, assumption-level, or evidence gaps?
6. Does the system keep editing when it should backtrack to strategy?
7. Does it rediscover previously rejected options without new evidence?
8. Are `UNKNOWN` results being coerced into PASS?
9. Is the Judge too permissive or too strict?
10. Are expensive discovery/adversarial stages being run on trivial tasks?

## Stress tests

Maintain a benchmark set containing:

- tasks with one obvious solution where discovery should be skipped;
- tasks where the first obvious solution is valid but dominated by a better architecture;
- tasks with a deliberately false inherited assumption;
- tasks where a cheap benchmark should resolve the decision;
- known-good artifacts;
- subtly wrong artifacts;
- impossible or contradictory tasks;
- tasks with intentionally unavailable evidence;
- tasks requiring a narrow fix without breaking previous behavior.

A strong system should search when search matters, stop searching when evidence is needed, backtrack at the correct depth, verify with independent evidence, and stop cleanly on impossible tasks.

## Script

For simple JSONL run logs, `scripts/calculate_metrics.py` computes baseline aggregate metrics using only the Python standard library.
