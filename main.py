#!/usr/bin/env python3
"""Entry point for the 27 November 2026 world-news image.

The finished broadsheet lives in this repository as page.png, drawn
at build time by render.py from the day file content.py. This program
simply places a copy of it where the competition expects the entry,
at /output/entry.png (or in MAKEFUN_OUTPUT_DIR when that is set),
and double-checks the result is a whole 1024x1024 PNG inside the
1 MiB size cap. It reads nothing from the network and writes the
same bytes on every run.
"""

import os
import shutil
import sys

CAP_BYTES = 1024 * 1024
WANT_W, WANT_H = 1024, 1024

HERE = os.path.dirname(os.path.abspath(__file__))


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.png")


def main():
    src = os.path.join(HERE, "page.png")
    dst = entry_path()
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        head = fh.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        sys.exit("entry.png is not a PNG file")
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    if (width, height) != (WANT_W, WANT_H):
        sys.exit("entry.png is %dx%d, expected 1024x1024" % (width, height))
    # a whole PNG ends with its IEND chunk; a truncated copy is not one
    with open(dst, "rb") as fh:
        fh.seek(-12, os.SEEK_END)
        tail = fh.read(12)
    if tail[4:8] != b"IEND" or tail[8:12] != b"\xaeB`\x82":
        sys.exit("entry.png is missing its IEND chunk")
    size = os.path.getsize(dst)
    if size > CAP_BYTES:
        sys.exit("entry.png is %d bytes, over the 1 MiB cap" % size)
    print("wrote %s %d bytes" % (dst, size))


if __name__ == "__main__":
    main()
