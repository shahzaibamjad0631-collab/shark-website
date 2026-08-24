# -*- coding: utf-8 -*-
"""SHARK — shared page templates / components (Python string-based, no runtime deps)."""

from data import CONFIG, NAV, FOOTER_LINKS_COMPANY, FOOTER_LINKS_PRODUCTS, FOOTER_LINKS_CONTACT, whatsapp_href
import icons

SITE_NAME = CONFIG["site_name"]

# ---------------------------------------------------------------------------
# Brand mark — the actual SHARK logo (supplied by the client): a shield
# containing a shark fin merging into a flame. Every place brand() is used
# in this site (header, mobile drawer, footer) sits on a dark background,
# so we use the white+red recolor of the logo for legibility.
# ---------------------------------------------------------------------------
def brand(dark_bg=True, small=False):
    cls = "brand" + (" small" if small else "")
    return f'''<a href="/index.html" class="{cls}">
      <img src="/assets/img/shark-mark-white.png" alt="" class="mark" width="38" height="37">
      <span class="word">
        <img src="/assets/img/shark-wordmark-white.png" alt="SHARK Fire and Safety Equipment" class="wordmark-img">
        <span class="sub">Fire &amp; Safety Equipment</span>
      </span>
    </a>'''

# ---------------------------------------------------------------------------
# Homepage opening intro — 4 clean photographs, shown once per browser
# session (sessionStorage), then split apart to reveal the hero underneath.
# No text/numbers/logo on the images themselves — see style.css for the
# zoom-in/hold/split timeline and the prefers-reduced-motion override.
# ---------------------------------------------------------------------------
def intro_overlay():
    imgs = [
        ("/assets/img/intro-1.jpg", "20% 45%"),
        ("/assets/img/intro-2.jpg", "35% 40%"),
        ("/assets/img/intro-3.jpg", "68% 55%"),
        ("/assets/img/intro-4.jpg", "60% 42%"),
    ]
    panels = "\n    ".join(
        f'<div class="intro-panel"><img src="{src}" alt="" fetchpriority="high" decoding="async" style="object-position:{pos};"></div>'
        for src, pos in imgs
    )
    return f'''<script>if(sessionStorage.getItem("sharkIntroPlayed")){{document.documentElement.classList.add("no-intro");}}</script>
  <div class="intro-overlay" id="introOverlay" aria-hidden="true">
    {panels}
  </div>'''

# ---------------------------------------------------------------------------
# <head> block
# ---------------------------------------------------------------------------
def meta(title, description, path, schema_json=None, og_type="website"):
    canonical = CONFIG["base_url"].rstrip("/") + path
    desc = description.replace('"', "&quot;")
    schema_script = f'<script type="application/ld+json">{schema_json}</script>' if schema_json else ""
    return f'''<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="SHARK Equipment Safety and Fire Trading">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
{schema_script}'''

# ---------------------------------------------------------------------------
# Header / nav
# ---------------------------------------------------------------------------
def header(active_path):
    links = []
    for label, href in NAV:
        active = " active" if href == active_path else ""
        links.append(f'<a href="{href}" class="{active.strip()}">{label}</a>')
    nav_html = "\n      ".join(links)
    wa = whatsapp_href()
    return f'''<header class="site-header">
    <div class="header-row">
      {brand()}
      <nav class="main-nav">
      {nav_html}
      </nav>
      <div class="header-cta">
        <a href="{wa}" class="icon-btn" aria-label="WhatsApp SHARK" target="_blank" rel="noopener">{icons.UI['whatsapp']}</a>
        <a href="/contact.html" class="btn btn-primary desktop-only">Request a Quote</a>
      </div>
      <button class="burger icon-btn" aria-label="Open menu">{icons.UI['menu']}</button>
    </div>
  </header>'''

def mobile_drawer(active_path):
    links = []
    for label, href in NAV:
        active = " active" if href == active_path else ""
        links.append(f'<a href="{href}" class="{active.strip()}">{label} {icons.UI["chevron-right"]}</a>')
    nav_html = "\n      ".join(links)
    wa = whatsapp_href()
    return f'''<div class="mobile-drawer">
    <div class="mobile-drawer-top">
      {brand()}
      <button class="drawer-close icon-btn" aria-label="Close menu">{icons.UI['close']}</button>
    </div>
    <nav>
      {nav_html}
    </nav>
    <div class="mobile-drawer-foot">
      <a href="/contact.html" class="btn btn-primary btn-block">Request a Quote</a>
      <a href="{wa}" class="btn btn-outline-light btn-block" target="_blank" rel="noopener">WhatsApp Us</a>
    </div>
  </div>'''

def mobile_cta_bar():
    wa = whatsapp_href()
    return f'''<div class="mobile-cta-bar">
    <div class="row">
      <a href="{wa}" class="wa" target="_blank" rel="noopener">{icons.UI['whatsapp']} WhatsApp</a>
      <a href="/contact.html" class="rq">Request Quote</a>
    </div>
  </div>'''

