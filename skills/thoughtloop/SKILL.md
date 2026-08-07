---
name: thoughtloop
description: Use for important tasks that benefit from deliberate solution search, explicit tradeoffs, implementation, independent evidence, and bounded correction. Adapt the depth to the task. Optional subagent mode adds narrow, fresh-context delegation when its accuracy benefit justifies its cost.
---

# ThoughtLoop

ThoughtLoop is a lightweight way to solve important problems without either rushing to the first plausible idea or verifying forever.

Use the mental model:

`DISCOVER -> DECIDE -> EXECUTE -> PROVE`

The stages are a guide, not a ritual. Skip a stage when it adds no useful signal.

## Start with a small contract

Before acting, identify as much as is useful of:

- the objective and hard requirements;
- preferences or inherited assumptions that may be revisable;
- concrete acceptance criteria;
- facts that could change the approach;
- the consequence of being wrong;
- the available time, token, tool, and delegation budget.

Do not invent requirements. Make important assumptions visible, and keep the contract compact.

For complex work, use `references/state-contract.md` as optional compact state guidance. Do not create state merely to satisfy a template.

## Choose the least expensive useful path

- **Direct:** execute and run proportionate checks for mechanical or tightly specified work.
- **Deliberate:** explore a few genuinely different approaches, then choose one when design freedom matters.
- **Deep:** challenge the framing as well when the task involves architecture, difficult debugging, costly reversals, or uncertain assumptions.

Increase verification with the consequence of failure. High verification risk does not automatically require broad brainstorming.

## Optional subagent mode

Activate it explicitly with wording such as:

```text
$thoughtloop --subagents --budget=balanced <task>
```

or:

```text
Use ThoughtLoop in subagent mode for this task.
```

When active:

1. Set `delegation.mode=subagents` and use the requested budget. If no budget is given, use `balanced`.
2. Keep the parent agent responsible for the contract, synthesis, edits, final verdict, and user communication.
3. Delegate narrow, independent questions or review slices. Do not send the whole task to several agents and compare prose.
4. Give each agent only the relevant objective, criteria, files, and evidence. Start with a fresh context (`fork_context=false` or the platform equivalent) unless inherited context is specifically needed. Never request hidden chain-of-thought.
5. Use lower-cost agents for bounded exploration, mechanical inspection, or first-pass review when adequate. Reserve the strongest available reasoning for difficult tradeoffs, synthesis, disputed evidence, and final decisions.
6. Parallelize only independent work. Apply these starting budgets, adjusting for risk and available tooling:
   - `light`: one narrow subtask;
   - `balanced`: up to two complementary subtasks, normally search plus evidence/review;
   - `deep`: up to three complementary subtasks, with at most one follow-up round after new evidence or a concrete disagreement.
   Across all budgets, allow at most one follow-up delegation round. If that does not resolve the issue, synthesize, verify, or escalate rather than spawning indefinitely.
7. Treat agent output as evidence or advice, not authority. Resolve disagreement with tests, sources, or a focused follow-up rather than a vote.
8. Do not spend delegation budget when the task is already clear, cheap to verify, or blocked by missing information. If the platform cannot provide subagents, continue in parent-only mode and report that limitation.

Useful assignments include:

- one agent searches solution families;
- one challenges assumptions or reviews a disjoint risk area;
- one gathers evidence or runs a targeted check;
- one reviews the integrated result for regressions.

The parent should pass concise findings between stages rather than replaying every agent transcript.

## Discover

When alternatives could materially change the result, use `$explorer` to cover different solution families, not cosmetic variants. Use `$challenger` when the framing or an inherited constraint may be wrong. Stop when relevant families are covered or an experiment is more valuable than more ideation.

Read `references/routing.md` when the appropriate depth or verification risk is unclear, and `references/solution-space-search.md` when discovery needs more structure.

## Decide

Use `$synthesizer` when there are meaningful alternatives. Eliminate hard-constraint violations, make tradeoffs explicit, combine strengths only when the hybrid stays understandable, and identify decision-sensitive unknowns. Choose to `BUILD`, `EXPERIMENT`, or `EXPLORE`; do not use arbitrary scores unless the task has a real scoring model.

## Execute

Use `$builder` to implement the selected approach. Preserve hard requirements and passing behavior. If implementation evidence invalidates the approach, surface the strategic problem instead of silently changing direction. Revisions should be narrow unless deeper evidence requires backtracking.

## Prove

Use `$ground-truth-verifier` for the strongest practical independent evidence, then `$judge` to compare that evidence with the criteria. Runtime behavior, tests, type checks, deterministic checks, authoritative sources, and raw calculations usually outrank model opinion. Missing evidence is `UNKNOWN`, not `PASS`.

Read `references/evidence-ladder.md` when evidence sources compete.

Use `$adversarial-review` after ordinary checks for high-risk work or when explicitly requested. Keep hypotheses separate from confirmed findings.

## Correct at the right depth

After a failure, use `$revision-manager` or equivalent reasoning to decide whether it is:

- `IMPLEMENTATION` — the approach is sound but the artifact is wrong;
- `STRATEGY` — the chosen approach is structurally poor;
- `ASSUMPTION_OR_FRAME` — a premise or boundary was falsified;
- `EVIDENCE_GAP` — the result is not established yet;
- `CONTRADICTION_OR_LIMIT` — requirements, tools, permissions, or budget prevent a defensible result.

Revise locally only for implementation failures. Backtrack to the relevant stage for deeper failures. Do not oscillate between the same options without new evidence.

Read `references/failure-depth.md` when the correct route is unclear.

## Stop and deliver

Stop when the required criteria are supported, or explain precisely what remains unknown or blocked. Bound discovery, revisions, and delegation according to risk and budget. A useful handoff states:

- what was decided and why;
- what changed;
- what evidence was collected;
- which criteria are `PASS`, `FAIL`, or `UNKNOWN`;
- remaining risks and the next useful action.

Never require or record hidden chain-of-thought. Keep alternatives, assumptions, decisions, evidence, tests, and concise rationales.

## Composition

Use specialist skills as needed:

- `$explorer`, `$challenger`, and `$synthesizer` for discovery and decisions;
- `$builder` and `$revision-manager` for execution;
- `$ground-truth-verifier`, `$judge`, and `$adversarial-review` for proof;
- `$loop-evaluator` to improve the problem-solving process itself.

Prefer domain-specific skills when they provide stronger evidence or implementation knowledge.
