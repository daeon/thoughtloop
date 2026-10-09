---
name: lean-agent-design
description: Simplify an agent, skill pack, or multi-step AI workflow by finding duplicated responsibilities, instruction conflicts, unneeded delegation, and cost-heavy loops. Use for agent architecture reviews or bloated prompt systems; not for unrelated code formatting.
---

# Lean Agent Design

Optimize for reliable accepted outcomes per unit of total effort, not for the number of agents, rules, tool calls, or prompt tokens. This skill is standalone.

## Procedure
1. **Define the job.** State the outcome, critical constraints, what fails today, and observable quality measures. Note any unsupported premises about agent effectiveness.
2. **Map the actual flow.** Identify entry points, prompts, tool permissions, agents, handoffs, feedback loops, and acceptance checks. Use only components that exist; do not invent infrastructure.
3. **Identify duplication.** Find responsibilities covered by multiple prompts, review stages that repeat the same evidence, unused memory, and routing that could be deterministic.
4. **Pick the cheapest sufficient shape.** Compare: direct deterministic code; a fixed workflow with optional model calls; one agent; multiple independent agents. Consider latency, model cost, human review, reliability, permissions, and maintenance.
5. **Propose deletions before additions.** State what to remove, combine, narrow, or leave alone. Preserve necessary security, authorization, and recovery controls.
6. **Define a falsifiable comparison.** Select representative tasks, acceptance criteria, elapsed time, human time, failure rate, and cost. Compare baseline versus proposed design under similar conditions.
7. **Set a stopping condition.** Recommend retaining added complexity only if measured improvement justifies it or it is required for safety.

## Output
| Component | Problem / evidence | Proposed change | Risk | How to measure |
|---|---|---|---|---|

Include a **minimum viable workflow**, what not to change, and an explicit measurement plan.

## Constraints
Do not automatically argue for fewer agents: independent search or review can be beneficial. Do not remove required audit trails, permission gates, or independently observable checks merely to reduce tokens.
