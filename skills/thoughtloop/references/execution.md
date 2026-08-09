# Execution reference

Execute only after the selected strategy is sufficiently supported or the user
has explicitly chosen it. Make the smallest coherent authorized change that
satisfies the acceptance criteria.

- preserve hard requirements and passing behavior;
- make material assumptions and uncertainties visible;
- do not silently change strategy;
- surface strategic conflicts for correction;
- return changed artifacts, useful context, and recommended checks;
- avoid unrelated cleanup or opportunistic rewrites.

Use a reproduction-first check when changing behavior:

- bug fix: reproduce the original symptom before the production change when practical;
- refactor: capture the current behavior before restructuring;
- migration: exercise old, transitional, and new paths;
- performance work: record a baseline and variance before optimizing;
- generated files, configuration, documentation, and disposable probes may use
  an explicit exception when a test-first loop would not add signal.

Do not silently rewrite the decision record when implementation contradicts the
selected strategy. Route the conflict back to `decide` or `correct`.

For a correction, fix the smallest surface that addresses the blocking failure
and rerun regression-sensitive checks before claiming progress.
