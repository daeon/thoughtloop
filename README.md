# ThoughtLoop

**Think wider. Build better. Prove it.**

ThoughtLoop is an installable Codex skill pack for **deliberate problem solving**:

> **Discover → Decide → Execute → Prove**

The pack now uses two nested loops:

- an **outer strategic loop** that searches the solution space, challenges assumptions, selects an approach, and backtracks when the strategy or framing is wrong;
- an **inner evidence-first loop** that implements, verifies, judges, and minimally corrects the selected approach.

The central idea is simple:

> Do not perfectly verify the first plausible idea. Search enough first, then prove what you build.

## Why ThoughtLoop

Most coding agents converge on the first plausible approach and spend their remaining effort polishing it. ThoughtLoop deliberately separates **search** from **proof**: it explores materially different approaches when the problem warrants it, commits using explicit tradeoffs and evidence, then independently verifies the chosen result.

The public mental model is simple:

> **Think wider. Build better. Prove it.**

Internally, that becomes **Discover → Decide → Execute → Prove** with bounded backtracking at the level where failure actually originates.

## Skills

| Stage | Skill | Role |
|---|---|---|
| Orchestration | `thoughtloop` | Routes exploration depth, verification risk, and failure-depth backtracking. |
| Compatibility | `self-correction` | Deprecated explicit alias that redirects to `thoughtloop`. |
| Discover | `explorer` | Searches materially different solution families and proposes discriminating experiments. |
| Discover | `challenger` | Attacks framing, assumptions, inherited constraints, and local optima before commitment. |
| Decide | `synthesizer` | Eliminates dominated options, combines strengths, and chooses BUILD / EXPERIMENT / EXPLORE. |
| Execute | `builder` | Implements the selected strategy or a minimal targeted revision. |
| Execute / Control | `revision-manager` | Classifies failure depth and routes to revise, reconsider, rediscover, verify, or escalate. |
| Prove | `ground-truth-verifier` | Collects deterministic or authoritative evidence. |
| Prove | `judge` | Applies criteria to artifact + evidence using PASS / FAIL / UNKNOWN. |
| Prove | `adversarial-review` | Searches an apparently finished artifact for hidden defects and fragile assumptions. |
| Meta | `loop-evaluator` | Measures search quality, decision quality, correction efficiency, and proof reliability. |

Only `thoughtloop` permits implicit invocation. The deprecated `self-correction` alias remains explicit-only for compatibility. Specialist skills are explicit by default so they do not trigger on unrelated work.

## Architecture

```text
Problem
  │
  ▼
ThoughtLoop Router
  │
  ├── DISCOVER ──► Explorer ──► Challenger (when warranted)
  │                                  │
  │                                  ▼
  ├── DECIDE ────────────────► Synthesizer
  │                                  │
  │                         ┌────────┼────────┐
  │                         │        │        │
  │                      BUILD   EXPERIMENT  EXPLORE
  │                         │        │        │
  │                         ▼        └────┐   └──► Discover
  ├── EXECUTE ───────────► Builder       │
  │                         │             │
  │                         ▼             │
  └── PROVE ───────► Verifier ─► Judge ◄─┘
                                  │
                 ┌────────────────┼──────────────────┐
                 │                │                  │
              PASS      IMPLEMENTATION FAIL     DEEPER FAIL
                 │                │                  │
                 ▼                ▼                  ▼
             deliver      Revision Manager    strategy/frame/evidence
                                                   backtrack
```

For high-risk work, ordinary PASS can be followed by `adversarial-review` before delivery.

## Failure-depth routing

A key invariant is: **fix the level that is actually wrong**.

| Failure depth | Meaning | Route |
|---|---|---|
| `IMPLEMENTATION` | Strategy is sound; artifact is wrong | Revision Manager → Builder → Prove |
| `STRATEGY` | Selected approach is structurally poor | Synthesizer → alternative/hybrid → Execute |
| `ASSUMPTION_OR_FRAME` | Premise or boundary is wrong | Challenger/Explorer → Synthesizer |
| `EVIDENCE_GAP` | Correctness cannot yet be established | Verifier / discriminating experiment |
| `CONTRADICTION_OR_LIMIT` | Requirements/tools/budgets block success | Escalate / expose unresolved state |

