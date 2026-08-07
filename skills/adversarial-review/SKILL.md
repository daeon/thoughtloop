---
name: adversarial-review
description: Explicit red-team review for an artifact that already appears to satisfy ordinary criteria. Use for high-risk work or when asked to find hidden defects, edge cases, regressions, security issues, contradictions, misuse paths, or fragile assumptions. Report hypotheses separately from evidence-backed findings.
---

# Adversarial Review

Attempt to break an apparently finished artifact without inventing defects.

## Review lenses

Select only the lenses relevant to the task:

- counterexamples and edge cases;
- requirement ambiguity;
- regression risk;
- failure recovery;
- security and trust boundaries;
- data integrity;
- concurrency or ordering;
- compatibility;
- factual contradiction;
- misuse or unexpected inputs;
- hidden coupling and second-order effects.

## Procedure

1. Start from the acceptance criteria and claimed evidence.
2. Identify fragile assumptions that ordinary verification may not cover.
3. Construct concrete counterexamples or abuse cases.
4. Use tools/tests when available to convert hypotheses into evidence.
5. Separate:
   - `confirmed_findings` — evidence-backed defects;
   - `hypotheses` — plausible but unverified concerns;
   - `coverage_gaps` — important behavior not yet tested.
6. Do not force a fixed number of findings.
7. Do not downgrade ordinary passing evidence without a concrete reason.

## Output

Return findings ranked by expected impact and evidence strength. Each confirmed finding should state:

- affected criterion or invariant;
- reproduction/counterexample;
- evidence;
- likely impact;
- recommended verification step.

Unverified hypotheses must not be presented as established defects.
