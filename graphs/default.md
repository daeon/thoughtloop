# Default graph

Use the smallest route that can establish the requested result.

```text
task
  -> ThoughtLoop intake
  -> [unknowns or material choice?]
       no  -> Execute
       yes -> Gapfinder -> Discover or Investigate -> Decide
  -> Verify -> Final judgment
  -> [high consequence or subtle risk?]
       yes -> Review -> Final judgment
       no  -> stop
  -> [failure or unknown?] -> Correct at the correct depth
```

The graph is lazy. Nodes are selected by evidence and consequence of being
wrong, not by a fixed checklist.
