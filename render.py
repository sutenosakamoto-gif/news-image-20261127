#!/usr/bin/env python3
"""Draw the 27 Nov 2026 world-news broadsheet and save it as page.png.

One page, 1024x1024, cream newsprint. Everything is drawn with PIL
and real OFL fonts; nothing is fetched at run time. Run it and it
writes page.png next to this file.
"""

import os
from PIL import Image, ImageDraw, ImageFont

import content as day

PAGE_W, PAGE_H = 1024, 1024
EDGE = 22                      # outer margin
PAPER = (247, 241, 221)        # cream newsprint
INK = (26, 22, 18)             # near-black
FAINT = (120, 110, 92)         # muted caption ink
RULE = (60, 52, 40)            # hairline rule
RED = (178, 34, 28)            # headline red
SKY = (205, 224, 232)          # map sea
LAND = (216, 196, 154)         # map land dots
CARD_BG = (252, 249, 240)
CARD_LINE = (168, 156, 128)

SERIF = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Italic.ttf"
SERIF_X = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Black.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"

_fonts = {}


def typeface(path, px):
    key = (path, px)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(path, px)
    return _fonts[key]


def split_lines(d, text, font, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(d, lines, x, y, font, fill=INK, gap=2, align="left"):
    for line in lines:
        if align == "center":
            w = d.textlength(line, font=font)
            d.text((x - w / 2, y), line, font=font, fill=fill)
        else:
            d.text((x, y), line, font=font, fill=fill)
        y += font.size + gap
    return y


def hline(d, x0, x1, y, fill=RULE, width=1):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- scenes
# Each painter gets (draw, x0, y0, x1, y1) and draws a flat little
# scene that names its story. All coordinates are local to the box.

def _chip(d, x_right, y, text):
    """Red tag, right-aligned so its right edge sits at x_right."""
    f = typeface(SANS_B, 11)
    w = d.textlength(text, font=f) + 10
    x = x_right - w
    d.rounded_rectangle([x, y, x + w, y + 16], radius=3, fill=RED)
    d.text((x + 5, y + 2), text, font=f, fill=(255, 255, 255))


def scene_summit(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(38, 52, 74))
    d.rectangle([x0, y1 - 26, x1, y1], fill=(24, 34, 52))
    # long table
    d.ellipse([x0 + 18, y1 - 46, x1 - 18, y1 - 18], fill=(12, 18, 30))
    d.ellipse([x0 + 18, y1 - 46, x1 - 18, y1 - 34], fill=(70, 88, 118))
    # three flags behind the table
    for i, col in enumerate([(0, 60, 140), (255, 205, 0), (200, 40, 40)]):
        fx = x0 + 34 + i * 52
        d.line([(fx, y0 + 14), (fx, y1 - 44)], fill=(220, 220, 220), width=2)
        d.rectangle([fx, y0 + 14, fx + 34, y0 + 30], fill=col)
    # seated heads
    for i in range(5):
        cx = x0 + 30 + i * ((x1 - x0 - 60) // 4)
        d.ellipse([cx - 6, y1 - 58, cx + 6, y1 - 46], fill=(232, 205, 160))


def scene_drone(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(16, 24, 48))
    for sx, sy in [(0.12, 0.2), (0.3, 0.12), (0.55, 0.28), (0.78, 0.15),
                   (0.9, 0.35), (0.42, 0.4), (0.65, 0.08)]:
        d.ellipse([x0 + sx * (x1 - x0) - 1, y0 + sy * (y1 - y0) - 1,
                   x0 + sx * (x1 - x0) + 1, y0 + sy * (y1 - y0) + 1],
                  fill=(255, 255, 200))
    # dashed flight path
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    for i in range(6):
        px = x0 + 10 + i * 14
        d.line([(px, cy + 26 - i * 4), (px + 8, cy + 22 - i * 4)],
               fill=(255, 120, 100), width=2)
    # drone body
    d.ellipse([cx - 16, cy - 8, cx + 16, cy + 8], fill=(240, 240, 240))
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)
    for dx, dy in [(-22, -12), (22, -12), (-22, 12), (22, 12)]:
        d.line([(cx + dx * 0.6, cy + dy * 0.6), (cx + dx, cy + dy)],
               fill=(200, 200, 200), width=2)
        d.ellipse([cx + dx - 7, cy + dy - 2, cx + dx + 7, cy + dy + 2],
                  outline=(255, 255, 255), width=2)


def scene_bars(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(238, 240, 235))
    w = (x1 - x0) / 7
    heights = [0.25, 0.32, 0.3, 0.45, 0.55, 0.72, 0.9]
    tops = []
    for i, h in enumerate(heights):
        bx = x0 + 8 + i * w
        top = y1 - 10 - h * (y1 - y0 - 22)
        col = RED if i == 6 else (28, 68, 128)
        d.rectangle([bx, top, bx + w - 8, y1 - 10], fill=col)
        tops.append((bx + (w - 8) / 2, top))
    for (ax, ay), (bx, by) in zip(tops, tops[1:]):
        d.line([(ax, ay), (bx, by)], fill=RED, width=2)


def scene_wheat(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(243, 226, 170))
    h = y1 - y0
    rows = max(1, (h - 22) // 12)
    for i in range(5):
        sx = x0 + 22 + i * ((x1 - x0 - 44) // 4)
        d.line([(sx, y1 - 6), (sx, y0 + 14)], fill=(150, 118, 40), width=2)
        for j in range(rows):
            gy = y0 + 16 + j * 12
            d.ellipse([sx - 5, gy, sx + 5, gy + 8], fill=(198, 152, 40))
        d.ellipse([sx - 4, y0 + 8, sx + 4, y0 + 16], fill=(180, 132, 30))


def scene_bridge(d, x0, y0, x1, y1):
    h = y1 - y0
    d.rectangle([x0, y0, x1, y1], fill=(168, 205, 220))
    d.rectangle([x0, y1 - int(h * 0.25), x1, y1], fill=(120, 170, 195))
    # floating bridge segments
    deck_y = y0 + int(h * 0.42)
    for i in range(5):
        bx = x0 + 12 + i * ((x1 - x0 - 24) // 5)
        d.rectangle([bx, deck_y, bx + 26, deck_y + 10], fill=(90, 90, 96))
        d.rectangle([bx + 4, deck_y + 10, bx + 22, y1 - int(h * 0.28)],
                    fill=(70, 70, 76))
    # small ship at the far end
    d.polygon([(x1 - 52, y1 - int(h * 0.3)), (x1 - 14, y1 - int(h * 0.3)),
               (x1 - 20, y1 - int(h * 0.18)), (x1 - 46, y1 - int(h * 0.18))],
              fill=(40, 40, 48))


def scene_boat(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(190, 215, 228))
    d.rectangle([x0, y1 - 20, x1, y1], fill=(140, 180, 205))
    for wy in (y1 - 16, y1 - 8):
        d.line([(x0 + 8, wy), (x1 - 8, wy)], fill=(255, 255, 255), width=2)
    # little white boat
    bx = (x0 + x1) // 2
    d.polygon([(bx - 34, y1 - 34), (bx + 34, y1 - 34), (bx + 24, y1 - 20),
               (bx - 24, y1 - 20)], fill=(250, 250, 250))
    d.rectangle([bx - 12, y1 - 48, bx + 12, y1 - 34], fill=(220, 60, 50))
    d.line([(bx, y1 - 48), (bx, y0 + 12)], fill=(90, 80, 70), width=2)


def scene_storm(d, x0, y0, x1, y1):
    h = y1 - y0
    d.rectangle([x0, y0, x1, y1], fill=(120, 138, 158))
    d.ellipse([x0 + 8, y0 + 4, x0 + 70, y0 + 22], fill=(70, 80, 96))
    d.ellipse([x0 + 44, y0 + 2, x0 + 110, y0 + 20], fill=(88, 98, 114))
    d.ellipse([x1 - 76, y0 + 6, x1 - 12, y0 + 24], fill=(70, 80, 96))
    for i in range(7):
        rx = x0 + 14 + i * 16
        d.line([(rx, y0 + int(h * 0.55)), (rx - 5, y0 + int(h * 0.78))],
               fill=(200, 215, 230), width=2)
    # lightning, kept inside the picture box
    lx = (x0 + x1) // 2
    d.line([(lx, y0 + int(h * 0.42)), (lx - 7, y0 + int(h * 0.62)),
            (lx + 2, y0 + int(h * 0.62)), (lx - 6, y0 + int(h * 0.85))],
           fill=(255, 220, 60), width=3)
    # house silhouettes
    d.rectangle([x0 + 16, y1 - 14, x0 + 44, y1 - 4], fill=(40, 46, 58))
    d.rectangle([x1 - 46, y1 - 16, x1 - 16, y1 - 4], fill=(40, 46, 58))


def scene_pact(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(238, 232, 210))
    cols = [(200, 40, 40), (0, 110, 60), (30, 60, 120)]
    for i, col in enumerate(cols):
        fx = x0 + 26 + i * ((x1 - x0 - 52) // 2)
        d.line([(fx, y0 + 12), (fx, y1 - 30)], fill=(90, 80, 66), width=2)
        d.rectangle([fx, y0 + 12, fx + 30, y0 + 30], fill=col)
        d.ellipse([fx - 5, y1 - 38, fx + 5, y1 - 28], fill=(60, 52, 40))
    d.rectangle([x0 + 10, y1 - 26, x1 - 10, y1 - 16], fill=(120, 100, 70))


def scene_garment(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(235, 228, 210))
    # folded shirt stack, only the folds that fit inside the box
    for i, col in enumerate([(200, 60, 50), (60, 110, 170), (240, 200, 90)]):
        sy = y1 - 18 - i * 14
        if sy - 10 < y0:
            continue
        d.rectangle([x0 + 22, sy - 10, x1 - 22, sy], fill=col)
    # shirt outline above the stack, kept inside the picture box
    cx = (x0 + x1) // 2
    top = y0 + 6
    bot = y1 - 32
    d.polygon([(cx - 8, top), (cx + 8, top), (cx + 24, top + 8),
               (cx + 36, top + 24), (cx + 26, top + 28), (cx + 20, top + 18),
               (cx + 20, bot), (cx - 20, bot), (cx - 20, top + 18),
               (cx - 26, top + 28), (cx - 36, top + 24), (cx - 24, top + 8)],
              fill=(250, 250, 248), outline=(90, 80, 66))
    d.rectangle([x1 - 46, y0 + 8, x1 - 14, y0 + 24], fill=(255, 255, 255),
                outline=RED)
    d.text((x1 - 40, y0 + 10), "$", font=typeface(SERIF_B, 12), fill=RED)


def scene_gavel(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(52, 44, 38))
    # sound block
    d.rectangle([x0 + 18, y1 - 26, x1 - 18, y1 - 12], fill=(120, 84, 48))
    # gavel head and handle, diagonal
    d.line([(x0 + 26, y1 - 34), (x1 - 30, y0 + 22)], fill=(150, 104, 58),
           width=7)
    d.rectangle([x1 - 52, y0 + 12, x1 - 14, y0 + 34], fill=(120, 84, 48))
    d.rectangle([x0 + 16, y1 - 44, x0 + 52, y1 - 26], fill=(120, 84, 48))


def scene_ship(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(176, 208, 224))
    for wy in (y1 - 18, y1 - 10):
        d.line([(x0 + 6, wy), (x1 - 6, wy)], fill=(255, 255, 255), width=2)
    # cargo ship
    d.polygon([(x0 + 12, y1 - 30), (x1 - 12, y1 - 30), (x1 - 22, y1 - 16),
               (x0 + 22, y1 - 16)], fill=(52, 60, 70))
    for i, col in enumerate([(200, 60, 50), (40, 110, 160), (230, 180, 60),
                             (60, 140, 90)]):
        cx = x0 + 26 + i * 24
        d.rectangle([cx, y1 - 46, cx + 20, y1 - 30], fill=col)


def scene_pitch(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(70, 140, 70))
    d.rectangle([x0 + 8, y0 + 8, x1 - 8, y1 - 8], outline=(255, 255, 255),
                width=2)
    d.line([(x0 + (x1 - x0) // 2, y0 + 8), (x0 + (x1 - x0) // 2, y1 - 8)],
           fill=(255, 255, 255), width=2)
    d.ellipse([x0 + (x1 - x0) // 2 - 14, (y0 + y1) // 2 - 14,
               x0 + (x1 - x0) // 2 + 14, (y0 + y1) // 2 + 14],
              outline=(255, 255, 255), width=2)
    d.ellipse([x0 + 18, y0 + 16, x0 + 34, y0 + 32], fill=(255, 255, 255))
    d.ellipse([x1 - 34, y1 - 32, x1 - 18, y1 - 16], fill=(30, 30, 30))


def scene_vial(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(232, 240, 238))
    # vial
    vx = (x0 + x1) // 2 - 26
    d.rounded_rectangle([vx, y0 + 22, vx + 26, y1 - 10], radius=5,
                        fill=(180, 215, 225), outline=(60, 100, 120),
                        width=2)
    d.rectangle([vx + 6, y0 + 12, vx + 20, y0 + 22], fill=(60, 100, 120))
    d.rectangle([vx + 3, y1 - 30, vx + 23, y1 - 12], fill=(255, 255, 255))
    # syringe, diagonal
    d.line([(x1 - 52, y0 + 14), (x1 - 16, y0 + 50)], fill=(140, 140, 140),
           width=4)
    d.line([(x1 - 58, y0 + 8), (x1 - 46, y0 + 20)], fill=(140, 140, 140),
           width=3)


def scene_candles(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(240, 238, 230))
    w = (x1 - x0) / 6
    vals = [(0.3, 0.55, True), (0.45, 0.7, True), (0.6, 0.5, False),
            (0.5, 0.75, True), (0.65, 0.85, True), (0.8, 0.95, False)]
    for i, (lo, hi, up) in enumerate(vals):
        cx = x0 + 8 + i * w + w / 2
        top = y1 - 12 - max(lo, hi) * (y1 - y0 - 24)
        bot = y1 - 12 - min(lo, hi) * (y1 - y0 - 24)
        d.line([(cx, y1 - 12 - hi * (y1 - y0 - 24) - 6),
                (cx, y1 - 12 - lo * (y1 - y0 - 24) + 6)],
               fill=INK, width=1)
        col = (40, 140, 80) if up else (200, 50, 40)
        d.rectangle([cx - 7, top, cx + 7, bot], fill=col)


def scene_bank(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(36, 54, 88))
    # pediment
    d.polygon([(x0 + 14, y0 + 26), (x1 - 14, y0 + 26),
               ((x0 + x1) // 2, y0 + 8)], fill=(235, 230, 215))
    # columns
    for i in range(4):
        cx = x0 + 22 + i * ((x1 - x0 - 44) // 3)
        d.rectangle([cx - 6, y0 + 28, cx + 6, y1 - 14], fill=(235, 230, 215))
    d.rectangle([x0 + 10, y1 - 14, x1 - 10, y1 - 6], fill=(235, 230, 215))
    d.rectangle([x0 + 10, y0 + 26, x1 - 10, y0 + 30], fill=(235, 230, 215))


def scene_yen(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(238, 230, 205))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    r = min(26, (y1 - y0) // 2 - 3)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(180, 40, 36))
    d.text((cx - 11, cy - 16), "\u00a5", font=typeface(SERIF_X, 28),
           fill=(255, 255, 255))
    for dx, dy in [(-38, 18), (38, -14), (34, 20)]:
        d.ellipse([cx + dx - 7, cy + dy - 7, cx + dx + 7, cy + dy + 7],
                  fill=(212, 175, 55), outline=(150, 110, 20))


SCENES = {"summit": scene_summit, "drone": scene_drone, "bars": scene_bars,
          "wheat": scene_wheat, "bridge": scene_bridge, "boat": scene_boat,
          "storm": scene_storm, "pact": scene_pact, "garment": scene_garment,
          "gavel": scene_gavel, "ship": scene_ship, "pitch": scene_pitch,
          "vial": scene_vial, "candles": scene_candles, "bank": scene_bank,
          "yen": scene_yen}


# ------------------------------------------------------------------- map
# Rough continent outlines as (lon, lat) polygons, from general
# geographic knowledge. Dots are drawn on a grid where they fall
# inside one of these shapes.

CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 80),
     (-75, 73), (-60, 60), (-55, 47), (-70, 42), (-75, 35), (-80, 26),
     (-84, 30), (-90, 21), (-97, 16), (-105, 20), (-110, 23), (-120, 34),
     (-125, 40), (-125, 49), (-140, 60), (-155, 58), (-165, 60)],
    [(-80, 10), (-75, 11), (-62, 10), (-52, 5), (-50, 0), (-44, -3),
     (-35, -8), (-40, -20), (-48, -28), (-58, -35), (-65, -41), (-70, -52),
     (-74, -54), (-73, -40), (-70, -20), (-80, -5)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 51), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 55), (24, 59), (28, 60), (30, 62), (32, 70), (40, 68),
     (44, 66), (40, 60), (35, 55), (30, 46), (28, 44), (23, 40), (19, 42),
     (12, 44), (8, 44), (3, 43), (-2, 37), (-9, 37)],
    [(-17, 15), (-10, 5), (-8, -5), (9, -1), (12, -5), (13, -12),
     (14, -17), (12, -18), (16, -28), (20, -35), (28, -33), (33, -26),
     (36, -18), (40, -11), (41, -2), (46, 2), (51, 11), (43, 12),
     (38, 18), (33, 27), (30, 31), (22, 33), (11, 34), (10, 37), (0, 36),
     (-6, 35), (-10, 31), (-15, 27), (-17, 21)],
    [(32, 36), (36, 36), (43, 41), (48, 42), (52, 44), (55, 47), (60, 45),
     (66, 45), (70, 50), (75, 55), (80, 60), (85, 68), (90, 72), (100, 76),
     (110, 76), (120, 73), (130, 72), (140, 72), (155, 70), (160, 66),
     (170, 66), (178, 65), (170, 60), (162, 56), (158, 52), (150, 59),
     (142, 55), (140, 45), (135, 43), (130, 35), (127, 35), (122, 30),
     (120, 25), (115, 22), (110, 20), (108, 12), (105, 9), (100, 8),
     (98, 10), (95, 15), (92, 21), (90, 22), (86, 20), (82, 17), (80, 13),
     (77, 8), (75, 12), (72, 20), (68, 23), (66, 25), (62, 25), (58, 26),
     (56, 27), (52, 29), (50, 30), (48, 30), (44, 29), (42, 30), (39, 32),
     (36, 36)],
    [(113, -22), (114, -30), (115, -35), (120, -34), (129, -32),
     (132, -32), (136, -35), (140, -38), (145, -38), (150, -37),
     (153, -32), (153, -27), (150, -23), (146, -19), (142, -11),
     (136, -12), (132, -11), (130, -13), (126, -14), (122, -17),
     (117, -20)],
]


def inside_poly(lon, lat, poly):
    """Ray-casting point-in-polygon test."""
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > lat) != (yj > lat):
            xin = (xj - xi) * (lat - yi) / (yj - yi) + xi
            if lon < xin:
                inside = not inside
        j = i
    return inside


def on_land(lon, lat):
    return any(inside_poly(lon, lat, p) for p in CONTINENTS)


def paint_dots(d, box, lon0, lon1, lat0, lat1, step=7):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    lon = lon0
    while lon <= lon1:
        lat = lat0
        while lat <= lat1:
            if on_land(lon, lat):
                px = x0 + (lon - lon0) / (lon1 - lon0) * w
                py = y1 - (lat - lat0) / (lat1 - lat0) * h
                d.ellipse([px - 1.6, py - 1.6, px + 1.6, py + 1.6],
                          fill=LAND)
            lat += (lat1 - lat0) / h * step
        lon += (lon1 - lon0) / w * step


def geo_to_xy(lon, lat, box, lon0, lon1, lat0, lat1):
    x0, y0, x1, y1 = box
    px = x0 + (lon - lon0) / (lon1 - lon0) * (x1 - x0)
    py = y1 - (lat - lat0) / (lat1 - lat0) * (y1 - y0)
    return px, py


def paint_pin(d, x, y, num, r=9):
    d.ellipse([x - r, y - r, x + r, y + r], fill=RED,
              outline=(255, 255, 255), width=2)
    f = typeface(SANS_B, 11 if num < 10 else 10)
    t = str(num)
    tw = d.textlength(t, font=f)
    d.text((x - tw / 2, y - 6), t, font=f, fill=(255, 255, 255))


# Pins that would collide on the main map get a small push, with a
# leader line back to the true spot.
PIN_PUSH = {4: (-12, 10), 8: (12, -10), 5: (-12, -9), 14: (12, 10),
            6: (-4, -12), 16: (12, 7)}


# ------------------------------------------------------------------ page

def build_page():
    img = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    d = ImageDraw.Draw(img)
    x0, x1 = EDGE, PAGE_W - EDGE

    # ---- masthead + date + subhead + region line
    y = 6
    f_mast = typeface(SERIF_X, 22)
    tw = d.textlength(day.PAPER_NAME, font=f_mast)
    d.text(((PAGE_W - tw) / 2, y), day.PAPER_NAME, font=f_mast, fill=INK)
    y += 30
    hline(d, x0, x1, y, width=2)
    y += 4
    f_date = typeface(SERIF_B, 38)
    tw = d.textlength(day.DAY_LINE, font=f_date)
    d.text(((PAGE_W - tw) / 2, y), day.DAY_LINE, font=f_date, fill=INK)
    y += 46
    f_dek = typeface(SERIF_I, 17)
    tw = d.textlength(day.DEK_LINE, font=f_dek)
    d.text(((PAGE_W - tw) / 2, y), day.DEK_LINE, font=f_dek, fill=RED)
    y += 18
    parts = ["%d STORIES" % day.STORY_TOTAL]
    parts += ["%s %d" % (name, n) for name, n in day.REGION_TALLY]
    region_line = "  \u00b7  ".join(parts)
    f_reg = typeface(SANS_B, 13)
    tw = d.textlength(region_line, font=f_reg)
    d.text(((PAGE_W - tw) / 2, y), region_line, font=f_reg, fill=INK)
    y += 14
    hline(d, x0, x1, y, width=2)

    # ---- numbers strip
    y += 4
    d.text((x0, y), "THE DAY IN NUMBERS", font=typeface(SANS_B, 12),
           fill=RED)
    y += 12
    cell_w = (x1 - x0) / len(day.FIGURES)
    for i, (val, cap) in enumerate(day.FIGURES):
        cx = x0 + i * cell_w
        f_val = typeface(SERIF_B, 20)
        tw = d.textlength(val, font=f_val)
        d.text((cx + (cell_w - tw) / 2, y), val, font=f_val, fill=INK)
        f_cap = typeface(SANS, 9)
        tw = d.textlength(cap, font=f_cap)
        d.text((cx + (cell_w - tw) / 2, y + 22), cap, font=f_cap,
               fill=FAINT)
        if i:
            d.line([(cx, y + 2), (cx, y + 32)], fill=CARD_LINE, width=1)
    y += 32
    hline(d, x0, x1, y)

    # ---- timeline, two columns
    y += 4
    d.text((x0, y), "THE DAY IN TIME \u2014 ALL TIMES UTC",
           font=typeface(SANS_B, 12), fill=RED)
    y += 13
    col_w = (x1 - x0) / 2
    f_time = typeface(SANS_B, 11)
    f_lab = typeface(SANS, 11)
    for i, (when, what) in enumerate(day.TIMELINE):
        col = i % 2
        row = i // 2
        tx = x0 + col * col_w
        ty = y + row * 12
        d.text((tx, ty), when, font=f_time, fill=RED)
        ww = d.textlength(when, font=f_time)
        d.text((tx + ww + 6, ty), what, font=f_lab, fill=INK)
    y += 4 * 12 + 3
    hline(d, x0, x1, y)

    # ---- three leads
    y += 4
    lead_h = 156
    lead_w = (x1 - x0 - 16) / 3
    for i, item in enumerate(day.FEATURED[:3]):
        bx = x0 + i * (lead_w + 8)
        d.rectangle([bx, y, bx + lead_w, y + lead_h], fill=CARD_BG,
                    outline=CARD_LINE, width=1)
        SCENES[item["art"]](d, bx + 1, y + 1, bx + lead_w - 1, y + 72)
        _chip(d, bx + lead_w - 5, y + 6, item["chip"])
        f_head = typeface(SERIF_B, 18)
        hl = split_lines(d, item["head"], f_head, lead_w - 14)
        ty = draw_lines(d, hl[:3], bx + 7, y + 78, f_head, gap=0)
        # deck gets only the lines that fit above the footer line
        f_deck = typeface(SANS, 11)
        dl = split_lines(d, item["deck"], f_deck, lead_w - 14)
        room = (y + lead_h - 13) - (ty + 2)
        n_deck = max(0, min(len(dl), room // 13))
        draw_lines(d, dl[:n_deck], bx + 7, ty + 2, f_deck, fill=FAINT,
                   gap=0)
        f_foot = typeface(SANS_B, 10)
        d.text((bx + 7, y + lead_h - 13),
               "%d \u00b7 %s" % (item["no"], item["level"]), font=f_foot,
               fill=RED)
        tw = d.textlength(item["region"], font=f_foot)
        d.text((bx + lead_w - 7 - tw, y + lead_h - 13), item["region"],
               font=f_foot, fill=FAINT)
    y += lead_h + 4

    # ---- middle tier: 5 + 4 + 4 cards
    rows = [day.FEATURED[3:8], day.FEATURED[8:12], day.FEATURED[12:16]]
    card_h = 111
    for row in rows:
        n = len(row)
        cw = (x1 - x0 - (n - 1) * 8) / n
        for i, item in enumerate(row):
            bx = x0 + i * (cw + 8)
            d.rectangle([bx, y, bx + cw, y + card_h], fill=CARD_BG,
                        outline=CARD_LINE, width=1)
            SCENES[item["art"]](d, bx + 1, y + 1, bx + cw - 1, y + 43)
            _chip(d, bx + cw - 4, y + 5, item["chip"])
            f_head = typeface(SERIF_B, 14)
            hl = split_lines(d, item["head"], f_head, cw - 12)
            ty = draw_lines(d, hl[:2], bx + 6, y + 47, f_head, gap=0)
            # deck gets only the lines that fit above the footer line
            f_deck = typeface(SANS, 10)
            dl = split_lines(d, item["deck"], f_deck, cw - 12)
            room = (y + card_h - 11) - (ty + 1)
            n_deck = max(0, min(len(dl), room // 12))
            draw_lines(d, dl[:n_deck], bx + 6, ty + 1, f_deck, fill=FAINT,
                       gap=0)
            f_foot = typeface(SANS_B, 9)
            d.text((bx + 6, y + card_h - 11),
                   "%d \u00b7 %s" % (item["no"], item["level"]), font=f_foot,
                   fill=RED)
            tw = d.textlength(item["region"], font=f_foot)
            d.text((bx + cw - 6 - tw, y + card_h - 11), item["region"],
                   font=f_foot, fill=FAINT)
        y += card_h + 4

    # ---- map band
    d.text((x0, y), "WHERE IT HAPPENED \u2014 PIN NUMBERS MATCH STORY NUMBERS",
           font=typeface(SANS_B, 12), fill=RED)
    y += 12
    map_y0, map_y1 = y, y + 64
    inset = (x1 - 268, map_y0, x1, map_y1)
    main_box = (x0, map_y0, x1 - 276, map_y1)
    d.rectangle([x0, map_y0, x1, map_y1], fill=SKY, outline=CARD_LINE)
    paint_dots(d, main_box, -170, 190, -55, 75)
    d.text((x0 + 6, map_y1 - 14), "PACIFIC", font=typeface(SANS, 9),
           fill=FAINT)
    d.text((main_box[2] - 52, map_y1 - 14), "ATLANTIC",
           font=typeface(SANS, 9), fill=FAINT)
    inset_nos = {1, 2, 12, 15}
    for item in day.FEATURED:
        lon, lat = item["geo"]
        if item["no"] in inset_nos:
            continue
        px, py = geo_to_xy(lon, lat, main_box, -170, 190, -55, 75)
        dx, dy = PIN_PUSH.get(item["no"], (0, 0))
        if (dx, dy) != (0, 0):
            d.line([(px, py), (px + dx, py + dy)], fill=RED, width=1)
        paint_pin(d, px + dx, py + dy, item["no"])
    # Europe inset
    d.rectangle([inset[0], inset[1], inset[2], inset[3]], fill=SKY,
                outline=CARD_LINE, width=2)
    paint_dots(d, inset, -12, 38, 35, 62, step=6)
    d.text((inset[0] + 6, inset[1] + 4), "EUROPE \u2014 DETAIL",
           font=typeface(SANS_B, 10), fill=INK)
    for item in day.FEATURED:
        if item["no"] not in inset_nos:
            continue
        lon, lat = item["geo"]
        px, py = geo_to_xy(lon, lat, inset, -12, 38, 35, 62)
        paint_pin(d, px, py, item["no"])
    y = map_y1 + 6

    # ---- ALSO list, three columns
    d.text((x0, y), "ALSO ON FRIDAY 27 NOVEMBER",
           font=typeface(SANS_B, 12), fill=RED)
    y += 12
    f_also = typeface(SANS_B, 10)
    col_w = (x1 - x0) / 3
    for i, (num, head) in enumerate(day.BRIEFS):
        col = i % 3
        row = i // 3
        tx = x0 + col * col_w
        ty = y + row * 10
        label = "%d. %s" % (num, head)
        while d.textlength(label, font=f_also) > col_w - 6 and len(label) > 4:
            label = label[:-4] + "\u2026"
        d.text((tx, ty), label, font=f_also, fill=INK)
    y += 7 * 10 + 4
    hline(d, x0, x1, y)

    # ---- DATE CHECK
    y += 4
    d.text((x0, y), "DATE CHECK \u2014 EXCLUDED AS OTHER DAYS\u2019 NEWS",
           font=typeface(SANS_B, 12), fill=RED)
    y += 12
    f_dc_lab = typeface(SANS_B, 10)
    f_dc = typeface(SANS, 10)
    for label, text in day.DATECHECK:
        lw = d.textlength(label, font=f_dc_lab)
        d.text((x0, y), label, font=f_dc_lab, fill=RED)
        lines = split_lines(d, text, f_dc, (x1 - x0) - lw - 10)
        draw_lines(d, lines, x0 + lw + 8, y, f_dc, gap=0)
        y += max(1, len(lines)) * 11 + 1
    y += 2
    hline(d, x0, x1, y)

    # ---- legend + footnote
    y += 2
    f_leg = typeface(SANS, 10)
    tw = d.textlength(day.LEGEND, font=f_leg)
    d.text(((PAGE_W - tw) / 2, y), day.LEGEND, font=f_leg, fill=INK)
    y += 10
    tw = d.textlength(day.FOOTNOTE, font=f_leg)
    d.text(((PAGE_W - tw) / 2, y), day.FOOTNOTE, font=f_leg, fill=FAINT)
    print("layout ends at y=%d (page height %d)" % (y + 10, PAGE_H))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "page.png")
    img.save(out)
    print("wrote %s %d bytes" % (out, os.path.getsize(out)))


if __name__ == "__main__":
    build_page()
