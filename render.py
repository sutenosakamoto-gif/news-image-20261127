#!/usr/bin/env python3
"""Build-time renderer: draws the 27 Nov 2026 broadsheet with PIL + OFL fonts.

Writes page.png (1024x1024). Run: python3 render.py
Fonts are system Noto (OFL): Noto Serif Display Black for the masthead/date,
Noto Serif Bold for headlines, Noto Serif for body, Noto Serif Italic for
the subhead, Noto Sans Condensed for labels/tags.
"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C

W, H = 1024, 1024
MX = 18  # side margin
CREAM = (247, 242, 231)
PAPER2 = (238, 231, 214)
INK = (24, 24, 24)
RED = (176, 30, 36)
BLUE = (31, 78, 121)
SEA = (168, 196, 214)
LAND = (226, 214, 182)
GREY = (110, 105, 95)
GOLD = (176, 141, 42)
DARK = (38, 52, 74)
GREEN = (46, 110, 60)

FONT_DIR = "/usr/share/fonts/truetype/noto"


def F(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_BLACK = lambda s: F("NotoSerifDisplay-Black.ttf", s)
F_SERIF_B = lambda s: F("NotoSerif-Bold.ttf", s)
F_SERIF = lambda s: F("NotoSerif-Regular.ttf", s)
F_SERIF_I = lambda s: F("NotoSerif-Italic.ttf", s)
F_COND_B = lambda s: F("NotoSans-CondensedBold.ttf", s)
F_COND = lambda s: F("NotoSans-Condensed.ttf", s)


def wrap(draw, text, font, max_w):
    """Greedy word wrap; returns list of lines (never splits a word)."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, font, color, leading=None, align="l",
               box_w=None):
    if leading is None:
        leading = font.size + 2
    for line in lines:
        lx = x
        if align == "c":
            lx = x + (box_w - draw.textlength(line, font=font)) // 2
        elif align == "r":
            lx = x + box_w - draw.textlength(line, font=font)
        draw.text((lx, y), line, font=font, fill=color)
        y += leading
    return y


def chip(draw, x, y, text, font):
    """Red figure chip, top-right anchored at (x, y) as its right edge."""
    w = int(draw.textlength(text, font=font)) + 12
    h = font.size + 8
    draw.rounded_rectangle([x - w, y, x, y + h], radius=3, fill=RED)
    draw.text((x - w + 6, y + 4), text, font=font, fill=CREAM)
    return w


# ---------------- illustrations (code-drawn, literal) ----------------

def ill_summit(d, x, y, w, h):
    """EU council: ring of gold stars over a long table with flags."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER2)
    cx, cy = x + int(w * 0.5), y + int(h * 0.28)
    for i in range(12):
        a = math.radians(i * 30)
        d.ellipse([cx + int(w * 0.26) * math.cos(a) - 2,
                   cy + int(h * 0.16) * math.sin(a) - 2,
                   cx + int(w * 0.26) * math.cos(a) + 2,
                   cy + int(h * 0.16) * math.sin(a) + 2], fill=GOLD)
    d.ellipse([x + int(w * 0.18), y + int(h * 0.55), x + int(w * 0.82),
               y + int(h * 0.78)], fill=INK)
    for i in range(3):
        fx = x + int(w * (0.30 + i * 0.20))
        d.line([fx, y + int(h * 0.30), fx, y + int(h * 0.55)], fill=INK,
               width=2)
        d.rectangle([fx, y + int(h * 0.30), fx + 12, y + int(h * 0.40)],
                    fill=RED if i != 1 else BLUE)


def ill_drone(d, x, y, w, h):
    """Night sky, radar arcs, one drone with red warning blink."""
    d.rectangle([x, y, x + w, y + h], fill=DARK)
    cx, cy = x + int(w * 0.30), y + int(h * 0.55)
    for r in (10, 20, 30):
        d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=SEA, width=2)
    dx, dy = x + int(w * 0.68), y + int(h * 0.35)
    d.rectangle([dx - 12, dy - 3, dx + 12, dy + 3], fill=(220, 220, 220))
    d.rectangle([dx - 3, dy - 8, dx + 3, dy + 8], fill=(220, 220, 220))
    for sx in (-16, 16):
        d.ellipse([dx + sx - 4, dy - 4, dx + sx + 4, dy + 4], fill=RED)
    d.ellipse([dx - 3, dy - 3, dx + 3, dy + 3], fill=RED)
    d.line([dx, dy + 8, dx - 6, dy + 18], fill=(220, 220, 220), width=2)
    d.line([dx, dy + 8, dx + 6, dy + 18], fill=(220, 220, 220), width=2)


def ill_bars(d, x, y, w, h):
    """Rising market bars, last bar red, red trend arrow."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER2)
    vals = (0.25, 0.35, 0.30, 0.55, 0.48, 0.72, 0.88)
    bw = w / (len(vals) + 1)
    for i, v in enumerate(vals):
        bx = x + int(bw * (i + 0.6))
        d.rectangle([bx, y + h - 8 - int(h * v * 0.8), bx + int(bw * 0.7),
                     y + h - 8], fill=BLUE if i < 6 else RED)
    d.line([x + 6, y + h - 8, x + w - 6, y + int(h * 0.12)], fill=RED, width=3)
    d.polygon([(x + w - 6, y + int(h * 0.12)), (x + w - 16, y + int(h * 0.12)),
               (x + w - 6, y + int(h * 0.12) + 8)], fill=RED)


