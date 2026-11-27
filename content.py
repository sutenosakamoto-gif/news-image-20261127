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
            "\u00b7  China stocks jump 12%")

REGION_TALLY = [("EUROPE", 5), ("ASIA-PACIFIC", 14), ("MIDDLE EAST", 3),
                ("AFRICA", 3), ("NORTH AMERICA", 5), ("OCEANIA", 2),
                ("GLOBAL", 5)]
STORY_TOTAL = 37

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
    {"no": 3, "region": "ASIA-PACIFIC", "level": "CONFIRMED",
     "head": "China stocks jump as Beijing vows market support",
     "deck": "Shanghai +3%, STAR 50 +12% as Beijing vows support.",
     "chip": "+12%", "art": "bars", "geo": (121.5, 31.2)},
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
    {"no": 6, "region": "ASIA-PACIFIC", "level": "OFFICIAL",
     "head": "South Korea sends six North Koreans home",
     "deck": "Rescued from a drifting boat; a seventh chose to remain.",
     "chip": "6 SENT HOME", "art": "boat", "geo": (129.0, 37.0)},
    {"no": 7, "region": "NORTH AMERICA", "level": "CONFIRMED",
     "head": "Black Friday after the nor\u2019easter",
     "deck": ("900,000 lost power at the peak; flood warnings into "
              "Friday."),
     "chip": "900,000 OUT", "art": "storm", "geo": (-74.0, 40.7)},
    {"no": 8, "region": "MIDDLE EAST", "level": "OFFICIAL",
     "head": "Erdogan ratifies the Mecca defence pact",
     "deck": "Pact with Pakistan and Saudi Arabia; ratified 5 Nov.",
     "chip": "3 NATIONS", "art": "pact", "geo": (39.8, 21.4)},
    {"no": 9, "region": "ASIA-PACIFIC", "level": "REPORTED",
     "head": "Brands shift $254m of garment orders",
     "deck": ("From Bangladesh to India amid unrest; $400m+ production "
              "losses."),
     "chip": "$254M", "art": "garment", "geo": (90.4, 23.8)},
    {"no": 10, "region": "ASIA-PACIFIC", "level": "REPORTED",
     "head": "Indonesia nickel tycoon faces treason claim",
     "deck": "Official says Arif Kurniawan may have fled to China.",
     "chip": "TREASON?", "art": "gavel", "geo": (106.8, -6.2)},
    {"no": 11, "region": "MIDDLE EAST", "level": "REPORTED",
     "head": "Iran warns on Gulf military presence",
     "deck": "Tehran says a foreign presence would heighten tensions.",
     "chip": "GULF", "art": "ship", "geo": (56.0, 26.0)},
    {"no": 12, "region": "EUROPE", "level": "CONFIRMED",
     "head": "Marseille fan violence condemned; 11 hurt",
     "deck": "French and Bulgarian leaders condemn Thursday\u2019s clashes.",
     "chip": "11 HURT", "art": "pitch", "geo": (5.4, 43.3)},
    {"no": 13, "region": "AFRICA", "level": "CONFIRMED",
     "head": "Gavi restores malaria vaccine funding",
     "deck": "$30m first payment to Dakar\u2019s Institut Pasteur.",
     "chip": "$30M", "art": "vial", "geo": (-17.4, 14.7)},
    {"no": 14, "region": "GLOBAL", "level": "CONFIRMED",
     "head": "Asian shares steady; dollar\u2019s third monthly gain",
     "deck": "Nikkei +0.7%, Kospi +2%, MSCI Asia ex-Japan +0.5%.",
     "chip": "+0.7%", "art": "candles", "geo": (114.2, 22.3)},
    {"no": 15, "region": "EUROPE", "level": "REPORTED",
     "head": "World Bank gives Ukraine $450m as EU loan stalls",
     "deck": "$415m IBRD loan backed by Japan, $35m IDA credit.",
     "chip": "$450M", "art": "bank", "geo": (30.5, 50.4)},
    {"no": 16, "region": "ASIA-PACIFIC", "level": "OFFICIAL",
     "head": "Tokyo core inflation hits a 16-month high",
     "deck": "Bolsters the case for a BoJ hike as soon as next month.",
     "chip": "16-MO HIGH", "art": "yen", "geo": (139.7, 35.7)},
]

# Briefs: number and one headline line each.
BRIEFS = [
    (17, "SAUDI CONDEMNS KUWAIT STRIKE; IRAN DENIES ROLE"),
    (18, "EUROPA LEAGUE: BOURNEMOUTH 2-1 AT CELTA; MILAN 4-2"),
    (19, "NZ 246/5 ON DAY ONE OF 2ND TEST v INDIA"),
    (20, "CAMBODIA, THAILAND AGREE SITE VISIT IN SEA ROW"),
    (21, "HETERO NEARS INDIA NOD FOR GENERIC HIV DRUG"),
    (22, "CONGO MOBILISES AGAINST MPOX"),
    (23, "AIRASIA DELAYS STAFF PAY TO MONTH-END, NOV\u2013MAR"),
    (24, "JAPAN TOBACCO +2% ON IMPERIAL BRANDS TALK"),
    (25, "RAND +1% TO 17.37 AS METALS RALLY"),
    (26, "DOLLAR NEAR 22-MONTH PEAK; INDEX 103.81"),
    (27, "US MARKETS REOPEN FOR HALF-DAY BLACK FRIDAY"),
    (28, "MACY\u2019S BALLOONS RE-INFLATED FOR SATURDAY"),
    (29, "NJ TRANSIT HONOURS RAIL TICKETS ON BUSES"),
    (30, "EURO FLAT AT $1.0964; KIWI $0.5482"),
    (31, "BRENT $96.14, +3.9% FOR THE WEEK"),
    (32, "NIKKEI +0.7% FRI; KOSPI +2%"),
    (33, "TWO-YEAR TREASURY YIELD 4.6705%"),
    (34, "CHINA CABINET PLANS NEW MARKET POLICIES"),
    (35, "SEOUL WEIGHS WIDER NAVY ROLE IN GULF OF OMAN"),
    (36, "SANDPAPERGATE FORUM WILL NOT APPORTION BLAME"),
    (37, "CHINA FACTORY SLUMP SEEN LASTING; PMI 49.4"),
]

# Emblematic figures for the numbers strip: big value, small caption.
FIGURES = [
    ("16", "HUNGER HOTSPOTS"),
    ("+12%", "CHINA STAR 50 INDEX"),
    ("$96.14", "BRENT CRUDE, FRI"),
    ("40+", "DRONES DOWNED"),
    ("24 of 27", "EU BACKS UKRAINE LOAN"),
    ("6", "N. KOREANS SENT HOME"),
    ("$254M", "GARMENT ORDERS"),
]

# The day in time order. Times are UTC.
TIMELINE = [
    ("EARLY HRS", "Drone crosses into Latvia"),
    ("01:41", "EU summit ends with no deal"),
    ("04:44", "Seoul sends six North Koreans home"),
    ("05:12", "Iran warns on Gulf military presence"),
    ("06:52", "Riyadh leads Kuwait-strike condemnation"),
    ("07:43", "Rand firms as metals rally"),
    ("07:51", "Paris, Sofia condemn Marseille violence"),
    ("AFTERNOON", "China stocks jump: STAR 50 +12%"),
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
]

LEGEND = ("CONFIRMED = 2+ outlets  \u00b7  OFFICIAL = on the record  \u00b7  "
          "REPORTED = one outlet  \u00b7  CLAIM = one side\u2019s account")
FOOTNOTE = "Scenes are drawn illustrations, not photographs."
