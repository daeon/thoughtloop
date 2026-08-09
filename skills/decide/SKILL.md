---
name: decide
description: Select, combine, or plan from evidence and tradeoffs; use select or plan mode without implementing the result.
---

# Decide

Use `select` after exploration or investigation to choose the next defensible move. Use `plan` when the output must be an implementation brief led by architecture-changing decisions.

Consider requirements, evidence, challenged assumptions, reversibility, complexity, performance, reliability, operations, user impact, and budget. Reject hard-constraint violations and dominated options. Preserve rejected approaches so they are not rediscovered without new evidence.

Choose one action:

- `BUILD` when the strategy is supported;
- `EXPERIMENT` when a cheap measurement could change the decision;
- `EXPLORE` when a material solution family or framing is missing.

For `plan`, state success criteria, decisions and defaults, architecture/data and interface impacts, lifecycle behavior, failure modes, validation, rollback, files likely touched, invalidators, and mechanical steps. Return a `DecisionRecord`; do not edit the artifact or pretend qualitative judgment is a numeric proof.

Make an implementation plan executable without over-specifying it. For each
independently testable task, name likely files, consumed and produced
interfaces, dependencies, verification command and expected observation,
rollback or invalidation conditions, and unresolved placeholders. Review the
plan for missing requirements, contradictions, inconsistent names, and tasks
too large to verify independently before handing it to `execute`.
