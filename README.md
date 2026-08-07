# ThoughtLoop

**Think wider. Build better. Prove it.**

ThoughtLoop is an installable Codex skill pack for deliberate problem solving:

> **Discover -> Decide -> Execute -> Prove**

It helps an agent search when alternatives matter, challenge weak framing, choose with explicit tradeoffs, implement economically, and establish correctness with evidence. The stages are adaptive guidance—not a mandatory ceremony.

## Skills

| Stage | Skill | Role |
|---|---|---|
| Orchestration | `thoughtloop` | Routes the appropriate amount of search, execution, proof, correction, and optional delegation. |
| Compatibility | `self-correction` | Deprecated explicit alias that redirects to `thoughtloop`. |
| Discover | `explorer` | Covers materially different solution families. |
| Discover | `challenger` | Tests framing and inherited assumptions before commitment. |
| Decide | `synthesizer` | Chooses, combines, or experimentally distinguishes approaches. |
| Execute | `builder` | Implements the selected strategy or a targeted revision. |
| Control | `revision-manager` | Routes failures to the level that is actually wrong. |
| Prove | `ground-truth-verifier` | Collects independent evidence. |
| Prove | `judge` | Applies `PASS`, `FAIL`, or `UNKNOWN` to criteria. |
| Prove | `adversarial-review` | Looks for hidden defects after ordinary checks. |
| Meta | `loop-evaluator` | Measures loop quality, evidence quality, and budget use. |

Only `thoughtloop` permits implicit invocation. Other skills are explicit by default so they do not trigger on unrelated work.

## Subagent mode

Subagent mode is opt-in:

```text
$thoughtloop --subagents --budget=balanced Redesign this caching layer.
```

It uses narrow, fresh-context delegation when that adds independent signal. The parent agent remains responsible for decisions, edits, evidence synthesis, and the final result. Lower-cost agents are appropriate for bounded search or mechanical checks; stronger reasoning is reserved for tradeoffs, disagreements, and final decisions.

Use no delegation for trivial work, roughly one agent for a moderate decision, and two or three for complex or high-risk work. These are starting points, not quotas. Do not request or record hidden chain-of-thought.

## Quick start

```text
$thoughtloop Redesign this caching layer. Explore only if materially different approaches could change the result, then implement and prove the choice.
```

Use a specialist directly when you want one stage:

```text
$explorer Search for materially different ways to reduce p99 latency.
$challenger Challenge the assumptions behind this architecture.
$ground-truth-verifier Verify whether this implementation satisfies the stated behavior.
$adversarial-review Try to break this refactor after its ordinary tests pass.
```

## Install

### As a Codex plugin

The repository is packaged as a skills-only plugin via `.codex-plugin/plugin.json` and includes `.agents/plugins/marketplace.json` for local marketplace testing.

### As standalone local skills

Codex discovers user skills from `$HOME/.agents/skills`. Install all skills with:

```bash
python scripts/install_local.py
```

Use `--copy` for independent copies and `--force` to replace existing skill paths. Remove them with:

```bash
python scripts/uninstall_local.py
```

## Validate

```bash
python tests/validate_pack.py
python skills/loop-evaluator/scripts/calculate_metrics.py examples/sample-loop-log.jsonl
```

The validator uses only the Python standard library. The metrics script reports signals such as exploration, revisions, regressions, unknowns, cost, tokens, and runtime; interpret them in context rather than treating them as a single quality score.

## Compatibility

`$self-correction` remains a deprecated, explicit-only alias for older workflows. New integrations should call `$thoughtloop` directly.

## License

MIT. See [LICENSE](LICENSE).
