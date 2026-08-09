#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from run_behavioral_evals import extract_observation, score_trace, summarize, load_cases


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

    def test_extracts_observation_from_noisy_jsonl_output(self) -> None:
        output = 'starting runner\n{"progress": 1}\n{"selected_route":["execute","verify"],"final_verdict":"PASS"}\n'
        self.assertEqual(extract_observation(output)["final_verdict"], "PASS")

    def test_missing_observation_is_unknown(self) -> None:
        trace = {"expected": {"should_trigger": True, "route_contains": ["verify"],
                              "final_policy": ["PASS"], "max_delegations": 0}, "observation": {}}
        self.assertEqual(score_trace(trace)["overall"], "UNKNOWN")

    def test_scores_observable_route_verdict_and_delegation(self) -> None:
        trace = {"expected": {"should_trigger": True, "route_contains": ["execute", "verify"],
                              "final_policy": ["PASS"], "max_delegations": 1},
                 "observation": {"selected_route": ["execute", "verify"], "final_verdict": "PASS",
                                  "delegation_count": 1}}
        result = score_trace(trace)
        self.assertEqual(result["overall"], "PASS")
        self.assertTrue(all(value == "PASS" for value in result["dimensions"].values()))

    def test_summary_keeps_unknown_separate_from_failure(self) -> None:
        traces = [{"score": {"overall": "PASS", "dimensions": {"activation": "PASS"}}},
                  {"score": {"overall": "UNKNOWN", "dimensions": {"activation": "UNKNOWN"}}}]
        summary = summarize(traces)
        self.assertEqual(summary["pass_rate"], 0.5)
        self.assertEqual(summary["unknown_rate"], 0.5)
        self.assertEqual(summary["dimensions"]["activation"]["UNKNOWN"], 1)


if __name__ == "__main__":
    unittest.main()
