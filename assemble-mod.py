"""Regenerate the historical distribution filenames from the ILô dock source."""
from pathlib import Path

root = Path(__file__).resolve().parent
source = (root / "ilo.wh.cpp").read_bytes()
for filename in ("assembled-mod.cpp", "taskbar-dock-like.wh.cpp"):
    (root / filename).write_bytes(source)
