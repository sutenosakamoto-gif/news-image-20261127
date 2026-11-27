# World News — 27 November 2026 (one-image summary)

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/sutenosakamoto-gif/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/sutenosakamoto-gif/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

A one-image broadsheet front page summarising thirty-seven world news
stories of Friday, 27 November 2026, prepared as an entry
for the make.fun bounty "Sum up 27 November's world news in one image"
(final deadline 2026-11-29 09:00 JST).

## Contents

- `main.py` — the entry point: a standard-library only program that
  copies the finished page to `/output/entry.png` (no network). It checks
  the page is a 1024×1024 PNG under the 1 MiB cap before copying.
- `page.png` — the finished 1024×1024 front page.
- `render.py` — the build-time renderer that drew `page.png` from
  `content.py` with real fonts (system Noto Serif, OFL).
- `content.py` — the day's stories, numbers, timeline and exclusions
  as structured data.
- `SOURCES.md` — the thirty-seven stories, their sources (outlet + date)
  and URLs.

## How to run

```bash
python3 main.py   # standard library only, no dependencies
```

Running `python3 main.py` copies `page.png` to `/output/entry.png`,
falling back to `./entry.png` next to the script when `/output` is not
writable. The render is deterministic: repeated runs produce identical
bytes.

To re-render the page from the structured content (build-time only,
needs PIL and the Noto fonts):

```bash
python3 render.py   # writes page.png
```

## The thirty-seven stories

Lead panels (large):

1. EU leaders end summit with no deal on budget or Ukraine loan
   (Reuters) — CONFIRMED
2. Drone crosses into Latvia as Russia downs 40-plus (Reuters) —
   CONFIRMED
3. China stocks jump as Beijing vows market support (Reuters) —
   CONFIRMED

Medium panels:

4. UN warns famine risks rising in 16 hotspots
5. China tests new Taiwan landing tactics
6. South Korea sends six North Koreans home
7. Black Friday after the nor'easter
8. Erdogan ratifies the Mecca defence pact
9. Brands shift $254m of garment orders out of Bangladesh
10. Indonesia nickel tycoon faces a treason claim
11. Iran warns on Gulf military presence
12. Marseille fan violence condemned; 11 hurt
13. Gavi restores malaria vaccine funding
14. Asian shares steady; dollar's third monthly gain
15. World Bank gives Ukraine $450m as EU loan stalls
16. Tokyo core inflation hits a 16-month high

Plus twenty-one briefs (17–37), a world map with numbered pins and a
Europe detail inset, a THE DAY IN NUMBERS strip, a UTC timeline, and a
DATE CHECK footer naming the stories excluded as other days' news —
including the Kuwait drone strike, the Gaza overnight strikes, the
Jazan refinery attack, the Trump–Putin post, the ECB chief pick and
the Lukoil sale, all 25–26 November substance.
