# Independent AI Antipattern Prevention Toolkit

**Standalone by design.** No dependency on a particular repository, another skill, a supervisor skill, any vendor's model, external packages, or a custom orchestration graph.

## Included

- `AGENTS.md`: portable global instructions for Codex-style repositories (optional).
- `CLAUDE.md`: equivalent global instructions for Claude Code projects (optional).
- `skills/`: eight individually installable, self-contained Agent Skills. Every `SKILL.md` includes a when-to-use description, procedure, stopping rules, and output shape. No skill calls another.
- `agents/claude/`: three **optional** independently usable read-only specialist agents using Claude Code's native agent Markdown format. Their full prompts are contained in each file. For another agent runtime, copy the Markdown body after frontmatter into your agent's instructions and configure its tools separately.
- `evals/cases.jsonl`: positive and negative triggering fixtures for each skill, plus action safety examples. Fixtures are proposed behavioral tests, not model-executed benchmark results.
- `scripts/validate.py`: standard-library-only checks for file structure and fixture coverage. Validation is optional, not a skill dependency.

## Skill selection

| Skill | Use for | Don't invoke for |
|---|---|---|
| `falsify-assumptions` | Diagnoses, uncertain root causes, material decisions | Trivial changes |
| `evidence-audit` | Checking factual claims and verified completion | Free-form ideation |
| `test-oracle-audit` | Newly generated/modified tests, migrations, bug fixes | Unrelated prose |
| `lean-agent-design` | Removing workflow and instruction sprawl | Routine code formatting |
| `independent-review` | Adversarial requirements-first artifact review | Every tiny edit |
| `safe-external-actions` | Consequential writes, ambiguous timeouts, retries | Read-only inspection |
| `context-reconciliation` | Contradictory or stale notes, corrected state | Fully current context |
| `automation-reliability-audit` | Scheduled monitors, recurring reports, reliability incidents | One-off research |

Each skill is optional. Install only what you need. No global policy file is required for them to work.

## Install a skill independently

Copy **one** directory (for example `skills/falsify-assumptions/`) to a discovery path used by your agent:

```bash
# Codex: project-scoped skill
mkdir -p .agents/skills
cp -R /path/to/ai-antipatterns-independent/skills/falsify-assumptions .agents/skills/

# Claude Code: project-scoped skill
mkdir -p .claude/skills
cp -R /path/to/ai-antipatterns-independent/skills/falsify-assumptions .claude/skills/
```

Paths shown are common native project skill locations. Check your runtime's active skill discovery settings if customized. You can invoke a skill explicitly by name or let the runtime decide based on its frontmatter description.

For an optional global policy, merge `AGENTS.md` into the target project's existing `AGENTS.md` for Codex, or `CLAUDE.md` into its existing `CLAUDE.md` for Claude Code. **Do not overwrite existing instructions blindly.** These two files contain the same policy adapted only by filename; choose the relevant one, rather than stacking both within a single runtime.

## Install an optional Claude Code specialist agent

```bash
mkdir -p .claude/agents
cp /path/to/ai-antipatterns-independent/agents/claude/specification-critic.md .claude/agents/
```

The agent can inspect files with read-only tool configuration; it does not call other skills. If the host does not support subagents or its tool names differ, use the body as a standalone prompt and set read-only permissions in the host.

## Example invocations

- "Use `falsify-assumptions` to investigate why the p99 latency rose after the last deployment. Find the smallest decisive probe."
- "Use `test-oracle-audit` on the tests generated for this retry bug. Could they pass even if writes duplicate?"
- "Use `safe-external-actions` before retrying the spreadsheet append after a timeout. Check for an existing event ID."
- "Use `lean-agent-design` to simplify this creator/critic/refiner flow and design a fair baseline comparison."
- "Use `automation-reliability-audit` on a recurring inbox monitor. Distinguish no urgent email from the inability to check mail."

## Design principles

1. Small global rules; procedural detail lives in individual skills.
2. Narrow descriptions with positive and negative activation boundaries.
3. No hidden dependency, mandatory orchestrator, recursive delegation, or skill-to-skill invocation.
4. No permission escalation through prompt text. External actions need actual authorization and appropriate tool safeguards.
5. Evidence and observable state outrank apparent agreement.
6. A failed, partial, or unknown outcome stays visible.
7. Evaluate additions against a baseline and retire those without material benefit.

## Validation

```bash
python3 scripts/validate.py
```

This checks structural portability and case coverage; it does **not** demonstrate that a live agent will reliably obey the instructions. Validate behavior in your own runner with the scenarios in `evals/cases.jsonl`.

## Sources for format (not dependencies)

- Agent Skills specification: https://agentskills.io/specification
- OpenAI Agent Skills documentation: https://developers.openai.com/api/docs/guides/tools-skills
- Claude Code agent configurations: https://code.claude.com/docs/en/sub-agents
