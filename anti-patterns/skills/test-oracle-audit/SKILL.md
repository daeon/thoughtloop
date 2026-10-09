---
name: test-oracle-audit
description: Detect circular assertions, weak test oracles, overmocking, and regression tests that merely bless generated code. Use when reviewing newly generated or altered tests, bug fixes, migrations, or API behavior; skip unrelated writing tasks.
---

# Test Oracle Audit

A green test is meaningful only if its expected result reflects the intended behavior. Perform this audit without invoking other skills or agents.

## Procedure
1. **Recover the contract.** Derive expected behavior from the original requirement, API/schema specification, established example, or verified pre-change behavior. Mark any missing contract as `UNKNOWN`.
2. **Inspect assertions.** Identify where tests copy the implementation's output, assert tautologies, weaken expectations, swallow errors, or rely on snapshot updates without review.
3. **Probe sensitivity.** Ask whether each important test would fail under a plausible defect (e.g. reversed sign, duplicate action, wrong user ID, empty input, unexpected exception). If allowed and practical, demonstrate with a safe, reversible mutation or run against the original bug.
4. **Check integration boundaries.** Identify whether mocks omit the actual failure surface: persistence, authorization, timeouts, concurrency, external API shape, or data migration.
5. **Inspect test changes critically.** Call out changes that remove assertions, skip failures, or change expected values to match a regression.
6. **Recommend smallest better test.** Write the expected behavior first, name a realistic counterexample, and propose or implement a focused check only if authorized.

## Output
- **Contract / expected result** with its source
- **Tests inspected** (paths or descriptions)
- **Confirmed oracle defects** versus suspected coverage gaps
- **Minimal improvement** (test input, independent expected output, why it should fail if broken)
- **Outcome**: adequate for checked scope / inadequate / unknown

## Guardrails
Do not make arbitrary test changes without a source of expected behavior. Do not call a passing isolated unit suite proof of system-wide correctness. Do not invent execution output.
