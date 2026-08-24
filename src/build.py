# -*- coding: utf-8 -*-
"""SHARK — static site generator. Run: python3 build.py"""
import os, sys, shutil, json
sys.path.insert(0, os.path.dirname(__file__))

import data, templates as T, icons

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")

def write(rel_path, html):
    full = os.path.join(DIST, rel_path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", rel_path)

def org_schema():
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": data.CONFIG["legal_name"],
        "url": data.CONFIG["base_url"],
        "logo": data.CONFIG["base_url"] + "/assets/img/shark-mark.svg",
        "description": "Fire and safety equipment supplier in the UAE.",
    })

# ============================================================================
# HOME
# ============================================================================
def build_home():
    cats = data.HOME_CATEGORIES
    cat_tiles = []
    for i, c in enumerate(cats):
        icon = icons.CATEGORY.get(c["key"], "")
        cat_tiles.append(f'''<a href="{c['link']}" class="cat-tile reveal">
      <span class="cat-index">{str(i+1).zfill(2)}</span>
      <div class="cat-icon">{icon}</div>
      <div class="cat-name">{c['title']}</div>
      <div class="cat-desc">{c['desc']}</div>
      <div class="cat-link">Explore Products {icons.UI['arrow-right']}</div>
    </a>''')

    featured_html = "\n".join(T.feature_product(data.PRODUCTS_BY_SLUG[s]) for s in data.FEATURED_SLUGS)

    principle_html = "\n".join(f'''<div class="principle reveal">
      <div class="num">{p['n']}</div>
      <h3>{p['title']}</h3>
      <p>{p['text']}</p>
    </div>''' for p in data.WHY_PRINCIPLES)

    ind_rows = "\n".join(f'''<a href="/industries.html#{ind['key']}" class="industry-row reveal">
      <div class="idx">{str(i+1).zfill(2)}</div>
      <h3>{ind['name']}</h3>
      <div class="meta">{ind['summary']}</div>
      <div class="arrow">{icons.UI['arrow-right']}</div>
    </a>''' for i, ind in enumerate(data.INDUSTRIES))

    faq_html = "\n".join(T.faq_item(q, a, open_first=(i==0)) for i, (q, a) in enumerate(data.FAQS[:6]))

    wa = data.whatsapp_href()

    # Hero background slider — 4 clean fire-safety photographs, one full-bleed
    # image at a time, auto-advancing with a slow crossfade + subtle zoom.
    # Desktop/tablet focal points target where the equipment sits in each
    # photo; mobile crops are tuned separately via .hero-slide:nth-child in
    # style.css so the subject stays framed on a taller, narrower viewport.
    hero_slides_data = [
        "20% 42%",
        "28% 55%",
        "68% 52%",
        "62% 40%",
    ]
    hero_slides = []
    for i, pos in enumerate(hero_slides_data):
        n = i + 1
        active_cls = " active" if i == 0 else ""
        loading_attrs = 'fetchpriority="high" loading="eager"' if i == 0 else 'loading="lazy"'
        hero_slides.append(f'''<div class="hero-slide{active_cls}" data-slide="{n}">
        <picture>
          <source srcset="/assets/img/hero-slide-{n}.webp" type="image/webp">
          <img src="/assets/img/hero-slide-{n}.jpg" alt="" {loading_attrs} decoding="async" style="object-position:{pos};">
        </picture>
      </div>''')
    hero_slides_html = "\n      ".join(hero_slides)
    hero_dots_html = "\n        ".join(
        f'<span class="dot{" active" if i == 0 else ""}" data-dot="{i+1}"></span>' for i in range(4)
    )

    # Hero eyebrow — small red brand line above the H1. Split into one <span>
    # per character (left-to-right, staggered animation-delay) for a clean
    # left-aligned typing/reveal effect. Total reveal ~1.8s, plays once on
    # load; reduced-motion visitors get the sitewide override that collapses
    # animation-duration/delay to ~0, so it just appears instantly for them.
    import html as _html
    hero_eyebrow_text = "SHARK · Fire & Safety Equipments"
    HERO_EYEBROW_TOTAL_S = 1.8
    _n_chars = len(hero_eyebrow_text)
    _step = HERO_EYEBROW_TOTAL_S / max(_n_chars, 1)
    hero_eyebrow_chars = "".join(
        f'<span class="ch" style="animation-delay:{i * _step:.3f}s">{_html.escape(ch) if ch != " " else "&nbsp;"}</span>'
        for i, ch in enumerate(hero_eyebrow_text)
    )

    # Main hero heading — premium word-by-word "curtain" reveal: each word is
    # masked (overflow hidden) and slides up into view, left to right, one
    # after another. Replaces the plain fade used elsewhere in the hero.
    HERO_WORD_STEP_S = 0.07
    HERO_WORD_START_S = 0.1
    _word_i = [0]
    def _hero_word(w):
        i = _word_i[0]; _word_i[0] += 1
        delay = HERO_WORD_START_S + i * HERO_WORD_STEP_S
        return f'<span class="hero-word"><span style="animation-delay:{delay:.3f}s">{_html.escape(w)}</span></span>'
    hero_h1_html = (
        f'{_hero_word("FIRE")} {_hero_word("&")} {_hero_word("SAFETY")} {_hero_word("EQUIPMENT.")}<br>'
        f'{_hero_word("BUILT")} {_hero_word("AROUND")} <em>{_hero_word("PROTECTION.")}</em>'
    )

    body = f'''
  <section class="hero">
    <div class="hero-slider" aria-hidden="true" id="heroSlider">
      {hero_slides_html}
      <div class="hero-slider-overlay"></div>
    </div>
    <div class="container-wide">
      <div class="hero-copy">
        <div class="eyebrow on-dark hero-eyebrow" aria-label="{_html.escape(hero_eyebrow_text)}"><span aria-hidden="true">{hero_eyebrow_chars}</span></div>
        <h1 class="hero-heading">{hero_h1_html}</h1>
        <p class="hero-sub">Professional fire fighting and safety equipment for commercial, industrial and
          business requirements across the UAE.</p>
        <div class="hero-actions">
          {T.btn("Request a Quote", "/contact.html", "primary")}
          {T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")}
        </div>
        <div class="hero-dots" aria-hidden="true">
          {hero_dots_html}
        </div>
      </div>
    </div>
    <div class="hero-strip">
      <div class="container-wide" style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px;">
        <span class="tag">FIRE SAFETY EQUIPMENT</span>
        <span>COMMERCIAL <span class="sep">&bull;</span> INDUSTRIAL <span class="sep">&bull;</span> PROFESSIONAL</span>
      </div>
    </div>
  </section>

  <section class="pad-lg">
    <div class="container">
      {T.section_head("Product Categories", "FIRE PROTECTION, MADE PRACTICAL.",
        "Browse equipment by category to find what a space or project requires &mdash; from first-response tools to full fire-point setups.")}
    </div>
    <div class="cat-strip">
      {"".join(cat_tiles)}
    </div>
  </section>

  <section class="pad-lg">
    <div class="container">
      {T.section_head("Featured Equipment", "EQUIPMENT BUILT FOR THE JOB.",
        "A selection from our catalogue across core categories. Full technical detail and current availability on request.")}
      <div style="display:flex;flex-direction:column;gap:1px;background:var(--paper-dim);">
        {featured_html}
      </div>
      <div style="text-align:center;margin-top:48px;">
        {T.btn("View Full Catalogue", "/products.html", "dark")}
      </div>
    </div>
  </section>

  <section class="on-dark">
    <div class="container" style="padding-top:96px;">
      {T.section_head("Why SHARK", "SUPPLY YOU CAN DEPEND ON.", "", center=False)}
    </div>
    <div class="principle-row">
      {principle_html}
    </div>
    <div style="height:96px;"></div>
  </section>

  <section class="pad-lg">
    <div class="container">
      {T.section_head("Industries", "EQUIPMENT MATCHED TO THE ENVIRONMENT.",
        "SHARK supplies across a range of UAE business sectors, each with its own equipment priorities.")}
      <div class="industry-list">
        {ind_rows}
      </div>
    </div>
  </section>

  {T.cta_banner("NEED THE RIGHT FIRE &amp; SAFETY EQUIPMENT?",
    "Send us your requirement and our team will help you identify the right equipment for your application.",
    [T.btn("Request a Quote", "/contact.html", "primary"),
     T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")])}

  <section class="pad-lg">
    <div class="container split">
      <div class="reveal">
        <div class="eyebrow">About SHARK</div>
        <h2 style="font-size:clamp(26px,3.6vw,38px);margin-top:14px;line-height:1.15;">Professional equipment.
          Straightforward supply.</h2>
        <p class="muted" style="margin-top:20px;font-size:16px;line-height:1.75;">{data.ABOUT_BLOCKS['overview']}</p>
        <div style="margin-top:32px;">{T.btn("About SHARK", "/about.html", "outline")}</div>
      </div>
      <div class="visual reveal">
        <div class="grid-overlay" style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:32px 32px;"></div>
        <div style="position:absolute;inset:0;color:#3a3d42;">{icons.PRODUCT_ART['safety-equipment']}</div>
      </div>
    </div>
  </section>

  <section class="pad-lg" style="background:var(--paper-dim);">
    <div class="container">
      {T.section_head("Frequently Asked", "QUESTIONS, ANSWERED.", "", split_html=T.btn("View All FAQs", "/faq.html", "outline", icon="arrow-right"))}
      <div class="faq-list" style="max-width:820px;">
        {faq_html}
      </div>
    </div>
  </section>

  {T.cta_banner("LET&rsquo;S TALK ABOUT YOUR REQUIREMENT.",
    "Whatever the size of the enquiry, our team is ready to help you specify the right fire and safety equipment.",
    [T.btn("Request a Quote", "/contact.html", "primary"),
     T.btn("Contact SHARK", "/contact.html", "outline-light")], extra_class="alt")}
'''
    hero_preload = '<link rel="preload" as="image" href="/assets/img/hero-slide-1.jpg" fetchpriority="high">'
    write("/index.html", T.page(
        "SHARK | Fire &amp; Safety Equipment Supplier in the UAE",
        "SHARK supplies fire fighting and safety equipment for commercial, industrial and business "
        "requirements across the UAE — fire extinguishers, hose reels, cabinets, alarms and more.",
        "/index.html", body, schema_json=org_schema(), preload_html=hero_preload))

