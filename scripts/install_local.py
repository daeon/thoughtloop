#!/usr/bin/env python3
"""Install this pack's skills into the current user's Codex skill directory.

Default behavior creates symlinks in ~/.agents/skills so edits to this checkout
are picked up immediately. Use --copy if you prefer independent copies.
"""
from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
DEST = Path.home() / ".agents" / "skills"


def remove_target(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--copy", action="store_true", help="copy skills instead of symlinking")
    ap.add_argument("--force", action="store_true", help="replace existing skill paths")
    args = ap.parse_args()

    DEST.mkdir(parents=True, exist_ok=True)
    skills = sorted(p for p in SOURCE.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    for src in skills:
        dst = DEST / src.name
        if dst.exists() or dst.is_symlink():
            if not args.force:
                print(f"SKIP {dst} (already exists; use --force to replace)")
                continue
            remove_target(dst)

        if args.copy:
            shutil.copytree(src, dst)
            print(f"COPY {src.name} -> {dst}")
        else:
            try:
                dst.symlink_to(src, target_is_directory=True)
                print(f"LINK {src.name} -> {dst}")
            except OSError as exc:
                print(f"WARN symlink failed for {src.name}: {exc}; copying instead")
                shutil.copytree(src, dst)
                print(f"COPY {src.name} -> {dst}")

    print("Done. Codex detects skill changes automatically; restart if the skills do not appear.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
