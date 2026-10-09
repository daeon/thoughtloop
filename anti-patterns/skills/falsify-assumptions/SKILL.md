---
name: falsify-assumptions
description: Challenge a diagnosis, preferred solution, or material decision by identifying credible competing hypotheses and cheap disconfirming tests. Use for uncertain root causes, architectural choices, and high-impact assumptions; not for routine mechanical tasks.
---

# Falsify Assumptions

Use this procedure when the cost of accepting the wrong explanation or design is meaningful. This skill is complete by itself and requires no other skills, agents, or tools beyond those available for the task.

## Input
The question or proposed explanation, available observations, constraints, and what decision will depend on the answer. If an essential input is missing, proceed with bounded assumptions and label them; ask only when the missing fact determines a high-consequence choice.

## Procedure
1. **Neutralize anchoring.** Rewrite the problem as observed behavior versus expected behavior, without embedding the proposed cause as fact.
2. **Generate distinct alternatives.** Supply two or three *materially different* hypotheses, including a simple or null explanation when plausible. Do not generate token alternatives merely to reach a number.
3. **Find the discriminators.** For each serious hypothesis, name one observation supporting it and one that would falsify or substantially weaken it.
4. **Rank by evidence and reversibility.** Distinguish measured facts from intuition. Avoid false numerical probabilities; qualitative confidence is acceptable with reasons.
5. **Choose the cheapest decisive next check.** Prefer a targeted log query, failing reproduction, small experiment, primary source, or specific code inspection over an expensive investigation.
6. **Update the answer.** After evidence is obtained, revise the diagnosis. If the check cannot be run, clearly label the conclusion provisional.

## Output
- **Observed facts** (with source or how observed)
- **Working hypothesis** and material alternative(s)
- **Cheapest disconfirming check** and expected observations
- **Decision now**: investigate, proceed provisionally, or stop
- **Unknowns** that could reverse the decision

## Stop rules
Do not demand exhaustive alternatives. Skip deep analysis when the task is trivial, the conclusion is directly observable, or more debate will not change the decision.

## Example
Input: "The service is slow, so add caching." Possible alternatives: DB lock contention, fan-out latency, or a missing index. Compare traces before adding cache complexity.
