# Structured content for the 27 November 2026 world-news broadsheet.
# Every item verified against a dated 27 Nov 2026 wire/official source
# (see SOURCES.md). Certainty: CONFIRMED = wire reports the fact directly;
# OFFICIAL = official statement/statistics; REPORTED = wire reports it citing
# a source; CLAIM = one party's claim, attribution kept in the headline/body.
# DATING: 25-26 Nov substance (Kuwait strike, Gaza strikes, Jazan refinery,
# Trump-Putin post, ECB chief, Lukoil sale) is excluded from the featured
# tier and named in DATECHECK instead.

MASTHEAD = "THE DAY'S WORLD"
DATE_LINE = "FRIDAY 27 NOVEMBER 2026"
SUBHEAD = ("EU summit ends with no deal  \u00b7  A drone crosses into Latvia  "
           "\u00b7  China stocks jump 12%")
REGION_COUNTS = [("EUROPE", 5), ("ASIA-PACIFIC", 14), ("MIDDLE EAST", 3),
                 ("AFRICA", 3), ("NORTH AMERICA", 5), ("OCEANIA", 2),
                 ("GLOBAL", 5)]
TOTAL_STORIES = 37

# num, region, certainty, headline, body, chip, illustration kind, (lon, lat)
LEADS = [
    (1, "EUROPE", "CONFIRMED",
     "EU leaders end summit with no deal on budget or Ukraine loan",
     "24 of 27 back the \u20ac45bn loan; the \u20ac1.58tn budget moves to "
     "17\u201318 Dec. Day two cancelled.",
     "NO DEAL", "summit", (4.35, 50.85)),
    (2, "EUROPE", "CONFIRMED",
     "Drone crosses into Latvia as Russia downs 40-plus",
     "NATO member\u2019s airspace briefly violated in the early hours; "
     "alerts as Leningrad repels a raid.",
     "40+ DOWNED", "drone", (24.1, 56.95)),
    (3, "ASIA-PACIFIC", "CONFIRMED",
     "China stocks jump as Beijing vows market support",
     "Shanghai +3%, STAR 50 +12% after the cabinet promises new "
     "policies to steady markets.",
     "+12%", "bars", (121.5, 31.2)),
]

# num, region, certainty, headline, body, chip, illustration kind, (lon, lat)
MIDDLE = [
    (4, "GLOBAL", "OFFICIAL",
     "UN warns famine risks rising in 16 hotspots",
     "Sudan, South Sudan, Somalia, N. Nigeria and Yemen face the "
     "gravest threats.",
     "16 HOTSPOTS", "wheat", (32.5, 15.6)),
    (5, "ASIA-PACIFIC", "REPORTED",
     "China tests new Taiwan landing tactics",
     "Civilian ships linked as a floating bridge; drills run on in "
     "Dacheng Bay, 280 km away.",
     "280 KM", "bridge", (118.0, 24.0)),
    (6, "ASIA-PACIFIC", "OFFICIAL",
     "South Korea sends six North Koreans home",
     "Rescued from a drifting boat; a seventh chose to remain.",
     "6 SENT HOME", "boat", (129.0, 37.0)),
    (7, "NORTH AMERICA", "CONFIRMED",
     "Black Friday after the nor\u2019easter",
     "900,000 lost power at the peak; flood warnings into Friday; "
     "Macy\u2019s balloons re-inflated.",
     "900,000 OUT", "storm", (-74.0, 40.7)),
    (8, "MIDDLE EAST", "OFFICIAL",
     "Erdogan ratifies the Mecca defence pact",
     "Turkey completes ratification of the pact with Pakistan and "
     "Saudi Arabia.",
     "3 NATIONS", "flags", (32.9, 39.9)),
    (9, "ASIA-PACIFIC", "REPORTED",
     "Brands shift $254m of garment orders out of Bangladesh",
     "Zara and H&M move orders to India amid unrest; $400m+ in "
     "production losses.",
     "$254M", "factory", (90.4, 23.8)),
    (10, "ASIA-PACIFIC", "REPORTED",
     "Indonesia nickel tycoon faces a treason claim",
     "Official says Arif Kurniawan may have fled to China.",
     "TREASON?", "court", (106.8, -6.2)),
    (11, "MIDDLE EAST", "REPORTED",
     "Iran warns on Gulf military presence",
     "Tehran says a foreign presence would heighten tensions; Seoul "
     "readies a wider naval role.",
     "GULF", "ship", (51.0, 26.0)),
    (12, "EUROPE", "CONFIRMED",
     "Marseille fan violence condemned; 11 hurt",
     "French and Bulgarian leaders condemn Thursday\u2019s clashes.",
     "11 HURT", "stadium", (5.4, 43.3)),
    (13, "AFRICA", "CONFIRMED",
     "Gavi restores malaria vaccine funding",
     "$30m first payment to Dakar\u2019s Institut Pasteur for yellow "
     "fever vaccine work.",
     "$30M", "vial", (17.4, 14.7)),
    (14, "GLOBAL", "CONFIRMED",
     "Asian shares steady; dollar\u2019s third monthly gain",
     "Nikkei +0.7%, Kospi +2%, MSCI Asia ex-Japan +0.5% in a holiday "
     "lull.",
     "+0.7%", "line", (139.7, 35.7)),
    (15, "EUROPE", "REPORTED",
     "World Bank gives Ukraine $450m as EU loan stalls",
     "$415m IBRD loan backed by Japan, $35m IDA credit, to the "
     "general fund.",
     "$450M", "bank", (30.5, 50.4)),
    (16, "ASIA-PACIFIC", "OFFICIAL",
     "Tokyo core inflation hits a 16-month high",
     "Bolsters the case for a Bank of Japan hike as soon as next month.",
     "16-MO HIGH", "yen", (139.7, 35.7)),
]

