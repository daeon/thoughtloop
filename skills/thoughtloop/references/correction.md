# Correction reference

Classify evidence-backed failures before changing the artifact:

- `IMPLEMENTATION`: return to Execute;
- `STRATEGY`: return to Decide;
- `ASSUMPTION_OR_FRAME`: return to Discover or Investigate;
- `EVIDENCE_GAP`: return to Verify or Investigate;
- `CONTRADICTION_OR_LIMIT`: explain the blocker or escalate.

Protect passing criteria and state the regression checks. Do not repeat a local
patch without new evidence. Two failed local corrections against the same
blocker are a signal to backtrack.
