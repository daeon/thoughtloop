# Debugging graph

```text
symptom
  -> Gapfinder: identify missing context and cheapest falsifiers
  -> Investigate(debugging | logs)
  -> [root cause supported?]
       no  -> Verify or gather the next probe
       yes -> Decide
  -> Builder when a fix is authorized
  -> Verify regression and reproduction checks
  -> Judge
```

Do not patch a plausible hypothesis merely because it is attractive. If two
local revisions fail against the same blocker, route back to the hypothesis or
problem boundary.
