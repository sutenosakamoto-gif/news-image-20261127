# Day file for the 27 November 2026 world-news broadsheet.
# Every fact below is taken from STORYLIST.md / SOURCES.md, themselves
# verified against dated 27 Nov 2026 wire or official sources.
# Certainty: CONFIRMED = a wire reports the fact directly;
# OFFICIAL = an official statement or statistic; REPORTED = a wire
# reports it citing a source; CLAIM = one party's claim, with the
# attribution kept inside the headline or deck.
# DATING: substance from 25-26 Nov (Kuwait strike, Gaza strikes, Jazan
# refinery, Trump-Putin post, ECB chief, Lukoil sale) is excluded from
# the featured tier and named in DATECHECK instead.

PAPER_NAME = "THE DAY'S WORLD"
DAY_LINE = "FRIDAY 27 NOVEMBER 2026"
DEK_LINE = ("EU summit ends with no deal  \u00b7  A drone crosses into Latvia  "
            "\u00b7  Wall Street\u2019s best week in a year")

REGION_TALLY = [("EUROPE", 9), ("ASIA-PACIFIC", 13), ("MIDDLE EAST", 5),
                ("AFRICA", 4), ("NORTH AMERICA", 3), ("OCEANIA", 1),
                ("LATIN AMERICA", 2), ("GLOBAL", 6)]
STORY_TOTAL = 43

# Each featured item: number, region, certainty, headline, deck (two
# short lines), chip text for the picture, picture kind, map position
# as (longitude, latitude).
FEATURED = [
    {"no": 1, "region": "EUROPE", "level": "CONFIRMED",
     "head": "EU leaders end summit with no deal on budget or Ukraine loan",
     "deck": "24 of 27 back the \u20ac45bn loan; budget to 17\u201318 Dec.",
     "chip": "NO DEAL", "art": "summit", "geo": (4.35, 50.85)},
    {"no": 2, "region": "EUROPE", "level": "CONFIRMED",
     "head": "Drone crosses into Latvia as Russia downs 40-plus",
     "deck": "Early-hours violation; Leningrad downs 40+ drones.",
     "chip": "40+ DOWNED", "art": "drone", "geo": (24.1, 56.95)},
    {"no": 3, "region": "NORTH AMERICA", "level": "CONFIRMED",
     "head": "Wall Street jumps to its best week in over a year",
     "deck": "S&P 500 +1.6% to 7,297.49; Nasdaq +2.3%, Dow +1.2%.",
     "chip": "BEST WEEK +5.6%", "art": "bars", "geo": (-74.0, 40.7)},
    {"no": 4, "region": "GLOBAL", "level": "OFFICIAL",
     "head": "UN warns famine risks rising in 16 hotspots",
     "deck": ("Sudan, S. Sudan, Somalia, N. Nigeria, Yemen at gravest "
              "risk."),
     "chip": "16 HOTSPOTS", "art": "wheat", "geo": (32.5, 15.6)},
    {"no": 5, "region": "ASIA-PACIFIC", "level": "REPORTED",
     "head": "China tests new Taiwan landing tactics",
     "deck": ("Civilian ships linked as a bridge; drills in Dacheng Bay, "
              "280 km away."),
     "chip": "280 KM", "art": "bridge", "geo": (118.0, 24.0)},
    {"no": 6, "region": "ASIA-PACIFIC", "level": "CONFIRMED",
     "head": "China stocks jump as Beijing vows market support",
     "deck": "Shanghai +3%, STAR 50 +12% as Beijing vows support.",
     "chip": "+12%", "art": "bars", "geo": (121.5, 31.2)},
    {"no": 7, "region": "NORTH AMERICA", "level": "CONFIRMED",
     "head": "Black Friday after the nor\u2019easter",
     "deck": ("900,000 lost power at the peak; flood warnings into "
              "Friday."),
     "chip": "900,000 OUT", "art": "storm", "geo": (-71.0, 42.4)},
    {"no": 8, "region": "MIDDLE EAST", "level": "OFFICIAL",
     "head": "Erdogan ratifies the Mecca defence pact",
     "deck": "Pact with Pakistan and Saudi Arabia; ratified 5 Nov.",
     "chip": "3 NATIONS", "art": "pact", "geo": (39.8, 21.4)},
    {"no": 9, "region": "ASIA-PACIFIC", "level": "REPORTED",
     "head": "Brands shift $254m of garment orders",
     "deck": ("From Bangladesh to India amid unrest; $400m+ production "
              "losses."),
     "chip": "$254M", "art": "garment", "geo": (90.4, 23.8)},
    {"no": 10, "region": "ASIA-PACIFIC", "level": "OFFICIAL",
     "head": "Beijing plans new market-support policies",
     "deck": "Cabinet to push dividends, buybacks; stabilisation steps.",
     "chip": "NEW POLICIES", "art": "bank", "geo": (116.4, 39.9)},
    {"no": 11, "region": "EUROPE", "level": "CONFIRMED",
     "head": "Nine Ukrainian children return from Russia",
     "deck": "Melania Trump mediated; 2,875 children brought home in all.",
     "chip": "9 CHILDREN HOME", "art": "boat", "geo": (31.3, 51.5)},
    {"no": 12, "region": "EUROPE", "level": "CONFIRMED",
     "head": "Russia fires 155 drones at Ukraine overnight",
     "deck": "110 downed, hits at 27 sites; Estonia scrambles NATO jets.",
     "chip": "155 DRONES", "art": "drone", "geo": (35.2, 47.8)},
    {"no": 13, "region": "AFRICA", "level": "CONFIRMED",
     "head": "Gavi restores malaria vaccine funding",
     "deck": "$30m first payment to Dakar\u2019s Institut Pasteur.",
     "chip": "$30M", "art": "vial", "geo": (-17.4, 14.7)},
    {"no": 14, "region": "LATIN AMERICA", "level": "CONFIRMED",
     "head": "Brazil markets rally as Lula taps bank chief",
     "deck": "Real +4.7%, Bovespa +3.9% on market-friendly pick.",
     "chip": "REAL +4.7%", "art": "candles", "geo": (-46.6, -23.5)},
    {"no": 15, "region": "EUROPE", "level": "REPORTED",
     "head": "World Bank gives Ukraine $450m as EU loan stalls",
     "deck": "$415m IBRD loan backed by Japan, $35m IDA credit.",
     "chip": "$450M", "art": "bank", "geo": (30.5, 50.4)},
    {"no": 16, "region": "ASIA-PACIFIC", "level": "OFFICIAL",
     "head": "Tokyo core inflation hits a 16-month high",
     "deck": "Bolsters the case for a BoJ hike as soon as next month.",
     "chip": "16-MO HIGH", "art": "yen", "geo": (139.7, 35.7)},
]

