#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "core" / "graph.json"
CASES = ROOT / "tests" / "graph_cases.json"


def main() -> int:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    canonical = {item["name"]: item for item in graph["canonical"]}
    assert graph["orchestrator"] == "thoughtloop"
    assert sum(item["implicit"] for item in canonical.values()) == 1
    assert canonical["thoughtloop"]["implicit"] is True

    public = set(canonical)
    actual = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    assert actual == public, f"graph registry mismatch: actual={sorted(actual)}"

    implicit_names = []
    for name, item in canonical.items():
        skill_dir = ROOT / "skills" / name
        assert (skill_dir / "SKILL.md").exists(), f"missing canonical skill: {name}"
        policy = (skill_dir / "agents" / "openai.yaml").read_text(encoding="utf-8")
        is_implicit = bool(re.search(r"allow_implicit_invocation:\s*true\b", policy))
        assert is_implicit == item["implicit"], f"invocation mismatch: {name}"
        if is_implicit:
            implicit_names.append(name)
        for mode in item.get("modes", []):
            assert mode in (skill_dir / "SKILL.md").read_text(encoding="utf-8")

    assert implicit_names == ["thoughtloop"]

    cases = json.loads(CASES.read_text(encoding="utf-8"))
    assert len(cases) >= 9, "fixtures should cover graph, failure, handoff, and evaluation routes"
    ids = set()
    for case in cases:
        assert case["id"] not in ids, f"duplicate graph case: {case['id']}"
        ids.add(case["id"])
        route = case["route"]
        assert route, f"empty route: {case['id']}"
        for step in route:
            assert step.split(":", 1)[0] in canonical, f"unknown node in {case['id']}: {step}"
        kind = case.get("kind", "verdict")
        if kind == "verdict":
            assert "verify" in route and "judge" in route, f"missing proof in {case['id']}"
            assert route.index("verify") < route.index("judge"), f"verification order: {case['id']}"
            if "review" in route:
                assert route.index("judge") < route.index("review"), f"review order: {case['id']}"
        elif kind == "continuity":
            assert "thoughtloop" in route and route[-1] in {"handoff", "evaluate"}, f"continuity route: {case['id']}"
        else:
            raise AssertionError(f"unknown fixture kind: {kind}")

    assert any("discover" in case["route"] for case in cases)
    assert any(step.startswith("investigate:") for case in cases for step in case["route"])
    assert any("revise" in case["route"] for case in cases)
    assert any("handoff" in case["route"] for case in cases)
    assert any("evaluate" in case["route"] for case in cases)
    assert any("standard-english" in case["route"] for case in cases)
    print(f"OK: {len(canonical)} canonical nodes, {len(cases)} graph fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
