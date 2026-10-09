---
name: evidence-audit
description: Audit claims, factual answers, technical completion statements, or deliverables against observable evidence and freshness. Use when correctness matters or an agent asserts that work is complete; not for pure creative brainstorming.
---

# Evidence Audit

Independently assess whether *specific claims* are supported. This skill stands alone: do not require another verifier, critic, or skill framework.

## Procedure
1. **Extract claims.** List only claims that could materially affect acceptance, safety, cost, correctness, or the user's decision.
2. **Choose the right oracle.** Use direct runtime behavior, resulting system state, integration checks, source files, primary documentation, reproducible measurements, or scoped tests. Prefer direct checks over another model's assurances.
3. **Check provenance.** Record artifact/version, source identity, time or recency where relevant, scope, and limitations. Detect citation mismatch, stale sources, incomplete tool execution, and proxy metrics.
4. **Classify each claim.** `PASS` = sufficient supporting evidence for the specified scope; `FAIL` = evidence of noncompliance; `UNKNOWN` = unavailable, stale, partial, or inconclusive evidence.
5. **Try a counterexample.** For consequential positive claims, ask which realistic failure the present evidence would miss. If it matters, perform or recommend a focused check.
6. **Apply a verdict.** A blocking `FAIL` makes the overall outcome `FAIL`; otherwise a blocking `UNKNOWN` makes it `UNKNOWN`; otherwise `PASS` within checked scope. Do not silently treat unchecked criteria as passed.

## Output
| Criterion / claim | Evidence and provenance | Result | Limitation or next check |
|---|---|---|---|

Conclude with an explicitly scoped verdict and any blocking unknowns. Differentiate 'command accepted' from 'effect observed.' Never imply a test or live check ran when it did not.

## Non-goals
Do not edit the artifact merely to make a check pass. Do not demand full integration testing for a cosmetic change. Do not pretend model confidence is independent evidence.
