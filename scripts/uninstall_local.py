#!/usr/bin/env python3
"""Remove this pack's skills from ~/.agents/skills."""
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
DEST = Path.home() / ".agents" / "skills"


def main() -> int:
    for src in sorted(p for p in SOURCE.iterdir() if p.is_dir() and (p / "SKILL.md").exists()):
        dst = DEST / src.name
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
            print(f"REMOVE {dst}")
        elif dst.is_dir():
            shutil.rmtree(dst)
            print(f"REMOVE {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