# Briefs: number and one headline line each. Stage 2 (28 Nov): five
# stage-1 briefs dropped (Congo mpox, Japan Tobacco, Macy's balloons,
# NJ Transit, Sandpapergate), the China cabinet item promoted to the
# featured tier, four featured items demoted into this list, market
# briefs updated to Friday closes, and eight late wire stories added.
BRIEFS = [
    (17, "IRAQ PM MOVES TO REIN IN ARMED GROUPS"),
    (18, "EUROPA LEAGUE: BOURNEMOUTH 2-1 AT CELTA; MILAN 4-2"),
    (19, "ARMED MEN KILL 17 IN NIGERIA\u2019S PLATEAU STATE"),
    (20, "CAMBODIA, THAILAND AGREE SITE VISIT IN SEA ROW"),
    (21, "DOLLAR INDEX 104.04, NEAR 22-MONTH PEAK"),
    (22, "SAUDI CONDEMNS KUWAIT STRIKE; IRAN DENIES ROLE"),
    (23, "SEOUL SENDS SIX NORTH KOREANS HOME"),
    (24, "KENYA CULT LEADER CONVICTED OVER 123 MORE DEATHS"),
    (25, "EIGHT DEAD ON MIGRANT BOAT OFF CANARY ISLANDS"),
    (26, "THANKSGIVING ONLINE SALES $37.2BN, +4.6%"),
    (27, "HETERO NEARS INDIA NOD FOR GENERIC HIV DRUG"),
    (28, "US NAVY DISABLES SHIP BREAKING IRAN BLOCKADE"),
    (29, "AIRASIA DELAYS STAFF PAY TO MONTH-END, NOV\u2013MAR"),
    (30, "MARSEILLE FAN VIOLENCE CONDEMNED; 11 HURT"),
    (31, "EURO $1.0933; KIWI $0.5482"),
    (32, "NIKKEI +0.7%; KOSPI +2%; MSCI ASIA EX-JAPAN +0.5%"),
    (33, "TWO-YEAR TREASURY YIELD 4.6705%"),
    (34, "IRAN WARNS ON GULF MILITARY PRESENCE"),
    (35, "INDONESIA NICKEL TYCOON FACES TREASON CLAIM"),
    (36, "RAND +1% TO 17.37 AS METALS RALLY"),
    (37, "SPAIN PARTIES MAKE FINAL PITCH BEFORE SUNDAY VOTE"),
    (38, "BRENT $96.14, +3.9% FOR THE WEEK"),
    (39, "SEOUL WEIGHS WIDER NAVY ROLE IN GULF OF OMAN"),
    (40, "ARGENTINA BANS CENTRAL BANK PRINTING FOR GOVT"),
    (41, "NZ 246/5 ON DAY ONE OF 2ND TEST v INDIA"),
    (42, "CPTPP TALKS: UAE, INDONESIA, PHILIPPINES IN QUEUE"),
    (43, "CHINA PMI SEEN AT 49.4 (POLL); DATA DUE NOV 30"),
]