This prevents the common agent failure mode of repeatedly editing an implementation when the architecture or premise is the real problem.

## Adaptive compute

Exploration depth and verification risk are separate axes.

### Exploration

- **0 — Execute:** mechanical/tightly specified.
- **1 — Consider alternatives:** a few plausible strategies.
- **2 — Deep search:** architecture, hard debugging, consequential refactor.
- **3 — Open problem:** framing/assumptions themselves may be wrong.

### Verification

- **Low:** deterministic checks cover most risk.
- **Medium:** multiple requirements, sources, regressions, partial observability.
- **High:** costly failures, security/privacy/production boundaries, subtle defects.

Examples:

```text
rename symbol                 exploration 0 / verification low
parser redesign               exploration 1 / verification medium
performance architecture      exploration 2 / verification medium-high
novel system/product problem  exploration 3 / verification depends on stakes
security patch                exploration 0-1 / verification high
```

## Discovery quality

`$explorer` does not simply “brainstorm five ideas.” It searches by orthogonal dimensions such as architecture, timing, state ownership, operational complexity, and constraint inversion.

When useful, it creates an idea graph rather than a flat list:

```text
problem
├── avoid work
│   ├── precompute
│   └── change contract
├── reuse work
│   ├── local cache
│   └── distributed cache
└── move work
    ├── event-driven
    └── build-time
```

Discovery stops when new ideas are mostly variants or when the remaining uncertainty is empirical. At that point, the system should **measure**, not keep thinking.

## Core guarantees

1. **Search and proof are separate capabilities.**
2. **Meaningful divergence happens before commitment when warranted.**
3. **The Challenger attacks framing; Adversarial Review attacks the finished artifact.**
4. **Selection uses explicit tradeoffs, not fake `8.7/10` precision.**
5. **Evidence outranks model confidence.**
6. **Lack of evidence becomes `UNKNOWN`, not `PASS`.**
7. **Failure is classified by depth before another retry.**
8. **Revisions are minimal and regression-aware.**
9. **Both discovery and correction are bounded.**
10. **Hidden chain-of-thought is never required or logged.** Store observable evidence, alternatives, decisions, tests, critiques, and concise rationales instead.

## Quick start

```text
$thoughtloop Redesign this caching layer. Search materially different approaches, choose deliberately, implement the best one, and prove it with evidence.
```

Use specialist skills directly when you want only one stage, for example `$explorer`, `$challenger`, `$ground-truth-verifier`, or `$adversarial-review`.

## Install / use

### As a Codex plugin

The repository is packaged as a skills-only plugin via `.codex-plugin/plugin.json` and includes `.agents/plugins/marketplace.json` for local/repository marketplace testing.

### As standalone local skills

Codex discovers user skills from `$HOME/.agents/skills`. Install all skills with:

```bash
python scripts/install_local.py
```

This creates symlinks by default. Use `--copy` for independent copies and `--force` to replace existing skill paths.

Remove them with:

```bash
python scripts/uninstall_local.py
```

## Examples

```text
$thoughtloop Redesign this caching path. Explore materially different architectures, benchmark the decision-sensitive unknowns, implement the best option, and verify it.

$thoughtloop Diagnose this intermittent race. Search multiple causal models before changing code, then prove the fix with a reproduction test.

$explorer Search the solution space for reducing p99 latency without adding another service.

$challenger Challenge the assumptions behind this architecture before we commit.

$synthesizer Decide between these approaches and tell me whether we should build, experiment, or explore further.

$ground-truth-verifier Verify whether this implementation satisfies the stated behavior.

$adversarial-review Try to break this refactor after its ordinary tests pass.

$loop-evaluator Evaluate these run logs for premature convergence and correction-loop waste.
```

## Compatibility

`$self-correction` is retained as a deprecated, explicit-only alias for users of pre-ThoughtLoop releases. New documentation and integrations should use `$thoughtloop`. The alias contains no independent workflow logic; it delegates to ThoughtLoop.

## Validate the pack

```bash
python tests/validate_pack.py
```

The validator uses only the Python standard library.

To exercise the sample metrics log:

```bash
python skills/loop-evaluator/scripts/calculate_metrics.py examples/sample-loop-log.jsonl
```

## License

MIT. See `LICENSE`.
