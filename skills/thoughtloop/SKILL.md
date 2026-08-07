---
name: thoughtloop
description: Use for important tasks that benefit from deliberate solution-space search, strategy selection, implementation, independent verification, and bounded correction. Trigger for hard problems, architecture choices, debugging with multiple hypotheses, rigorous review, deliberate problem solving, self-correction, or requests to improve until evidence-backed criteria pass. Route adaptively: discover only when design freedom warrants it, and verify only as deeply as risk warrants.
---

# ThoughtLoop

Use ThoughtLoop to solve important tasks with two nested loops:

- an **outer strategic loop** that searches, challenges, and selects approaches;
- an **inner execution loop** that builds, verifies, judges, and minimally corrects.

The core workflow is:

`DISCOVER -> DECIDE -> EXECUTE -> PROVE`

Do not merely ask the same model to reconsider its answer. Do not verify the first plausible idea so aggressively that you miss a substantially better one.

## Core principles

1. **Diverge before converging when the task has meaningful design freedom.**
2. **Challenge framing before optimizing inside it.**
3. **Commit deliberately; do not choose by arbitrary numeric scores.**
4. **Prefer independent evidence over model confidence.**
5. **Backtrack at the depth where the failure originates.**
6. **Use the smallest exploration and verification budgets that fit the task.**
7. **Bound both brainstorming and correction loops.**

When another installed specialist skill is better suited to discovery, implementation, evidence collection, or evaluation, compose with it instead of duplicating domain expertise.

## Step 1 — Build the problem contract

Derive a compact state before acting:

- `objective`: what outcome is needed;
- `hard_constraints`: user/repository/interface requirements that cannot be violated;
- `soft_constraints`: preferences and inherited design choices that may be challenged;
- `acceptance_criteria`: at most 8 concrete criteria for the finished result;
- `important_unknowns`: facts that could change the approach;
- `exploration_level`: `0`, `1`, `2`, or `3`;
- `verification_risk`: `low`, `medium`, or `high`;
- `max_execution_revisions`: default `3`;
- `max_strategic_backtracks`: default `2`;
- `max_discovery_passes`: default `2`.

Do not invent hidden user requirements. Derive constraints and criteria from the request, repository instructions, tests, specifications, observed behavior, and authoritative sources.

Read `references/routing.md` when exploration or verification intensity is not obvious.

## Step 2 — Route exploration separately from verification

Exploration and verification answer different questions:

- **Exploration:** Are we solving the problem in the best available way?
- **Verification:** Did the chosen solution actually satisfy the requirements?

### Exploration level 0 — Execute

Use when the task is mechanical, tightly specified, or has one obvious implementation path.

`Builder -> Prove`

### Exploration level 1 — Consider alternatives

Use when a moderate design choice exists.

`Explorer(about 3 approaches) -> Synthesizer -> Execute -> Prove`

### Exploration level 2 — Deep search

Use for architecture, difficult debugging, significant refactors, or decisions with several plausible strategies.

`Explorer -> Challenger -> Synthesizer -> Execute -> Prove`

### Exploration level 3 — Open problem

Use for ambiguous, strategic, novel, or high-leverage problems where framing itself may be wrong.

Use orthogonal discovery lenses, an idea graph when helpful, and up to the bounded discovery budget. Prefer experiments over endless ideation when remaining uncertainty is empirical.

Do not invoke discovery stages just to spend tokens.

## Step 3 — DISCOVER

When `exploration_level > 0`, invoke `$explorer` when available.

The Explorer should search **materially different solution families**, not generate cosmetic variants. It should expose unexplored branches and identify experiments that could discriminate between leading ideas.

When `exploration_level >= 2`, the framing is uncertain, or the obvious solution may be locally optimal, invoke `$challenger`.

The Challenger should distinguish:

- hard constraints;
- evidence-backed assumptions;
- inherited conventions;
- conveniences;
- unknowns.

Do not let the Challenger override explicit hard requirements without evidence.

Read `references/solution-space-search.md` for search lenses and stopping rules.

## Step 4 — DECIDE

Invoke `$synthesizer` when discovery produced multiple meaningful approaches.

The Synthesizer should:

- eliminate hard-constraint violations and dominated options;
- combine compatible strengths where useful;
- expose tradeoffs and decision-sensitive unknowns;
- choose `BUILD`, `EXPERIMENT`, or `EXPLORE`;
- avoid arbitrary numeric scoring.

If a cheap experiment can decide between leading strategies, run the experiment before committing. Treat experiments as evidence, not as another brainstorming turn.

