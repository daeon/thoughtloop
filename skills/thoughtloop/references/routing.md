# Routing reference

ThoughtLoop is the only implicitly invoked entry point. The other public nodes
are independently callable and may receive compact state from the orchestrator.

| Node | Responsibility | Default posture |
|---|---|---|
| thoughtloop | Route, execute, judge, correct, and preserve state | adaptive orchestration |
| gapfinder | Surface expensive unknowns and choose discovery depth | bounded reconnaissance |
| discover | Search options, challenge framing, or build probes | no commitment |
| investigate | Map code, debug failures, analyze logs, or measure performance | read-only |
| decide | Select, combine, or plan from evidence and tradeoffs | no implementation |
| verify | Collect criterion-specific independent evidence | no final outcome |
| review | Red-team a result after ordinary checks | evidence-backed findings |
| handoff | Compress continuation-critical state | no unrelated investigation |

Internal operations owned by `thoughtloop` are `execute`, `final-judgment`, and
`correct`. They are graph roles, not separately installed skills.

```text
Direct:       execute -> verify -> final-judgment
Deliberate:   gapfinder -> discover -> decide -> execute -> verify -> final-judgment
Engineering:  gapfinder -> investigate -> decide -> execute -> verify -> final-judgment
Deep:         gapfinder -> discover/investigate -> decide -> execute
              -> verify -> review -> final-judgment
Correction:   correct -> discover | investigate | decide | execute | verify
```

These are conditional routes, not a mandatory checklist. Choose the smallest
route that can establish the requested result.
