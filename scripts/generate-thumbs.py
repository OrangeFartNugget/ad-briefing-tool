"""
Generate WebP thumbnails for the ad briefing tool.

Usage:
  python3 scripts/generate-thumbs.py
  python3 scripts/generate-thumbs.py --src "example pictures" --out thumbs --width 520 --quality 75

Requirements:
  pip install pillow
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
  parser = argparse.ArgumentParser()
  parser.add_argument("--src", default="example pictures", help="Source folder of full images")
  parser.add_argument("--out", default="thumbs", help="Output folder of webp thumbnails")
  parser.add_argument("--width", type=int, default=520, help="Max width for thumbnails")
  parser.add_argument("--quality", type=int, default=75, help="WebP quality")
  parser.add_argument("--overwrite", action="store_true", help="Overwrite existing thumbs")
  args = parser.parse_args()

  try:
    from PIL import Image  # type: ignore
  except Exception as e:
    raise SystemExit(
      "Missing Pillow. Install with: pip install pillow\n" + str(e)
    )

  src_dir = Path(args.src)
  out_dir = Path(args.out)
  out_dir.mkdir(parents=True, exist_ok=True)

  exts = {".jpg", ".jpeg", ".png", ".webp"}
  inputs = [p for p in src_dir.iterdir() if p.is_file() and p.suffix.lower() in exts]
  if not inputs:
    print(f"No images found in: {src_dir}")
    return

  generated = 0
  skipped = 0

  for p in sorted(inputs):
    out_name = p.stem + ".webp"
    out_path = out_dir / out_name

    if out_path.exists() and not args.overwrite:
      skipped += 1
      continue

    im = Image.open(p)
    im = im.convert("RGB")
    w, h = im.size
    if w > args.width:
      new_h = int(h * (args.width / w))
      im = im.resize((args.width, new_h), Image.Resampling.LANCZOS)
    im.save(out_path, "WEBP", quality=args.quality, method=6)
    generated += 1

  print(f"Done. generated={generated}, skipped={skipped}, out={out_dir}")


if __name__ == "__main__":
  main()

