---
name: thoughtloop
description: Use implicitly for consequential multi-step coding work involving material alternatives, uncertain causes, migrations, compatibility, security, performance, or independent proof. Do not invoke for simple explanations, formatting, trivial edits, routine commands, or tasks already governed by a more specific skill.
---

# ThoughtLoop

ThoughtLoop is the pack's only orchestrator. Use the mental model:

```text
DISCOVER -> DECIDE -> EXECUTE -> PROVE
```

The stages are adaptive guidance, not mandatory ceremony. Small tasks stay
small. Consequential work receives the minimum deeper discovery and proof that
the risk justifies.

## Intake and route selection

Identify the objective, hard requirements, acceptance criteria, material
assumptions, consequence of being wrong, and available time, tool, and
delegation budget. Make important assumptions visible; do not invent a contract
merely to fill a template.

Choose the least expensive useful route:

- **Direct:** `execute -> verify -> final-judgment` for mechanical or tightly
  specified work.
- **Deliberate:** `gapfinder -> discover -> decide -> execute -> verify ->
  final-judgment` when meaningful alternatives matter.
- **Engineering:** `gapfinder -> investigate -> decide -> execute -> verify ->
  final-judgment` for repository changes, debugging, logs, performance,
  migration, security, release, or compatibility work.
- **Deep:** add challenge, independent investigation, or `review` when framing,
  reversibility, or failure consequence justifies it.

Read the route references under `references/routes/` when the task matches a
profile. When a public specialist is available and the host supports loading
it, follow that specialist's instructions for its stage. Otherwise perform the
compact fallback described in this directory.

## Public capability nodes

These are the independently callable capabilities in the pack:

| Node | Use |
|---|---|
| `$gapfinder` | Surface expensive unknowns and choose discovery depth |
| `$discover` | Search solution families, challenge framing, or probe alternatives |
| `$investigate` | Map repositories, debug failures, analyze logs, or measure performance |
| `$decide` | Select an approach or create a risk-first plan |
| `$verify` | Collect criterion-specific independent evidence |
| `$review` | Red-team high-risk or subtle results after ordinary checks |
| `$handoff` | Preserve compact continuation state |

`thoughtloop` owns execution, final judgment, correction routing, and loop
evaluation as internal stages. They are not separate public skills.

## Observable state

Pass compact, observable state between stages. Preserve facts, assumptions,
alternatives, decisions, evidence, tests, critiques, concise rationales, and
the next action. Never request or record hidden chain-of-thought. The installed
contracts are in `references/contracts.md`.

Evidence outranks confidence. An unavailable check is `UNKNOWN`, not an
implicit pass. A final `PASS` requires every blocking criterion to have
sufficient supporting evidence and no unresolved blocking review finding.

## Specialist-independent fallback

When a selected public specialist cannot be loaded, continue with these
minimum stage behaviors instead of treating the graph edge as executable code:

- **Discover:** identify materially different solution or explanation families,
  expose assumptions, and name the cheapest falsifier for each important
  difference.
- **Decide:** choose `BUILD`, `EXPERIMENT`, or `EXPLORE`; preserve rejected
  approaches and state which evidence would change the choice.
- **Execute:** make the smallest coherent authorized change and preserve passing
  behavior.
- **Verify:** gather criterion-specific evidence, provenance, and limitations;
  separate supporting, failing, and inconclusive results.
- **Review:** for high-risk or subtle work, seek counterexamples, regressions,
  security issues, contradictions, and coverage gaps.
- **Final judgment:** derive criterion-level `PASS`, `FAIL`, or `UNKNOWN` from
  all verification and review evidence; do not pass with unresolved blocking
  review findings.
- **Correct:** classify the failure depth and return to the stage that owns the
  wrong assumption.

These fallbacks are sufficient to complete every route with only the installed
`thoughtloop` directory present. Specialist instructions add depth; they are
not runtime dependencies.

## Optional subagent mode

Delegation is opt-in. Use bounded independent questions only when they add
signal that is worth their cost. The parent owns the task contract, synthesis,
edits, evidence, final outcome, and user communication. The installed budget
policy is in `references/budget-policy.md`; its budgets are `light`, `balanced`,
and `deep`.

If subagents are unavailable, continue in parent-only mode. Prefer a fresh context
when the host supports it, and require each delegated result to name
the question, evidence inspected, result, uncertainty, and whether it changed
anything. Do not delegate a task that is already clear, cheap to verify, or
blocked by missing authority.

Use lower-cost agents for bounded inspection when adequate, and reserve
stronger reasoning for disputed evidence and final synthesis.

## Internal execution stages

### Execute

Make the smallest coherent authorized change after the strategy is sufficiently
supported. Preserve requirements and passing behavior. If implementation
evidence invalidates the strategy, stop and route the conflict to correction
rather than silently changing the plan. See `references/execution.md`.

### Final judgment

Evaluate each material criterion independently:

- `PASS` — evidence is sufficient to support compliance;
- `FAIL` — evidence demonstrates noncompliance;
- `UNKNOWN` — evidence is insufficient or unavailable.

The overall result is `FAIL` if a blocking criterion fails, otherwise `UNKNOWN`
if a blocking criterion remains unknown, otherwise `PASS`.

### Correct

Classify a blocking failure as implementation, strategy, assumption or frame,
evidence gap, or contradiction or limit. Return to the stage that owns the
wrong assumption. After two failed local corrections against the same blocker,
backtrack instead of repeating the same patch. See `references/correction.md`.

## Stop conditions

Stop with a visible blocker when authority, required evidence, or a safe
rollback path is unavailable. Do not turn missing evidence into confidence or
continue indefinitely after repeated failure.
