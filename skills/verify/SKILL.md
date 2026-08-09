---
name: verify
description: Gather independent evidence for acceptance criteria from runtime behavior, tests, tools, authoritative sources, raw data, or deterministic checks.
---

# Verify

Establish what can be known from evidence. For each material criterion, choose the strongest practical check: real runtime behavior and integration checks, focused tests, static checks, authoritative sources, or direct calculations.

Return an `EvidenceSet` with criterion, check, observable result, provenance, and limitations. Separate supporting evidence, failing evidence, and inconclusive evidence. A green check supports only the behavior it covers.

For material checks, include freshness and scope when observable:

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

Re-run the original symptom for a bug fix when practical. Do not present a
focused check as full-suite coverage, and independently check delegated claims
before using them in final judgment.

Unavailable evidence is `UNKNOWN`. Do not issue the final outcome; the
orchestrator's `final-judgment` stage does that. Do not rewrite the artifact to
make a check pass.
