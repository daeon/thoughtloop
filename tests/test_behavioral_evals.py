#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from run_behavioral_evals import load_cases


class BehavioralEvalTests(unittest.TestCase):
    def test_corpus_has_expected_shape(self) -> None:
        cases = load_cases(ROOT / "evals" / "cases.jsonl")
        self.assertGreaterEqual(len(cases), 20)
        self.assertTrue(any(case["should_trigger"] for case in cases))
        self.assertTrue(any(not case["should_trigger"] for case in cases))

    def test_baseline_is_explicitly_pending_until_run(self) -> None:
        baseline = json.loads((ROOT / "evals" / "baselines" / "2.0.0.json").read_text(encoding="utf-8"))
        self.assertEqual(baseline["version"], "2.0.0")
        self.assertEqual(baseline["status"], "pending_real_run")
        for key in ("model", "platform", "commit", "pass_rate", "token_use", "runtime_seconds"):
            self.assertIn(key, baseline)


if __name__ == "__main__":
    unittest.main()
