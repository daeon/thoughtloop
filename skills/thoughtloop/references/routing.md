# Adaptive routing

Choose the least expensive path that still gives enough search and evidence for the task.

| Exploration | Use when | Typical path |
|---|---|---|
| Direct | Mechanical, tightly specified, reversible | Builder -> Prove |
| Deliberate | Several plausible approaches or a moderate design choice | Explorer -> Synthesizer -> Execute -> Prove |
| Deep | Architecture, difficult debugging, costly reversals, or uncertain framing | Explorer -> Challenger -> Synthesizer -> Execute -> Prove |

Verification is a separate choice:

- **Low:** proportionate deterministic checks are usually enough.
- **Medium:** use independent evidence and a criterion-level verdict.
- **High:** add adversarial review or another focused check when failure would be costly, subtle, or security-sensitive.

Subagent mode is also separate from exploration depth. Use it only when delegation adds independent signal. A balanced default is no agent for trivial work, one for a moderate decision, and two or three for complex or high-risk work. Reduce or increase that budget based on cost, latency, and consequence.

Do not invoke every stage mechanically. Skip discovery when alternatives are immaterial, and stop discovery when experiments or evidence are more valuable than more ideas.
