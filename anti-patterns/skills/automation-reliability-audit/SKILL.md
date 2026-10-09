---
name: automation-reliability-audit
description: Review recurring jobs, monitoring agents, and scheduled reports for silent failures, missed sources, duplicate actions, stale state, and misleading success or no-change reports. Use for automation design or reliability incidents; not for one-off answers.
---

# Automation Reliability Audit

This is a self-contained, default read-only audit. Inspect a scheduled or event-driven workflow even if it uses no external agent framework.

## Procedure
1. **Identify the contract.** Name trigger/cadence, sources, freshness requirements, output destination, notification rules, permissions, and definition of a successful run.
2. **Map failure modes.** Check unreachable source, expired credentials, partial reads, malformed or stale data, duplicate delivery, write timeout after success, missed schedule, and alert fatigue.
3. **Require separate status states.** Distinguish `CHECKED_NO_CHANGE`, `CHECKED_NEW_INFO`, `PARTIALLY_CHECKED`, `FAILED`, and `NOT_RUN`. Never conflate unavailable data with an empty result.
4. **Inspect recoverability.** Check idempotency/reconciliation, last confirmed successful checkpoint, detection of repeated failures, bounded retries, and operator escalation. Never assume tools can safely retry arbitrary actions.
5. **Verify observability.** Identify exactly what logs, metrics, receipt IDs, or read-after-write checks prove each step. Consider relevant privacy and data-retention limits.
6. **Prioritize remediation.** Recommend the smallest controls that detect or prevent consequential incidents, not a new agent for each failure mode.
7. **Define a fault drill.** Suggest one or two safe simulations: missing source, timed-out write, duplicated event, or stale cursor. State expected state and notification behavior.

## Output
- **Workflow and coverage:** expected versus verified sources and outcomes
- **Failure matrix:** trigger, observable symptom, user consequence, existing control, proposed minimal control
- **Run states:** explicit definitions for success, no-change, partial, failed, and not-run
- **Top 3 fixes:** ranked by consequence and effort
- **Fault drills:** input, expected handling, and evidence required

## Boundaries
Do not claim to have run a scheduled job or modified automation configuration unless that actually occurred. Where logs or tools are unavailable, clearly state the audit is a design review, not an operational verification.