Stop discovery when new ideas are mostly variants, relevant solution families are covered, or remaining uncertainty requires evidence rather than more ideation.

## Step 5 — EXECUTE

Invoke `$builder` when available.

Give the Builder the **selected strategy**, task contract, and relevant evidence. Do not give it the entire rejected-idea transcript unless needed.

The Builder should produce a complete artifact plus observable assumptions, unresolved uncertainties, and recommended checks. It is not the final authority on correctness.

For a revision, provide only:

- current artifact or relevant patch context;
- failed/unknown blocking criteria;
- supporting evidence;
- the selected strategy and invariants;
- the minimal correction plan.

## Step 6 — PROVE with independent evidence

Invoke `$ground-truth-verifier` when available.

Use the strongest practical evidence source. Read `references/evidence-ladder.md` when choosing between alternatives.

Examples:

- runtime behavior;
- compiler/type-checker output;
- unit/integration tests;
- static analysis;
- repository specifications;
- primary sources and official documentation;
- raw data and recalculation;
- deterministic structural checks.

A model's assertion that something is correct is not ground truth.

Then invoke `$judge` when available.

Every criterion receives exactly one status:

- `PASS` — sufficient evidence supports compliance;
- `FAIL` — evidence demonstrates noncompliance;
- `UNKNOWN` — available evidence cannot establish the criterion.

Never convert `UNKNOWN` into `PASS` for convenience.

## Step 7 — Classify failure depth before retrying

Do not assume every failure should trigger another implementation edit.

Classify a blocking failure as one of:

### `IMPLEMENTATION`

The strategy remains sound; the artifact is wrong or incomplete.

Route:

`Revision Manager -> Builder -> Prove`

### `STRATEGY`

Repeated or structural evidence shows the selected approach is poorly suited, excessively complex, or unable to satisfy the criteria economically.

Route:

`Synthesizer -> choose another/hybrid strategy -> Execute -> Prove`

### `ASSUMPTION_OR_FRAME`

Evidence falsifies an assumption or reveals that the problem boundary is wrong.

Route:

`Challenger / Explorer -> Synthesizer -> Execute -> Prove`

### `EVIDENCE_GAP`

The artifact may be correct, but the needed fact is unknown.

Route:

`Verifier / discriminating experiment -> Judge`

Do not rewrite code merely to compensate for unavailable evidence.

### `CONTRADICTION_OR_LIMIT`

Requirements conflict, permissions/tools are insufficient, or the task cannot be established within the available system.

Route:

`Escalate / report unresolved state`

Read `references/failure-depth.md` for the routing contract.

## Step 8 — Revise minimally when the failure is implementation-level

Invoke `$revision-manager` when available.

The correction plan should:

- target blocking failures first;
- preserve already-passing behavior and strategic invariants;
- identify regression-sensitive areas;
- avoid broad rewrites unless evidence requires them;
- recommend a deeper backtrack if the failure is structural rather than local.

After revision, rerun all checks plausibly affected by the change.

## Step 9 — Adversarial review when justified

For high verification risk or explicitly requested rigorous review, invoke `$adversarial-review` after ordinary criteria pass.

Treat adversarial findings as hypotheses until evidence supports them. Confirmed findings re-enter the failure-depth router rather than automatically causing local revisions.

## Step 10 — Bound both loops

Deliver when all required criteria are `PASS` and no justified strategic concern remains unresolved.

Stop or escalate when any applies:

- `max_execution_revisions` is reached;
- the same blocking implementation failure persists across two revisions;
- `max_strategic_backtracks` is reached;
- `max_discovery_passes` is reached;
- new discovery produces only near-duplicates;
- requirements are contradictory;
- required evidence is inaccessible;
- the latest attempt makes no measurable progress;
- a high-risk blocking `UNKNOWN` remains unresolved.

Do not keep brainstorming or correcting indefinitely.

## Step 11 — Deliver

Return:

1. the finished artifact or completed change;
2. the selected approach and any material tradeoff worth preserving;
3. a concise verification summary;
4. any material unresolved `UNKNOWN` items;
5. what was actually tested, measured, or checked.

Do not expose or require hidden chain-of-thought. Record observable evidence, alternatives, decisions, critiques, tests, and concise rationales only.

## Composition with other skills

Specialist skills may act as nodes in any stage:

- architecture/design skills can feed Discover;
- benchmarking/profiling skills can run discriminating experiments;
- domain implementation skills can feed Execute;
- security/testing/source-retrieval skills can feed Prove;
- language/style standards can become explicit Judge criteria.

Prefer specialist capabilities over generic model critique.
