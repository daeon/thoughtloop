# ThoughtLoop repository instructions

ThoughtLoop is a Codex skill pack for deliberate problem solving. Preserve the public architecture **Discover → Decide → Execute → Prove** and the tagline **Think wider. Build better. Prove it.**

## Repository invariants

- `skills/thoughtloop/` is the primary orchestrator and the only skill that permits implicit invocation.
- `skills/self-correction/` is a deprecated explicit-only compatibility alias. Do not add independent orchestration logic there.
- Specialist skills remain explicit-only unless a future design change is justified and tested.
- Evidence must outrank model confidence; unavailable evidence is `UNKNOWN`, never an implicit `PASS`.
- Keep exploration and verification bounded.
- Do not require, request, or log hidden chain-of-thought. Store observable evidence, alternatives, decisions, tests, critiques, and concise rationales instead.
- Keep `.agents/plugins/marketplace.json` as the canonical local marketplace metadata; do not add a duplicate root copy.

## Before committing changes

Run:

```bash
python tests/validate_pack.py
python skills/loop-evaluator/scripts/calculate_metrics.py examples/sample-loop-log.jsonl
```

When installer behavior changes, smoke-test install and uninstall against an isolated temporary HOME.
