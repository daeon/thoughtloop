---
name: handoff
description: Produce a compact continuation record with decisions, evidence, risks, open questions, artifacts, and next actions for another agent or session.
---

# Handoff

Use when work moves to another agent, tool harness, branch, or session. Preserve continuation-critical context without broadening scope or copying the transcript. Prefer paths, URLs, commits, issue IDs, commands, and verification output over long excerpts.

Include:

- purpose and current repo/branch/artifact state;
- decisions and their evidence;
- relevant files and contracts;
- verified and unverified claims;
- open questions, blockers, risks, and rollback notes;
- suggested skills and the next concrete action.

Use the user-specified path; otherwise use a repo-local `.agent-state/handoffs/<short-task-slug>.md` when appropriate. Read an existing target before overwriting. A handoff is a `HandoffRecord`, not durable memory unless the user explicitly asks to save it.
