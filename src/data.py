# -*- coding: utf-8 -*-
"""
SHARK — content data, separated from templates/markup.
All contact details, certifications, stats and history are intentionally
left as bracketed placeholders — nothing here is invented. Replace the
CONFIG placeholders once real details are confirmed.
"""

# ============================================================================
# SITE CONFIG — placeholders clearly marked. Swap these once confirmed.
# ============================================================================
CONFIG = {
    "site_name": "SHARK",
    "legal_name": "Shark Equipment Safety and Fire Trading – L.L.C – S.P.C",
    "tagline": "Fire & Safety Equipment Trading",
    # Placeholder domain — replace with the real registered domain once purchased.
    "domain": "www.sharksafety-uae.com",
    "base_url": "https://www.sharksafety-uae.com",
    "phone_display": "[PHONE NUMBER]",
    "phone_tel": "#",
    "whatsapp_display": "+971 56 133 9723",
    "whatsapp_digits": "971561339723",
    "whatsapp_message": "Hello SHARK, I would like to enquire about your fire and safety equipment.",
    "email": "[EMAIL ADDRESS]",
    "address_line": "[BUSINESS ADDRESS]",
    "address_city": "[EMIRATE], United Arab Emirates",
    "hours_weekday": "[BUSINESS HOURS — e.g. Sunday–Thursday, 9:00 AM–6:00 PM]",
    "hours_weekend": "[WEEKEND HOURS, IF APPLICABLE]",
    "map_embed": "",  # placeholder — add a Google Maps embed URL once the address is confirmed
}

def whatsapp_href(message=None):
    import urllib.parse
    msg = message or CONFIG["whatsapp_message"]
    return "https://wa.me/%s?text=%s" % (CONFIG["whatsapp_digits"], urllib.parse.quote(msg))

# ============================================================================
# NAVIGATION
# ============================================================================
NAV = [
    ("Home", "/index.html"),
    ("About", "/about.html"),
    ("Products", "/products.html"),
    ("Solutions", "/solutions.html"),
    ("Industries", "/industries.html"),
    ("Projects", "/applications.html"),
    ("Resources", "/resources.html"),
    ("Contact", "/contact.html"),
]

FOOTER_LINKS_COMPANY = [
    ("About SHARK", "/about.html"),
    ("Why SHARK", "/why-shark.html"),
    ("Industries", "/industries.html"),
    ("Applications", "/applications.html"),
    ("Resources", "/resources.html"),
    ("FAQ", "/faq.html"),
]
FOOTER_LINKS_PRODUCTS = [
    ("Fire Extinguishers", "/products.html?cat=extinguishers"),
    ("Fire Hoses & Reels", "/products.html?cat=hoses"),
    ("Fire Cabinets", "/products.html?cat=cabinets"),
    ("Fire Alarm Equipment", "/products.html?cat=alarms"),
    ("Emergency & Exit Lighting", "/products.html?cat=emergency-lighting"),
    ("Safety Equipment", "/products.html?cat=safety-equipment"),
]
FOOTER_LINKS_CONTACT = [
    ("Request a Quote", "/contact.html"),
    ("Solutions", "/solutions.html"),
    ("Contact SHARK", "/contact.html"),
]

# ============================================================================
# PRODUCT CATEGORIES (10 — canonical catalogue order)
# ============================================================================
PRODUCT_CATEGORIES = [
    {"key": "extinguishers", "num": "01", "name": "Fire Extinguishers",
     "desc": "Portable fire extinguishers for commercial, industrial and business environments."},
    {"key": "hoses", "num": "02", "name": "Fire Hoses",
     "desc": "Fire hoses built for reliable water and agent delivery in fire fighting applications."},
    {"key": "hose-reels", "num": "03", "name": "Hose Reels",
     "desc": "Fixed and swing-type hose reel units for fast first-response deployment."},
    {"key": "cabinets", "num": "04", "name": "Fire Cabinets",
     "desc": "Fire hose and equipment cabinets for organized, code-compliant equipment storage."},
    {"key": "hydrant", "num": "05", "name": "Fire Hydrant Equipment",
     "desc": "Hydrant valves, landing valves and coupling equipment for fire water networks."},
    {"key": "alarms", "num": "06", "name": "Fire Alarm Equipment",
     "desc": "Detection and alarm devices for early fire warning across facilities."},
    {"key": "emergency-lighting", "num": "07", "name": "Emergency Lighting",
     "desc": "Emergency and escape lighting to support safe evacuation during power loss."},
    {"key": "exit-signs", "num": "08", "name": "Exit Signs",
     "desc": "Illuminated and photoluminescent exit signage for clear evacuation routing."},
    {"key": "accessories", "num": "09", "name": "Fire Fighting Accessories",
     "desc": "Brackets, signage, tools and accessories that support fire equipment installations."},
    {"key": "safety-equipment", "num": "10", "name": "Safety Equipment",
     "desc": "General workplace safety equipment for facilities, warehouses and industrial sites."},
]
CAT_BY_KEY = {c["key"]: c for c in PRODUCT_CATEGORIES}

