---
name: evaluate
description: Inspect run outcomes to improve search, decisions, execution, verification, correction, routing, and budget use without judging the artifact itself.
---

# Evaluate

Evaluate the loop, not the artifact. Inspect whether the work searched enough, converged appropriately, used evidence, corrected at the right depth, and spent delegation budget economically.

Useful signals include exploration and experiment use, approach diversity, duplicate ideas, first-pass success, revisions, repeated failures, backtracking, regressions, PASS/FAIL/UNKNOWN reliability, tokens, runtime, cost, and whether a subagent added independent signal. Use `scripts/calculate_metrics.py` for JSONL logs when applicable.

Recommend routing, prompt, evidence, stopping, or budget changes. Treat aggregates as signals, not proof, and do not rewrite the artifact under review.
