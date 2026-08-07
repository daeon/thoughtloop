# Example — research / decision support

Prompt:

```text
$thoughtloop Recommend an architecture for this workflow. Search several materially different models, challenge our assumptions about scale and consistency, identify what evidence would distinguish them, then verify the final recommendation against primary sources and measured constraints.
```

Expected routing:

1. Explorer covers different architecture families rather than several variants of one stack.
2. Challenger separates hard requirements from inherited design conventions.
3. Synthesizer identifies any decision-sensitive unknown that should be measured before commitment.
4. Builder produces the recommendation/implementation plan only after selection.
5. Verifier checks technical claims against primary documentation, measurements, or repository evidence.
6. Judge preserves UNKNOWN where the evidence cannot establish a claim.
7. New evidence that invalidates the chosen architecture triggers strategy reconsideration, not prose polishing.