# Home page editorial category navigation (8 tiles — hoses/reels and
# emergency/exit lighting are paired, matching the homepage brief).
HOME_CATEGORIES = [
    {"key": "extinguishers", "title": "Fire Extinguishers",
     "desc": "Portable extinguishers for commercial, industrial and business use.",
     "link": "/products.html?cat=extinguishers"},
    {"key": "hoses", "title": "Fire Hoses & Hose Reels",
     "desc": "Hose lines and reel units for organized, fast first response.",
     "link": "/products.html?cat=hoses"},
    {"key": "cabinets", "title": "Fire Cabinets",
     "desc": "Code-conscious storage for hoses, extinguishers and accessories.",
     "link": "/products.html?cat=cabinets"},
    {"key": "hydrant", "title": "Fire Hydrant Equipment",
     "desc": "Valves and couplings for fire water distribution networks.",
     "link": "/products.html?cat=hydrant"},
    {"key": "alarms", "title": "Fire Alarm Equipment",
     "desc": "Detection and alarm devices for early warning systems.",
     "link": "/products.html?cat=alarms"},
    {"key": "emergency-lighting", "title": "Emergency & Exit Lighting",
     "desc": "Escape lighting and exit signage for safe evacuation.",
     "link": "/products.html?cat=emergency-lighting"},
    {"key": "accessories", "title": "Fire Fighting Accessories",
     "desc": "Brackets, tools and signage supporting fire equipment.",
     "link": "/products.html?cat=accessories"},
    {"key": "safety-equipment", "title": "Safety Equipment",
     "desc": "General workplace and industrial safety equipment.",
     "link": "/products.html?cat=safety-equipment"},
]

# ============================================================================
# PRODUCTS
# ============================================================================
def _p(slug, name, cat, short, overview, features, specs, applications, variants, image=None):
    return {"slug": slug, "name": name, "cat": cat, "short": short, "overview": overview,
            "features": features, "specs": specs, "applications": applications, "variants": variants,
            "image": image}