def ill_wheat(d, x, y, w, h):
    """Dry field: sun over wheat stalks, one stalk bent."""
    d.rectangle([x, y, x + w, y + h], fill=(240, 224, 170))
    sx, sy = x + int(w * 0.78), y + int(h * 0.26)
    d.ellipse([sx - 10, sy - 10, sx + 10, sy + 10], fill=(230, 170, 60))
    for i in range(5):
        bx = x + int(w * (0.12 + i * 0.17))
        d.line([bx, y + h - 4, bx, y + int(h * 0.45)], fill=GOLD, width=2)
        for k in range(3):
            gy = y + int(h * (0.45 + k * 0.12))
            d.line([bx, gy, bx - 6, gy + 5], fill=GOLD, width=2)
            d.line([bx, gy, bx + 6, gy + 5], fill=GOLD, width=2)
    d.line([x + int(w * 0.80), y + h - 4, x + int(w * 0.88),
            y + int(h * 0.60)], fill=(150, 110, 50), width=2)


def ill_bridge(d, x, y, w, h):
    """Landing drill: civilian hulls linked into a floating bridge."""
    d.rectangle([x, y, x + w, y + h], fill=SEA)
    d.polygon([(x, y + int(h * 0.62)), (x + int(w * 0.25), y + int(h * 0.30)),
               (x + int(w * 0.45), y + int(h * 0.62)), (x, y + h)],
              fill=LAND)
    for i in range(3):
        hx = x + int(w * (0.28 + i * 0.22))
        d.rectangle([hx, y + int(h * 0.55), hx + int(w * 0.18),
                     y + int(h * 0.72)], fill=INK)
        d.rectangle([hx + 4, y + int(h * 0.48), hx + int(w * 0.18) - 4,
                     y + int(h * 0.55)], fill=(255, 255, 255), outline=INK)
    d.line([x + int(w * 0.28), y + int(h * 0.52),
            x + int(w * 0.82), y + int(h * 0.52)], fill=RED, width=2)


def ill_boat(d, x, y, w, h):
    """Small boat on the sea, heading home."""
    d.rectangle([x, y, x + w, y + h], fill=SEA)
    for wy in (0.30, 0.55, 0.80):
        d.line([x + 6, y + int(h * wy), x + w - 6, y + int(h * wy)],
               fill=(255, 255, 255), width=1)
    hx, hy = x + int(w * 0.25), y + int(h * 0.50)
    d.polygon([(hx, hy), (hx + int(w * 0.50), hy),
               (hx + int(w * 0.42), hy + int(h * 0.20)),
               (hx + int(w * 0.08), hy + int(h * 0.20))], fill=INK)
    d.line([hx + int(w * 0.25), hy, hx + int(w * 0.25),
            hy - int(h * 0.30)], fill=INK, width=2)
    d.polygon([(hx + int(w * 0.25), hy - int(h * 0.30)),
               (hx + int(w * 0.25), hy - int(h * 0.05)),
               (hx + int(w * 0.42), hy - int(h * 0.05))], fill=RED)


