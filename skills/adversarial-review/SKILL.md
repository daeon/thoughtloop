---
name: adversarial-review
description: Explicit red-team review for an artifact that appears to satisfy ordinary criteria. Use for high-risk work or when asked to find hidden defects, regressions, security issues, contradictions, misuse paths, or fragile assumptions. Separate evidence-backed findings from hypotheses.
---

# Adversarial Review

Try to break the finished artifact without inventing defects. Start with the acceptance criteria and claimed evidence, then examine only the risk lenses that fit: edge cases, ambiguity, regressions, recovery, security, data integrity, concurrency, compatibility, factual contradiction, misuse, and hidden coupling.

Construct concrete counterexamples or abuse cases and use tools or tests to turn plausible concerns into evidence. Do not downgrade passing evidence without a specific reason.

Report findings by impact and evidence strength. Separate:

- confirmed findings with a reproduction or supporting evidence;
- hypotheses that still need verification;
- important coverage gaps.

For each confirmed finding, state the affected criterion, evidence, likely impact, and next verification or correction. Do not force a fixed number of findings.