PRODUCTS = [
    _p("abc-dry-powder-fire-extinguisher", "ABC Dry Powder Fire Extinguisher", "extinguishers",
       "Multi-purpose dry powder extinguisher for Class A, B and C fire risks.",
       "A multi-purpose portable extinguisher intended for general commercial and industrial areas where "
       "solid, liquid and gas fire risks may all be present. Dry powder agent is discharged under pressure "
       "to knock down flame quickly across mixed-risk environments.",
       ["Suitable for Class A, B and C fire risk areas", "Pressure gauge for at-a-glance status checks",
        "Wall-bracket and stand-mount compatible", "Corrosion-resistant cylinder body",
        "Clear operating instructions on the label"],
       [("Agent Type", "Dry Chemical Powder (ABC)"), ("Fire Class", "A, B, C"),
        ("Capacity", "Specification available on request"), ("Mounting", "Wall bracket / floor stand"),
        ("Cylinder Finish", "Specification available on request")],
       ["Offices and commercial units", "Warehouses and storage areas", "Retail premises", "Construction sites"],
       ["Common capacities: 1kg, 2kg, 4kg, 6kg, 9kg — confirm current availability with our team"],
       image="/assets/img/products/abc-dry-powder-fire-extinguisher.png"),
    _p("co2-fire-extinguisher", "CO2 Fire Extinguisher", "extinguishers",
       "Clean-agent extinguisher suited to electrical and equipment fire risk.",
       "Carbon dioxide extinguishers discharge a clean, non-conductive gas agent that leaves no residue — "
       "a practical choice near electrical panels, server rooms and sensitive equipment.",
       ["Non-conductive discharge for electrical risk areas", "Leaves no residue on equipment",
        "Horn-style discharge nozzle", "Suitable for enclosed equipment spaces",
        "Compact cylinder profile"],
       [("Agent Type", "Carbon Dioxide (CO2)"), ("Fire Class", "B, C (electrical)"),
        ("Capacity", "Specification available on request"), ("Mounting", "Wall bracket / floor stand"),
        ("Discharge Type", "Horn nozzle")],
       ["Server and IT rooms", "Electrical switch rooms", "Workshops with machinery", "Commercial kitchens (non-cooking-oil equipment areas)"],
       ["Common capacities: 2kg, 5kg — confirm current availability with our team"],
       image="/assets/img/products/co2-fire-extinguisher.png"),
    _p("foam-fire-extinguisher", "Foam Fire Extinguisher", "extinguishers",
       "Foam-based extinguisher suited to flammable liquid and general fire risk.",
       "Foam extinguishers are effective against flammable liquid fires as well as general combustible "
       "material risk, forming a smothering blanket over the fire surface.",
       ["Effective on Class A and B fire risk", "Smothering foam blanket action",
        "Reduced re-ignition risk on liquid fires", "Wall-bracket and stand-mount compatible",
        "Corrosion-resistant cylinder body"],
       [("Agent Type", "AFFF Foam"), ("Fire Class", "A, B"),
        ("Capacity", "Specification available on request"), ("Mounting", "Wall bracket / floor stand"),
        ("Cylinder Finish", "Specification available on request")],
       ["Fuel and liquid storage areas", "Industrial facilities", "Car parks and workshops", "Warehousing"],
       ["Common capacities: 3 litre, 6 litre, 9 litre — confirm current availability with our team"],
       image="/assets/img/products/foam-fire-extinguisher.png"),
    _p("water-fire-extinguisher", "Water Fire Extinguisher", "extinguishers",
       "Water-based extinguisher for standard Class A combustible material risk.",
       "A straightforward water-jet or spray extinguisher for standard combustible material risk such as "
       "wood, paper, textiles and general solid materials.",
       ["Suitable for Class A fire risk", "Simple, reliable operation", "Wall bracket or stand mount",
        "Corrosion-resistant cylinder body", "Clear operating instructions on the label"],
       [("Agent Type", "Water (jet or spray)"), ("Fire Class", "A"),
        ("Capacity", "Specification available on request"), ("Mounting", "Wall bracket / floor stand"),
        ("Cylinder Finish", "Specification available on request")],
       ["Offices", "Hotels and hospitality areas", "Retail premises", "Educational and institutional buildings"],
       ["Common capacities: 6 litre, 9 litre — confirm current availability with our team"],
       image="/assets/img/products/water-fire-extinguisher.png"),

    _p("layflat-fire-hose", "Layflat Fire Hose", "hoses",
       "Flexible layflat hose for fire hydrant and hose reel water delivery.",
       "Layflat fire hose sections used to deliver water from hydrant or hose reel points to the point of "
       "application. Designed to lie flat for compact storage and unroll quickly when needed.",
       ["Flexible, compact-storage construction", "Coupling ends for hydrant/reel connection",
        "Abrasion-conscious outer layer", "Suitable for cabinet or reel storage",
        "Available in standard fire-service lengths"],
       [("Type", "Layflat delivery hose"), ("Coupling", "Specification available on request"),
        ("Length", "Specification available on request"), ("Diameter", "Specification available on request")],
       ["Fire hose cabinets", "Hydrant landing valve connections", "Construction site fire points", "Industrial fire points"],
       ["Common lengths: 15m, 30m sections — confirm current availability with our team"]),
    _p("rubber-lined-fire-hose", "Rubber-Lined Fire Hose", "hoses",
       "Reinforced rubber-lined hose for higher-duty fire fighting use.",
       "A reinforced rubber-lined hose construction intended for higher-duty fire fighting applications "
       "where durability and repeated use are priorities.",
       ["Reinforced multi-layer construction", "Built for repeated deployment", "Coupling-ready ends",
        "Suitable for hydrant and pump connections", "Available in standard fire-service lengths"],
       [("Type", "Rubber-lined delivery hose"), ("Coupling", "Specification available on request"),
        ("Length", "Specification available on request"), ("Diameter", "Specification available on request")],
       ["Industrial fire points", "Warehouse fire systems", "Construction site fire points", "Facility fire pump rooms"],
       ["Common lengths: 15m, 30m sections — confirm current availability with our team"]),
    _p("hose-coupling-set", "Hose Coupling Set", "hoses",
       "Coupling and connector sets for fire hose lines.",
       "Coupling components used to connect hose sections to hydrants, reels and branch pipes/nozzles as "
       "part of a complete fire hose line.",
       ["Compatible with standard layflat hose ends", "Durable metal construction",
        "Designed for repeated connect/disconnect use", "Available in standard fire-service sizes"],
       [("Type", "Instantaneous / threaded coupling"), ("Material", "Specification available on request"),
        ("Size", "Specification available on request")],
       ["Hose-to-hydrant connections", "Hose-to-branch pipe connections", "Fire pump room fittings"],
       ["Specification available on request"]),

    _p("swing-arm-hose-reel", "Swing-Arm Hose Reel", "hose-reels",
       "Wall-mounted swing-type hose reel for fast manual first response.",
       "A swing-arm hose reel unit mounted to a wall or recess, allowing the reel to pivot outward for "
       "quick, unobstructed hose deployment during first response.",
       ["Pivoting swing-arm bracket", "Continuous hose supply while in use", "Wall or recess mounting",
        "Manually operated shut-off valve", "Compact housing footprint"],
       [("Type", "Swing-arm hose reel"), ("Hose Length", "Specification available on request"),
        ("Mounting", "Wall / recessed"), ("Valve", "Manual shut-off")],
       ["Commercial building corridors", "Hotel and hospitality floors", "Retail premises", "Office buildings"],
       ["Specification available on request"]),
    _p("fixed-hose-reel", "Fixed Hose Reel", "hose-reels",
       "Fixed-position hose reel unit for straightforward manual deployment.",
       "A fixed hose reel unit designed for straightforward manual deployment in facilities where a "
       "pivoting arm is not required.",
       ["Fixed wall-mounted housing", "Continuous hose supply while in use", "Manually operated shut-off valve",
        "Compact housing footprint", "Straightforward maintenance access"],
       [("Type", "Fixed hose reel"), ("Hose Length", "Specification available on request"),
        ("Mounting", "Wall mounted"), ("Valve", "Manual shut-off")],
       ["Warehouses", "Industrial facilities", "Car parks", "Back-of-house commercial areas"],
       ["Specification available on request"]),
    _p("hose-reel-cabinet-unit", "Hose Reel Cabinet Unit", "hose-reels",
       "Enclosed cabinet housing for hose reel equipment.",
       "An enclosed cabinet housing that protects and presents hose reel equipment neatly within a "
       "building's fire-point locations.",
       ["Enclosed protective housing", "Clear signage-ready front face", "Wall or recessed mounting",
        "Designed for quick-access deployment", "Durable construction for daily environments"],
       [("Type", "Reel housing cabinet"), ("Mounting", "Wall / recessed"),
        ("Finish", "Specification available on request")],
       ["Commercial buildings", "Hotels", "Retail environments", "Office fire points"],
       ["Specification available on request"]),

    _p("single-door-hose-cabinet", "Single-Door Fire Hose Cabinet", "cabinets",
       "Single-door cabinet for hose, extinguisher and accessory storage.",
       "A single-door fire hose cabinet providing an organized, protected storage point for hose lines, "
       "extinguishers and related fire fighting accessories at a designated fire point.",
       ["Single hinged access door", "Organized internal layout", "Wall-mounted installation",
        "Signage-ready front panel", "Durable construction for daily building use"],
       [("Configuration", "Single door"), ("Mounting", "Wall mounted"),
        ("Dimensions", "Specification available on request"), ("Finish", "Specification available on request")],
       ["Corridor fire points", "Stairwell landings", "Warehouse fire points", "Commercial building common areas"],
       ["Specification available on request"]),
    _p("double-door-hose-cabinet", "Double-Door Fire Hose Cabinet", "cabinets",
       "Larger double-door cabinet for combined hose and extinguisher storage.",
       "A double-door fire hose cabinet suited to locations that combine hose reel storage with additional "
       "extinguisher or accessory space in a single fire point.",
       ["Double hinged access doors", "Increased internal storage capacity", "Wall-mounted installation",
        "Signage-ready front panel", "Durable construction for daily building use"],
       [("Configuration", "Double door"), ("Mounting", "Wall mounted"),
        ("Dimensions", "Specification available on request"), ("Finish", "Specification available on request")],
       ["Large commercial floors", "Industrial facilities", "Multi-equipment fire points", "Warehousing"],
       ["Specification available on request"]),
    _p("recessed-fire-cabinet", "Recessed Fire Cabinet", "cabinets",
       "Recessed-mount cabinet for a flush, low-profile fire point.",
       "A recessed-mount cabinet designed to sit flush within a wall cavity, keeping corridors and public "
       "areas clear while still providing quick access to fire equipment.",
       ["Flush recessed installation", "Low-profile corridor footprint", "Signage-ready front panel",
        "Organized internal layout", "Durable construction for daily building use"],
       [("Configuration", "Recessed"), ("Mounting", "Recessed wall cavity"),
        ("Dimensions", "Specification available on request"), ("Finish", "Specification available on request")],
       ["Hotels", "Office towers", "Retail corridors", "Residential and mixed-use buildings"],
       ["Specification available on request"]),

    _p("hydrant-landing-valve", "Hydrant Landing Valve", "hydrant",
       "Landing valve for fire hydrant riser connections.",
       "A landing valve installed at hydrant riser outlets, allowing fire hose lines to be connected for "
       "water delivery during fire fighting operations.",
       ["Standard hydrant riser connection", "Durable valve body construction",
        "Manual operation handwheel", "Coupling-ready outlet"],
       [("Type", "Landing valve"), ("Connection", "Specification available on request"),
        ("Material", "Specification available on request")],
       ["Building hydrant risers", "Stairwell fire points", "Industrial fire water networks"],
       ["Specification available on request"]),
    _p("hydrant-standpipe-equipment", "Hydrant Standpipe Equipment", "hydrant",
       "Standpipe components for fire water riser systems.",
       "Standpipe system components used to carry water from a supply point up through a building or "
       "site's fire fighting riser network.",
       ["Riser-compatible construction", "Coupling-ready connections", "Durable valve and pipe fittings",
        "Supports multi-floor hydrant systems"],
       [("Type", "Standpipe / riser component"), ("Material", "Specification available on request")],
       ["Multi-storey buildings", "Industrial sites", "Construction site fire risers"],
       ["Specification available on request"]),
    _p("fire-hydrant-coupling", "Fire Hydrant Coupling", "hydrant",
       "Coupling components for hydrant-to-hose connections.",
       "Coupling components used to connect delivery hoses to hydrant outlets and landing valves as part "
       "of a fire water network.",
       ["Compatible with standard hydrant outlets", "Durable metal construction",
        "Designed for repeated connect/disconnect use"],
       [("Type", "Hydrant coupling"), ("Material", "Specification available on request"),
        ("Size", "Specification available on request")],
       ["Hydrant outlet connections", "Fire pump room fittings", "Site fire water points"],
       ["Specification available on request"]),

    _p("addressable-smoke-detector", "Addressable Smoke Detector", "alarms",
       "Point smoke detector for addressable fire alarm systems.",
       "A point-type smoke detector designed for integration into an addressable fire alarm system, "
       "providing early detection at ceiling or void level.",
       ["Point-type smoke sensing", "Addressable system compatible", "Low-profile ceiling mount",
        "Status indicator LED"],
       [("Type", "Addressable smoke detector"), ("Mounting", "Ceiling"),
        ("Compatibility", "Specification available on request")],
       ["Offices", "Commercial buildings", "Warehouses", "Hotel guest floors"],
       ["Specification available on request"]),
    _p("conventional-heat-detector", "Conventional Heat Detector", "alarms",
       "Heat detector for conventional fire alarm zones.",
       "A heat-sensing detector suited to conventional fire alarm zone wiring, intended for areas where "
       "heat rise is a more reliable trigger than smoke.",
       ["Heat-rise / fixed-temperature sensing", "Conventional zone wiring compatible",
        "Ceiling-mounted housing", "Status indicator LED"],
       [("Type", "Heat detector"), ("Mounting", "Ceiling"),
        ("System Type", "Conventional")],
       ["Kitchens and plant rooms", "Warehouses", "Car parks", "Industrial areas"],
       ["Specification available on request"]),
    _p("fire-alarm-manual-call-point", "Fire Alarm Manual Call Point", "alarms",
       "Manual break-glass call point for raising a fire alarm.",
       "A manual call point allowing building occupants to raise the fire alarm directly, typically "
       "positioned along escape routes.",
       ["Break-glass / resettable operation", "Positioned along escape routes",
        "Compatible with addressable or conventional panels", "Clear signage-ready housing"],
       [("Type", "Manual call point"), ("Mounting", "Wall mounted, escape route height"),
        ("System Type", "Specification available on request")],
       ["Corridors and stairwells", "Building entrances/exits", "Warehouses", "Commercial floors"],
       ["Specification available on request"]),

    _p("led-emergency-bulkhead", "LED Emergency Bulkhead Light", "emergency-lighting",
       "Maintained/non-maintained emergency bulkhead light.",
       "An LED emergency bulkhead fitting that activates on mains power failure, supporting safe movement "
       "through corridors and stairwells during an evacuation.",
       ["LED light source", "Maintained / non-maintained operation modes",
        "Backup battery activation on power loss", "Wall or ceiling mounting"],
       [("Light Source", "LED"), ("Operation", "Maintained / non-maintained"),
        ("Duration", "Specification available on request")],
       ["Corridors", "Stairwells", "Car parks", "Back-of-house areas"],
       ["Specification available on request"]),
    _p("emergency-exit-bulkhead", "Emergency Exit Bulkhead Light", "emergency-lighting",
       "Combined exit-route bulkhead light for escape corridors.",
       "A combined bulkhead-style light fitting positioned along an escape route to maintain visibility "
       "of the path of travel during an emergency.",
       ["LED light source", "Escape-route optimized beam", "Backup battery activation on power loss",
        "Wall or ceiling mounting"],
       [("Light Source", "LED"), ("Operation", "Maintained / non-maintained"),
        ("Duration", "Specification available on request")],
       ["Escape corridors", "Stairwells", "Assembly areas", "Warehouse aisles"],
       ["Specification available on request"]),

    _p("led-exit-sign-single-side", "LED Exit Sign — Single Sided", "exit-signs",
       "Illuminated single-sided exit sign for directional guidance.",
       "An illuminated single-sided exit sign used to mark evacuation routes and final exit doors clearly, "
       "even in low-light conditions.",
       ["LED illumination", "Maintained / non-maintained operation modes",
        "Wall or ceiling mounting", "Clear pictogram-based signage"],
       [("Light Source", "LED"), ("Orientation", "Single sided"),
        ("Duration", "Specification available on request")],
       ["Final exit doors", "Corridors", "Retail floors", "Office buildings"],
       ["Specification available on request"]),
    _p("led-exit-sign-double-side", "LED Exit Sign — Double Sided", "exit-signs",
       "Illuminated double-sided exit sign for corridor and junction visibility.",
       "A double-sided illuminated exit sign suited to corridor junctions and open areas where the "
       "direction of travel needs to be visible from more than one side.",
       ["LED illumination", "Maintained / non-maintained operation modes",
        "Ceiling suspended or wall mounting", "Clear pictogram-based signage"],
       [("Light Source", "LED"), ("Orientation", "Double sided"),
        ("Duration", "Specification available on request")],
       ["Corridor junctions", "Open floor plates", "Warehouses", "Assembly halls"],
       ["Specification available on request"]),

    _p("fire-blanket", "Fire Blanket", "accessories",
       "Fire blanket for small fire smothering and personal protection.",
       "A compact fire blanket used to smother small fires or to wrap around a person as protection during "
       "an evacuation.",
       ["Quick-release storage pouch/case", "Suitable for small fire smothering",
        "Compact wall-mounted housing", "Simple pull-and-deploy operation"],
       [("Type", "Fire blanket"), ("Storage", "Wall-mounted case"),
        ("Size", "Specification available on request")],
       ["Commercial kitchens", "Laboratories", "Offices", "Workshops"],
       ["Specification available on request"]),
    _p("fire-extinguisher-stand", "Fire Extinguisher Stand", "accessories",
       "Free-standing stand for extinguisher placement.",
       "A free-standing floor stand for positioning a fire extinguisher clearly and accessibly where wall "
       "mounting is not practical.",
       ["Free-standing floor placement", "Stable base construction",
        "Compatible with standard extinguisher sizes", "Signage-ready design"],
       [("Type", "Floor stand"), ("Compatibility", "Standard extinguisher cylinders")],
       ["Warehouses", "Car parks", "Construction sites", "Open floor areas"],
       ["Specification available on request"]),
    _p("fire-safety-signage-set", "Fire Safety Signage Set", "accessories",
       "Signage set for fire equipment locations and escape routes.",
       "A set of fire safety signage used to mark extinguisher points, hose reel locations, assembly "
       "points and escape route directions clearly across a facility.",
       ["Photoluminescent or rigid signage options", "Pictogram-based, clear identification",
        "Suitable for indoor use", "Supports code-conscious equipment marking"],
       [("Type", "Fire safety signage"), ("Material", "Specification available on request")],
       ["Fire point identification", "Escape route marking", "Assembly point marking", "Equipment location signage"],
       ["Specification available on request"]),

    _p("industrial-safety-helmet", "Industrial Safety Helmet", "safety-equipment",
       "Head protection for industrial and construction environments.",
       "A protective safety helmet intended for general industrial and construction site head protection "
       "requirements.",
       ["Adjustable internal harness", "Impact-resistant shell", "Ventilated design options",
        "Lightweight for extended wear"],
       [("Type", "Industrial safety helmet"), ("Adjustment", "Ratchet / adjustable harness")],
       ["Construction sites", "Industrial facilities", "Warehouses", "Maintenance work"],
       ["Specification available on request"]),
    _p("high-visibility-safety-vest", "High-Visibility Safety Vest", "safety-equipment",
       "High-visibility vest for site and facility safety.",
       "A high-visibility vest supporting worker visibility across construction sites, warehouses and "
       "operational facilities.",
       ["High-visibility fabric with reflective strips", "Adjustable/breathable fit options",
        "Suitable for day and low-light conditions"],
       [("Type", "High-visibility vest"), ("Sizing", "Specification available on request")],
       ["Construction sites", "Warehouses", "Logistics yards", "Facility maintenance teams"],
       ["Specification available on request"]),
    _p("safety-gloves", "Industrial Safety Gloves", "safety-equipment",
       "General-purpose protective gloves for facility and industrial tasks.",
       "General-purpose protective gloves suited to facility maintenance, handling and general industrial "
       "tasks where hand protection is required.",
       ["Grip-enhanced palm construction", "General handling and maintenance use",
        "Available across general sizing"],
       [("Type", "Industrial safety gloves"), ("Sizing", "Specification available on request")],
       ["Warehousing", "Facility maintenance", "Industrial handling tasks", "Construction sites"],
       ["Specification available on request"]),
]
PRODUCTS_BY_SLUG = {p["slug"]: p for p in PRODUCTS}

