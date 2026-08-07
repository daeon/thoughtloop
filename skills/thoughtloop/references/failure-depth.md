# Failure-depth routing

The correction system should fix the level that is actually wrong.

## IMPLEMENTATION

Evidence: local bug, missing case, syntax/type issue, requirement omitted while strategy remains valid.

Action: minimal revision, preserve passing invariants, rerun affected checks.

## STRATEGY

Evidence: repeated local fixes do not solve the problem; architecture conflicts with a criterion; complexity/performance profile makes success uneconomic; a rejected approach is now favored by new evidence.

Action: return to Synthesizer. Reuse the prior portfolio and new evidence. Do not rediscover everything from scratch unless assumptions changed.

## ASSUMPTION_OR_FRAME

Evidence: a premise was falsified; the symptom is downstream of another issue; a supposed hard constraint is actually inherited; the problem boundary prevents a good solution.

Action: Challenger and/or Explorer, then Synthesizer. Record which premise changed so the next search differs from the previous one.

## EVIDENCE_GAP

Evidence: Judge returns UNKNOWN because a necessary observation/source/test is absent.

Action: acquire evidence or run a discriminating experiment. Do not mutate the artifact solely to force a pass.

## CONTRADICTION_OR_LIMIT

Evidence: requirements cannot simultaneously hold; needed permissions/data/tools are unavailable; maximum budgets are reached with no defensible path.

Action: escalate or deliver the unresolved state with concrete blockers.

## Anti-oscillation rule

Track strategic backtracks. Do not alternate indefinitely between the same approaches. A previously rejected approach should be reconsidered only when new evidence, constraints, or assumptions materially change the decision.