def ill_storm(d, x, y, w, h):
    """Nor'easter: spiral low over the coast, rain slanting in."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 226, 232))
    d.polygon([(x, y + h), (x + int(w * 0.30), y + int(h * 0.55)),
               (x + int(w * 0.42), y + int(h * 0.62)),
               (x + int(w * 0.55), y + h)], fill=LAND)
    cx, cy = x + int(w * 0.62), y + int(h * 0.48)
    for r in (8, 16, 24, 32):
        d.arc([cx - r, cy - r, cx + r, cy + r], 20, 300, fill=BLUE, width=3)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)
    for i in range(6):
        rx = x + int(w * (0.12 + i * 0.13))
        d.line([rx, y + int(h * 0.14), rx - 5, y + int(h * 0.30)],
               fill=BLUE, width=2)


def ill_flags(d, x, y, w, h):
    """Three vertical banners: Turkey red, Pakistan green, Saudi green."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER2)
    cols = [RED, GREEN, (0, 122, 61)]
    for i, col in enumerate(cols):
        fx = x + int(w * (0.10 + i * 0.30))
        d.rectangle([fx, y + int(h * 0.12), fx + int(w * 0.22),
                     y + int(h * 0.85)], fill=col)
        d.ellipse([fx + int(w * 0.07), y + int(h * 0.38),
                   fx + int(w * 0.15), y + int(h * 0.46)],
                  fill=(255, 255, 255))
    d.line([x + int(w * 0.10), y + int(h * 0.88), x + int(w * 0.90),
            y + int(h * 0.88)], fill=INK, width=2)


def ill_factory(d, x, y, w, h):
    """Garment factory: saw-tooth roof, smokestack, shirt on a line."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER2)
    d.rectangle([x + int(w * 0.10), y + int(h * 0.45), x + int(w * 0.70),
                 y + int(h * 0.85)], fill=INK)
    d.polygon([(x + int(w * 0.10), y + int(h * 0.45)),
               (x + int(w * 0.30), y + int(h * 0.28)),
               (x + int(w * 0.50), y + int(h * 0.45)),
               (x + int(w * 0.70), y + int(h * 0.28)),
               (x + int(w * 0.70), y + int(h * 0.45))], fill=INK)
    d.rectangle([x + int(w * 0.74), y + int(h * 0.18), x + int(w * 0.82),
                 y + int(h * 0.85)], fill=INK)
    for i in range(3):
        d.ellipse([x + int(w * (0.74 + i * 0.02)), y + int(h * (0.08 - i * 0.02)),
                   x + int(w * (0.80 + i * 0.02)), y + int(h * (0.14 - i * 0.02))],
                  fill=GREY)
    d.rectangle([x + int(w * 0.16), y + int(h * 0.60), x + int(w * 0.24),
                 y + int(h * 0.72)], fill=(255, 255, 255), outline=RED)


def ill_court(d, x, y, w, h):
    """Courthouse portico with a red gavel bar."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER2)
    d.polygon([(x + int(w * 0.2), y + int(h * 0.15)),
               (x + int(w * 0.8), y + int(h * 0.15)),
               (x + int(w * 0.5), y + int(h * 0.02))], fill=INK)
    for i in range(4):
        cx0 = x + int(w * (0.22 + i * 0.15))
        d.rectangle([cx0, y + int(h * 0.20), cx0 + 6, y + int(h * 0.80)],
                    fill=INK)
    d.rectangle([x + int(w * 0.15), y + int(h * 0.80), x + int(w * 0.85),
                 y + int(h * 0.86)], fill=INK)
    d.line([x + int(w * 0.62), y + int(h * 0.55), x + int(w * 0.92),
            y + int(h * 0.40)], fill=RED, width=3)
    d.rectangle([x + int(w * 0.86), y + int(h * 0.34), x + int(w * 0.98),
                 y + int(h * 0.46)], fill=RED)


def ill_ship(d, x, y, w, h):
    """Container ship on the Gulf."""
    d.rectangle([x, y, x + w, y + h], fill=SEA)
    hx, hy = x + int(w * 0.12), y + int(h * 0.55)
    d.polygon([(hx, hy), (hx + int(w * 0.76), hy),
               (hx + int(w * 0.68), hy + int(h * 0.22)),
               (hx + int(w * 0.08), hy + int(h * 0.22))], fill=INK)
    cols = [RED, GOLD, BLUE, (40, 120, 70)]
    for r in range(2):
        for i in range(4):
            d.rectangle([hx + 8 + i * 16, hy - 10 - r * 11,
                         hx + 22 + i * 16, hy - 1 - r * 11],
                        fill=cols[(i + r) % 4])
    d.rectangle([hx + int(w * 0.70), hy - 22, hx + int(w * 0.76), hy],
                fill=(255, 255, 255), outline=INK)