# ============================================================================
# ABOUT
# ============================================================================
def build_about():
    ab = data.ABOUT_BLOCKS
    wa = data.whatsapp_href()

    def visual(art_key, tone="#3a3d42"):
        return f'''<div class="visual reveal">
          <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:32px 32px;"></div>
          <div style="position:absolute;inset:0;color:{tone};">{icons.PRODUCT_ART.get(art_key,'')}</div>
        </div>'''

    supply_grid = "\n".join(f'''<div class="reveal" style="display:flex;align-items:center;gap:14px;padding:18px 0;border-bottom:1px solid var(--paper-dim);">
        <div class="cat-icon" style="width:44px;height:44px;margin:0;">{icons.CATEGORY.get(c['key'],'')}</div>
        <div style="font-family:var(--font-head);font-weight:700;font-size:15px;">{c['name']}</div>
      </div>''' for c in data.PRODUCT_CATEGORIES)

    audiences = ["Facility Managers", "Procurement Managers", "Operations Managers", "Safety Officers",
                 "MEP Contractors", "Construction Companies", "Facilities Management Companies",
                 "Property Management Companies", "Building Owners", "Warehouse Operators",
                 "Industrial Companies", "Hotels", "Restaurants", "Retail Businesses", "Offices",
                 "Commercial Property Owners"]
    audience_chips = "\n".join(f'<span class="chip" style="cursor:default;">{a}</span>' for a in audiences)

    body = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("About", None)])}
      <h1>PROTECTION STARTS WITH<br>THE RIGHT EQUIPMENT.</h1>
      <p>{ab['overview']}</p>
    </div>
  </section>

  <section class="pad-lg">
    <div class="container split">
      <div class="reveal">
        <div class="eyebrow">Company Overview</div>
        <h2 style="font-size:clamp(24px,3.2vw,34px);margin-top:14px;">Who SHARK is.</h2>
        <p class="muted" style="margin-top:20px;font-size:16px;line-height:1.8;">{ab['overview']}</p>
      </div>
      {visual('safety-equipment')}
    </div>
  </section>

  <section class="pad-lg" style="background:var(--paper-dim);">
    <div class="container split reverse">
      <div class="reveal">
        <div class="eyebrow">Our Approach</div>
        <h2 style="font-size:clamp(24px,3.2vw,34px);margin-top:14px;">Matched to the space, not a fixed package.</h2>
        <p class="muted" style="margin-top:20px;font-size:16px;line-height:1.8;">{ab['approach']}</p>
      </div>
      {visual('hydrant')}
    </div>
  </section>

  <section class="pad-lg">
    <div class="container">
      {T.section_head("What We Supply", "CORE EQUIPMENT CATEGORIES.", ab['supply'])}
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 40px;">
        {supply_grid}
      </div>
      <div style="margin-top:36px;">{T.btn("View Full Catalogue", "/products.html", "outline")}</div>
    </div>
  </section>

  <section class="pad-lg on-dark">
    <div class="container">
      {T.section_head("Who We Serve", "BUSINESSES THAT NEED EQUIPMENT THEY CAN RELY ON.", ab['serve'])}
      <div class="chip-row">
        {audience_chips}
      </div>
    </div>
  </section>

  <section class="pad-lg">
    <div class="container split">
      <div class="reveal">
        <div class="eyebrow">Quality Commitment</div>
        <h2 style="font-size:clamp(24px,3.2vw,34px);margin-top:14px;">Transparent about specification.</h2>
        <p class="muted" style="margin-top:20px;font-size:16px;line-height:1.8;">{ab['quality']}</p>
      </div>
      {visual('cabinets')}
    </div>
  </section>

  <section class="pad-lg" style="background:var(--paper-dim);">
    <div class="container split reverse">
      <div class="reveal">
        <div class="eyebrow">Customer Support</div>
        <h2 style="font-size:clamp(24px,3.2vw,34px);margin-top:14px;">Enquiries, followed through.</h2>
        <p class="muted" style="margin-top:20px;font-size:16px;line-height:1.8;">{ab['support']}</p>
        <div style="margin-top:28px;">{T.btn("Contact SHARK", "/contact.html", "outline")}</div>
      </div>
      {visual('alarms')}
    </div>
  </section>

  {T.cta_banner("LET&rsquo;S TALK ABOUT YOUR REQUIREMENT.",
    "Reach out with your product, quantity and timeline and our team will follow up directly.",
    [T.btn("Request a Quote", "/contact.html", "primary"),
     T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")])}
'''
    write("/about.html", T.page(
        "About SHARK | Fire &amp; Safety Equipment Supplier in the UAE",
        "SHARK is a UAE-based supplier of fire fighting and safety equipment, serving commercial, "
        "industrial and business requirements with a professional, transparent approach.",
        "/about.html", body))

# ============================================================================
# PRODUCTS — catalogue + detail template
# ============================================================================
def build_products():
    wa = data.whatsapp_href()
    chips = ['<button class="chip active" data-cat="all">All</button>']
    for c in data.PRODUCT_CATEGORIES:
        chips.append(f'<button class="chip" data-cat="{c["key"]}">{c["name"]}</button>')
    cards = "\n".join(T.product_card(p) for p in data.PRODUCTS)

    body = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("Products", None)])}
      <h1>FIRE &amp; SAFETY EQUIPMENT CATALOGUE.</h1>
      <p>Browse SHARK&rsquo;s fire fighting and safety equipment by category. Every product page carries clear
        technical detail &mdash; where a specification isn&rsquo;t yet confirmed, we say so rather than guess.</p>
    </div>
  </section>

  <section class="pad-lg">
    <div class="container">
      <div class="filter-bar" data-product-filter>
        <div class="chip-row">
          {"".join(chips)}
        </div>
        <div class="search-field">
          {icons.UI['search']}
          <input type="text" placeholder="Search products&hellip;" data-product-search aria-label="Search products">
        </div>
      </div>
      <div class="product-grid cols-4">
        {cards}
      </div>
      <div class="results-empty">No products match your search. Try a different keyword or category, or
        <a href="/contact.html" style="color:var(--red);font-weight:700;">send us your requirement directly</a>.</div>
    </div>
  </section>

  {T.cta_banner("CAN&rsquo;T FIND WHAT YOU NEED?",
    "Send us your requirement directly and our team will help you source the right equipment.",
    [T.btn("Request a Quote", "/contact.html", "primary"),
     T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")])}
<script>
(function(){{
  var params = new URLSearchParams(window.location.search);
  var cat = params.get("cat");
  if(cat){{
    var chip = document.querySelector('.chip[data-cat="'+cat+'"]');
    if(chip) chip.click();
  }}
}})();
</script>
'''
    write("/products.html", T.page(
        "Fire &amp; Safety Equipment Catalogue | SHARK",
        "Browse SHARK's full catalogue of fire fighting and safety equipment — extinguishers, hoses, "
        "hose reels, cabinets, hydrant equipment, alarms, emergency lighting and more.",
        "/products.html", body))

def build_product_detail(p):
    from data import CAT_BY_KEY
    cat = CAT_BY_KEY[p["cat"]]
    wa = data.whatsapp_href(f"Hello SHARK, I would like to enquire about the {p['name']}.")
    art = icons.PRODUCT_ART.get(p["cat"], "")
    has_photo = bool(p.get("image"))
    main_media = (f'<img src="{p["image"]}" alt="{p["name"]}" loading="eager" decoding="async">'
                  if has_photo else art)

    if has_photo:
        thumbs = f'<div class="pd-thumb active"><img src="{p["image"]}" alt="{p["name"]}" loading="lazy" decoding="async"></div>'
    else:
        thumbs = "\n".join(f'<div class="pd-thumb{" active" if i==0 else ""}">{art}</div>' for i in range(4))
    features = "\n".join(f"<li>{f}</li>" for f in p["features"])
    specs = "\n".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in p["specs"])
    applications = "\n".join(f"<li>{a}</li>" for a in p["applications"])
    variants = "\n".join(f'<span class="variant-chip">{v}</span>' for v in p["variants"])

    related = data.products_in(p["cat"], exclude_slug=p["slug"], limit=3)
    if len(related) < 3:
        others = [x for x in data.PRODUCTS if x["slug"] != p["slug"] and x not in related][:3-len(related)]
        related += others
    related_html = "\n".join(T.product_card(r) for r in related)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Product",
        "name": p["name"],
        "description": p["overview"],
        "category": cat["name"],
        "brand": {"@type": "Brand", "name": "SHARK"},
    })

    body = f'''
  <section class="pad-md">
    <div class="container">
      {T.breadcrumbs([("Products", "/products.html"), (cat["name"], f"/products.html?cat={cat['key']}"), (p["name"], None)])}
      <div class="pd-grid" style="margin-top:32px;">
        <div data-gallery>
          <div class="pd-gallery-main">{main_media}</div>
          <div class="pd-thumbs">{thumbs}</div>
        </div>
        <div>
          <div class="pd-cat">{cat['name']}</div>
          <h1 class="pd-title">{p['name']}</h1>
          <p class="pd-overview">{p['overview']}</p>
          <div class="pd-actions">
            {T.btn("Request Quote", "/contact.html?product=" + p['slug'], "primary")}
            {T.btn("WhatsApp Enquiry", wa, "outline", icon="whatsapp", target="_blank")}
          </div>

          <div class="pd-block">
            <h3>Key Features</h3>
            <ul class="pd-features">{features}</ul>
          </div>

          <div class="pd-block">
            <h3>Technical Specifications</h3>
            <table class="spec-table">{specs}</table>
          </div>

          <div class="pd-block">
            <h3>Applications</h3>
            <ul class="pd-features">{applications}</ul>
          </div>

          <div class="pd-block">
            <h3>Available Variants</h3>
            <div class="variant-row">{variants}</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="pad-lg" style="background:var(--paper-dim);">
    <div class="container">
      {T.section_head("Related Products", "YOU MAY ALSO NEED.")}
      <div class="product-grid cols-3">
        {related_html}
      </div>
    </div>
  </section>
'''
    write(f"/products/{p['slug']}.html", T.page(
        f"{p['name']} | SHARK Fire &amp; Safety Equipment",
        p["short"], f"/products/{p['slug']}.html", body, schema_json=schema, og_type="product"))

