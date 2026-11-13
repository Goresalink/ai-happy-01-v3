#!/usr/bin/env python3
"""Copy the happy entry image into the output directory.

The image is stored in this repository as entry.png. Running this
program places an identical copy at /output/entry.png for judging.
"""

from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
OUT = Path("/output") / "entry.png"


def main() -> None:
    image = SRC.read_bytes()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(image)
    copied = OUT.read_bytes()
    assert copied == image, "output does not match the source image"
    print(f"wrote {len(copied)} bytes to {OUT}")


if __name__ == "__main__":
    main()
