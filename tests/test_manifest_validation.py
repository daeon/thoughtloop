#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from validate_pack import validate_manifest


class ManifestValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        manifest_path = ROOT / ".codex-plugin" / "plugin.json"
        cls.manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    def assert_invalid(self, mutate) -> None:
        manifest = copy.deepcopy(self.manifest)
        mutate(manifest)
        with self.assertRaises(AssertionError):
            validate_manifest(manifest)

    def test_current_manifest_is_valid(self) -> None:
        validate_manifest(self.manifest)

    def test_version_accepts_semver_prerelease_and_build_metadata(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["version"] = "2.0.0-rc.1+build.7"
        validate_manifest(manifest)

    def test_rejects_missing_author(self) -> None:
        self.assert_invalid(lambda manifest: manifest.pop("author"))

    def test_rejects_mismatched_developer_name(self) -> None:
        self.assert_invalid(lambda manifest: manifest["interface"].update(developerName="Someone Else"))

    def test_rejects_long_prompt(self) -> None:
        self.assert_invalid(lambda manifest: manifest["interface"].update(defaultPrompt=["x" * 129]))

    def test_rejects_unsupported_category(self) -> None:
        self.assert_invalid(lambda manifest: manifest["interface"].update(category="Unknown"))


if __name__ == "__main__":
    unittest.main()
