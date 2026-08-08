#!/usr/bin/env python3
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / "scripts" / "install_local.py"
UNINSTALL = ROOT / "scripts" / "uninstall_local.py"
EXPECTED_SKILLS = {
    "thoughtloop",
    "gapfinder",
    "discover",
    "investigate",
    "decide",
    "verify",
    "review",
    "handoff",
}
REQUIRED_REFERENCES = {
    "contracts.md",
    "routing.md",
    "budget-policy.md",
    "evidence-ladder.md",
    "execution.md",
    "correction.md",
    "routes/direct.md",
    "routes/deliberate.md",
    "routes/investigation.md",
    "routes/deep.md",
}


class LocalInstallTests(unittest.TestCase):
    def run_script(self, script: Path, home: Path, *args: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["HOME"] = str(home)
        return subprocess.run(
            [sys.executable, str(script), *args],
            cwd=ROOT,
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_copy_install_is_self_contained_and_uninstall_is_scoped(self) -> None:
        with tempfile.TemporaryDirectory() as raw_home:
            home = Path(raw_home)
            result = self.run_script(INSTALL, home, "--copy")
            self.assertEqual(result.returncode, 0, result.stderr)

            installed_root = home / ".agents" / "skills"
            installed = {path.name for path in installed_root.iterdir()}
            self.assertEqual(installed, EXPECTED_SKILLS)

            orchestrator = installed_root / "thoughtloop"
            references = {
                path.relative_to(orchestrator / "references").as_posix()
                for path in (orchestrator / "references").rglob("*")
                if path.is_file()
            }
            self.assertTrue(REQUIRED_REFERENCES <= references)

            for path in orchestrator.rglob("*"):
                if not path.is_file():
                    continue
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("core/", text, path)
                self.assertNotIn("graphs/", text, path)

            unrelated = installed_root / "unrelated"
            unrelated.mkdir()
            (unrelated / "keep.txt").write_text("keep", encoding="utf-8")
            result = self.run_script(UNINSTALL, home)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((unrelated / "keep.txt").exists())
            self.assertEqual({path.name for path in installed_root.iterdir()}, {"unrelated"})

    def test_symlink_install_is_reversible(self) -> None:
        with tempfile.TemporaryDirectory() as raw_home:
            home = Path(raw_home)
            result = self.run_script(INSTALL, home)
            self.assertEqual(result.returncode, 0, result.stderr)
            installed_root = home / ".agents" / "skills"
            self.assertTrue(all(path.is_symlink() for path in installed_root.iterdir()))

            result = self.run_script(UNINSTALL, home)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(any(installed_root.iterdir()))

    def test_orchestrator_can_be_copied_without_repository_files(self) -> None:
        with tempfile.TemporaryDirectory() as raw_target:
            target = Path(raw_target) / "thoughtloop"
            shutil.copytree(ROOT / "skills" / "thoughtloop", target)
            for reference in REQUIRED_REFERENCES:
                self.assertTrue((target / "references" / reference).exists(), reference)
            for path in target.rglob("*"):
                if path.is_file():
                    text = path.read_text(encoding="utf-8")
                    self.assertNotIn("../", text, path)
                    self.assertNotIn("core/", text, path)
                    self.assertNotIn("graphs/", text, path)


if __name__ == "__main__":
    unittest.main()
