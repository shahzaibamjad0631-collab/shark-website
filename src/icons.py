# -*- coding: utf-8 -*-
"""
SHARK — custom SVG icon system.
Hand-built line-art (stroke=currentColor), no external icon libraries,
no photography. Keeps the whole site's visual language technical and
consistent, per brand direction (industrial engineering aesthetic).
"""

# ---------------------------------------------------------------------------
# Small UI icons — 24x24 viewBox, stroke style
# ---------------------------------------------------------------------------
UI = {
"arrow-right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M4 12h16M14 6l6 6-6 6"/></svg>',
"arrow-up-right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M7 17L17 7M9 7h8v8"/></svg>',
"chevron-right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M9 6l6 6-6 6"/></svg>',
"search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.3-4.3"/></svg>',
"whatsapp": '<svg viewBox="0 0 32 32" fill="currentColor"><path d="M16.02 3C9.4 3 4.02 8.38 4.02 15c0 2.23.62 4.32 1.68 6.11L4 29l8.1-1.63A11.9 11.9 0 0016.02 27C22.65 27 28 21.62 28 15S22.65 3 16.02 3zm0 21.8c-1.98 0-3.83-.56-5.4-1.53l-.39-.23-4.8.97 1-4.67-.25-.4a9.68 9.68 0 01-1.55-5.24c0-5.4 4.4-9.8 9.82-9.8 5.4 0 9.8 4.4 9.8 9.8s-4.4 9.9-9.98 9.9z"/><path d="M21.3 17.68c-.29-.15-1.72-.85-1.98-.94-.27-.1-.46-.15-.66.14-.2.29-.75.94-.92 1.13-.17.2-.34.22-.63.07-.29-.14-1.22-.45-2.33-1.44-.86-.77-1.44-1.71-1.61-2-.17-.29-.02-.44.13-.59.13-.13.29-.34.44-.51.15-.17.2-.29.29-.48.1-.2.05-.36-.02-.51-.07-.15-.66-1.6-.91-2.19-.24-.57-.48-.5-.66-.5-.17-.01-.36-.01-.56-.01-.2 0-.51.07-.78.36-.27.29-1.02 1-1.02 2.44s1.05 2.83 1.2 3.03c.15.2 2.06 3.15 5 4.42.7.3 1.24.48 1.67.61.7.22 1.34.19 1.84.12.56-.08 1.72-.7 1.96-1.38.24-.68.24-1.26.17-1.38-.07-.13-.26-.2-.55-.35z"/></svg>',
"phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M6.5 4h3l1.5 4-2 1.5a11 11 0 005.5 5.5l1.5-2 4 1.5v3a1.5 1.5 0 01-1.6 1.5A16 16 0 015 5.6 1.5 1.5 0 016.5 4z"/></svg>',
"mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3.5" y="5.5" width="17" height="13" rx="1"/><path d="M4 6.5l8 6.5 8-6.5"/></svg>',
"pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 21s7-6.6 7-11.5A7 7 0 105 9.5C5 14.4 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.4"/></svg>',
"clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>',
"check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
"menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
"close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 5l14 14M19 5L5 19"/></svg>',
"linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 100 5 2.5 2.5 0 000-5zM3.5 9h3v11.5h-3V9zM9.5 9h2.9v1.6h.04c.4-.76 1.4-1.6 2.9-1.6 3.1 0 3.7 2 3.7 4.7v6.8h-3v-6c0-1.4 0-3.3-2-3.3-2 0-2.3 1.6-2.3 3.2v6.1h-3V9z"/></svg>',
"instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3.5" y="3.5" width="17" height="17" rx="4"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1"/></svg>',
"facebook": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8.5h2.5V5H14c-2.2 0-3.5 1.4-3.5 3.6V11H8v3.5h2.5V21H14v-6.5h2.3l.4-3.5H14V9c0-.4.2-.5.6-.5z"/></svg>',
"quality": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l2.3 4.7 5.2.7-3.8 3.6.9 5.2L12 15.7 7.4 17.2l.9-5.2-3.8-3.6 5.2-.7L12 3z"/></svg>',
"supply": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 7l9-4 9 4-9 4-9-4z"/><path d="M3 7v10l9 4 9-4V7M12 11v10"/></svg>',
"support": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3.2"/><path d="M4.5 4.5l4.3 4.3M19.5 4.5l-4.3 4.3M4.5 19.5l4.3-4.3M19.5 19.5l-4.3-4.3"/></svg>',
"customer": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8.2" r="3.4"/><path d="M4.8 20c1-3.6 4-5.6 7.2-5.6s6.2 2 7.2 5.6"/></svg>',
}

