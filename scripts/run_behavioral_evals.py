#!/usr/bin/env python3
"""Run prompt cases through a configurable agent command and capture traces."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "evals" / "cases.jsonl"


def load_cases(path: Path) -> list[dict]:
    cases = []
    seen = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            case = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"line {line_number}: invalid JSON: {exc}") from exc
        required = {"id", "prompt", "should_trigger", "expected_route_contains", "expected_final_policy", "max_delegations"}
        missing = required - case.keys()
        if missing:
            raise ValueError(f"line {line_number}: missing fields {sorted(missing)}")
        if case["id"] in seen:
            raise ValueError(f"line {line_number}: duplicate case id {case['id']}")
        seen.add(case["id"])
        if not isinstance(case["should_trigger"], bool):
            raise ValueError(f"line {line_number}: should_trigger must be boolean")
        if not isinstance(case["expected_route_contains"], list):
            raise ValueError(f"line {line_number}: expected_route_contains must be a list")
        if not isinstance(case["expected_final_policy"], list) or not case["expected_final_policy"]:
            raise ValueError(f"line {line_number}: expected_final_policy must be a non-empty list")
        if not isinstance(case["max_delegations"], int) or isinstance(case["max_delegations"], bool):
            raise ValueError(f"line {line_number}: max_delegations must be an integer")
        cases.append(case)
    if not 20 <= len(cases) <= 40:
        raise ValueError(f"expected 20 to 40 evaluation cases, found {len(cases)}")
    if not any(case["should_trigger"] for case in cases):
        raise ValueError("evaluation corpus has no positive cases")
    if not any(not case["should_trigger"] for case in cases):
        raise ValueError("evaluation corpus has no negative controls")
    return cases


def extract_observation(stdout: str) -> dict:
    """Extract optional structured observations without requiring a host format."""
    try:
        value = json.loads(stdout)
    except json.JSONDecodeError:
        return {}
    if not isinstance(value, dict):
        return {}
    return {
        key: value[key]
        for key in ("selected_route", "final_verdict", "delegation_count", "artifacts")
        if key in value
    }


def run_case(case: dict, runner: list[str], timeout: int) -> dict:
    started = time.monotonic()
    completed = subprocess.run(
        [*runner, case["prompt"]],
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
        env=os.environ.copy(),
    )
    elapsed = time.monotonic() - started
    stdout = completed.stdout[-20000:]
    stderr = completed.stderr[-20000:]
    return {
        "id": case["id"],
        "prompt": case["prompt"],
        "expected": {
            "should_trigger": case["should_trigger"],
            "route_contains": case["expected_route_contains"],
            "final_policy": case["expected_final_policy"],
            "max_delegations": case["max_delegations"],
        },
        "returncode": completed.returncode,
        "elapsed_seconds": round(elapsed, 3),
        "observation": extract_observation(stdout),
        "stdout": stdout,
        "stderr": stderr,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--validate-only", action="store_true")
    ap.add_argument(
        "--runner",
        nargs="+",
        default=["codex", "exec"],
        help="agent command; the case prompt is appended as the final argument",
    )
    args = ap.parse_args()

    try:
        cases = load_cases(args.cases)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if args.validate_only:
        print(f"Validated {len(cases)} behavioral evaluation cases")
        return 0

    traces = []
    for case in cases:
        try:
            traces.append(run_case(case, args.runner, args.timeout))
        except subprocess.TimeoutExpired as exc:
            traces.append({"id": case["id"], "error": f"timeout after {args.timeout}s", "stdout": exc.stdout or "", "stderr": exc.stderr or ""})
    payload = {"cases": len(cases), "runner": args.runner, "traces": traces}
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