def products_in(cat_key, exclude_slug=None, limit=None):
    items = [p for p in PRODUCTS if p["cat"] == cat_key and p["slug"] != exclude_slug]
    return items[:limit] if limit else items

FEATURED_SLUGS = [
    "abc-dry-powder-fire-extinguisher", "swing-arm-hose-reel",
    "single-door-hose-cabinet", "led-exit-sign-single-side",
]

# ============================================================================
# INDUSTRIES
# ============================================================================
INDUSTRIES = [
    {"key": "construction", "name": "Construction",
     "summary": "Active construction sites carry constantly changing fire risk as work progresses.",
     "requirements": ["Site fire points at active work areas", "Temporary and permanent equipment as phases progress",
                       "Equipment that can be relocated as the site develops"],
     "equipment": ["extinguishers", "hoses", "safety-equipment", "accessories"]},
    {"key": "commercial-buildings", "name": "Commercial Buildings",
     "summary": "Office towers and mixed-use commercial buildings need consistent, well-presented fire equipment across common areas.",
     "requirements": ["Corridor and lobby fire points", "Consistent equipment presentation across floors",
                       "Cabinet and signage coordination with interior finishes"],
     "equipment": ["extinguishers", "cabinets", "hose-reels", "exit-signs"]},
    {"key": "facilities-management", "name": "Facilities Management",
     "summary": "FM teams manage fire equipment across multiple buildings and need dependable, straightforward supply.",
     "requirements": ["Consistent equipment specification across sites", "Reliable replenishment for consumable items",
                       "Clear product information for asset records"],
     "equipment": ["extinguishers", "alarms", "emergency-lighting", "cabinets"]},
    {"key": "industrial", "name": "Industrial Facilities",
     "summary": "Industrial sites often combine higher fire load with process-specific hazards.",
     "requirements": ["Equipment suited to process and material risk", "Durable equipment for demanding environments",
                       "Hydrant and hose infrastructure for larger footprints"],
     "equipment": ["extinguishers", "hydrant", "hoses", "safety-equipment"]},
    {"key": "warehousing", "name": "Warehousing",
     "summary": "Large floor plates and high-value stock make fast-response equipment placement important.",
     "requirements": ["Wide-coverage extinguisher and hose reel placement", "Equipment suited to racking and aisle layouts",
                       "Durable housings for high-traffic environments"],
     "equipment": ["extinguishers", "hose-reels", "hoses", "safety-equipment"]},
    {"key": "hospitality", "name": "Hospitality",
     "summary": "Hotels and hospitality venues need equipment that performs reliably while fitting guest-facing spaces.",
     "requirements": ["Cabinet and signage design suited to interiors", "Coverage across guest floors and back-of-house",
                       "Kitchen and back-of-house specific equipment"],
     "equipment": ["extinguishers", "cabinets", "exit-signs", "emergency-lighting"]},
    {"key": "retail", "name": "Retail",
     "summary": "Retail spaces need equipment that is accessible without disrupting the customer experience.",
     "requirements": ["Low-profile or recessed equipment options", "Clear signage for staff and customers",
                       "Coverage across sales floor and stockroom"],
     "equipment": ["extinguishers", "exit-signs", "cabinets", "accessories"]},
    {"key": "offices", "name": "Offices",
     "summary": "Office environments prioritize clean presentation alongside dependable coverage.",
     "requirements": ["Consistent placement across floors", "Equipment that fits modern office interiors",
                       "Simple, clear signage for occupants"],
     "equipment": ["extinguishers", "exit-signs", "emergency-lighting", "alarms"]},
    {"key": "property-management", "name": "Property Management",
     "summary": "Property managers oversee fire equipment across portfolios of owned or managed buildings.",
     "requirements": ["Standardized specification across a portfolio", "Dependable long-term supply relationship",
                       "Clear documentation to support building records"],
     "equipment": ["extinguishers", "cabinets", "alarms", "emergency-lighting"]},
]
IND_BY_KEY = {i["key"]: i for i in INDUSTRIES}