def ill_stadium(d, x, y, w, h):
    """Football pitch from above, one red flash at the stands."""
    d.rectangle([x, y, x + w, y + h], fill=(70, 140, 80))
    d.rectangle([x + int(w * 0.14), y + int(h * 0.12), x + int(w * 0.86),
                 y + int(h * 0.88)], fill=(90, 170, 100),
                outline=(255, 255, 255))
    d.line([x + int(w * 0.5), y + int(h * 0.12), x + int(w * 0.5),
            y + int(h * 0.88)], fill=(255, 255, 255), width=2)
    d.line([x + int(w * 0.14), y + int(h * 0.5), x + int(w * 0.86),
            y + int(h * 0.5)], fill=(255, 255, 255), width=2)
    d.ellipse([x + int(w * 0.5) - 8, y + int(h * 0.5) - 8,
               x + int(w * 0.5) + 8, y + int(h * 0.5) + 8],
              outline=(255, 255, 255), width=2)
    d.ellipse([x + int(w * 0.80) - 5, y + int(h * 0.20) - 5,
               x + int(w * 0.80) + 5, y + int(h * 0.20) + 5], fill=RED)


def ill_vial(d, x, y, w, h):
    """Vaccine vial and syringe on a tray."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER2)
    vx, vy = x + int(w * 0.18), y + int(h * 0.30)
    d.rectangle([vx, vy, vx + int(w * 0.22), vy + int(h * 0.45)],
                fill=(255, 255, 255), outline=INK)
    d.rectangle([vx + 4, vy - int(h * 0.08), vx + int(w * 0.22) - 4, vy],
                fill=RED)
    d.rectangle([vx + 4, vy + int(h * 0.12), vx + int(w * 0.22) - 4,
                 vy + int(h * 0.30)], fill=SEA)
    sx = x + int(w * 0.55)
    d.line([sx, y + int(h * 0.25), sx + int(w * 0.30), y + int(h * 0.65)],
           fill=INK, width=3)
    d.line([sx + int(w * 0.30), y + int(h * 0.65),
            sx + int(w * 0.38), y + int(h * 0.73)], fill=INK, width=1)
    d.rectangle([sx - 6, y + int(h * 0.20), sx + 6, y + int(h * 0.28)],
                fill=RED)


def ill_line(d, x, y, w, h):
    """Steady line chart, gently rising."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER2)
    for i in range(4):
        yy = y + int(h * (0.2 + i * 0.2))
        d.line([x + 4, yy, x + w - 4, yy], fill=(210, 204, 190), width=1)
    pts = [(0.05, 0.72), (0.22, 0.66), (0.38, 0.70), (0.55, 0.45),
           (0.72, 0.38), (0.88, 0.18)]
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        d.line([x + w * ax, y + h * ay, x + w * bx, y + h * by],
               fill=RED, width=3)
    d.ellipse([x + w * 0.88 - 4, y + h * 0.18 - 4, x + w * 0.88 + 4,
               y + h * 0.18 + 4], fill=RED)


def ill_bank(d, x, y, w, h):
    """Bank facade with a red arrow pointing to the vault."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER2)
    for bx in (0.12, 0.58):
        px = x + int(w * bx)
        d.polygon([(px, y + h * 0.18), (px + int(w * 0.28), y + h * 0.18),
                   (px + int(w * 0.14), y + h * 0.05)], fill=INK)
        for i in range(3):
            cx0 = px + int(w * (0.03 + i * 0.09))
            d.rectangle([cx0, y + h * 0.22, cx0 + 5, y + h * 0.82], fill=INK)
        d.rectangle([px - 3, y + h * 0.82, px + int(w * 0.28) + 3,
                     y + h * 0.88], fill=INK)
    d.line([x + int(w * 0.44), y + int(h * 0.45), x + int(w * 0.56),
            y + int(h * 0.45)], fill=RED, width=3)
    d.polygon([(x + int(w * 0.56), y + int(h * 0.45)),
               (x + int(w * 0.50), y + int(h * 0.38)),
               (x + int(w * 0.50), y + int(h * 0.52))], fill=RED)


def ill_yen(d, x, y, w, h):
    """Big yen sign with a rising red arrow."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER2)
    d.text((x + int(w * 0.30), y + int(h * 0.10)), "\u00a5",
           font=F_SERIF_B(int(h * 0.62)), fill=INK)
    d.line([x + int(w * 0.68), y + int(h * 0.75), x + int(w * 0.88),
            y + int(h * 0.25)], fill=RED, width=4)
    d.polygon([(x + int(w * 0.88), y + int(h * 0.25)),
               (x + int(w * 0.78), y + int(h * 0.25)),
               (x + int(w * 0.88), y + int(h * 0.38))], fill=RED)


ILLUSTRATIONS = {
    "summit": ill_summit, "drone": ill_drone, "bars": ill_bars,
    "wheat": ill_wheat, "bridge": ill_bridge, "boat": ill_boat,
    "storm": ill_storm, "flags": ill_flags, "factory": ill_factory,
    "court": ill_court, "ship": ill_ship, "stadium": ill_stadium,
    "vial": ill_vial, "line": ill_line, "bank": ill_bank, "yen": ill_yen,
}

