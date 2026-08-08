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

For a correction, fix the smallest surface that addresses the blocking failure
and rerun regression-sensitive checks before claiming progress.
