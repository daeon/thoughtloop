---
name: review
description: Red-team a result after ordinary checks for hidden defects, regressions, security issues, contradictions, misuse paths, or fragile assumptions.
---

# Review

Start with the acceptance criteria and claimed evidence. Examine only the risk lenses that fit: edge cases, regressions, recovery, security, data integrity, concurrency, compatibility, factual contradiction, misuse, and hidden coupling. Use concrete counterexamples or tests to turn plausible concerns into evidence.

Return a `ReviewReport` with confirmed findings, hypotheses needing verification,
and important coverage gaps separately. For each confirmed finding, name the
criterion, evidence, impact, severity, and next correction or check. Review
findings become evidence for the orchestrator's `final-judgment` stage; review
does not issue a second unconsumed verdict.