# num, region, certainty, headline (kept short: ALSO lines), detail
ALSO = [
    (17, "MIDDLE EAST", "REPORTED",
     "Saudi condemns Kuwait strike; Iran denies role",
     "Arab condemnation published Friday; the strike was Thursday."),
    (18, "EUROPE", "CONFIRMED",
     "Europa League: Bournemouth 2-1 at Celta; Milan 4-2",
     "Plzen 4-0 Benfica; Besiktas tie halted 30 min after fan clashes."),
    (19, "OCEANIA", "CONFIRMED",
     "NZ 246/5 on day one of 2nd test v India",
     "Latham 59 and Blundell dig in at Christchurch."),
    (20, "ASIA-PACIFIC", "CONFIRMED",
     "Cambodia, Thailand agree site visit in sea row",
     "Visit to disputed islands in UN-backed proceedings."),
    (21, "ASIA-PACIFIC", "REPORTED",
     "Hetero nears India nod for generic HIV drug",
     "Lenacapavir launch expected in February."),
    (22, "AFRICA", "REPORTED",
     "Congo mobilises against mpox",
     "Communities mobilised in the Republic of the Congo."),
    (23, "ASIA-PACIFIC", "REPORTED",
     "AirAsia delays staff pay to month-end",
     "Delay runs November to March as cash is conserved."),
    (24, "ASIA-PACIFIC", "REPORTED",
     "Japan Tobacco +2% on Imperial takeover talk",
     "JT may partner on a bid for the UK cigarette maker."),
    (25, "AFRICA", "CONFIRMED",
     "Rand +1% to 17.37 as metals rally",
     "Early trade on Friday, up from the previous close."),
    (26, "GLOBAL", "CONFIRMED",
     "Dollar near 22-month peak; index 103.81",
     "Monday it hit 104.53, the highest since March last year."),
    (27, "NORTH AMERICA", "CONFIRMED",
     "US markets reopen for half-day Black Friday",
     "S&P futures +0.8%, Nasdaq futures +1% higher."),
    (28, "NORTH AMERICA", "CONFIRMED",
     "Macy\u2019s balloons re-inflated for Saturday",
     "The 100th parade starts 8:30 a.m. Saturday."),
    (29, "NORTH AMERICA", "CONFIRMED",
     "NJ Transit honours rail tickets on buses",
     "Cross-honouring runs Thursday and Friday."),
    (30, "GLOBAL", "CONFIRMED",
     "Euro flat at $1.0964; kiwi $0.5482",
     "Friday foreign-exchange levels."),
    (31, "GLOBAL", "CONFIRMED",
     "Brent $96.14, up 3.9% for the week",
     "First weekly rise in four; down 18% for the month."),
    (32, "ASIA-PACIFIC", "CONFIRMED",
     "Nikkei +0.7%; Kospi +2% on Friday",
     "Nikkei +2.7% for the week, still \u22128.4% for the month."),
    (33, "NORTH AMERICA", "CONFIRMED",
     "Two-year Treasury yield 4.6705%",
     "Cash market reopens after the US holiday."),
    (34, "ASIA-PACIFIC", "OFFICIAL",
     "China cabinet plans new market policies",
     "Dividends and buybacks pushed; stabilisation improved."),
    (35, "ASIA-PACIFIC", "REPORTED",
     "Seoul weighs wider navy role in Gulf of Oman",
     "Parliament reviews expanding the Cheonghae unit."),
    (36, "OCEANIA", "CONFIRMED",
     "Sandpapergate forum will not apportion blame",
     "Terms of reference published on Friday."),
    (37, "ASIA-PACIFIC", "REPORTED",
     "China factory slump seen lasting; PMI 49.4",
     "Forecast, second month in contraction."),
]

