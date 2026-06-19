#!/usr/bin/env python3
"""Scan vanilla_palette_*.nbt files and maintain palettes.json manifest."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "palettes.json"

NETEASE_RE = re.compile(r"^vanilla_palette_netease_(\d+)\.nbt$")
VANILLA_RE = re.compile(r"^vanilla_palette_(\d+)\.nbt$")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    entries = []
    for path in sorted(ROOT.glob("vanilla_palette_*.nbt")):
        name = path.name
        m = NETEASE_RE.match(name)
        if m:
            protocol, netease = int(m.group(1)), True
        else:
            m = VANILLA_RE.match(name)
            if not m:
                continue
            protocol, netease = int(m.group(1)), False
        entries.append(
            {
                "file": name,
                "protocol": protocol,
                "netease": netease,
                "size": path.stat().st_size,
                "sha256": sha256(path),
            }
        )

    entries.sort(key=lambda e: (e["netease"], e["protocol"]))

    data = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(entries),
        "palettes": entries,
    }

    OUT.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote {OUT.relative_to(ROOT)} with {len(entries)} entries")


if __name__ == "__main__":
    main()
