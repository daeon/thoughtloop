#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

CANONICAL_SKILLS = {
    "thoughtloop",
    "gapfinder",
    "discover",
    "investigate",
    "decide",
    "builder",
    "verify",
    "judge",
    "review",
    "revise",
    "handoff",
    "evaluate",
    "standard-english",
}
EXPECTED_SKILLS = CANONICAL_SKILLS


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"{path}: frontmatter must start at byte 0")
    try:
        _, fm, _ = text.split("---", 2)
    except ValueError:
        raise AssertionError(f"{path}: malformed frontmatter")
    out = {}
    for raw in fm.strip().splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise AssertionError(f"{path}: unsupported frontmatter line: {raw!r}")
        key, value = raw.split(":", 1)
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def main() -> int:
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert NAME_RE.fullmatch(manifest["name"]), "plugin name must be kebab-case"
    assert manifest.get("skills") == "./skills/", "manifest skills path should be ./skills/"
    assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "version must be semver-like"
    assert manifest["version"] == "1.0.0", "expected v1.0.0 cohesive graph release"

    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    assert len(skill_dirs) == len(EXPECTED_SKILLS), (
        f"expected {len(EXPECTED_SKILLS)} skills, found {len(skill_dirs)}"
    )

    names = set()
    for d in skill_dirs:
        skill = d / "SKILL.md"
        assert skill.exists(), f"missing {skill}"
        fm = parse_frontmatter(skill)
        name = fm.get("name", "")
        desc = fm.get("description", "")
        assert name == d.name, f"{skill}: name must match directory"
        assert NAME_RE.fullmatch(name), f"{skill}: invalid name"
        assert len(name) <= 64, f"{skill}: name exceeds 64 chars"
        assert desc, f"{skill}: missing description"
        assert len(desc) <= 1024, f"{skill}: description exceeds 1024 chars"
        assert name not in names, f"duplicate skill name: {name}"
        names.add(name)

        openai_yaml = d / "agents" / "openai.yaml"
        assert openai_yaml.exists(), f"missing {openai_yaml}"
        y = openai_yaml.read_text(encoding="utf-8")
        assert "allow_implicit_invocation:" in y, f"{openai_yaml}: missing invocation policy"

    assert names == EXPECTED_SKILLS, f"unexpected skill set: {sorted(names)}"

    for d in skill_dirs:
        y = (d / "agents" / "openai.yaml").read_text(encoding="utf-8")
        is_true = bool(re.search(r"allow_implicit_invocation:\s*true\b", y))
        assert is_true == (d.name == "thoughtloop"), (
            f"{d.name}: implicit invocation should be true only for thoughtloop"
        )

    required_files = [
        ROOT / "core/contracts.md",
        ROOT / "core/graph.json",
        ROOT / "core/routing.md",
        ROOT / "core/budget-policy.md",
        ROOT / "graphs/default.md",
        ROOT / "graphs/engineering.md",
        ROOT / "graphs/debugging.md",
        ROOT / "graphs/writing.md",
        ROOT / "tests/graph_cases.json",
        ROOT / "tests/validate_graph.py",
        ROOT / "skills/thoughtloop/references/routing.md",
        ROOT / "skills/thoughtloop/references/evidence-ladder.md",
        ROOT / "skills/thoughtloop/references/state-contract.md",
        ROOT / "skills/thoughtloop/references/solution-space-search.md",
        ROOT / "skills/thoughtloop/references/failure-depth.md",
        ROOT / "skills/evaluate/scripts/calculate_metrics.py",
    ]
    for path in required_files:
        assert path.exists(), f"missing {path}"

    orchestrator = (ROOT / "skills/thoughtloop/SKILL.md").read_text(encoding="utf-8")
    for phrase in [
        "DISCOVER -> DECIDE -> EXECUTE -> PROVE",
        "$gapfinder",
        "$discover",
        "$investigate",
        "$decide",
        "$verify",
        "$judge",
        "$review",
        "$revise",
        "--subagents",
        "budget=balanced",
        "delegation.mode=subagents",
        "fork_context=false",
        "light",
        "deep",
        "fresh context",
        "lower-cost",
    ]:
        assert phrase in orchestrator, f"orchestrator missing required architecture token: {phrase}"

    canonical_text = {
        name: (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
        for name in CANONICAL_SKILLS
    }
    for name, text in canonical_text.items():
        assert f"name: {name}" in text, f"canonical node missing frontmatter: {name}"

    for action in ("`BUILD`", "`EXPERIMENT`", "`EXPLORE`"):
        assert action in canonical_text["decide"], f"decision contract missing: {action}"
    for phrase in ("UNKNOWN",):
        assert phrase in canonical_text["verify"], f"verification contract missing: {phrase}"
        assert phrase in canonical_text["judge"], f"judgment contract missing: {phrase}"
    assert "PASS" in canonical_text["judge"] and "FAIL" in canonical_text["judge"]
    assert "No external profile required" in canonical_text["standard-english"]

    assert manifest["name"] == "thoughtloop", "plugin must remain branded thoughtloop"
    assert manifest.get("interface", {}).get("displayName") == "ThoughtLoop", "displayName must be ThoughtLoop"
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Think wider. Build better. Prove it." in readme, "tagline missing"
    assert "Subagent mode" in readme and "--subagents" in readme, "subagent mode documentation missing"
    for section in (
        "Table of contents",
        "Why ThoughtLoop",
        "Canonical graph",
        "Quick start",
        "Install",
        "Validate",
        "Roadmap",
        "Contributing",
        "Security",
    ):
        assert section in readme, f"README section missing: {section}"
    for document in ("CONTRIBUTING.md", "SECURITY.md"):
        assert (ROOT / document).exists(), f"missing repository document: {document}"
    assert not (ROOT / "marketplace.example.json").exists(), "duplicate marketplace metadata should not be present"
    assert not (ROOT / "DEPLOY_TO_GITHUB.md").exists(), "obsolete deployment guide should not be present"
    for removed in (
        "self-correction",
        "explorer",
        "challenger",
        "prototype-probe",
        "codebase-analysis",
        "debugging-forensics",
        "log-forensics",
        "performance-forensics",
        "synthesizer",
        "risk-first-plan",
        "ground-truth-verifier",
        "adversarial-review",
        "revision-manager",
        "loop-evaluator",
        "engineering-team",
    ):
        assert not (ROOT / "skills" / removed).exists(), f"removed compatibility path must not be present: {removed}"
    for path in ROOT.rglob("*"):
        if path.is_file() and path != Path(__file__) and ".git" not in path.parts:
            text = path.read_text(encoding="utf-8", errors="replace")
            assert "self-correction" not in text, f"stale self-correction reference in {path}"

    print(
        f"OK: {manifest['name']} {manifest['version']} with "
        f"{len(CANONICAL_SKILLS)} canonical nodes"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise SystemExit(1)