# ============================================================================
# WHY SHARK — principles (no invented stats)
# ============================================================================
WHY_PRINCIPLES = [
    {"n": "01", "title": "Quality-Focused",
     "text": "We select equipment on the basis of build quality and suitability for the environment it will serve."},
    {"n": "02", "title": "Reliable Supply",
     "text": "Straightforward sourcing and stock handling so equipment reaches you when your project or facility needs it."},
    {"n": "03", "title": "Professional Support",
     "text": "Our team helps identify the right equipment for your requirement, not just the closest match on a list."},
    {"n": "04", "title": "Customer-First Approach",
     "text": "We work around your enquiry, quantity and timeline rather than a fixed, one-size-fits-all process."},
]
WHY_SHARK_LONG = [
    {"title": "Professional Product Selection",
     "text": "We take the time to understand what an environment actually requires before recommending equipment — matching product type to the risk and setting rather than defaulting to a single catalogue line."},
    {"title": "Reliable Supply",
     "text": "Business enquiries need dependable turnaround. We aim to keep the sourcing and supply process clear and straightforward from enquiry to delivery."},
    {"title": "Clear Communication",
     "text": "Procurement and facilities teams deal with enough ambiguity. We keep quotes, product information and timelines as clear as possible."},
    {"title": "B2B Focus",
     "text": "SHARK is built around business, project and facility requirements — not one-off retail counter sales."},
    {"title": "Responsive Support",
     "text": "Whether the enquiry arrives by phone, WhatsApp or the contact form, our team follows up to understand what's needed."},
    {"title": "Safety-Conscious Approach",
     "text": "Fire and safety equipment exists to protect people and property. We treat every enquiry with that in mind, not as a routine transaction."},
]

