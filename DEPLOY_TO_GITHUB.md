# Deploy ThoughtLoop to GitHub

This archive is intended to become the repository root for a standalone public repository named **`thoughtloop`**.

## Recommended repository metadata

- **Repository name:** `thoughtloop`
- **Description:** `Deliberate problem solving for coding agents — discover, decide, execute, and prove.`
- **License:** MIT
- **Visibility:** Public
- **Default branch:** `main`
- **Suggested topics:** `codex`, `codex-skills`, `agent-skills`, `coding-agents`, `ai-agents`, `agentic-coding`, `deliberation`, `problem-solving`, `verification`, `self-correction`, `software-engineering`

## Deployment checklist

1. Extract the archive so these files are at the repository root.
2. Run `python tests/validate_pack.py`.
3. Run `python skills/loop-evaluator/scripts/calculate_metrics.py examples/sample-loop-log.jsonl`.
4. Initialize or create the GitHub repository `thoughtloop`.
5. Commit the complete repository as `Initial ThoughtLoop release`.
6. Push to `main`.
7. Confirm the rendered README starts with **ThoughtLoop** and **Think wider. Build better. Prove it.**
8. Confirm `.codex-plugin/plugin.json` reports plugin name `thoughtloop` and version `0.4.0`.

## Codex deployment prompt

If this ZIP is uploaded into a Codex session, the following instruction is sufficient:

> Extract this archive and deploy it as a new public GitHub repository named `thoughtloop`. Preserve the archive contents as the repository root. Read `AGENTS.md` first, run the validation and sample metrics commands, fix any packaging issue you find without changing the intended architecture, create the repository with the metadata in `DEPLOY_TO_GITHUB.md`, commit as `Initial ThoughtLoop release`, push `main`, and return the repository URL plus validation results.
