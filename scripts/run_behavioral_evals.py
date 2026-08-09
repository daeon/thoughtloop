#!/usr/bin/env python3
"""Run prompt cases through a configurable agent command and capture traces."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import time
from pathlib import Path
from typing import Any

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


OBSERVATION_KEYS = (
    "triggered", "selected_route", "route", "final_verdict", "delegation_count",
    "artifacts", "authorization", "evidence", "review", "tokens", "cost",
)


def _observation(value: Any) -> dict:
    if not isinstance(value, dict):
        return {}
    return {key: value[key] for key in OBSERVATION_KEYS if key in value}


def extract_observation(stdout: str) -> dict:
    """Extract the last usable observation from JSON, JSONL, or fenced output.

    Hosts are free to print progress, diagnostics, and a final JSON observation.
    The old runner required stdout to be exactly one JSON object, which made a
    valid observation disappear as soon as a host printed one status line.
    """
    candidates = [stdout.strip()]
    candidates.extend(re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", stdout, re.DOTALL))
    candidates.extend(line.strip() for line in stdout.splitlines() if line.strip().startswith("{"))
    for candidate in reversed(candidates):
        try:
            value = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        observation = _observation(value)
        if observation:
            return observation
    return {}


def _route(observation: dict) -> list[str] | None:
    route = observation.get("selected_route", observation.get("route"))
    if isinstance(route, str):
        return [part for part in re.split(r"\s*(?:->|>|,|/)\s*", route) if part]
    if isinstance(route, list) and all(isinstance(item, str) for item in route):
        return route
    return None


def score_trace(trace: dict) -> dict:
    """Score only observable fields; absent fields remain ``UNKNOWN``."""
    expected = trace.get("expected", {})
    observation = trace.get("observation", {})
    route = _route(observation)
    route_set = set(route or [])
    expected_route = expected.get("route_contains", [])
    observed_trigger = observation.get("triggered")
    if not isinstance(observed_trigger, bool):
        observed_trigger = bool(route) if route is not None else None

    dimensions: dict[str, str] = {}
    if observed_trigger is None:
        dimensions["activation"] = "UNKNOWN"
    else:
        dimensions["activation"] = "PASS" if observed_trigger == expected.get("should_trigger") else "FAIL"

    if route is None:
        dimensions["route_compliance"] = "UNKNOWN"
    else:
        dimensions["route_compliance"] = "PASS" if all(stage in route_set for stage in expected_route) else "FAIL"

    verdict = observation.get("final_verdict")
    allowed = expected.get("final_policy", [])
    dimensions["verdict_policy"] = (
        "UNKNOWN" if not isinstance(verdict, str) else
        "PASS" if verdict in allowed else "FAIL"
    )

    delegations = observation.get("delegation_count")
    maximum = expected.get("max_delegations")
    if not isinstance(delegations, int) or isinstance(delegations, bool):
        dimensions["delegation_limit"] = "UNKNOWN"
    else:
        dimensions["delegation_limit"] = "PASS" if delegations <= maximum else "FAIL"

    known = [value for value in dimensions.values() if value != "UNKNOWN"]
    overall = "FAIL" if "FAIL" in known else "UNKNOWN" if len(known) != len(dimensions) else "PASS"
    return {"dimensions": dimensions, "overall": overall}


def run_case(case: dict, runner: list[str], timeout: int, *, condition: str = "current", repetition: int = 1) -> dict:
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
    trace = {
        "id": case["id"],
        "condition": condition,
        "repetition": repetition,
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
    trace["score"] = score_trace(trace)
    return trace


def run_suite(cases: list[dict], runner: list[str], timeout: int, repetitions: int, condition: str) -> list[dict]:
    traces = []
    for repetition in range(1, repetitions + 1):
        for case in cases:
            try:
                traces.append(run_case(case, runner, timeout, condition=condition, repetition=repetition))
            except subprocess.TimeoutExpired as exc:
                trace = {
                    "id": case["id"], "condition": condition, "repetition": repetition,
                    "error": f"timeout after {timeout}s", "stdout": exc.stdout or "", "stderr": exc.stderr or "",
                    "observation": {},
                }
                trace["score"] = {"dimensions": {}, "overall": "UNKNOWN"}
                traces.append(trace)
    return traces


def summarize(traces: list[dict]) -> dict:
    scores = [trace.get("score", {}).get("overall") for trace in traces]
    dimensions = {}
    for trace in traces:
        for name, value in trace.get("score", {}).get("dimensions", {}).items():
            dimensions.setdefault(name, {"PASS": 0, "FAIL": 0, "UNKNOWN": 0})[value] += 1
    return {
        "runs": len(traces),
        "pass_rate": None if not scores else scores.count("PASS") / len(scores),
        "fail_rate": None if not scores else scores.count("FAIL") / len(scores),
        "unknown_rate": None if not scores else scores.count("UNKNOWN") / len(scores),
        "dimensions": dimensions,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--repetitions", type=int, default=1)
    ap.add_argument("--control-runner", nargs="+", help="optional runner for a paired control condition")
    ap.add_argument("--model", help="model identifier recorded in the run metadata")
    ap.add_argument("--reasoning-effort")
    ap.add_argument("--platform")
    ap.add_argument("--baseline", type=Path, help="existing baseline to compare against")
    ap.add_argument("--write-baseline", type=Path, help="write a completed baseline; refuses to overwrite an existing file")
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

    if args.repetitions < 1:
        raise SystemExit("--repetitions must be at least 1")
    traces = run_suite(cases, args.runner, args.timeout, args.repetitions, "current")
    controls = run_suite(cases, args.control_runner, args.timeout, args.repetitions, "control") if args.control_runner else []
    payload = {
        "schema_version": "2",
        "metadata": {"model": args.model, "reasoning_effort": args.reasoning_effort, "platform": args.platform,
                      "commit": os.environ.get("GIT_COMMIT"), "repetitions": args.repetitions},
        "cases": len(cases), "runner": args.runner, "control_runner": args.control_runner,
        "summary": summarize(traces), "control_summary": summarize(controls) if controls else None,
        "traces": traces, "control_traces": controls,
    }
    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        payload["baseline_comparison"] = {"version": baseline.get("version"), "status": baseline.get("status"),
                                           "pass_rate": baseline.get("pass_rate")}
    if args.write_baseline:
        if args.write_baseline.exists():
            raise SystemExit(f"refusing to overwrite existing baseline: {args.write_baseline}")
        args.write_baseline.parent.mkdir(parents=True, exist_ok=True)
        summary = payload["summary"]
        baseline = {"version": "2.1.0", "status": "real_run", "description": "Model-backed ThoughtLoop evaluation baseline.",
                    "model": args.model, "reasoning_effort": args.reasoning_effort, "platform": args.platform,
                    "commit": payload["metadata"]["commit"], "date": time.strftime("%Y-%m-%d"),
                    "repetitions": args.repetitions, "gates": summary["dimensions"],
                    "pass_rate": summary["pass_rate"], "token_use": None, "runtime_seconds": None}
        args.write_baseline.write_text(json.dumps(baseline, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
