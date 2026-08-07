# Adaptive routing: exploration depth × verification risk

Choose the least expensive workflow that still searches enough of the solution space **and** establishes correctness to the level the task warrants.

These are independent axes.

## Exploration depth

### 0 — Execute

Use when all are mostly true:

- task is mechanical or tightly specified;
- one implementation path is obvious;
- alternative architectures are unlikely to change the outcome;
- ambiguity is low.

Typical path: Builder -> Prove.

### 1 — Consider alternatives

Use when:

- there are a few plausible implementation strategies;
- a moderate refactor/design choice exists;
- selecting the wrong local approach would create avoidable work.

Typical path: Explorer (about 3 families) -> Synthesizer -> Execute.

### 2 — Deep search

Use when any are true:

- architecture or system boundaries are changing;
- debugging has multiple plausible causal models;
- the task has meaningful cost/performance/complexity tradeoffs;
- the obvious solution may be locally optimal;
- a wrong strategy would be expensive to unwind.

Typical path: Explorer -> Challenger -> Synthesizer -> Execute.

### 3 — Open problem

Use when:

- requirements or framing are themselves uncertain;
- the problem is strategic or novel;
- success depends on challenging inherited constraints;
- there is high leverage in discovering a non-obvious solution family.

Use bounded multi-lens discovery. Stop when new ideas are mostly variants or when experiments are more valuable than further ideation.

## Verification risk

### Low

Use when all are mostly true:

- failure impact is low;
- task is reversible;
- deterministic checks cover most important behavior.

Typical prove path: deterministic checks -> deliver.

### Medium

Use when any are true:

- multiple requirements interact;
- deterministic checks cover only part of correctness;
- factual claims need source verification;
- regressions are plausible.

Typical prove path: Verifier -> Judge -> targeted revision.

### High

Use when any are true:

- failure could be materially costly;
- security, privacy, permissions, money, production data, or legal/compliance boundaries are involved;
- failures may be subtle and tests are incomplete;
- the user requests adversarial or exhaustive review.

Typical prove path: Verifier -> Judge -> Adversarial Review -> regression verification.

## Matrix examples

- Rename a symbol: exploration 0, verification low.
- Nontrivial parser fix with two plausible strategies: exploration 1, verification medium.
- Performance architecture redesign: exploration 2, verification medium/high.
- Novel product/system design with unclear assumptions: exploration 3, verification according to consequence.
- High-risk but mechanically specified security patch: exploration 0/1, verification high.

Do not confuse high verification risk with a need for broad exploration; they are separate decisions.
