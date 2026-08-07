# Example — coding / architecture

Prompt:

```text
$thoughtloop Reduce p99 latency in this parsing service without changing its external contract. Explore materially different approaches before editing, measure the decision-sensitive unknowns, then implement and verify the best option.
```

Expected routing:

1. Contract: external behavior is hard; implementation shape is soft.
2. Exploration level 2, verification risk medium.
3. Explorer searches distinct families such as avoiding work, caching, moving work, or algorithmic redesign.
4. Challenger asks whether the current request boundary or repeated work is itself the problem.
5. Synthesizer chooses BUILD only if evidence is enough; otherwise requests a focused benchmark.
6. Builder implements the selected strategy.
7. Verifier runs targeted benchmark, tests, type/static checks as relevant.
8. Judge returns PASS / FAIL / UNKNOWN.
9. A local bug routes to revision; structural performance failure routes back to Synthesizer; falsified workload assumptions route back to Discover.
10. Regression checks rerun after every implementation change.