def wa_float():
    wa = whatsapp_href()
    return f'<a href="{wa}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat with SHARK on WhatsApp">{icons.UI["whatsapp"]}</a>'

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
def footer():
    def li(items):
        return "\n        ".join(f'<li><a href="{href}">{label}</a></li>' for label, href in items)
    wa = whatsapp_href()
    return f'''<footer class="site-footer">
    <div class="footer-top">
      <div class="footer-brand">
        {brand()}
        <p>SHARK supplies fire fighting and safety equipment for commercial, industrial and business
          requirements across the UAE — extinguishers, hose reels, cabinets, alarm equipment, emergency
          lighting and general safety equipment.</p>
        <div class="footer-social">
          <a href="#" aria-label="LinkedIn">{icons.UI['linkedin']}</a>
          <a href="#" aria-label="Instagram">{icons.UI['instagram']}</a>
          <a href="#" aria-label="Facebook">{icons.UI['facebook']}</a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Company</h5>
        <ul>{li(FOOTER_LINKS_COMPANY)}</ul>
      </div>
      <div class="footer-col">
        <h5>Products</h5>
        <ul>{li(FOOTER_LINKS_PRODUCTS)}</ul>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <ul>{li(FOOTER_LINKS_CONTACT)}
        <li><a href="{wa}" target="_blank" rel="noopener">WhatsApp SHARK</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Get In Touch</h5>
        <ul>
          <li>{CONFIG['phone_display']}</li>
          <li>{CONFIG['email']}</li>
          <li>{CONFIG['address_city']}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span data-year></span> {CONFIG['legal_name']}. All rights reserved.</p>
      <div class="legal-links">
        <a href="/privacy-policy.html">Privacy Policy</a>
        <a href="/terms-and-conditions.html">Terms &amp; Conditions</a>
      </div>
    </div>
  </footer>'''

# ---------------------------------------------------------------------------
# Small components
# ---------------------------------------------------------------------------
def btn(label, href, style="primary", icon="arrow-right", extra_class="", target=None, block=False):
    cls = f"btn btn-{style} {extra_class}".strip()
    if block: cls += " btn-block"
    t = f' target="{target}" rel="noopener"' if target else ""
    ic = icons.UI.get(icon, "")
    return f'<a href="{href}" class="{cls}"{t}>{label}{ic}</a>'

def section_head(eyebrow, heading, desc="", center=False, split_html="", tag="h2"):
    cls = "section-head" + (" center" if center else "") + (" split" if split_html else "")
    desc_html = f"<p>{desc}</p>" if desc else ""
    if split_html:
        return f'''<div class="{cls} reveal">
      <div>
        <div class="eyebrow">{eyebrow}</div>
        <{tag}>{heading}</{tag}>
        {desc_html}
      </div>
      {split_html}
    </div>'''
    return f'''<div class="{cls} reveal">
      <div class="eyebrow">{eyebrow}</div>
      <{tag}>{heading}</{tag}>
      {desc_html}
    </div>'''

def breadcrumbs(items):
    """items: list of (label, href|None) — last item is current page (no href)."""
    parts = ['<a href="/index.html">Home</a>']
    for i, (label, href) in enumerate(items):
        parts.append('<span class="sep">/</span>')
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span class="current">{label}</span>')
    return f'<div class="crumbs">{"".join(parts)}</div>'

def eyebrow_only(text, dark=False):
    cls = "eyebrow on-dark" if dark else "eyebrow"
    return f'<div class="{cls}">{text}</div>'

# ---------------------------------------------------------------------------
# Cards
# ---------------------------------------------------------------------------
def product_card(p, cat_name=None):
    from data import CAT_BY_KEY
    cat = cat_name or CAT_BY_KEY[p["cat"]]["name"]
    art = icons.PRODUCT_ART.get(p["cat"], "")
    wa = whatsapp_href(f"Hello SHARK, I would like to enquire about the {p['name']}.")
    return f'''<article class="product-card reveal" data-product-card data-cat="{p['cat']}" data-name="{p['name']}">
      <div class="product-media"><span class="cat-chip">{cat}</span>{art}</div>
      <div class="product-body">
        <div class="p-cat">{cat}</div>
        <h3>{p['name']}</h3>
        <p>{p['short']}</p>
        <div class="product-actions">
          <a href="/products/{p['slug']}.html" class="btn btn-outline btn-sm">View Product</a>
          <a href="{wa}" class="btn btn-dark btn-sm" target="_blank" rel="noopener">Request Pricing</a>
        </div>
      </div>
    </article>'''

