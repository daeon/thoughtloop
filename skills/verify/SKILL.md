---
name: verify
description: Gather independent evidence for acceptance criteria from runtime behavior, tests, tools, authoritative sources, raw data, or deterministic checks.
---

# Verify

Establish what can be known from evidence. For each material criterion, choose the strongest practical check: real runtime behavior and integration checks, focused tests, static checks, authoritative sources, or direct calculations.

Return an `EvidenceSet` with criterion, check, observable result, provenance, and limitations. Separate supporting evidence, failing evidence, and inconclusive evidence. A green check supports only the behavior it covers.

Unavailable evidence is `UNKNOWN`. Do not issue the final verdict; `$judge` does that. Do not rewrite the artifact to make a check pass.