# ---------------------------------------------------------------------------
# Category / product-type icons — 32x32 viewBox, used at small size
# (category tiles, industry equipment lists, spec chips)
# ---------------------------------------------------------------------------
CATEGORY = {
"extinguishers": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="11" y="11" width="9" height="16" rx="2"/><rect x="14" y="8" width="4" height="3"/><path d="M13 8c0-3 2-4.5 3-4.5s3 1.5 3 4.5"/><path d="M14.5 6.3h3"/><path d="M18 9.5c4.5.3 6.5 3 6 5.5-.3 1.6-2 2.6-3.5 2.6"/><path d="M19.3 14.3l2.6.6-.6 2.2-2.6-.6z"/><circle cx="15.5" cy="14" r="1"/><path d="M13 18.5h5M13 22.5h5"/></svg>',
"hoses": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M5 9c4 0 4 4 8 4s4-4 8-4 4 4 8 4"/><path d="M5 15c4 0 4 4 8 4s4-4 8-4 4 4 8 4"/><path d="M5 21c4 0 4 4 8 4s4-4 8-4 4 4 8 4"/></svg>',
"hose-reels": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="14" cy="16" r="9"/><circle cx="14" cy="16" r="4.4"/><circle cx="14" cy="16" r="1.2" fill="currentColor" stroke="none"/><path d="M23 16h4M23 12.5l3-2M23 19.5l3 2"/></svg>',
"cabinets": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="8" y="5" width="16" height="22" rx="0.5"/><path d="M8 12h16M14 18.5h4M11 22h10"/><circle cx="20.5" cy="15" r="0.9" fill="currentColor" stroke="none"/></svg>',
"hydrant": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M13 12V8.5a3 3 0 016 0V12"/><rect x="11.5" y="12" width="9" height="13" rx="1"/><path d="M8 15.5h3.5M20.5 15.5H24M8 20h3.5M20.5 20H24"/><path d="M13.5 25v2.5h5V25"/></svg>',
"alarms": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="9" y="8" width="14" height="14" rx="1"/><circle cx="16" cy="15" r="4"/><path d="M16 4.5V8M16 22v3.5M6 15h3M23 15h3"/></svg>',
"emergency-lighting": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="10" y="6" width="12" height="9" rx="1"/><path d="M14 15l-2 11 8-7h-4l2-4z" fill="currentColor" stroke="none"/></svg>',
"exit-signs": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="5" y="10" width="22" height="11" rx="1"/><path d="M10 15.5h5M13 12.5v6M21 12.5l3 3-3 3M21 15.5h3"/></svg>',
"accessories": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M20.5 6a4.5 4.5 0 00-6 5.9L6 20.4l2.6 2.6 8.5-8.5A4.5 4.5 0 0022.5 8l-3 3-2-2 3-3z"/></svg>',
"safety-equipment": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M16 4.5l9 3.4v6.8c0 6-3.8 10-9 12.4-5.2-2.4-9-6.4-9-12.4V7.9L16 4.5z"/><path d="M12 16l3 3 5.5-5.5"/></svg>',
}