# Simplified continent outlines (lon, lat) — stylised, recognisable.
N_AMERICA = [(-168, 66), (-158, 58), (-152, 60), (-140, 60), (-130, 54),
             (-125, 49), (-124, 42), (-120, 34), (-114, 29), (-110, 24),
             (-105, 20), (-97, 16), (-90, 14), (-83, 9), (-79, 9), (-81, 13),
             (-87, 16), (-90, 21), (-96, 19), (-97, 26), (-93, 30),
             (-84, 30), (-81, 26), (-80, 32), (-76, 35), (-74, 39),
             (-70, 42), (-65, 44), (-60, 46), (-55, 47), (-60, 50),
             (-64, 58), (-72, 62), (-85, 66), (-95, 69), (-110, 68),
             (-125, 70), (-145, 70), (-158, 71), (-168, 66)]
S_AMERICA = [(-79, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12),
             (-72, -18), (-70, -30), (-73, -44), (-70, -54), (-66, -55),
             (-62, -45), (-57, -34), (-52, -32), (-48, -28), (-41, -23),
             (-39, -17), (-35, -9), (-38, -4), (-44, -2), (-50, 0),
             (-53, 4), (-58, 6), (-62, 9), (-68, 11), (-72, 12), (-77, 8)]
AFRICA = [(-17, 15), (-16, 20), (-11, 27), (-5, 35), (0, 36), (10, 37),
          (19, 32), (25, 32), (30, 31), (34, 28), (37, 22), (39, 18),
          (43, 11), (51, 11), (51, 6), (42, -2), (40, -8), (40, -15),
          (36, -20), (32, -26), (28, -33), (20, -35), (15, -27),
          (12, -18), (13, -12), (9, -1), (9, 4), (-8, 4), (-13, 8),
          (-17, 12)]
EURASIA = [(-10, 36), (-9, 43), (-2, 44), (-4, 48), (-1, 49), (2, 51),
           (5, 53), (8, 57), (10, 59), (5, 62), (12, 65), (18, 69),
           (25, 71), (30, 70), (40, 68), (50, 69), (60, 69), (70, 72),
           (80, 73), (90, 75), (100, 76), (110, 74), (120, 73), (130, 72),
           (140, 72), (150, 70), (160, 70), (170, 67), (178, 65),
           (170, 60), (162, 56), (158, 52), (150, 59), (142, 55),
           (141, 50), (140, 45), (135, 43), (130, 42), (127, 40),
           (122, 38), (120, 35), (122, 32), (118, 25), (110, 21),
           (108, 18), (105, 10), (100, 8), (98, 10), (94, 17), (92, 21),
           (89, 22), (86, 20), (80, 15), (77, 8), (75, 12), (73, 16),
           (70, 20), (66, 25), (61, 25), (58, 26), (56, 27), (54, 26),
           (52, 25), (50, 29), (48, 30), (44, 29), (41, 28), (39, 24),
           (38, 21), (35, 20), (35, 16), (39, 13), (43, 12), (45, 13),
           (48, 14), (51, 16), (55, 17), (58, 20), (57, 24), (54, 24),
           (51, 26), (50, 29), (48, 30), (44, 29), (40, 31), (36, 36),
           (33, 36), (30, 36), (27, 37), (23, 36), (20, 39), (19, 42),
           (15, 44), (12, 44), (8, 44), (3, 43), (0, 40), (-2, 37),
           (-6, 36)]
AUSTRALIA = [(114, -22), (114, -30), (115, -33), (118, -35), (124, -33),
             (129, -32), (132, -32), (135, -35), (138, -35), (140, -38),
             (145, -38), (150, -37), (153, -32), (153, -27), (150, -23),
             (146, -19), (142, -15), (142, -11), (140, -17), (136, -15),
             (135, -12), (132, -11), (130, -13), (126, -14), (122, -17),
             (118, -20)]

EUROPE_INSET = [(-10, 36), (-9, 43), (-2, 44), (-4, 48), (-1, 49), (2, 51),
                (5, 53), (8, 57), (10, 59), (18, 56), (21, 55), (24, 58),
                (28, 59), (30, 60), (30, 70), (25, 71), (18, 69), (12, 65),
                (5, 62), (5, 58), (8, 57), (10, 59), (5, 60), (5, 62),
                (12, 58), (18, 56), (21, 54), (19, 52), (14, 54), (12, 54),
                (8, 54), (3, 51), (-2, 50), (-5, 48), (-2, 47), (-1, 44),
                (3, 43), (7, 44), (12, 44), (14, 45), (19, 42), (19, 40),
                (16, 40), (16, 38), (12, 38), (8, 39), (3, 38), (-1, 37),
                (-6, 36), (-9, 37), (-9, 43), (-10, 36)]


