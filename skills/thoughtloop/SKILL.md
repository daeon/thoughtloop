---
name: thoughtloop
description: Use for important tasks that benefit from adaptive discovery, explicit tradeoffs, economical execution, independent proof, and bounded correction.
---

# ThoughtLoop

ThoughtLoop is the single orchestrator for the pack. Use the mental model:

```text
DISCOVER -> DECIDE -> EXECUTE -> PROVE
```

The stages and graph are adaptive guidance, not a mandatory ceremony. Small
tasks stay small. High-risk work receives deeper discovery, engineering
investigation, independent evidence, and—when useful—red-team review.

## Intake

Identify the objective, hard requirements, acceptance criteria, material
assumptions, consequence of being wrong, and available time/tool/delegation
budget. Make important assumptions visible; do not invent a contract merely to
fill a template.

Choose the least expensive useful route:

- **Direct:** `builder -> verify -> judge` for mechanical or tightly specified
  work.
- **Deliberate:** `gapfinder -> discover -> decide -> builder -> verify ->
  judge` when meaningful alternatives matter.
- **Engineering:** `gapfinder -> investigate -> decide -> builder -> verify ->
  judge` for repository changes, debugging, logs, performance, migration,
  security, release, or compatibility work.
- **Deep:** add challenge, independent investigation, or review when framing,
  reversibility, or failure consequence justifies it.

Use `graphs/` for route examples, `core/contracts.md` for observable handoffs,
`core/routing.md` for node boundaries, and `core/budget-policy.md` for
delegation.

## Canonical graph nodes

Route to the smallest node that owns the next question:

| Node | Use |
|---|---|
| `$gapfinder` | Unknowns, falsifiers, and discovery-depth selection |
| `$discover` | Solution search, framing challenge, or prototype probes |
| `$investigate` | Repository, debugging, logs, or performance forensics |
| `$decide` | Selection or risk-first planning |
| `$builder` | Implementation or targeted revision |
| `$verify` | Independent evidence collection |
| `$judge` | Criterion-level PASS, FAIL, or UNKNOWN |
| `$review` | Post-check red-team review |
| `$revise` | Failure-depth routing |
| `$handoff` | Compact continuation state |
| `$evaluate` | Loop and budget improvement |
| `$standard-english` | Explicit language and documentation standards |

## Optional subagent mode

Activate only explicitly:

```text
$thoughtloop --subagents --budget=balanced <task>
```

When active, set `delegation.mode=subagents` and use `light`, `balanced`, or
`deep`. The parent owns the contract, synthesis, edits, evidence, verdict, and
user communication. Delegate narrow, independent questions with fresh context
(`fork_context=false` or the platform equivalent). Use lower-cost agents for
bounded search or mechanical review when adequate; reserve stronger reasoning
for disputed evidence and final decisions.

Starting budgets:

- `light`: one narrow subtask;
- `balanced`: up to two complementary subtasks;
- `deep`: up to three complementary subtasks and one follow-up round.

Across all budgets, allow at most one follow-up delegation round. Do not spend
delegation budget when the task is already clear, cheap to verify, or blocked by
missing authority. If subagents are unavailable, continue in parent-only mode.

## Decide and prove

Use `$decide` after meaningful discovery or investigation. It must choose
`BUILD`, `EXPERIMENT`, or `EXPLORE` and preserve rejected approaches. Use
`$builder` only after the strategy is sufficiently supported or the user has
explicitly chosen it.

Use `$verify` for the strongest practical evidence and `$judge` for the final
criterion-level verdict. Evidence outranks confidence. Missing evidence is
`UNKNOWN`, not an implicit `PASS`. Add `$review` for high-risk or subtle work.

After a failure, use `$revise` to distinguish:

- `IMPLEMENTATION` — revise locally;
- `STRATEGY` — return to `$decide`;
- `ASSUMPTION_OR_FRAME` — return to `$discover` or `$gapfinder`;
- `EVIDENCE_GAP` — return to `$verify` or `$investigate`;
- `CONTRADICTION_OR_LIMIT` — explain the blocker or escalate.

Do not loop indefinitely. Two failed local corrections against the same blocker
are a signal to backtrack.

## Observable state

Pass compact contracts between nodes. Store facts, assumptions, alternatives,
decisions, evidence, tests, critiques, and concise rationales only; never
request or record hidden chain-of-thought. State may be prose, a table, or JSON
but should preserve the contracts in `core/contracts.md`.