# ============================================================================
# FAQ
# ============================================================================
FAQS = [
    ("What fire safety equipment do you supply?",
     "SHARK supplies a range of fire fighting and safety equipment including fire extinguishers, fire hoses "
     "and hose reels, fire cabinets, fire hydrant equipment, fire alarm equipment, emergency and exit "
     "lighting, fire fighting accessories and general safety equipment. See our Products page for the full catalogue."),
    ("How can I request a quotation?",
     "You can request a quotation through the form on our Contact page, by WhatsApp, or by phone. Share the "
     "product, quantity and any project details and our team will follow up with pricing information."),
    ("Do you supply commercial projects?",
     "Yes. SHARK supplies fire and safety equipment for commercial, industrial and business requirements, "
     "including bulk and project-based enquiries."),
    ("Do you supply fire extinguishers?",
     "Yes. We supply a range of fire extinguisher types, including dry powder, CO2, foam and water "
     "extinguishers, suited to different fire risk categories."),
    ("Do you handle bulk requirements?",
     "Yes. We work with facility managers, contractors and businesses that need equipment supplied in bulk "
     "quantities for buildings, sites or ongoing projects."),
    ("How can I contact SHARK?",
     "You can reach SHARK by phone, WhatsApp or email, or by submitting a request through our Contact page. "
     "Full contact details are listed on the Contact page."),
    ("Which areas do you serve?",
     "SHARK operates within the UAE market. Please contact our team directly to confirm supply to your "
     "specific location."),
]

