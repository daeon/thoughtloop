#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProofContractTests(unittest.TestCase):
    def read(self, path: str) -> str:
        return (ROOT / path).read_text(encoding="utf-8")

    def test_orchestrator_has_fallbacks_for_every_internal_stage(self) -> None:
        text = self.read("skills/thoughtloop/SKILL.md")
        for stage in ("Discover", "Decide", "Execute", "Verify", "Review", "Final judgment", "Correct"):
            self.assertIn(f"**{stage}:**", text)
        self.assertIn("Specialist instructions add depth; they are", text)
        self.assertIn("not runtime dependencies", text)

    def test_review_is_evidence_for_final_judgment(self) -> None:
        orchestrator = self.read("skills/thoughtloop/SKILL.md")
        review = self.read("skills/review/SKILL.md")
        contracts = self.read("skills/thoughtloop/references/contracts.md")
        self.assertIn("ReviewReport", review)
        self.assertIn("final-judgment", review)
        self.assertIn("ReviewReport", contracts)
        self.assertIn("FinalOutcome", contracts)
        self.assertIn("unresolved blocking review finding", orchestrator)

    def test_route_fixtures_consume_review_before_final_judgment(self) -> None:
        cases = json.loads((ROOT / "tests/graph_cases.json").read_text(encoding="utf-8"))
        for case in cases:
            route = case["route"]
            if "review" in route:
                self.assertLess(route.index("review"), route.index("final-judgment"), case["id"])
            if case.get("kind", "verdict") == "verdict":
                self.assertEqual(route[-1], "final-judgment", case["id"])

    def test_runtime_does_not_advertise_pseudo_cli_flags(self) -> None:
        for path in (ROOT / "skills" / "thoughtloop", ROOT / "README.md"):
            files = [path] if path.is_file() else list(path.rglob("*.md"))
            for file in files:
                self.assertNotIn("--subagents", file.read_text(encoding="utf-8"), file)
                self.assertNotIn("fork_context=false", file.read_text(encoding="utf-8"), file)


if __name__ == "__main__":
    unittest.main()