# (big figure, caption) — all 27 Nov figures
NUMBERS = [
    ("16", "HUNGER HOTSPOTS, UN"),
    ("+12%", "CHINA STAR 50 INDEX"),
    ("$96.14", "BRENT CRUDE, FRI"),
    ("40+", "DRONES DOWNED, LENINGRAD"),
    ("24/27", "EU STATES BACK UKRAINE LOAN"),
    ("6", "N. KOREANS SENT HOME"),
    ("$254M", "GARMENT ORDERS LEAVE DHAKA"),
]

# (UTC time label, event) — time order
TIMELINE = [
    ("EARLY HRS", "Drone crosses into Latvia"),
    ("01:41", "EU summit ends with no deal"),
    ("04:44", "Seoul sends six North Koreans home"),
    ("05:12", "Iran warns on Gulf military presence"),
    ("06:52", "Riyadh leads Kuwait-strike condemnation"),
    ("07:43", "Rand firms as metals rally"),
    ("07:51", "Paris, Sofia condemn Marseille violence"),
    ("AFTERNOON", "China stocks jump; STAR 50 +12%"),
]

# (day label, exclusion note)
DATECHECK = [
    ("THU 26 NOV",
     "Kuwait drone strike kills 2 Italians; Gaza strikes kill nine; "
     "Jazan refinery hit; coalition destroys 50 Houthi targets."),
    ("THU 26 NOV",
     "Trump tells Putin to pull back aggression; Hamas warns on Gaza; "
     "ECB chief de Cos named; EU summit opens."),
    ("THU 26 NOV",
     "Venezuela to repeal opposition-ban law; Machado launches "
     "assemblies; Caracas puts debt at $237.5bn."),
    ("WED 25 NOV",
     "Lukoil sale to Boehly group; Musk\u2019s two SpaceX shares per US "
     "child; Macy\u2019s parade move decided."),
    ("WED 25 NOV",
     "Section 301 tariffs; US PCE +3.8%, GDP 4.3%; Shenzhou-24 launch; "
     "Cairo tanker fire, 31 dead; UK energy cap +26%."),
    ("WED 25 NOV",
     "SpaceX FCC nod for 1m satellites; Venezuela\u2013Shell $400m deal; "
     "Dhaka garment wage rise."),
    ("TUE 24 NOV",
     "Sudan RSF drone strikes kill 19 in Blue Nile; Senegal win AFCON "
     "title back at CAS; Chile seeks Cuba tribunal."),
    ("MON 23 NOV",
     "DRC to halt all cobalt exports from 30 Nov until further notice."),
    ("NOT YET",
     "Spain election Sun 29 Nov; OPEC+ meetings 29 Nov; ITLOS Falklands "
     "ruling Sat 28 Nov; Macy\u2019s 100th parade Sat 28 Nov."),
]

LEGEND = ("CONFIRMED = 2+ outlets  \u00b7  OFFICIAL = on the record  \u00b7  "
          "REPORTED = one outlet  \u00b7  CLAIM = one side\u2019s account")
ILLU_NOTE = "Scenes are drawn illustrations, not photographs."
