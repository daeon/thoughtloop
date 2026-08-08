#!/usr/bin/env python3
"""Calculate baseline ThoughtLoop metrics from JSONL logs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

BOOL_FIELDS = {
    "exploration_used",
    "experiment_before_commit",
    "approach_switched",
    "approach_switch_success",
    "first_pass",
    "success",
    "escalated",
    "repeated_failure",
}
INT_FIELDS = {
    "approach_count",
    "near_duplicate_ideas",
    "strategic_backtracks",
    "assumption_backtracks",
    "revisions",
    "blocking_failures_resolved",
    "regressions_introduced",
    "tokens",
}
NUMBER_FIELDS = {"cost", "runtime_seconds"}
VERDICTS = {"PASS", "FAIL", "UNKNOWN"}


def rate(num: int, den: int):
    return None if den == 0 else num / den


def validate_row(row: object, line_number: int) -> dict:
    if not isinstance(row, dict):
        raise ValueError(f"line {line_number}: expected a JSON object")

    for field in BOOL_FIELDS:
        if field in row and not isinstance(row[field], bool):
            raise ValueError(f"line {line_number}: {field} must be boolean")
    for field in INT_FIELDS:
        if field in row and (not isinstance(row[field], int) or isinstance(row[field], bool)):
            raise ValueError(f"line {line_number}: {field} must be an integer")
    for field in NUMBER_FIELDS:
        if field in row and (not isinstance(row[field], (int, float)) or isinstance(row[field], bool)):
            raise ValueError(f"line {line_number}: {field} must be numeric")
    if "final_verdict" in row and row["final_verdict"] not in VERDICTS:
        raise ValueError(f"line {line_number}: final_verdict must be PASS, FAIL, or UNKNOWN")
    if "ground_truth_good" in row and row["ground_truth_good"] is not None and not isinstance(row["ground_truth_good"], bool):
        raise ValueError(f"line {line_number}: ground_truth_good must be boolean or null")
    return row


def load_rows(path: Path) -> list[dict]:
    rows = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            raw = json.loads(line)
        except json.JSONDecodeError as e:
            raise ValueError(f"line {i}: invalid JSON: {e}") from e
        rows.append(validate_row(raw, i))
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", type=Path)
    args = ap.parse_args()

    try:
        rows = load_rows(args.jsonl)
    except ValueError as e:
        raise SystemExit(str(e)) from e

    n = len(rows)
    successes = [r for r in rows if r.get("success") is True]
    explored = [r for r in rows if r.get("exploration_used") is True]
    switched = [r for r in rows if r.get("approach_switched") is True]
    labeled = [r for r in rows if isinstance(r.get("ground_truth_good"), bool)]

    false_pass = sum(
        r.get("final_verdict") == "PASS" and r.get("ground_truth_good") is False
        for r in labeled
    )
    false_fail = sum(
        r.get("final_verdict") == "FAIL" and r.get("ground_truth_good") is True
        for r in labeled
    )
    gt_bad = sum(r.get("ground_truth_good") is False for r in labeled)
    gt_good = sum(r.get("ground_truth_good") is True for r in labeled)

    total_approaches = sum(int(r.get("approach_count", 0) or 0) for r in explored)
    total_duplicates = sum(int(r.get("near_duplicate_ideas", 0) or 0) for r in explored)
    total_resolved = sum(int(r.get("blocking_failures_resolved", 0) or 0) for r in rows)
    total_regressions = sum(int(r.get("regressions_introduced", 0) or 0) for r in rows)

    metrics = {
        "runs": n,
        "exploration_used_rate": rate(len(explored), n),
        "average_approach_count_when_explored": None if not explored else total_approaches / len(explored),
        "near_duplicate_idea_rate": rate(total_duplicates, total_approaches),
        "experiment_before_commit_rate": rate(sum(r.get("experiment_before_commit") is True for r in explored), len(explored)),
        "strategic_backtrack_rate": rate(sum(int(r.get("strategic_backtracks", 0) or 0) > 0 for r in rows), n),
        "assumption_backtrack_rate": rate(sum(int(r.get("assumption_backtracks", 0) or 0) > 0 for r in rows), n),
        "approach_switch_success_rate": rate(sum(r.get("approach_switch_success") is True for r in switched), len(switched)),
        "first_pass_success_rate": rate(sum(r.get("first_pass") is True for r in rows), n),
        "success_rate": rate(len(successes), n),
        "average_revisions_to_success": None if not successes else sum(int(r.get("revisions", 0) or 0) for r in successes) / len(successes),
        "escalation_rate": rate(sum(r.get("escalated") is True for r in rows), n),
        "unknown_rate": rate(sum(r.get("final_verdict") == "UNKNOWN" for r in rows), n),
        "false_pass_rate_on_bad_labeled_cases": rate(false_pass, gt_bad),
        "false_fail_rate_on_good_labeled_cases": rate(false_fail, gt_good),
        "blocking_failures_resolved": total_resolved,
        "regressions_introduced": total_regressions,
        "resolution_to_regression_ratio": None if total_regressions == 0 else total_resolved / total_regressions,
        "repeated_failure_rate": rate(sum(r.get("repeated_failure") is True for r in rows), n),
        "total_cost": sum(float(r.get("cost", 0) or 0) for r in rows),
        "total_tokens": sum(int(r.get("tokens", 0) or 0) for r in rows),
        "total_runtime_seconds": sum(float(r.get("runtime_seconds", 0) or 0) for r in rows),
    }
    print(json.dumps(metrics, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