def draw_map(d, x, y, w, h, polys, lon0, lon1, lat0, lat1):
    def px(lon, lat):
        return (x + (lon - lon0) / (lon1 - lon0) * w,
                y + (lat1 - lat) / (lat1 - lat0) * h)
    d.rectangle([x, y, x + w, y + h], fill=(216, 228, 236))
    for poly in polys:
        d.polygon([px(lon, lat) for lon, lat in poly], fill=LAND,
                  outline=(150, 140, 115))


def pin(d, px, py, num, dx=0, dy=0):
    cx, cy = px + dx, py + dy
    if dx or dy:
        d.line([px, py, cx, cy], fill=INK, width=1)
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=RED, outline=INK)
    d.text((cx, cy - 6), str(num), font=F_COND_B(10), fill=CREAM,
           anchor="ma")


ALSO_LINES = {
    17: "SAUDI CONDEMNS KUWAIT STRIKE; IRAN DENIES ROLE",
    18: "EUROPA LEAGUE: BOURNEMOUTH 2-1 AT CELTA; MILAN 4-2",
    19: "NZ 246/5 ON DAY ONE OF 2ND TEST v INDIA",
    20: "CAMBODIA, THAILAND AGREE SITE VISIT IN SEA ROW",
    21: "HETERO NEARS INDIA NOD FOR GENERIC HIV DRUG",
    22: "CONGO MOBILISES AGAINST MPOX",
    23: "AIRASIA DELAYS STAFF PAY TO MONTH-END",
    24: "JAPAN TOBACCO +2% ON IMPERIAL TAKEOVER TALK",
    25: "RAND +1% TO 17.37 AS METALS RALLY",
    26: "DOLLAR NEAR 22-MONTH PEAK; INDEX 103.81",
    27: "US MARKETS REOPEN FOR HALF-DAY BLACK FRIDAY",
    28: "MACY\u2019S BALLOONS RE-INFLATED FOR SATURDAY",
    29: "NJ TRANSIT HONOURS RAIL TICKETS ON BUSES",
    30: "EURO FLAT AT $1.0964; KIWI $0.5482",
    31: "BRENT $96.14, UP 3.9% FOR THE WEEK",
    32: "NIKKEI +0.7%; KOSPI +2% ON FRIDAY",
    33: "TWO-YEAR TREASURY YIELD 4.6705%",
    34: "CHINA CABINET PLANS NEW MARKET POLICIES",
    35: "SEOUL WEIGHS WIDER NAVY ROLE IN GULF OF OMAN",
    36: "SANDPAPERGATE FORUM WILL NOT APPORTION BLAME",
    37: "CHINA FACTORY SLUMP SEEN LASTING; PMI 49.4",
}