# ============================================================================
# RESOURCES / ARTICLES
# ============================================================================
ARTICLES = [
    {"slug": "fire-extinguisher-basics", "tag": "Equipment Guide", "art": "extinguishers",
     "title": "Fire Extinguisher Basics: What Every Facility Should Know",
     "excerpt": "A practical overview of how portable fire extinguishers work and why equipment type matters.",
     "body": [
        ("h2", "Why extinguisher type matters"),
        ("p", "Not every fire behaves the same way, and not every extinguisher agent is suited to every fire risk. "
              "Facilities typically encounter a mix of risk types across offices, storage areas, kitchens and "
              "plant rooms — which is why extinguisher selection is treated as a per-area decision rather than "
              "a single blanket choice."),
        ("h3", "Common fire classifications"),
        ("p", "Fires are broadly grouped by the type of material or risk involved: solid combustible materials "
              "like wood, paper and textiles; flammable liquids; flammable gases; and fires involving live "
              "electrical equipment. Understanding which risks are present in a given area is the starting "
              "point for choosing appropriate equipment."),
        ("h3", "Placement and accessibility"),
        ("p", "Beyond the extinguisher itself, where and how it's mounted matters. Equipment should be clearly "
              "visible, unobstructed, and positioned along natural routes of travel so it can be reached quickly "
              "if needed."),
        ("h3", "Working with a supplier"),
        ("p", "A good starting point when equipping or re-equipping a facility is to walk through each area with "
              "your supplier and identify the risk profile before finalizing equipment type and quantity."),
     ]},
    {"slug": "types-of-fire-extinguishers", "tag": "Equipment Guide", "art": "extinguishers",
     "title": "Types of Fire Extinguishers Explained",
     "excerpt": "An overview of dry powder, CO2, foam and water extinguisher types and where each is typically used.",
     "body": [
        ("h2", "The main extinguisher agent types"),
        ("p", "Portable fire extinguishers are generally categorized by the extinguishing agent they contain. "
              "Each agent type is suited to different combinations of fire risk."),
        ("h3", "Dry powder (ABC)"),
        ("p", "Multi-purpose dry powder extinguishers are commonly used in general commercial and industrial "
              "spaces where a mix of solid, liquid and gas fire risks may be present."),
        ("h3", "CO2 (carbon dioxide)"),
        ("p", "CO2 extinguishers discharge a clean, non-conductive gas, making them a common choice near "
              "electrical panels, server rooms and sensitive equipment where residue is a concern."),
        ("h3", "Foam"),
        ("p", "Foam extinguishers are effective on flammable liquid fires as well as general combustible "
              "material risk, forming a smothering layer across the fire surface."),
        ("h3", "Water"),
        ("p", "Water-based extinguishers are suited to standard combustible material risk such as wood, paper "
              "and textiles, and are common in general office and hospitality environments."),
     ]},
    {"slug": "fire-safety-equipment-guide", "tag": "Equipment Guide", "art": "cabinets",
     "title": "A Practical Guide to Core Fire Safety Equipment",
     "excerpt": "How extinguishers, hose reels, cabinets, alarms and emergency lighting work together as a system.",
     "body": [
        ("h2", "Fire safety equipment as a system"),
        ("p", "Individual pieces of fire safety equipment work best when considered as part of a coordinated "
              "system rather than in isolation — detection, first response, evacuation support and clear "
              "signage all play a role."),
        ("h3", "Detection and alarm"),
        ("p", "Smoke and heat detectors, together with manual call points, are typically the first stage — "
              "identifying a fire risk early and alerting occupants."),
        ("h3", "First response equipment"),
        ("p", "Extinguishers and hose reels give occupants or first responders a way to address a fire in its "
              "early stages, where safe and appropriate to do so."),
        ("h3", "Evacuation support"),
        ("p", "Emergency lighting and exit signage support safe movement toward assembly points, particularly "
              "if mains power is lost during an incident."),
        ("h3", "Storage and presentation"),
        ("p", "Fire cabinets keep hoses, extinguishers and accessories organized, protected and clearly "
              "identifiable at each fire point."),
     ]},
    {"slug": "emergency-lighting-basics", "tag": "Equipment Guide", "art": "emergency-lighting",
     "title": "Emergency Lighting Basics",
     "excerpt": "What emergency and exit lighting does, and why consistent coverage matters along escape routes.",
     "body": [
        ("h2", "What emergency lighting does"),
        ("p", "Emergency lighting activates automatically when mains power is lost, maintaining visibility "
              "along escape routes so occupants can move safely toward an exit."),
        ("h3", "Maintained vs non-maintained"),
        ("p", "Maintained fittings stay illuminated continuously, while non-maintained fittings activate only "
              "when mains power fails. The right choice depends on the space and how it's normally used."),
        ("h3", "Coverage along the escape route"),
        ("p", "Consistent lighting coverage — rather than isolated fittings — helps ensure there are no dark "
              "gaps along a corridor or stairwell during an evacuation."),
        ("h3", "Exit signage"),
        ("p", "Illuminated or photoluminescent exit signs work alongside emergency lighting to clearly mark the "
              "direction of travel toward the nearest safe exit."),
     ]},
    {"slug": "fire-hose-reel-basics", "tag": "Equipment Guide", "art": "hose-reels",
     "title": "Fire Hose Reel Basics",
     "excerpt": "How fixed and swing-arm hose reels are typically used, and where they fit alongside extinguishers.",
     "body": [
        ("h2", "What a hose reel is for"),
        ("p", "A fire hose reel provides a continuous water supply for first response, typically used where a "
              "sustained water application is more suitable than a portable extinguisher."),
        ("h3", "Fixed vs swing-arm"),
        ("p", "Fixed hose reels are mounted directly to a wall, while swing-arm units pivot outward from a "
              "recess or cabinet, which can make initial deployment more straightforward in tighter spaces."),
        ("h3", "Where hose reels are commonly used"),
        ("p", "Hose reels are common in corridors, warehouses, car parks and industrial facilities — locations "
              "where a connected water supply is available and sustained coverage is useful."),
        ("h3", "Working alongside extinguishers"),
        ("p", "Hose reels typically complement, rather than replace, portable extinguishers as part of a "
              "building's overall first-response equipment."),
     ]},
    {"slug": "workplace-fire-safety", "tag": "Safety Awareness", "art": "safety-equipment",
     "title": "Workplace Fire Safety: A Practical Starting Point",
     "excerpt": "General, practical considerations for keeping fire safety equipment ready and accessible.",
     "body": [
        ("h2", "Keeping equipment ready"),
        ("p", "Fire safety equipment is only useful if it's accessible, visible and in working order. A few "
              "practical habits go a long way toward keeping a workplace prepared."),
        ("h3", "Keep access clear"),
        ("p", "Extinguishers, hose reels and cabinets should never be blocked by stock, furniture or equipment "
              "— even temporarily."),
        ("h3", "Check visibility and signage"),
        ("p", "Equipment should be clearly signed and easy to locate, especially for staff or visitors unfamiliar "
              "with the building layout."),
        ("h3", "Review as the space changes"),
        ("p", "As a facility's layout, stock or use changes, it's worth reviewing whether existing equipment "
              "placement and types still match the current risk profile."),
        ("h3", "Work with your supplier"),
        ("p", "A supplier who understands your facility can help identify gaps or equipment that needs "
              "replacing or repositioning as your requirements evolve."),
     ]},
]
ARTICLES_BY_SLUG = {a["slug"]: a for a in ARTICLES}

