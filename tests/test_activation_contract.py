#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "activation_cases.jsonl"


class ActivationContractTests(unittest.TestCase):
    def test_description_is_bounded(self) -> None:
        text = (ROOT / "skills" / "thoughtloop" / "SKILL.md").read_text(encoding="utf-8")
        description = next(line for line in text.splitlines() if line.startswith("description:"))
        for phrase in (
            "consequential",
            "material alternatives",
            "Do not invoke",
            "simple explanations",
            "trivial edits",
            "routine commands",
            "more specific skill",
        ):
            self.assertIn(phrase, description)

    def test_positive_and_negative_controls_are_labeled(self) -> None:
        cases = [json.loads(line) for line in CASES.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertGreaterEqual(sum(case["should_trigger"] for case in cases), 3)
        self.assertGreaterEqual(sum(not case["should_trigger"] for case in cases), 4)
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in cases:
            self.assertTrue(case["prompt"])
            self.assertIn(case["should_trigger"], (True, False))
            self.assertTrue(case["reason"])


if __name__ == "__main__":
    unittest.main()
