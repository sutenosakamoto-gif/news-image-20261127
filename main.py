#!/usr/bin/env python3
"""Entry point for the 27 November 2026 world-news image.

Copies the finished broadsheet (page.png, rendered at build time by
render.py from content.py) to /output/entry.png. Standard library only,
no network, deterministic: two runs write identical bytes. The page
itself is the 27 Nov broadsheet: 37 stories, every one dated Friday
27 November 2026, with 25-26 Nov substance named in its DATE CHECK
footer instead of presented as the day's news.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
# The finished page is a 1024x1024 PNG of at most 1 MiB; check the header
# and size before copying so a bad build fails loudly instead of shipping
# a broken entry.
PNG_SIG = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def check_page(src):
    with open(src, "rb") as f:
        head = f.read(33)
    if head[:8] != PNG_SIG:
        raise ValueError("page.png is not a PNG file")
    width, height = int.from_bytes(head[16:20], "big"), int.from_bytes(
        head[20:24], "big")
    if (width, height) != (1024, 1024):
        raise ValueError(f"page.png is {width}x{height}, expected 1024x1024")
    size = os.path.getsize(src)
    if size > MAX_BYTES:
        raise ValueError(f"page.png is {size} bytes, over the 1 MiB cap")
    return size


def main():
    src = os.path.join(HERE, "page.png")
    check_page(src)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(outdir, exist_ok=True)
        dst = os.path.join(outdir, "entry.png")
    except OSError:
        dst = os.path.join(HERE, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
