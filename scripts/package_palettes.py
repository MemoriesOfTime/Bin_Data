#!/usr/bin/env python3
"""Package all vanilla_palette_*.nbt files into palettes.zip and record zip
metadata (file / size / sha256 / file_count) into the top-level `zip` field of
palettes.json so the manifest covers both nbt files and the bundle.
"""
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_ZIP = ROOT / "palettes.zip"
PALETTES_JSON = ROOT / "palettes.json"

MANIFEST_KEY_ORDER = ("generated_at", "count", "zip", "palettes")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    files = sorted(ROOT.glob("vanilla_palette_*.nbt"))
    if not files:
        raise SystemExit("No vanilla_palette_*.nbt files found")

    with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in files:
            zf.write(path, arcname=path.name)

    total = sum(p.stat().st_size for p in files)
    zip_size = OUT_ZIP.stat().st_size
    zip_sha = sha256(OUT_ZIP)
    ratio = (1 - zip_size / total) * 100 if total else 0
    print(f"Wrote {OUT_ZIP.relative_to(ROOT)} with {len(files)} files")
    print(f"  original:   {total} bytes")
    print(f"  compressed: {zip_size} bytes (-{ratio:.1f}%)")

    if not PALETTES_JSON.exists():
        print(
            f"WARNING: {PALETTES_JSON.relative_to(ROOT)} not found, "
            "skipping manifest update"
        )
        return

    data = json.loads(PALETTES_JSON.read_text(encoding="utf-8"))
    data["zip"] = {
        "file": OUT_ZIP.name,
        "size": zip_size,
        "sha256": zip_sha,
        "file_count": len(files),
    }
    ordered = {key: data[key] for key in MANIFEST_KEY_ORDER if key in data}
    for key, value in data.items():
        if key not in ordered:
            ordered[key] = value

    PALETTES_JSON.write_text(
        json.dumps(ordered, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Updated {PALETTES_JSON.relative_to(ROOT)} with zip metadata")


if __name__ == "__main__":
    main()
