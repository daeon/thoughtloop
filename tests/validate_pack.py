#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)

ALLOWED_CATEGORIES = {
    "Art & Design",
    "Business",
    "Communication",
    "Developer Tools",
    "Education",
    "Entertainment",
    "Finance",
    "Health & Fitness",
    "Lifestyle",
    "Marketing",
    "News",
    "Productivity",
    "Research",
    "Shopping",
    "Social",
    "Travel",
    "Utilities",
}

CANONICAL_SKILLS = {
    "thoughtloop",
    "gapfinder",
    "discover",
    "investigate",
    "decide",
    "verify",
    "review",
    "handoff",
}
EXPECTED_SKILLS = CANONICAL_SKILLS


def validate_manifest(manifest: dict) -> None:
    assert NAME_RE.fullmatch(manifest["name"]), "plugin name must be kebab-case"
    assert manifest.get("skills") == "./skills/", "manifest skills path should be ./skills/"
    assert SEMVER_RE.fullmatch(manifest["version"]), "version must follow semantic versioning"

    author = manifest.get("author")
    assert isinstance(author, dict), "manifest author must be an object"
    author_name = author.get("name", "")
    assert isinstance(author_name, str) and author_name.strip(), "author.name must be non-empty"

    interface = manifest.get("interface")
    assert isinstance(interface, dict), "manifest interface must be an object"
    display_name = interface.get("displayName", "")
    assert isinstance(display_name, str) and display_name.strip(), "displayName must be non-empty"
    assert len(display_name) <= 30, "displayName exceeds 30 characters"

    short_description = interface.get("shortDescription", "")
    assert isinstance(short_description, str) and short_description.strip(), (
        "shortDescription must be non-empty"
    )
    assert len(short_description) <= 30, "shortDescription exceeds 30 characters"

    developer_name = interface.get("developerName", "")
    assert isinstance(developer_name, str) and developer_name.strip(), (
        "developerName must be non-empty"
    )
    assert developer_name == author_name, "developerName must match author.name"

    category = interface.get("category")
    assert category in ALLOWED_CATEGORIES, f"unsupported plugin category: {category!r}"

    prompts = interface.get("defaultPrompt")
    assert isinstance(prompts, list), "defaultPrompt must be an array"
    assert 1 <= len(prompts) <= 3, "defaultPrompt must contain one to three prompts"
    assert len(set(prompts)) == len(prompts), "defaultPrompt entries must be unique"
    for prompt in prompts:
        assert isinstance(prompt, str) and prompt.strip(), "defaultPrompt entries must be non-empty"
        assert "\n" not in prompt and "\r" not in prompt, "defaultPrompt entries must be single-line"
        assert len(prompt) <= 128, "defaultPrompt entry exceeds 128 characters"


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
    validate_manifest(manifest)

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
        ROOT / "tests/graph_cases.json",
        ROOT / "tests/validate_graph.py",
        ROOT / "evals/activation_cases.jsonl",
        ROOT / "evals/cases.jsonl",
        ROOT / "evals/baselines/2.0.0.json",
        ROOT / "scripts/calculate_metrics.py",
        ROOT / "scripts/run_behavioral_evals.py",
        ROOT / "skills/thoughtloop/references/contracts.md",
        ROOT / "skills/thoughtloop/references/routing.md",
        ROOT / "skills/thoughtloop/references/budget-policy.md",
        ROOT / "skills/thoughtloop/references/evidence-ladder.md",
        ROOT / "skills/thoughtloop/references/execution.md",
        ROOT / "skills/thoughtloop/references/correction.md",
        ROOT / "skills/thoughtloop/references/routes/direct.md",
        ROOT / "skills/thoughtloop/references/routes/deliberate.md",
        ROOT / "skills/thoughtloop/references/routes/investigation.md",
        ROOT / "skills/thoughtloop/references/routes/deep.md",
    ]
    for path in required_files:
        assert path.exists(), f"missing {path}"

    orchestrator = (ROOT / "skills/thoughtloop/SKILL.md").read_text(encoding="utf-8")
    orchestrator_description = parse_frontmatter(ROOT / "skills/thoughtloop/SKILL.md")["description"]
    for phrase in (
        "consequential",
        "material alternatives",
        "Do not invoke",
        "simple explanations",
        "trivial edits",
        "routine commands",
        "more specific skill",
    ):
        assert phrase in orchestrator_description, f"activation boundary missing: {phrase}"
    for phrase in [
        "DISCOVER -> DECIDE -> EXECUTE -> PROVE",
        "$gapfinder",
        "$discover",
        "$investigate",
        "$decide",
        "$verify",
        "$review",
        "$handoff",
        "execute",
        "final-judgment",
        "correct",
        "references/contracts.md",
        "references/budget-policy.md",
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
    assert "UNKNOWN" in canonical_text["verify"], "verification contract missing: UNKNOWN"
    assert "ReviewReport" in canonical_text["review"], "review contract missing: ReviewReport"

    assert manifest["name"] == "thoughtloop", "plugin must remain branded thoughtloop"
    assert manifest.get("interface", {}).get("displayName") == "ThoughtLoop", "displayName must be ThoughtLoop"
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Think wider. Build better. Prove it." in readme, "tagline missing"
    assert "Subagent mode" in readme and "bounded" in readme, "subagent mode documentation missing"
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
    for removed in ("builder", "judge", "revise", "evaluate", "standard-english"):
        assert not (ROOT / "skills" / removed).exists(), f"internalized skill path remains: {removed}"
    for path in (ROOT / "README.md", ROOT / "skills" / "thoughtloop" / "SKILL.md"):
        text = path.read_text(encoding="utf-8")
        for removed in ("$builder", "$judge", "$revise", "$evaluate", "$standard-english"):
            assert removed not in text, f"stale public skill reference in {path}: {removed}"

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