# ============================================================================
# SOLUTIONS
# ============================================================================
def build_solutions():
    wa = data.whatsapp_href()
    items = [
        ("Equipment Supply", "supply",
         "Straightforward supply of fire fighting and safety equipment across our core catalogue "
         "categories, sized to your facility or project."),
        ("Product Sourcing", "search",
         "Where a specific equipment type or configuration is needed, our team helps source and confirm "
         "the right product for the requirement."),
        ("B2B Equipment Supply", "customer",
         "Built around business accounts — contractors, facility teams and companies procuring equipment "
         "for their operations rather than one-off retail purchases."),
        ("Project Requirements", "quality",
         "Support for construction and fit-out projects that need equipment specified and supplied across "
         "multiple fire points or phases."),
        ("Bulk Requirements", "support",
         "Quantity-based enquiries for portfolios, multi-site facilities or large single sites, handled as "
         "a single coordinated requirement."),
        ("Safety Equipment Solutions", "quality",
         "General workplace safety equipment supplied alongside core fire fighting categories for a single, "
         "consolidated enquiry."),
    ]
    cards = "\n".join(f'''<div class="industry-card reveal">
      <div class="tag-icon">{icons.UI.get(ic,'')}</div>
      <h3>{title}</h3>
      <p class="muted" style="margin-top:14px;font-size:14.5px;line-height:1.7;">{text}</p>
    </div>''' for title, ic, text in items)

    body = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("Solutions", None)])}
      <h1>EQUIPMENT SUPPLY, STRUCTURED<br>AROUND YOUR REQUIREMENT.</h1>
      <p>SHARK is registered for the retail sale of fire fighting and safety equipment. Our current focus is
        professional equipment supply &mdash; the services below reflect that scope today.</p>
    </div>
  </section>

  <section class="pad-lg">
    <div class="container">
      {T.section_head("What We Offer", "SUPPLY-FOCUSED SOLUTIONS.",
        "Installation, maintenance, AMC, testing and commissioning services are not offered at this time. "
        "This section will be updated if and when those services are confirmed.")}
      <div class="product-grid cols-3">
        {cards}
      </div>
    </div>
  </section>

  {T.cta_banner("HAVE A PROJECT OR BULK REQUIREMENT?",
    "Tell us what the project or facility needs and our team will help put together the right supply plan.",
    [T.btn("Request a Quote", "/contact.html", "primary"),
     T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")])}
'''
    write("/solutions.html", T.page(
        "Solutions | SHARK Fire &amp; Safety Equipment Supply",
        "SHARK's fire and safety equipment solutions — equipment supply, sourcing, B2B and bulk "
        "requirements, and project-based supply across the UAE.",
        "/solutions.html", body))

# ============================================================================
# INDUSTRIES
# ============================================================================
def build_industries():
    from data import CAT_BY_KEY
    wa = data.whatsapp_href()
    sections = []
    for ind in data.INDUSTRIES:
        equip_chips = "".join(f'<span class="variant-chip">{CAT_BY_KEY[k]["name"]}</span>' for k in ind["equipment"])
        req_html = "".join(f"<li>{r}</li>" for r in ind["requirements"])
        icon = icons.INDUSTRY.get(ind["key"], "")
        sections.append(f'''<div id="{ind['key']}" class="pad-md" style="border-bottom:1px solid var(--paper-dim);">
      <div class="container split reverse">
        <div class="reveal">
          <div class="eyebrow">Industry</div>
          <h2 style="font-size:clamp(24px,3.2vw,32px);margin-top:14px;">{ind['name']}</h2>
          <p class="muted" style="margin-top:16px;font-size:15.5px;line-height:1.75;">{ind['summary']}</p>
          <h4 style="margin-top:26px;font-size:12.5px;text-transform:uppercase;letter-spacing:.06em;">Common Requirements</h4>
          <ul style="margin-top:12px;display:flex;flex-direction:column;gap:8px;">{req_html}</ul>
          <h4 style="margin-top:26px;font-size:12.5px;text-transform:uppercase;letter-spacing:.06em;">Relevant Equipment</h4>
          <div class="variant-row" style="margin-top:12px;">{equip_chips}</div>
          <div style="margin-top:26px;">{T.btn("Discuss Your Requirement", "/contact.html", "outline")}</div>
        </div>
        <div class="visual reveal" style="aspect-ratio:1/1;">
          <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:28px 28px;"></div>
          <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;">
            <div style="width:96px;height:96px;color:#565a61;">{icon}</div>
          </div>
        </div>
      </div>
    </div>''')

    body = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("Industries", None)])}
      <h1>EQUIPMENT MATCHED TO<br>THE ENVIRONMENT.</h1>
      <p>Different UAE business sectors carry different fire risk profiles and equipment priorities. Here&rsquo;s
        how SHARK approaches each.</p>
    </div>
  </section>

  {"".join(sections)}

  {T.cta_banner("NOT SURE WHERE TO START?",
    "Tell us about your building or site and our team will help identify the right equipment mix.",
    [T.btn("Request a Quote", "/contact.html", "primary"),
     T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")])}
'''
    write("/industries.html", T.page(
        "Industries We Serve | SHARK Fire &amp; Safety Equipment",
        "SHARK supplies fire and safety equipment across construction, commercial buildings, industrial "
        "facilities, warehousing, hospitality, retail, offices and property management sectors in the UAE.",
        "/industries.html", body))

# ============================================================================
# APPLICATIONS (replaces fabricated "Projects")
# ============================================================================
def build_applications():
    wa = data.whatsapp_href()
    cards = "\n".join(f'''<div class="industry-card reveal">
      <div class="tag-icon">{icons.INDUSTRY.get(a['key'], icons.UI.get('quality',''))}</div>
      <h3>{a['title']}</h3>
      <p class="muted" style="margin-top:14px;font-size:14.5px;line-height:1.7;">{a['text']}</p>
    </div>''' for a in data.APPLICATIONS)

    body = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("Applications", None)])}
      <h1>WHERE SHARK EQUIPMENT<br>IS PUT TO WORK.</h1>
      <p>We don&rsquo;t publish project case studies until we can share verified, specific details. In the
        meantime, here&rsquo;s how our core equipment categories typically apply across UAE business
        environments.</p>
    </div>
  </section>

  <section class="pad-lg">
    <div class="container">
      <div class="product-grid cols-3">
        {cards}
      </div>
    </div>
  </section>

  {T.cta_banner("HAVE A PROJECT TO DISCUSS?",
    "Share your building type and requirement and we'll help identify suitable equipment.",
    [T.btn("Request a Quote", "/contact.html", "primary"),
     T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")])}
'''
    write("/applications.html", T.page(
        "Applications | SHARK Fire &amp; Safety Equipment",
        "How SHARK's fire and safety equipment applies across commercial, industrial, construction, "
        "warehouse, hospitality and retail environments in the UAE.",
        "/applications.html", body))

# ============================================================================
# WHY SHARK
# ============================================================================
def build_why_shark():
    wa = data.whatsapp_href()
    blocks = []
    for i, w in enumerate(data.WHY_SHARK_LONG):
        reverse = " reverse" if i % 2 else ""
        bg = ' style="background:var(--paper-dim);"' if i % 2 else ""
        blocks.append(f'''<div class="pad-md"{bg}>
      <div class="container split{reverse}">
        <div class="reveal">
          <div class="eyebrow">{str(i+1).zfill(2)}</div>
          <h2 style="font-size:clamp(24px,3.2vw,32px);margin-top:14px;">{w['title']}</h2>
          <p class="muted" style="margin-top:18px;font-size:16px;line-height:1.8;">{w['text']}</p>
        </div>
        <div class="visual reveal" style="aspect-ratio:16/11;">
          <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:30px 30px;"></div>
          <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;">
            <div style="width:120px;height:120px;color:#4b4e54;">{list(icons.PRODUCT_ART.values())[i % len(icons.PRODUCT_ART)]}</div>
          </div>
        </div>
      </div>
    </div>''')

    body = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("Why SHARK", None)])}
      <h1>STRONGER PROTECTION.<br>PROFESSIONAL SUPPLY.</h1>
      <p>No inflated claims, no invented statistics &mdash; just the principles that guide how SHARK
        approaches fire and safety equipment supply.</p>
    </div>
  </section>

  {"".join(blocks)}

  {T.cta_banner("SUPPLY YOU CAN DEPEND ON.",
    "Talk to our team about your fire and safety equipment requirement.",
    [T.btn("Request a Quote", "/contact.html", "primary"),
     T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")], extra_class="alt")}
'''
    write("/why-shark.html", T.page(
        "Why SHARK | Fire &amp; Safety Equipment Supplier",
        "The principles behind SHARK's approach to fire and safety equipment supply in the UAE — "
        "quality-focused, reliable, transparent and B2B-first.",
        "/why-shark.html", body))

# ============================================================================
# RESOURCES
# ============================================================================
def build_resources():
    wa = data.whatsapp_href()
    cards = "\n".join(T.article_card(a) for a in data.ARTICLES)
    body = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("Resources", None)])}
      <h1>SAFETY INSIGHTS &amp;<br>EQUIPMENT GUIDES.</h1>
      <p>Practical, educational articles about fire safety equipment &mdash; written to inform, not to
        replace professional fire safety advice specific to your building.</p>
    </div>
  </section>

  <section class="pad-lg">
    <div class="container">
      <div class="product-grid cols-3">
        {cards}
      </div>
    </div>
  </section>

  {T.cta_banner("HAVE A QUESTION ABOUT EQUIPMENT?",
    "If you can't find what you're looking for in our resources, our team is happy to help directly.",
    [T.btn("Contact SHARK", "/contact.html", "primary"),
     T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")])}
'''
    write("/resources.html", T.page(
        "Resources &amp; Safety Insights | SHARK",
        "Educational articles and guides on fire safety equipment — extinguishers, hose reels, "
        "emergency lighting and workplace fire safety basics.",
        "/resources.html", body))

def build_article(a):
    body_html = ""
    for tag, text in a["body"]:
        body_html += f"<{tag}>{text}</{tag}>\n"
    related = [x for x in data.ARTICLES if x["slug"] != a["slug"]][:3]
    related_html = "\n".join(T.article_card(r) for r in related)
    body = f'''
  <section class="pad-md">
    <div class="container">
      {T.breadcrumbs([("Resources", "/resources.html"), (a["title"], None)])}
      <div style="max-width:740px;margin:32px auto 0;">
        <div class="eyebrow">{a['tag']}</div>
        <h1 style="font-size:clamp(28px,4vw,42px);margin-top:16px;line-height:1.12;">{a['title']}</h1>
      </div>
      <div class="article-body-copy">
        {body_html}
      </div>
    </div>
  </section>

  <section class="pad-lg" style="background:var(--paper-dim);">
    <div class="container">
      {T.section_head("Related Reading", "MORE FROM RESOURCES.")}
      <div class="product-grid cols-3">
        {related_html}
      </div>
    </div>
  </section>
'''
    write(f"/resources/{a['slug']}.html", T.page(
        f"{a['title']} | SHARK Resources",
        a["excerpt"], f"/resources/{a['slug']}.html", body))

# ============================================================================
# FAQ
# ============================================================================
def build_faq():
    wa = data.whatsapp_href()
    faq_html = "\n".join(T.faq_item(q, a, open_first=(i == 0)) for i, (q, a) in enumerate(data.FAQS))
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in data.FAQS]
    })
    body = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("FAQ", None)])}
      <h1>FREQUENTLY ASKED<br>QUESTIONS.</h1>
      <p>Straightforward answers about what SHARK supplies and how to work with us.</p>
    </div>
  </section>

  <section class="pad-lg">
    <div class="container">
      <div class="faq-list" style="max-width:820px;margin:0 auto;">
        {faq_html}
      </div>
    </div>
  </section>

  {T.cta_banner("STILL HAVE A QUESTION?",
    "Reach out directly and our team will get back to you.",
    [T.btn("Contact SHARK", "/contact.html", "primary"),
     T.btn("WhatsApp Us", wa, "outline-light", icon="whatsapp", target="_blank")])}
'''
    write("/faq.html", T.page(
        "FAQ | SHARK Fire &amp; Safety Equipment",
        "Answers to common questions about SHARK's fire and safety equipment supply, quotations, "
        "bulk orders and coverage areas in the UAE.",
        "/faq.html", body, schema_json=schema))

# ============================================================================
# CONTACT / QUOTE
# ============================================================================
def build_contact():
    c = data.CONFIG
    wa = data.whatsapp_href()
    info_items = [
        ("phone", "Phone", c["phone_display"], f"tel:{c['phone_tel']}"),
        ("whatsapp", "WhatsApp", c["whatsapp_display"], wa),
        ("mail", "Email", c["email"], f"mailto:{c['email']}"),
        ("pin", "Location", f"{c['address_line']}, {c['address_city']}", None),
        ("clock", "Business Hours", f"{c['hours_weekday']}<br>{c['hours_weekend']}", None),
    ]
    info_html = ""
    for icon_key, label, value, href in info_items:
        val_html = f'<a href="{href}">{value}</a>' if href else f"<p>{value}</p>"
        info_html += f'''<div class="contact-info-item">
          <div class="ic">{icons.UI.get(icon_key,'')}</div>
          <div><h4>{label}</h4>{val_html}</div>
        </div>'''

    body = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("Contact", None)])}
      <h1>LET&rsquo;S TALK ABOUT YOUR<br>REQUIREMENT.</h1>
      <p>Share your product, quantity and project details and our team will follow up with a quotation.</p>
    </div>
  </section>

  <section class="pad-lg">
    <div class="container contact-grid">
      <div class="reveal">
        <div class="eyebrow">Contact SHARK</div>
        <h2 style="font-size:26px;margin-top:14px;">Reach us directly</h2>
        <div class="contact-info-list" style="margin-top:20px;">
          {info_html}
        </div>
      </div>
      <div class="form-panel reveal">
        <div class="eyebrow">Request a Quote</div>
        <h2 style="font-size:24px;margin-top:12px;margin-bottom:26px;">Tell us what you need</h2>
        {T.quote_form()}
      </div>
    </div>
  </section>
