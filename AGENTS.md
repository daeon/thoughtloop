# ThoughtLoop repository instructions

ThoughtLoop is a cohesive Codex skill pack for deliberate problem solving. Preserve the public architecture **Discover → Decide → Execute → Prove** and the tagline **Think wider. Build better. Prove it.**

## Repository invariants

- `skills/thoughtloop/` is the primary orchestrator and the only skill that permits implicit invocation.
- Canonical capability nodes own behavior and are the only supported public skill names.
- `core/contracts.md` is the shared observable state contract; do not create parallel schemas.
- `core/routing.md` is the canonical graph boundary; do not add a second orchestrator.
- Evidence must outrank model confidence; unavailable evidence is `UNKNOWN`, never an implicit `PASS`.
- Keep exploration and verification bounded.
- Do not require, request, or log hidden chain-of-thought. Store observable evidence, alternatives, decisions, tests, critiques, and concise rationales instead.
- Keep `.agents/plugins/marketplace.json` as the canonical local marketplace metadata; do not add a duplicate root copy.

## Before committing changes

Run:

```bash
python tests/validate_pack.py
python tests/validate_graph.py
python skills/evaluate/scripts/calculate_metrics.py examples/sample-loop-log.jsonl
```

When installer behavior changes, smoke-test install and uninstall against an isolated temporary HOME.
