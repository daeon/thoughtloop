---
name: gapfinder
description: Find expensive unknowns early and route non-trivial work through the smallest useful discovery, question, prototype, planning, or implementation pattern.
---

# Gapfinder

Use this as a compact decision-quality layer around non-trivial work. Expose assumptions that become expensive when discovered late, then keep momentum with a conservative reversible default.

Choose only the phase the task needs:

1. **Unknowns pass:** inspect the territory, assumptions, falsifiers, and cheapest useful probes.
2. **High-impact question:** ask only if the answer could change architecture, interfaces, lifecycle, behavior, tests, rollback, security, or production risk.
3. **Concrete options:** route to `$discover --mode=prototype` when an observable prototype is cheaper than abstract debate.
4. **Risk-first plan:** route to `$decide --mode=plan` when the implementation needs a reviewable brief.

Do not run every phase mechanically. Return a `DiscoveryBrief` containing what is known, important unknowns, hidden assumptions, failure modes, falsifiers, cheap discovery actions, and the recommended next node. Unknowns are not permission to invent requirements.

In a graph, Gapfinder routes. It does not own implementation, verification, or final decisions. Independently, it returns the same brief without invoking a second orchestrator.
