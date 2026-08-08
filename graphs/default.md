# Default graph

Use the smallest route that can establish the requested result.

```text
task
  -> ThoughtLoop intake
  -> [unknowns or material choice?]
       no  -> Builder
       yes -> Gapfinder -> Discover or Investigate -> Decide
  -> Verify -> Judge
  -> [high consequence or subtle risk?]
       yes -> Review
       no  -> stop
  -> [failure or unknown?] -> Revise at the correct depth
```

The graph is lazy. Nodes are selected by evidence and consequence of being
wrong, not by a fixed checklist.
