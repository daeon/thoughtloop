# Contributing

ThoughtLoop is a small, contract-driven skill pack. Contributions are welcome when they improve judgment, evidence quality, usability, or budget control without adding ceremony for its own sake.

## Before changing a skill

- Preserve the public architecture: **Discover → Decide → Execute → Prove**.
- Keep `thoughtloop` as the only implicitly invoked skill.
- Keep the canonical nodes independently callable; do not add compatibility aliases or a second orchestrator.
- Extend the installed references under `skills/thoughtloop/references/` rather than creating parallel state or orchestration policies.
- Treat evidence as stronger than confidence. Missing evidence remains `UNKNOWN`.
- Never request or record hidden chain-of-thought. Keep observable evidence, alternatives, decisions, tests, critiques, and concise rationales.
- Keep exploration, revisions, and delegation bounded.
- For behaviour-changing instructions, add or identify a pressure scenario that
  demonstrates the current failure before changing the instruction. Record the
  expected observable improvement and remaining uncertainty.
- Separate structural validator results from model-backed behavioural results.
  A passing schema test is not evidence that an agent followed the workflow.

## Local checks

Run the required checks from the repository root:

```bash
python tests/validate_pack.py
python tests/validate_graph.py
python scripts/calculate_metrics.py examples/sample-loop-log.jsonl
python scripts/run_behavioral_evals.py --validate-only
python -m unittest discover -s tests -p 'test_*.py' -v
git diff --check
```

For paired behavioural runs, use a control runner when available:

```bash
python scripts/run_behavioral_evals.py \
  --runner codex exec \
  --control-runner codex exec \
  --repetitions 3 --output evals/runs/paired.json
```

The runner scores only observable route, verdict, activation, and delegation
fields. Missing observations remain `UNKNOWN`. Baselines are write-once; use a
new file for a new model or instruction version rather than replacing history.

If installer behavior changes, test installation and removal against an isolated temporary home directory.

## Pull requests

Explain:

1. the problem or use case;
2. the smallest behavior or documentation change that addresses it;
3. the validation you ran;
4. any remaining uncertainty or breaking impact.

Avoid unrelated rewrites. For changes to orchestration or invocation behavior, update the validator, examples, changelog, and README together.
