# Failure-depth reference

Classify a blocking failure before correcting it:

| Depth | Signal | Corrective owner |
|---|---|---|
| `IMPLEMENTATION` | The strategy is sound but the artifact is wrong | Execute |
| `STRATEGY` | The approach conflicts with a criterion or is structurally poor | Decide |
| `ASSUMPTION_OR_FRAME` | A premise or problem boundary was falsified | Discover or Investigate |
| `EVIDENCE_GAP` | A needed test, source, or measurement is missing | Verify or Investigate |
| `CONTRADICTION_OR_LIMIT` | Requirements, authority, tools, or budget block a defensible result | Stop or escalate |

Protect passing criteria, state regression checks, and avoid unrelated cleanup.
Do not alternate between the same approaches without new evidence. After two
failed local corrections against the same blocker, backtrack.
