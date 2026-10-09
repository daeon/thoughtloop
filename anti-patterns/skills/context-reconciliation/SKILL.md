---
name: context-reconciliation
description: Reconcile stale memory, long conversation summaries, contradictory records, and uncertain completion states before a consequential decision. Use when past notes or cached context conflict with live sources or the user corrects a fact; not for tasks with adequate current context.
---

# Context Reconciliation

Prevent an old model inference from silently becoming a durable fact. This skill requires no external memory framework; use only context and records actually available.

## Procedure
1. **Identify the contested facts.** Limit the scope to details that could change the requested decision or action.
2. **Locate evidence.** Examine the current user statement, source record, revision history, previous observation, or documented state as permitted. Do not fabricate access to unavailable history.
3. **Label origin and status.** For every material item distinguish `USER_REPORTED`, `TOOL_OBSERVED`, `EXTERNALLY_SOURCED`, `INFERRED`, or `UNKNOWN`; also distinguish `PLANNED`, `ATTEMPTED`, `CONFIRMED`, `FAILED`, and `UNKNOWN` for actions.
4. **Compare freshness and authority.** Prefer recent direct observation and canonical records for mutable state. Newer is not automatically more authoritative: a mistaken update can conflict with a measured source.
5. **Resolve carefully.** Use explicit user corrections when applicable. If a contradiction cannot be settled, preserve both claims with provenance rather than merging them into a confident summary.
6. **Use only resolved facts.** Carry uncertainty forward into decisions. Update persistent state only when the current task and permissions authorize the write.

## Output
| Item | Claim | Source and date | Status | Resolution / next check |
|---|---|---|---|---|

Conclude with the facts safe to rely on and those still uncertain.

## Non-goals
Do not store personal details without authorization, infer secrets, or turn assistant speculation into a memory fact. Do not require hidden chain-of-thought; concise observable reasons suffice.
