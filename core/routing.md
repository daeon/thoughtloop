# Graph routing

ThoughtLoop is the only implicit entry point. Every other skill is independently
callable and may also receive state from the orchestrator.

| Node | Responsibility | Default posture |
|---|---|---|
| gapfinder | Surface expensive unknowns and choose discovery depth | bounded reconnaissance |
| discover | Search options, challenge framing, or build probes | no commitment |
| investigate | Map code, debug failures, analyze logs, measure performance | read-only |
| decide | Select, combine, or plan from evidence and tradeoffs | no implementation |
| builder | Make the selected change or targeted revision | smallest coherent edit |
| verify | Collect independent evidence | no final verdict |
| judge | Apply PASS, FAIL, or UNKNOWN | no rewriting |
| review | Red-team a result after ordinary checks | evidence-backed findings |
| revise | Route a failure to the level actually wrong | bounded correction |
| handoff | Compress continuation-critical state | no unrelated investigation |
| evaluate | Improve loop, routing, and budget use | does not judge artifact |
| standard-english | Apply explicit language standards when useful | preserve meaning |

```text
Direct:     builder -> verify -> judge
Deliberate: gapfinder -> discover -> decide -> builder -> verify -> judge
Debugging:  gapfinder -> investigate -> decide -> builder -> verify -> judge
Deep:       gapfinder -> discover -> investigate -> decide -> builder -> verify
            -> judge -> review
Failure:    revise -> discover | investigate | decide | builder | verify
```

These are conditional routes, not a mandatory pipeline. Every node is
independently callable, while `thoughtloop` is the only implicit entry point.
