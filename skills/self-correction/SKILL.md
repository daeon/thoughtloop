---
name: self-correction
description: Deprecated compatibility alias for ThoughtLoop. Use only when explicitly invoked by users or workflows that still call $self-correction. Do not maintain separate logic here; redirect the task to the $thoughtloop orchestrator and follow ThoughtLoop's Discover -> Decide -> Execute -> Prove workflow. New integrations should call $thoughtloop directly.
---

# Self-Correction (Deprecated Alias)

This skill exists only for compatibility with pre-ThoughtLoop releases.

Immediately delegate the user's task to `$thoughtloop` and follow that skill's current instructions. Do not duplicate, fork, or reinterpret the orchestration logic here.

When mentioning the workflow to the user, use the **ThoughtLoop** name.