def render():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([4, 4, W - 5, H - 5], outline=INK, width=2)
    y = 10

    # masthead
    f = F_BLACK(30)
    d.text((W // 2, y), C.MASTHEAD, font=f, fill=INK, anchor="ma")
    y += 34
    d.line([MX, y, W - MX, y], fill=INK, width=2)
    y += 8
    # date — largest type on the page
    f = F_BLACK(40)
    d.text((W // 2, y), C.DATE_LINE, font=f, fill=INK, anchor="ma")
    y += 46
    # red italic subhead
    f = F_SERIF_I(15)
    d.text((W // 2, y), C.SUBHEAD, font=f, fill=RED, anchor="ma")
    y += 20
    # region line
    parts = [f"{C.TOTAL_STORIES} STORIES"]
    parts += [f"{name} {n}" for name, n in C.REGION_COUNTS]
    f = F_COND_B(12)
    line = "  \u00b7  ".join(parts)
    assert d.textlength(line, font=f) <= W - 2 * MX, "region line too long"
    d.text((W // 2, y), line, font=f, fill=INK, anchor="ma")
    y += 18
    d.line([MX, y, W - MX, y], fill=INK, width=1)
    y += 7

    # ---- THE DAY IN NUMBERS ----
    f = F_COND_B(12)
    d.text((MX, y), "THE DAY IN NUMBERS", font=f, fill=RED)
    y += 15
    cell_w = (W - 2 * MX) // len(C.NUMBERS)
    f_num = F_SERIF_B(21)
    f_cap = F_COND(10)
    for i, (num, cap) in enumerate(C.NUMBERS):
        cx = MX + i * cell_w + cell_w // 2
        d.text((cx, y), num, font=f_num, fill=INK, anchor="ma")
        lines = wrap(d, cap, f_cap, cell_w - 10)
        assert len(lines) <= 2, f"numbers caption too long: {cap}"
        text_block(d, MX + i * cell_w + 5, y + 22, lines, f_cap, GREY,
                   leading=11, align="c", box_w=cell_w - 10)
        if i:
            d.line([MX + i * cell_w, y + 2, MX + i * cell_w, y + 38],
                   fill=GREY, width=1)
    y += 42
    d.line([MX, y, W - MX, y], fill=INK, width=1)
    y += 7

    # ---- UTC TIMELINE ----
    f = F_COND_B(12)
    d.text((MX, y), "THE DAY IN TIME \u2014 ALL TIMES UTC", font=f, fill=RED)
    y += 15
    col_w = (W - 2 * MX) // 3
    f_t = F_COND_B(11)
    f_e = F_SERIF(11)
    for i, (t, ev) in enumerate(C.TIMELINE):
        x = MX + (i % 3) * col_w
        yy = y + (i // 3) * 12
        d.text((x, yy), t, font=f_t, fill=RED)
        tw = d.textlength(t, font=f_t)
        d.text((x + tw + 5, yy), ev, font=f_e, fill=INK)
    y += 36
    d.line([MX, y, W - MX, y], fill=INK, width=1)
    y += 7

    # ---- LEADS ----
    lead_w = (W - 2 * MX - 16) // 3
    lead_h = 146
    ly = y
    f_head = F_SERIF_B(16)
    f_body = F_SERIF(11)
    f_tag = F_COND_B(10)
    for i, (num, region, cert, head, body, chip_text, kind,
            pin_xy) in enumerate(C.LEADS):
        x = MX + i * (lead_w + 8)
        d.rectangle([x, ly, x + lead_w, ly + lead_h], outline=INK, width=1)
        ix, iy, iw, ih = x + 4, ly + 4, lead_w - 8, 54
        ILLUSTRATIONS[kind](d, ix, iy, iw, ih)
        chip(d, ix + iw - 3, iy + 3, chip_text, F_COND_B(11))
        lines = wrap(d, head, f_head, lead_w - 12)
        assert len(lines) <= 2, f"lead headline too long: {head}"
        text_block(d, x + 6, ly + 62, lines, f_head, INK, leading=19)
        blines = wrap(d, body, f_body, lead_w - 12)
        assert len(blines) <= 2, f"lead body too long: {body}"
        text_block(d, x + 6, ly + 102, blines, f_body, INK, leading=13)
        d.text((x + 6, ly + lead_h - 14), f"{num}  \u00b7  {cert}", font=f_tag,
               fill=RED)
        d.text((x + lead_w - 6, ly + lead_h - 14), region, font=f_tag,
               fill=GREY, anchor="ra")
    y = ly + lead_h + 7

    # ---- MIDDLE TIER: rows of 5, 4, 4 ----
    # row 1: headline-only cards; rows 2-3: headline + 2-line body.
    rows = [(C.MIDDLE[0:5], 72, True), (C.MIDDLE[5:9], 94, False),
            (C.MIDDLE[9:13], 94, False)]
    f_mhead = F_SERIF_B(13)
    f_mbody = F_SERIF(10)
    f_mcert = F_COND_B(8)
    for row, rh, headline_only in rows:
        n = len(row)
        mw = (W - 2 * MX - (n - 1) * 6) // n
        for i, (num, region, cert, head, body, chip_text, kind,
                pin_xy) in enumerate(row):
            x = MX + i * (mw + 6)
            d.rectangle([x, y, x + mw, y + rh], outline=INK, width=1)
            ix, iy, iw, ih = x + 3, y + 3, mw - 6, 34
            ILLUSTRATIONS[kind](d, ix, iy, iw, ih)
            chip(d, ix + iw - 3, iy + 3, chip_text, F_COND_B(9))
            # certainty strip along the bottom of the illustration
            d.rectangle([ix, iy + ih - 10, ix + iw, iy + ih], fill=INK)
            d.text((ix + 4, iy + ih - 9), cert, font=f_mcert, fill=CREAM)
            lines = wrap(d, head, f_mhead, mw - 26)
            assert len(lines) <= 2, f"middle headline too long: {head}"
            text_block(d, x + 4, y + 41, lines, f_mhead, INK, leading=15)
            if not headline_only:
                blines = wrap(d, body, f_mbody, mw - 8)
                assert len(blines) <= 2, f"middle body too long: {body}"
                text_block(d, x + 4, y + 71, blines, f_mbody, GREY,
                           leading=11)
            d.text((x + mw - 4, y + 41), str(num), font=F_COND_B(11),
                   fill=RED, anchor="ra")
        y += rh + 5

    # ---- MAP ----
    f = F_COND_B(12)
    d.text((MX, y), "WHERE IT HAPPENED \u2014 PIN NUMBERS MATCH STORY NUMBERS",
           font=f, fill=RED)
    y += 13
    map_y = y
    map_h = 70
    map_w = 640
    draw_map(d, MX, map_y, map_w, map_h,
             [N_AMERICA, S_AMERICA, AFRICA, EURASIA, AUSTRALIA],
             -170, 190, -55, 75)
    d.rectangle([MX, map_y, MX + map_w, map_y + map_h], outline=INK, width=1)
    f_oc = F_COND(9)
    d.text((MX + 8, map_y + map_h - 12), "PACIFIC", font=f_oc, fill=GREY)
    d.text((MX + 300, map_y + map_h - 12), "ATLANTIC", font=f_oc, fill=GREY)

    def map_px(lon, lat):
        return (MX + (lon + 170) / 360.0 * map_w,
                map_y + (75 - lat) / 130.0 * map_h)

    # pins on the world map; 1, 2, 12, 15 live in the Europe inset
    nudges = {4: (0, 8), 5: (-16, 12), 6: (2, -14), 8: (0, -10),
              14: (16, -6), 16: (14, 8)}
    for item in C.LEADS + C.MIDDLE:
        num = item[0]
        if num in (1, 2, 12, 15):
            continue
        lon, lat = item[7]
        px, py = map_px(lon, lat)
        ndx, ndy = nudges.get(num, (0, 0))
        pin(d, px, py, num, dx=ndx, dy=ndy)
    # Europe inset
    ex, ew = MX + map_w + 8, W - MX - (MX + map_w + 8)
    draw_map(d, ex, map_y, ew, map_h, [EUROPE_INSET], -12, 32, 35, 62)
    d.rectangle([ex, map_y, ex + ew, map_y + map_h], outline=INK, width=1)
    d.rectangle([ex + 3, map_y + 3, ex + 92, map_y + 15], fill=CREAM)
    d.text((ex + 6, map_y + 4), "EUROPE \u2014 DETAIL", font=F_COND_B(10),
           fill=RED)
    for num, lon, lat in ((1, 4.35, 50.85), (2, 24.1, 56.95),
                          (12, 5.4, 43.3), (15, 30.5, 50.4)):
        px = ex + (lon + 12) / 44.0 * ew
        py = map_y + (62 - lat) / 27.0 * map_h
        pin(d, px, py, num)
    y = map_y + map_h + 7

    # ---- ALSO ----
    f = F_COND_B(12)
    d.text((MX, y), "ALSO ON FRIDAY 27 NOVEMBER", font=f, fill=RED)
    y += 13
    col_w = (W - 2 * MX) // 3
    f_a = F_COND_B(11)
    for i, item in enumerate(C.ALSO):
        num = item[0]
        x = MX + (i % 3) * col_w
        yy = y + (i // 3) * 11
        txt = ALSO_LINES[num]
        w = d.textlength(txt, font=f_a)
        assert w <= col_w - 30, f"ALSO line too long: {txt}"
        d.text((x, yy), f"{num}.", font=f_a, fill=RED)
        d.text((x + 20, yy), txt, font=f_a, fill=INK)
    y += 7 * 11 + 4

    # ---- DATE CHECK ----
    d.line([MX, y, W - MX, y], fill=INK, width=1)
    y += 5
    f = F_COND_B(12)
    d.text((MX, y), "DATE CHECK \u2014 EXCLUDED AS OTHER DAYS\u2019 NEWS, OR NOT YET",
           font=f, fill=RED)
    y += 13
    f_d = F_SERIF(10)
    f_dl = F_COND_B(10)
    for label, note in C.DATECHECK:
        d.text((MX, y), label, font=f_dl, fill=RED)
        lw = d.textlength(label, font=f_dl)
        lines = wrap(d, note, f_d, W - 2 * MX - lw - 8)
        assert len(lines) == 1, f"DATE CHECK line wraps: {note}"
        d.text((MX + lw + 8, y), lines[0], font=f_d, fill=INK)
        y += 11
    y += 2
    f_l = F_COND(10)
    d.text((MX, y), C.LEGEND, font=f_l, fill=GREY)
    y += 11
    d.text((MX, y), C.ILLU_NOTE, font=f_l, fill=GREY)
    y += 11

    assert y <= H - 4, f"page overflow: y={y}"
    return img


def main():
    img = render()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "page.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