# ============================================================================
# APPLICATIONS (replaces fabricated "Projects")
# ============================================================================
APPLICATIONS = [
    {"key": "commercial", "title": "Commercial Buildings",
     "text": "Equipping office towers and mixed-use buildings with extinguishers, cabinets, exit signage and emergency lighting across common areas."},
    {"key": "industrial", "title": "Industrial Facilities",
     "text": "Supplying extinguishers, hydrant equipment and hose lines suited to process areas, plant rooms and production floors."},
    {"key": "construction", "title": "Construction Sites",
     "text": "Providing fire points and safety equipment that can be positioned and relocated as a site progresses through its phases."},
    {"key": "warehouse", "title": "Warehousing & Logistics",
     "text": "Covering large floor plates and racking layouts with extinguishers, hose reels and general safety equipment."},
    {"key": "hospitality", "title": "Hospitality",
     "text": "Supplying equipment that fits guest-facing interiors while covering back-of-house and kitchen areas."},
    {"key": "retail", "title": "Retail",
     "text": "Fitting sales floors and stockrooms with accessible, clearly signed fire safety equipment."},
]

# ============================================================================
# ABOUT PAGE CONTENT
# ============================================================================
ABOUT_BLOCKS = {
    "overview": "SHARK Equipment Safety and Fire Trading is a UAE-based supplier of fire fighting and safety "
                "equipment, registered for the retail sale of safety and fire fighting equipment and devices. "
                "We work with businesses, contractors and facility teams to supply the equipment their premises "
                "and projects require.",
    "approach": "Our approach starts with understanding the space and the risk it presents, then matching "
                "equipment type, quantity and configuration to that requirement — rather than offering a single "
                "standard package regardless of setting.",
    "supply": "We supply core fire fighting and safety equipment categories including fire extinguishers, fire "
              "hoses and hose reels, fire cabinets, fire hydrant equipment, fire alarm equipment, emergency and "
              "exit lighting, fire fighting accessories and general safety equipment.",
    "serve": "We work with facility managers, procurement and operations teams, safety officers, MEP "
             "contractors, construction companies, facilities and property management companies, and building, "
             "warehouse, hospitality and retail operators across the UAE.",
    "quality": "We select the equipment we supply with attention to build quality and suitability for its "
               "intended environment, and we're transparent about specification — where a detail isn't yet "
               "confirmed, we say so rather than guess.",
    "support": "Enquiries can reach us by phone, WhatsApp, email or through our contact form. Our team follows "
               "up to understand product, quantity and timeline before confirming a quotation.",
}
