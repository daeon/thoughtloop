# Solution-space search

Discovery should maximize **meaningful coverage per token**, not raw idea count.

## Search dimensions

Look for approaches that differ across dimensions such as:

- architecture/boundary;
- state ownership;
- timing (precompute, runtime, asynchronous, event-driven);
- mechanism (cache, queue, index, protocol, algorithm);
- operational complexity;
- cost/performance profile;
- user interaction model;
- assumption set.

## Orthogonal lenses

Use a subset appropriate to the task:

- simplest possible;
- highest performance;
- lowest operational burden;
- exploit what already exists;
- remove the requirement;
- change the boundary;
- move work earlier/later;
- invert a key constraint;
- solve the upstream cause;
- use an adjacent-domain analogy.

## Diversity test

Two options are not materially different if they keep the same architecture, assumptions, and mechanism but change only libraries, naming, formatting, or minor implementation details.

## Idea graph

Group related approaches under parent strategies. Use the graph to detect overexplored branches and unvisited families.

## Experiments over speculation

When the decision depends on an empirical unknown, stop ideating and define the smallest discriminating experiment.

A useful experiment states:

- hypothesis/unknown;
- competing approaches;
- measurement;
- expected outcomes;
- which outcome favors which approach;
- cost/time/risk of the experiment.

## Discovery stopping rules

Stop when:

1. new ideas are mostly variants;
2. major relevant strategy families are represented;
3. one strategy dominates on hard constraints and material tradeoffs;
4. remaining uncertainty requires evidence;
5. the discovery budget is exhausted.