# ---------------------------------------------------------------------------
# Large technical illustrations — 100x100 viewBox, used on product cards /
# gallery / featured product panels. One consistent illustration per
# category (reused across products in that category, since real product
# photography has not been supplied).
# ---------------------------------------------------------------------------
PRODUCT_ART = {
"extinguishers": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<rect x="36" y="34" width="28" height="50" rx="6"/>
<rect x="44" y="25" width="12" height="9"/>
<path d="M40 25c0-9 6-13 10-13s10 4 10 13"/>
<path d="M44 19h12"/>
<path d="M56 28c14 1 20 9 18 17-1 5-6 8-11 8"/>
<path d="M60 45l8 2-2 7-8-2z"/>
<circle cx="50" cy="42" r="3"/>
<path d="M42 58h16M42 68h16"/>
<rect x="39" y="84" width="22" height="4" rx="1"/>
</svg>''',
"hoses": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<path d="M10 30c10 0 10 10 20 10s10-10 20-10 10 10 20 10 10-10 20-10"/>
<path d="M10 50c10 0 10 10 20 10s10-10 20-10 10 10 20 10 10-10 20-10"/>
<path d="M10 70c10 0 10 10 20 10s10-10 20-10 10 10 20 10 10-10 20-10"/>
<rect x="6" y="26" width="8" height="8" rx="1"/><rect x="6" y="66" width="8" height="8" rx="1"/>
</svg>''',
"hose-reels": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<circle cx="42" cy="50" r="30"/><circle cx="42" cy="50" r="21"/><circle cx="42" cy="50" r="12"/>
<circle cx="42" cy="50" r="3" fill="currentColor" stroke="none"/>
<rect x="10" y="46" width="10" height="8"/>
<path d="M70 50h14M78 40l8-6M78 60l8 6"/>
</svg>''',
"cabinets": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<rect x="26" y="12" width="48" height="76" rx="1"/>
<path d="M26 34h48M40 55h20M32 68h36"/>
<circle cx="63" cy="45" r="1.6" fill="currentColor" stroke="none"/>
<path d="M40 12v-4h20v4"/>
</svg>''',
"hydrant": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<path d="M40 34V22a10 10 0 0120 0v12"/>
<rect x="34" y="34" width="32" height="46" rx="3"/>
<path d="M22 46h12M66 46h12M22 62h12M66 62h12"/>
<path d="M42 80v10h16V80"/><path d="M50 10v8"/>
</svg>''',
"alarms": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<rect x="26" y="22" width="48" height="48" rx="2"/>
<circle cx="50" cy="46" r="14"/><circle cx="50" cy="46" r="5"/>
<path d="M50 8v10M50 78v10M12 46h10M78 46h10"/>
</svg>''',
"emergency-lighting": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<rect x="28" y="16" width="44" height="30" rx="2"/>
<circle cx="40" cy="31" r="6"/><circle cx="60" cy="31" r="6"/>
<path d="M44 46l-8 38 24-24H44l6-14z" fill="currentColor" stroke="none" opacity=".9"/>
</svg>''',
"exit-signs": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<rect x="10" y="34" width="80" height="32" rx="2"/>
<path d="M26 42v16M26 42h10M26 50h8M60 42l14 8-14 8M60 50h14"/>
<path d="M10 34l6-10h68l6 10"/>
</svg>''',
"accessories": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<path d="M64 20a13 13 0 00-17.6 17.6L18 66.2l6.8 6.8L53.4 44.4A13 13 0 0071 26.8l-8.6 8.6-6-6 8.6-8.6z"/>
<circle cx="22" cy="70" r="4"/>
</svg>''',
"safety-equipment": '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.2">
<path d="M50 10l26 10v20c0 18-11 30-26 38-15-8-26-20-26-38V20l26-10z"/>
<path d="M36 48l10 10 18-18"/>
</svg>''',
}

# ---------------------------------------------------------------------------
# Industry icons — 32x32
# ---------------------------------------------------------------------------
INDUSTRY = {
"construction": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M6 26V13l9-6 9 6v13"/><path d="M6 26h18M12 26v-7h6v7M20 10l6-4v9l-6 3"/></svg>',
"commercial": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="8" y="5" width="16" height="22"/><path d="M12 9h2M18 9h2M12 14h2M18 14h2M12 19h2M18 19h2"/><path d="M13 27v-5h6v5"/></svg>',
"industrial": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M5 26V15l6 4v-4l6 4v-4l6 4V26z"/><path d="M5 26h22M9 11V7M9 7h3M22 26v-4h3v4"/></svg>',
"warehouse": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M4 14l12-7 12 7v12H4z"/><path d="M4 14l12 6 12-6M16 20v6"/></svg>',
"hospitality": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M6 23V9M6 15h20a3 3 0 013 3v5"/><path d="M6 15v-2a3 3 0 013-3h4a3 3 0 013 3v2"/></svg>',
"retail": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M6 12l1.5-5h17L26 12"/><path d="M6 12v13h20V12M13 12v4a3 3 0 006 0v-4"/></svg>',
"offices": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="9" y="4" width="14" height="24"/><path d="M13 8h2M17 8h2M13 13h2M17 13h2M13 18h2M17 18h2"/><path d="M13 28v-4h6v4"/></svg>',
"property-management": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="12" r="5"/><path d="M15.5 15.5L27 27M23 23v4h4"/></svg>',
"facilities-management": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="16" cy="16" r="4.2"/><path d="M16 6v3M16 23v3M6 16h3M23 16h3M9 9l2 2M21 21l2 2M23 9l-2 2M11 21l-2 2"/></svg>',
}
