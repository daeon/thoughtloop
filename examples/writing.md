# Example — constrained writing

Prompt:

```text
$thoughtloop Rewrite this release note to comply with our terminology guide and 120-word limit, then verify both constraints.
```

Expected routing:

- exploration level 0 because the task is tightly specified;
- deterministic word-count and terminology checks first;
- editorial Judge only for criteria that are not mechanically checkable;
- no additional discovery overhead unless the user asks for alternative messaging strategies;
- no adversarial review unless stakes justify it.