def feature_product(p):
    from data import CAT_BY_KEY
    cat = CAT_BY_KEY[p["cat"]]["name"]
    art = icons.PRODUCT_ART.get(p["cat"], "")
    wa = whatsapp_href(f"Hello SHARK, I would like to enquire about the {p['name']}.")
    return f'''<article class="feature-product reveal">
      <div class="media">{art}</div>
      <div class="info">
        <div class="p-cat eyebrow">{cat}</div>
        <h3 style="font-size:26px;margin-top:14px;">{p['name']}</h3>
        <p class="muted" style="margin-top:14px;font-size:15px;line-height:1.7;">{p['short']}</p>
        <div class="product-actions" style="margin-top:26px;max-width:380px;">
          <a href="/products/{p['slug']}.html" class="btn btn-outline btn-sm">View Product</a>
          <a href="{wa}" class="btn btn-primary btn-sm" target="_blank" rel="noopener">Request Pricing</a>
        </div>
      </div>
    </article>'''

def industry_card(ind):
    icon = icons.INDUSTRY.get(ind["key"], "")
    return f'''<div class="industry-card reveal">
      <div class="tag-icon">{icon}</div>
      <h3>{ind['name']}</h3>
      <ul>{"".join(f"<li>{r}</li>" for r in ind['requirements'])}</ul>
      <a href="/industries.html#{ind['key']}" class="btn-ghost" style="margin-top:20px;display:inline-flex;">Discuss Your Requirement {icons.UI['arrow-right']}</a>
    </div>'''

def article_card(a):
    art = icons.PRODUCT_ART.get(a["art"], icons.CATEGORY.get(a["art"], ""))
    return f'''<article class="article-card reveal">
      <div class="article-media">{art}</div>
      <div class="article-body">
        <div class="article-tag">{a['tag']}</div>
        <h3>{a['title']}</h3>
        <p>{a['excerpt']}</p>
        <a href="/resources/{a['slug']}.html" class="article-read">Read Article {icons.UI['arrow-right']}</a>
      </div>
    </article>'''

def faq_item(q, a, open_first=False):
    cls = "faq-item open" if open_first else "faq-item"
    style = f'style="max-height:{ "400px" if open_first else "0" }"'
    return f'''<div class="{cls}">
      <button class="faq-q">{q}<span class="plus"></span></button>
      <div class="faq-a">
        <div class="faq-a-in">{a}</div>
      </div>
    </div>'''

def cta_banner(heading, text, buttons, extra_class=""):
    btn_html = " ".join(buttons)
    return f'''<section class="cta-banner {extra_class}">
    <div class="container reveal">
      <h2>{heading}</h2>
      <p>{text}</p>
      <div class="actions">{btn_html}</div>
    </div>
  </section>'''

# ---------------------------------------------------------------------------
# Quote form
# ---------------------------------------------------------------------------
def quote_form(product_name=None):
    prefill = f'value="{product_name}"' if product_name else ""
    return f'''<div data-form-wrapper>
    <form class="quote-form" data-quote-form novalidate>
      <div class="form-grid">
        <div class="field">
          <label>Full Name <span class="req">*</span></label>
          <input type="text" name="full_name" required>
        </div>
        <div class="field">
          <label>Company Name <span class="req">*</span></label>
          <input type="text" name="company_name" required>
        </div>
        <div class="field">
          <label>Phone <span class="req">*</span></label>
          <input type="tel" name="phone" required>
        </div>
        <div class="field">
          <label>Email</label>
          <input type="email" name="email">
        </div>
        <div class="field full">
          <label>Product Required <span class="req">*</span></label>
          <input type="text" name="product" {prefill} required>
        </div>
        <div class="field">
          <label>Quantity</label>
          <input type="text" name="quantity">
        </div>
        <div class="field">
          <label>Project / Requirement</label>
          <input type="text" name="project">
        </div>
        <div class="field full">
          <label>Message</label>
          <textarea name="message" rows="4"></textarea>
        </div>
      </div>
      <button type="submit" class="btn btn-primary btn-block" style="margin-top:8px;">Request Quotation</button>
      <p class="form-note">Fields marked <span class="req">*</span> are required. Our team will follow up on your enquiry directly.</p>
    </form>
    <div class="form-success">
      <div class="check">{icons.UI['check']}</div>
      <h3>Enquiry Received</h3>
      <p>Thank you — your request has been recorded. Our team will get back to you shortly to discuss your requirement.</p>
    </div>
  </div>'''

# ---------------------------------------------------------------------------
# Page shell
# ---------------------------------------------------------------------------
def page(title, description, path, body_html, schema_json=None, og_type="website", intro_html=None):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{meta(title, description, path, schema_json, og_type)}
</head>
<body>
  {intro_html or ""}
  {header(path)}
  {mobile_drawer(path)}
  {body_html}
  {footer()}
  {mobile_cta_bar()}
  {wa_float()}
  <script src="/assets/js/main.js"></script>
</body>
</html>'''
