#!/usr/bin/env python3
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from calculate_metrics import load_rows


class MetricsValidationTests(unittest.TestCase):
    def test_rejects_semantically_invalid_field_types(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            path = Path(raw_dir) / "invalid.jsonl"
            path.write_text('{"tokens":"5700"}\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "tokens must be an integer"):
                load_rows(path)

    def test_accepts_sample_log(self) -> None:
        rows = load_rows(ROOT / "examples" / "sample-loop-log.jsonl")
        self.assertEqual(len(rows), 3)

    def test_rejects_unknown_verdict(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            path = Path(raw_dir) / "invalid.jsonl"
            path.write_text('{"final_verdict":"MAYBE"}\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "final_verdict must be PASS"):
                load_rows(path)


if __name__ == "__main__":
    unittest.main()