# Emblematic figures for the numbers strip: big value, small caption.
FIGURES = [
    ("16", "HUNGER HOTSPOTS"),
    ("+12%", "CHINA STAR 50 INDEX"),
    ("$96.14", "BRENT CRUDE, FRI"),
    ("40+", "DRONES DOWNED"),
    ("24 of 27", "EU BACKS UKRAINE LOAN"),
    ("+1.6%", "S&P 500, BEST WEEK SINCE APR 2025"),
    ("$254M", "GARMENT ORDERS"),
]

# Stage-2 implementation note: the two-year Treasury yield of 4.6705%
# could not be confirmed as Friday's close (half-day session); it is
# kept as the near-close figure carried over from stage 1.

# The day in time order. Times are UTC.
TIMELINE = [
    ("EARLY HRS", "Drone crosses into Latvia"),
    ("OVERNIGHT", "Russia fires 155 drones at Ukraine"),
    ("01:41", "EU summit ends with no deal"),
    ("04:44", "Seoul sends six North Koreans home"),
    ("05:12", "Iran warns on Gulf military presence"),
    ("06:52", "Riyadh leads Kuwait-strike condemnation"),
    ("07:43", "Rand firms as metals rally"),
    ("07:51", "Paris, Sofia condemn Marseille violence"),
    ("AFTERNOON", "China stocks jump: STAR 50 +12%"),
    ("14:04", "Nine Ukrainian children return home"),
    ("18:00", "Wall Street closes: S&P +1.6%"),
]

# Dated exclusions: day label, then what happened and why it is not
# presented as 27 Nov news.
DATECHECK = [
    ("THU 26 NOV",
     "Kuwait strike kills 2 Italians; Gaza strikes kill 9; Jazan refinery "
     "hit, 1 Nepalese worker killed; 50 Houthi targets destroyed."),
    ("THU 26 NOV",
     "Trump tells Putin to pull back (Truth Social); Hamas warns on Gaza; "
     "ECB chief de Cos named; EU summit opens; Venezuela moves; Machado "
     "launches assemblies; Caracas debt $237.5bn."),
    ("WED 25 NOV",
     "Lukoil sale; Musk\u2019s two SpaceX shares per US child; Macy\u2019s "
     "parade move decided; Section 301 tariffs; US PCE +3.8%, GDP 4.3%."),
    ("WED 25 NOV",
     "Shenzhou-24 launch; Cairo tanker fire, 31 dead; UK energy cap +26%; "
     "SpaceX FCC nod; Venezuela\u2013Shell $400m; Dhaka garment wage rise."),
    ("TUE 24 NOV",
     "Sudan RSF strikes kill 19; Senegal win AFCON title back at CAS; "
     "Chile seeks Cuba tribunal; DRC cobalt halt (Mon 23 Nov)."),
    ("NOT YET",
     "Spain election Sun 29 Nov; OPEC+ 29 Nov; ITLOS Falklands ruling "
     "Sat 28 Nov; Macy\u2019s 100th parade Sat 28 Nov."),
    ("SAT 28 NOV",
     "NZ cricket day two; Peru helicopter crash, 8 killed; Halk TV "
     "takeover; Gaza clinic strike; Bronson Reed dies \u2014 all 28 Nov, "
     "not 27 Nov."),
    ("UNVERIFIED",
     "Trump\u2013Rutte wording claim; Nvidia credit watch \u2014 not used."),
]

LEGEND = ("CONFIRMED = 2+ outlets  \u00b7  OFFICIAL = on the record  \u00b7  "
          "REPORTED = one outlet  \u00b7  CLAIM = one side\u2019s account")
FOOTNOTE = "Scenes are drawn illustrations, not photographs."
