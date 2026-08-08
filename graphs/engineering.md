# Engineering graph

Use this profile for repository changes, debugging, migrations, performance,
security, release, or compatibility work.

```text
engineering route
  -> repository/component/contract map
  -> Gapfinder when assumptions or unknowns are expensive
  -> Investigate(repository | debugging | logs | performance)
  -> Decide(select | plan)
  -> Execute
  -> Verify
  -> Review for high-risk changes
  -> Final judgment
```

Read-only investigation remains read-only until the user requests a change.
Measurement precedes performance edits, and compatibility claims require
evidence from both old and new behavior.
