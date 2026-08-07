---
name: self-correction
description: Deprecated compatibility alias for ThoughtLoop. Use only when explicitly invoked by older users or workflows. Redirect to ThoughtLoop rather than maintaining a second workflow.
---

# Self-Correction (Deprecated Alias)

Immediately redirect the request to `$thoughtloop` and follow its current guidance, including optional subagent mode. Do not duplicate, fork, or reinterpret the orchestration logic. New integrations should call `$thoughtloop` directly.
