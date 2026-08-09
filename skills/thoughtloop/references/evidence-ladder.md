# Evidence and outcome reference

For each material criterion, use the strongest practical evidence available:

1. real runtime behavior and integration checks;
2. focused automated tests and deterministic checks;
3. static analysis, type checks, or direct calculations;
4. authoritative documentation or source evidence;
5. bounded reasoning that is clearly labeled as an assumption.

Record the criterion, check, observable result, provenance, and limitation.
Separate supporting, failing, and inconclusive evidence. A green check supports
only the behavior it covers.

Use exactly one final status per criterion:

- `PASS` when evidence supports compliance;
- `FAIL` when evidence demonstrates noncompliance;
- `UNKNOWN` when evidence is insufficient or unavailable.

Missing evidence never becomes an implicit pass. A blocking review finding must
be resolved or reflected in the final outcome before the task can pass.