'''
    write("/contact.html", T.page(
        "Contact &amp; Request a Quote | SHARK Fire &amp; Safety Equipment",
        "Contact SHARK to request a quotation for fire fighting and safety equipment — phone, WhatsApp, "
        "email or our online enquiry form.",
        "/contact.html", body))

# ============================================================================
# LEGAL
# ============================================================================
def build_legal():
    c = data.CONFIG
    privacy = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("Privacy Policy", None)])}
      <h1>PRIVACY POLICY.</h1>
    </div>
  </section>
  <section class="pad-lg">
    <div class="container legal-copy">
      <p class="legal-updated">Last updated: [DATE]</p>
      <p>This Privacy Policy explains how {c['legal_name']} ("SHARK", "we", "us") collects, uses and
        protects information submitted through this website.</p>
      <h2>Information We Collect</h2>
      <p>When you submit an enquiry or quotation request, we may collect your name, company name, phone
        number, email address, and details of the product or project you describe to us.</p>
      <h2>How We Use Information</h2>
      <ul>
        <li>To respond to enquiries and provide quotations.</li>
        <li>To follow up on business and product requirements.</li>
        <li>To maintain records of business communication.</li>
      </ul>
      <h2>Information Sharing</h2>
      <p>We do not sell your information. Information is only shared with third parties where necessary to
        fulfil your enquiry (for example, sourcing a specific product) or where required by law.</p>
      <h2>Data Security</h2>
      <p>We take reasonable steps to protect information submitted to us, but no method of transmission or
        storage is completely secure.</p>
      <h2>Contact</h2>
      <p>Questions about this policy can be directed to {c['email']}.</p>
      <p class="form-note">This is a general placeholder policy. Please have it reviewed by a qualified
        legal advisor before publishing, and update it to reflect your actual data handling practices.</p>
    </div>
  </section>
'''
    write("/privacy-policy.html", T.page(
        "Privacy Policy | SHARK", "Privacy Policy for SHARK Equipment Safety and Fire Trading.",
        "/privacy-policy.html", privacy))

    terms = f'''
  <section class="page-hero">
    <div class="container">
      {T.breadcrumbs([("Terms &amp; Conditions", None)])}
      <h1>TERMS &amp; CONDITIONS.</h1>
    </div>
  </section>
  <section class="pad-lg">
    <div class="container legal-copy">
      <p class="legal-updated">Last updated: [DATE]</p>
      <p>These Terms &amp; Conditions govern use of this website by {c['legal_name']} ("SHARK").</p>
      <h2>Use of Website</h2>
      <p>This website is provided for general information about SHARK's fire and safety equipment supply.
        Product information, including technical specifications, is provided to the best of our knowledge
        and marked as "available on request" where not yet confirmed.</p>
      <h2>Quotations &amp; Enquiries</h2>
      <p>Submitting a quotation request does not constitute a binding order. Pricing, availability and lead
        times are confirmed directly with our team following an enquiry.</p>
      <h2>Intellectual Property</h2>
      <p>Content on this website, including text and graphics, belongs to SHARK unless otherwise stated and
        may not be reproduced without permission.</p>
      <h2>Limitation of Liability</h2>
      <p>SHARK is not liable for decisions made solely on the basis of general information published on
        this website. Equipment selection should be confirmed directly with our team for your specific
        requirement.</p>
      <h2>Governing Law</h2>
      <p>These terms are governed by the laws of the United Arab Emirates.</p>
      <p class="form-note">This is a general placeholder document. Please have it reviewed by a qualified
        legal advisor before publishing, and update it to reflect your actual business terms.</p>
    </div>
  </section>
'''
    write("/terms-and-conditions.html", T.page(
        "Terms &amp; Conditions | SHARK", "Terms and Conditions for SHARK Equipment Safety and Fire Trading.",
        "/terms-and-conditions.html", terms))

# ============================================================================
# SEO — sitemap + robots
# ============================================================================
def build_seo_files():
    base = data.CONFIG["base_url"].rstrip("/")
    paths = ["/index.html", "/about.html", "/products.html", "/solutions.html", "/industries.html",
             "/applications.html", "/why-shark.html", "/resources.html", "/faq.html", "/contact.html",
             "/privacy-policy.html", "/terms-and-conditions.html"]
    paths += [f"/products/{p['slug']}.html" for p in data.PRODUCTS]
    paths += [f"/resources/{a['slug']}.html" for a in data.ARTICLES]
    urls = "\n".join(f"  <url><loc>{base}{p}</loc></url>" for p in paths)
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>'''
    write("/sitemap.xml", sitemap)

    robots = f'''User-agent: *
Allow: /

Sitemap: {base}/sitemap.xml
'''
    write("/robots.txt", robots)

if __name__ == "__main__":
    build_home()
    build_about()
    build_products()
    for _p in data.PRODUCTS:
        build_product_detail(_p)
    build_solutions()
    build_industries()
    build_applications()
    build_why_shark()
    build_resources()
    for _a in data.ARTICLES:
        build_article(_a)
    build_faq()
    build_contact()
    build_legal()
    build_seo_files()
    print("Done.")
