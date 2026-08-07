#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_SKILLS = {
    "thoughtloop",
    "self-correction",
    "explorer",
    "challenger",
    "synthesizer",
    "builder",
    "ground-truth-verifier",
    "judge",
    "revision-manager",
    "adversarial-review",
    "loop-evaluator",
}


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
    assert manifest["version"] == "0.4.0", "expected v0.4.0 ThoughtLoop release"

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

    # Only the master orchestrator should route implicitly.
    for d in skill_dirs:
        y = (d / "agents" / "openai.yaml").read_text(encoding="utf-8")
        is_true = bool(re.search(r"allow_implicit_invocation:\s*true\b", y))
        assert is_true == (d.name == "thoughtloop"), (
            f"{d.name}: implicit invocation should be true only for thoughtloop"
        )

    required_refs = [
        ROOT / "skills/thoughtloop/references/routing.md",
        ROOT / "skills/thoughtloop/references/evidence-ladder.md",
        ROOT / "skills/thoughtloop/references/state-contract.md",
        ROOT / "skills/thoughtloop/references/solution-space-search.md",
        ROOT / "skills/thoughtloop/references/failure-depth.md",
        ROOT / "skills/loop-evaluator/scripts/calculate_metrics.py",
    ]
    for p in required_refs:
        assert p.exists(), f"missing {p}"

    orchestrator = (ROOT / "skills/thoughtloop/SKILL.md").read_text(encoding="utf-8")
    for reference in [
        "references/routing.md",
        "references/solution-space-search.md",
        "references/evidence-ladder.md",
        "references/failure-depth.md",
        "references/state-contract.md",
    ]:
        assert reference in orchestrator, f"orchestrator does not link reference: {reference}"
    for phrase in [
        "DISCOVER -> DECIDE -> EXECUTE -> PROVE",
        "IMPLEMENTATION",
        "STRATEGY",
        "ASSUMPTION_OR_FRAME",
        "EVIDENCE_GAP",
        "$explorer",
        "$challenger",
        "$synthesizer",
        "--subagents",
        "budget=balanced",
        "delegation.mode=subagents",
        "fork_context=false",
        "`light`",
        "`deep`",
        "fresh context",
        "lower-cost",
    ]:
        assert phrase in orchestrator, f"orchestrator missing required architecture token: {phrase}"

    explorer = (ROOT / "skills/explorer/SKILL.md").read_text(encoding="utf-8")
    assert "Do not rank or select the winner" in explorer, "Explorer must not prematurely select"
    synthesizer = (ROOT / "skills/synthesizer/SKILL.md").read_text(encoding="utf-8")
    for action in ("`BUILD`", "`EXPERIMENT`", "`EXPLORE`"):
        assert action in synthesizer, f"Synthesizer routing contract missing: {action}"
    challenger = (ROOT / "skills/challenger/SKILL.md").read_text(encoding="utf-8")
    assert "$adversarial-review" in challenger, "Challenger/Adversarial distinction missing"

    assert manifest["name"] == "thoughtloop", "plugin must be branded thoughtloop"
    assert manifest.get("interface", {}).get("displayName") == "ThoughtLoop", "displayName must be ThoughtLoop"
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Think wider. Build better. Prove it." in readme, "tagline missing"
    assert "Subagent mode" in readme and "--subagents" in readme, "subagent mode documentation missing"
    for section in (
        "Table of contents",
        "Why ThoughtLoop",
        "How it works",
        "Quick start",
        "Install",
        "Validate",
        "Compatibility",
        "Roadmap",
        "Contributing",
        "Security",
    ):
        assert section in readme, f"README section missing: {section}"
    for document in ("CONTRIBUTING.md", "SECURITY.md"):
        assert (ROOT / document).exists(), f"missing repository document: {document}"
    assert not (ROOT / "marketplace.example.json").exists(), "duplicate marketplace metadata should not be present"
    assert not (ROOT / "DEPLOY_TO_GITHUB.md").exists(), "obsolete deployment guide should not be present"
    alias = (ROOT / "skills/self-correction/SKILL.md").read_text(encoding="utf-8")
    assert "$thoughtloop" in alias and "Deprecated" in alias, "compatibility alias must redirect to ThoughtLoop"

    print(f"OK: {manifest['name']} {manifest['version']} with {len(skill_dirs)} valid skills")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise SystemExit(1)
