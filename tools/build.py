"""يبني صفحات الموقع الثابتة بنفس الهيدر والفوتر. التشغيل: python tools/build.py"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FB = "https://www.facebook.com/skylineupvcwindow"
IG = "https://www.instagram.com/skylinepvc"
WA = "https://wa.me/201111934900"
ADDRESS = "شارع حسن مأمون، مدينة نصر، الحي الثامن، القاهرة، مصر"
MAPQ = "شارع حسن مأمون، مدينة نصر، الحي الثامن، القاهرة، مصر"

from urllib.parse import quote as _q
MAPS = "https://www.google.com/maps/place/%D9%84%D9%84%D8%A3%D8%A8%D9%88%D8%A7%D8%A8+%D9%88+%D8%A7%D9%84%D8%B4%D8%A8%D8%A7%D8%A8%D9%8A%D9%83+%D9%88+%D8%B4%D9%8A%D8%B4+%D8%A7%D9%84%D8%AD%D8%B5%D9%8A%D8%B1%D8%A9+_+Skyline+Upvc%E2%80%AD/@30.0587549,31.3539485,17z/data=!3m1!4b1!4m6!3m5!1s0x14583d00382c9361:0x3967d6e4ac025f7!8m2!3d30.0587503!4d31.3565234!16s%2Fg%2F11xrl8lt_v"
MAP_EMBED = "https://maps.google.com/maps?q=30.0587503,31.3565234&hl=ar&z=17&output=embed"

import time as _t
ASSET_V = str(int(_t.time()))

I = {
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/></svg>',
 "upload": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/></svg>',
 "image": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="9" cy="9" r="2"/><path d="m21 15-5-5L5 21"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 6.1 12.2 6.4 12.5a.8.8 0 0 0 1.2 0C12.9 21.2 19 14.2 19 9a7 7 0 0 0-7-7Zm0 9.6A2.6 2.6 0 1 1 12 6.4a2.6 2.6 0 0 1 0 5.2Z"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>',
 "fb": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3a5 5 0 0 0-5 5v2H7v4h2v7h4v-7h3l1-4h-4V9a1 1 0 0 1 1-1Z"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
 "sun": '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
 "moon": '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
 "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 "ext": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>',
 "video": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="5" width="14" height="14" rx="3"/><path d="m16 10 6-3v10l-6-3"/></svg>',
 "slide": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M12 4v16M8 12h2M14 12h2"/></svg>',
 "pano": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="6" width="20" height="12" rx="2.5"/><path d="M7 6v12M12 6v12M17 6v12"/></svg>',
 "balcony": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18M5 21v-8h14v8M9 13v8M15 13v8M5 13V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8"/></svg>',
 "shutter": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 8h18M3 12h18M3 16h18"/></svg>',
 "net": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/></svg>',
 "circle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18"/></svg>',
 "kitchen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 10h18M12 10v11M8 6.5h1M15 6.5h1M9 14v2M15 14v2"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/></svg>',
}

BRAND = '<a class="brand" href="index.html" aria-label="Skyline — الصفحة الرئيسية"><img class="logo-light" src="assets/logo-tagline.png" alt="Skyline — upvc for doors and windows — لاعمال البي في سي — باب وشباك — الإختيار الراقي لمن يُقَدِّر التفاصيل" width="896" height="629"><img class="logo-dark" src="assets/logo-tagline-dark.png" alt="" aria-hidden="true" width="896" height="629"></a>'

NAV = [("index.html", "الرئيسية"), ("index.html#about", "عن الشركة"), ("projects.html", "مشاريعنا"), ("gallery.html", "معرض الصور"), ("reviews.html", "آراء العملاء"), ("index.html#faq", "الأسئلة الشائعة"), ("contact.html", "تواصل معنا")]


SITE = "https://yahiaali97.github.io/SkylinePVC-Site/"
KEYWORDS = "شبابيك upvc, أبواب upvc, شبابيك يو بي في سي, شبابيك upvc مدينة نصر, شبابيك upvc القاهرة, تقفيل بلكونات, شيش حصيرة, شبابيك جرار, شبابيك بانوراما, سلك بليسيه, قطاع كومبين, قطاع كاترا, Skyline uPVC, سكاي لاين"


def head(title, desc):
    return f'''<!doctype html>
<html lang="ar-EG" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{KEYWORDS}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="__CANON__">
<meta name="theme-color" content="#08131f">
<meta name="geo.region" content="EG-C"><meta name="geo.placename" content="مدينة نصر، القاهرة"><meta name="geo.position" content="30.0587503;31.3565234"><meta name="ICBM" content="30.0587503, 31.3565234">
<meta property="og:type" content="website">
<meta property="og:locale" content="ar_EG">
<meta property="og:site_name" content="Skyline - For UPVC &amp; Shutter">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="__CANON__">
<meta property="og:image" content="{SITE}assets/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}assets/og-image.jpg">
<link rel="icon" href="assets/favicon-skyline.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-skyline-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/favicon-skyline-48.png" sizes="48x48" type="image/png">
<link rel="icon" href="assets/favicon-skyline-192.png" sizes="192x192" type="image/png">
<link rel="icon" href="assets/favicon-skyline-512.png" sizes="512x512" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon-skyline.png">
<link rel="preload" href="assets/fonts/ibm-plex-sans-arabic-arabic-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css?v={ASSET_V}">
<script>try{{var t=localStorage.getItem("skyline-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
__LD__
</head>
<body>
<a class="skip" href="#main">تخطَّ إلى المحتوى</a>
'''


def jsonld():
    import json, re
    biz = {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": SITE + "#business",
        "name": "Skyline - For UPVC & Shutter",
        "alternateName": ["سكاي لاين لأعمال اليو بي في سي", "Skyline uPVC", "سكاي لاين باب وشباك"],
        "description": "توريد وتركيب أبواب وشبابيك uPVC وشيش حصيرة وتقفيل بلكونات في جميع محافظات مصر — المعرض الرئيسي في مدينة نصر، القاهرة.",
        "slogan": "الإختيار الراقي لمن يُقَدِّر التفاصيل",
        "url": SITE,
        "logo": SITE + "assets/logo-tagline.png",
        "image": [SITE + "assets/og-image.jpg", SITE + "assets/hero-doors.jpg"],
        "telephone": "+201111934900",
        "foundingDate": "2019",
        "address": {"@type": "PostalAddress", "streetAddress": "شارع حسن مأمون، الحي الثامن", "addressLocality": "مدينة نصر",
                    "addressRegion": "القاهرة", "addressCountry": "EG"},
        "geo": {"@type": "GeoCoordinates", "latitude": 30.0587503, "longitude": 31.3565234},
        "hasMap": MAPS,
        "areaServed": {"@type": "Country", "name": "مصر"},
        "sameAs": [FB, IG],
        "contactPoint": [
            {"@type": "ContactPoint", "telephone": "+201111934900", "contactType": "sales", "availableLanguage": ["ar"]},
            {"@type": "ContactPoint", "telephone": "+201080477077", "contactType": "customer service", "availableLanguage": ["ar"]}],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
                       ["شبابيك وأبواب uPVC", "شبابيك جرار", "شبابيك بانوراما منطبق وباندا", "تقفيل بلكونات", "شيش حصيرة", "سلك متحرك وبليسيه"]],
    }
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a).strip()}} for q, a in FAQ]}
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Skyline uPVC", "url": SITE, "inLanguage": "ar-EG"}
    return "\n".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + "</script>" for x in (biz, faq, site))


def header(active):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    return f'''<div class="topbar"><div class="container">
  <a class="topbar-loc" href="{MAPS}" target="_blank" rel="noopener" title="افتح العنوان على خرائط جوجل">{I["pin"]}{ADDRESS}</a>
  <span class="topbar-links"><a href="tel:+201111934900" dir="ltr">01111934900</a><span aria-hidden="true">|</span><a href="tel:+201080477077" dir="ltr">01080477077</a><a class="topbar-pill" href="{WA}" target="_blank" rel="noopener">{I["wa"]}واتساب</a></span>
</div></div>
<header class="site-header">
  <div class="container">
    {BRAND}
    <nav class="nav" id="nav" aria-label="القائمة الرئيسية">{links}</nav>
    <div class="header-actions">
      <a class="btn btn-primary btn-sm" href="quote.html">{I["doc"]}اطلب عرض سعر</a>
      <button class="icon-btn theme-toggle" type="button" aria-label="تبديل الوضع الداكن">{I["sun"]}{I["moon"]}</button>
      <button class="icon-btn menu-toggle" type="button" aria-label="فتح القائمة" aria-expanded="false" aria-controls="nav">{I["menu"]}</button>
    </div>
  </div>
</header>
<main id="main">
'''


def phero(crumb, eyebrow, title, lead, extra=""):
    return f'''<section class="page-hero"><div class="container">
  <nav class="crumbs reveal" aria-label="مسار الصفحة"><a href="index.html">الرئيسية</a><span>/</span><span>{crumb}</span></nav>
  <p class="eyebrow reveal">{eyebrow}</p><h1 class="reveal reveal-d1">{title}</h1><p class="reveal reveal-d2">{lead}</p>{extra}
</div></section>'''


def footer(extra_scripts=""):
    nav = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f'''</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        {BRAND}
        <p class="muted" style="margin:14px 0 0">Skyline - For UPVC &amp; Shutter — توريد وتركيب أبواب وشبابيك uPVC وشيش حصيرة.</p>
        <div class="socials">
          <a class="icon-btn" href="{FB}" target="_blank" rel="noopener" aria-label="فيسبوك">{I["fb"]}</a>
          <a class="icon-btn" href="{IG}" target="_blank" rel="noopener" aria-label="إنستجرام">{I["ig"]}</a>
          <a class="icon-btn" href="{WA}" target="_blank" rel="noopener" aria-label="واتساب">{I["wa"]}</a>
        </div>
      </div>
      <div><h4>روابط</h4><ul>{nav}</ul></div>
      <div>
        <h4>المعرض الرئيسي</h4>
        <p style="margin:0 0 10px"><a href="{MAPS}" target="_blank" rel="noopener" title="افتح العنوان على خرائط جوجل">{ADDRESS}</a></p>
        <ul>
          <li><a href="tel:+201111934900" dir="ltr">01111934900</a></li>
          <li><a href="tel:+201080477077" dir="ltr">01080477077</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="y">2026</span> Skyline - For UPVC &amp; Shutter</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="تواصل عبر واتساب">{I["wa"]}</a>
<script src="assets/js/projects-data.js?v={ASSET_V}"></script>
<script src="assets/js/main.js?v={ASSET_V}"></script>
{extra_scripts}<script>document.getElementById("y").textContent=new Date().getFullYear()</script>
</body>
</html>
'''


MODAL = f'''<div class="modal" id="video-modal" role="dialog" aria-modal="true" aria-label="مشاهدة الفيديو">
  <div class="modal-box">
    <div class="modal-head"><span class="loc modal-loc"></span><button class="icon-btn modal-close" type="button" aria-label="إغلاق">{I["x"]}</button></div>
    <div class="modal-frame"></div>
    <div class="modal-foot">
      <a class="btn btn-primary btn-sm modal-fb" href="{FB}" target="_blank" rel="noopener">{I["fb"]}شاهد المنشور على فيسبوك</a>
      <p class="note">لو الفيديو ماظهرش هنا (فيسبوك بيمنع تضمين بعض الفيديوهات)، افتحه من الزرار ده.</p>
    </div>
  </div>
</div>
'''

SERVICES = [
    ("slide", "شبابيك وأبواب جرار", "وحدات جرار 2 و4 ضلفة مع سلك متحرك وعجل نحاس."),
    ("pano", "شبابيك بانوراما (منطبق وباندا)", "فتحات عريضة تفتح بالكامل بدون قواطع ثابتة."),
    ("balcony", "تقفيل بلكونات", "تقفيل البلكونة بزجاج دبل عازل للصوت والحرارة."),
    ("shutter", "شيش حصيرة", "شيش حصيرة يدوي للخصوصية والتحكم في الإضاءة."),
    ("net", "سلك متحرك وبليسيه", "حماية من الحشرات والأتربة مع تهوية مستمرة."),
    ("circle", "تصميمات خاصة", "دورانات وأقواس، زي شباك دائري كامل اتنفذ في فيصل."),
]

# ------------------------------------------------------------------ pages
SERVICES_FULL = [
    ("slide", "شبابيك وأبواب جرار", "الحل العملي لأغلب البيوت: حركة ناعمة، توفير في المساحة، وعزل محترم للصوت والتراب.",
     ["جرار 2 و4 ضلفة بمقاسات بانورامية", "عجل جرار نحاس للأوزان التقيلة", "سلك متحرك لتهوية من غير حشرات"]),
    ("pano", "شبابيك بانوراما (منطبق وباندا)", "لو عايز الشباك يفتح على آخره من غير قواطع ثابتة، بنصمم فتحات عريضة بتدخل أقصى إضاءة وتهوية.",
     ["دمج نظام المنطبق (Folding) مع الباندا", "تدعيم داخلي يتحمل الأبعاد الكبيرة", "سلك بليسيه مخفي وسهل الطي"]),
    ("balcony", "تقفيل بلكونات", "بنحوّل البلكونة لمساحة إضافية معزولة عن دوشة الشارع والتراب، وبتفضل منورة طول اليوم.",
     ["زجاج دبل بفراغ عازل 9 مم", "عاكس للخصوصية ومصنفر للأجزاء الثابتة", "تقسيم ذكي بين جرار وثابت"]),
    ("shutter", "شيش حصيرة", "حماية إضافية للشبابيك وتحكم كامل في ضوء الشمس والأتربة، مع طبقة عزل حراري وصوتي زيادة.",
     ["شيش حصيرة يدوي بميكانيزم متين", "خصوصية تامة وقت الحاجة", "حماية أعلى للفتحات"]),
    ("net", "سلك متحرك وبليسيه وثابت", "بنختار نوع السلك المناسب لكل فتحة عشان تستمتع بالهوا من غير ما تقلق من الحشرات.",
     ["سلك متحرك مع الجرار", "سلك بليسيه للمنطبق والمفصلي", "سلك ثابت للفتحات الصغيرة"]),
    ("circle", "تصميمات خاصة", "الدورانات والأقواس والأشكال غير التقليدية — زي شباك دائري كامل بداخله شباك مفصلي.",
     ["تشكيل uPVC بدوران كامل", "الحفاظ على عصب القطاع", "إحكام غلق تام"]),
]

WHY = [
    ("shield", "تأسيس الخدمة الشاقة", "بندعّم القطاع من جوه بحديد مجلفن، ونستخدم عجل نحاس ومفصلات صلب عشان الشغل يعيش سنين من غير أعطال."),
    ("pano", "خامات أصلية", "قطاعات كاترا وكومبين ومايسترو وكرافت لاين، وزجاج سان جوبان — مش أي حاجة والسلام."),
    ("slide", "مقاسات مظبوطة", "بنرفع المقاسات في الموقع قبل أي تنفيذ، عشان كل ضلفة تقفل وتفتح بالظبط."),
    ("net", "تقفيل نضيف", "تقفيل بالسيليكون والفوم وفينش متشطب، عشان مفيش تسريب ولا شكل مش مريح للعين."),
    ("balcony", "حلول على مقاس بيتك", "مش بنركّب شبابيك تقليدية وخلاص؛ بنختار النظام والزجاج واللون المناسبين لكل أوضة."),
    ("circle", "عملاء بيرجعولنا", "أكتر من عميل رجع لنا للمرة التانية والتالتة — وده أكبر شهادة على جودة الشغل."),
]

STEPS = [
    ("استشارة", "نفهم احتياجات بيتك أو مشروعك، ونقترح النظام والقطاع المناسبين."),
    ("معاينة", "رفع مقاسات في الموقع ومراجعة احتياج العزل الحراري والصوتي والخصوصية."),
    ("توريد وتجهيز", "تجهيز الشغل على المقاس بالقطاع والزجاج والإكسسوارات المتفق عليها."),
    ("تركيب وتسليم", "تركيب دقيق وتقفيل محكم، ثم تسليم الشغل وهو بيفتح ويقفل بنعومة."),
]

TRUST = [
    ("أ. أبو القاسم — مدينة نصر", "بعد ما قفلنا بلكونته الأولى، رجع لنا تاني عشان نقفل البلكونة الأكبر."),
    ("م. أحمد رمضان — عين شمس", "التعاون التالت معاه، في مشروع بقطاع كاترا بيج وزجاج مصنفر."),
    ("م. Mozeih Shaker — التجمع الأول", "توريد وتركيب uPVC لفيلا كاملة بقطاع كومبين وزجاج دبل عاكس."),
]


def page_index():
    services_full = "".join(f'<article class="svc-card"><div class="svc-icon">{I[ic]}</div><h3>{t}</h3><p>{d}</p><ul>' + "".join(f"<li>{b}</li>" for b in bl) + '</ul></article>' for ic, t, d, bl in SERVICES_FULL)
    why = "".join(f'<article class="why-card"><div class="svc-icon">{I[ic]}</div><h3>{t}</h3><p>{d}</p></article>' for ic, t, d in WHY)
    steps = "".join(f'<li class="jcard"><span class="jnum">0{i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS))
    trust = "".join(f'<figure class="trust-card"><blockquote>{d}</blockquote><figcaption>{n}</figcaption></figure>' for n, d in TRUST)
    faq_short = "".join(f'<details><summary>{q}</summary><div class="answer">{a}</div></details>' for q, a in FAQ)
    return head("Skyline For UPVC & Shutter — Window & Door System Manufacturer in Egypt", "Skyline سكاي لاين: توريد وتركيب شبابيك وأبواب uPVC، شبابيك جرار وبانوراما، تقفيل بلكونات وشيش حصيرة في جميع محافظات مصر. ضمان 10 سنين على القطاع — المعرض في مدينة نصر.") + header("index.html") + f'''
<section class="hero">
  <canvas id="hero3d" aria-hidden="true"></canvas>
  <div class="container hero-grid">
    <div>
      <p class="eyebrow reveal">Skyline - For UPVC &amp; Shutter</p>
      <h1 class="reveal reveal-d1">أبواب وشبابيك <span class="accent">uPVC</span><br><span class="accent">وشيش الحصيرة</span></h1>
      <p class="hero-lead reveal reveal-d2">توريد وتركيب أبواب وشبابيك uPVC وشيش حصيرة — من المعاينة لحد التسليم.</p>
      <div class="hero-actions reveal reveal-d3">
        <a class="btn btn-primary" href="quote.html">{I["doc"]}اطلب عرض سعر</a>
        <a class="btn btn-ghost" href="projects.html">{I["video"]}شوف مشاريعنا</a>
      </div>
      <p class="slogan reveal reveal-d3"><span>الإختيار الراقي</span> لمن يُقَدِّر التفاصيل</p>
    </div>
    <div class="hero-media reveal reveal-left reveal-d2">
      <figure class="hero-video"><video id="hero-video" poster="assets/video/poster.jpg" autoplay muted loop playsinline preload="auto" disablepictureinpicture disableremoteplayback width="1280" height="720" aria-label="فيديو تعريفي عن مواصفات خامات Skyline"><source src="assets/video/skyline-intro.webm" type="video/webm"><source src="assets/video/skyline-intro.mp4" type="video/mp4"></video></figure>
      <div class="hero-badge"><span class="hb-icon">{I["shield"]}</span><div><strong dir="ltr">1000+</strong><span>مشروع نفّذناه</span></div></div>
    </div>
  </div>
</section>

<section class="stats-band">
  <div class="container stats">
    <div class="stat reveal"><span class="stat-num" data-count="1000" data-suffix="+">0</span><span class="stat-label">مشروع نفّذناه</span></div>
    <div class="stat reveal reveal-d1"><span class="stat-num" data-count="27">0</span><span class="stat-label">بنشتغل في جميع محافظات مصر</span></div>
    <div class="stat reveal reveal-d2"><span class="stat-num" id="fb-followers" data-count="18000" data-format="k">0</span><span class="stat-label">متابع على فيسبوك</span></div>
  </div>
</section>

<section class="section">
  <div class="container about-split" id="about">
    <div class="reveal">
      <p class="eyebrow">من نحن</p>
      <h2 class="h2">شغل uPVC بيتعمل بضمير<br>من أول المعاينة لحد التسليم</h2>
      <p class="lead-p">Skyline - For UPVC &amp; Shutter شركة متخصصة في توريد وتركيب أبواب وشبابيك الـ uPVC والشيش الحصيرة، ومعرضها الرئيسي في مدينة نصر. بدأنا سنة 2019 بفكرة بسيطة: الشباك اللي بيتركب في بيتك لازم يعيش معاك العمر كله.</p>
      <p class="muted">عشان كده بنهتم بالتفاصيل اللي ما بتتشافش بسهولة: التدعيم اللي جوه القطاع، نوع العجل والمفصلات، طريقة التقفيل، ودقة المقاس. كل عملية بنختار لها النظام المناسب — جرار، منطبق، باندا أو مفصلي — والزجاج المناسب للعزل والخصوصية.</p>
      <ul class="check-list">
        <li><strong>قطاعات معروفة:</strong> ديكونيك، كاترا، كومبين، مايسترو، كرافت لاين، وينتك.</li>
        <li><strong>زجاج:</strong> سنجل ودبل وعاكس ومصنفر، وزجاج سان جوبان.</li>
        <li><strong>تأسيس:</strong> حديد مجلفن 1.25 مم، عجل نحاس، مفصلات صلب.</li>
      </ul>
      <div class="hero-actions" style="margin-top:22px"><a class="btn btn-ghost" href="gallery.html">معرض الصور</a></div>
    </div>
    <div class="about-media reveal reveal-left">
      <figure class="am-main"><img src="assets/gallery/1024769387253886-1.jpg" alt="فني Skyline في موقع فيلا بالتجمع الأول" loading="lazy" width="640" height="800"></figure>
      <figure class="am-sub"><img src="assets/gallery/4474589546149572-3.jpg" alt="تقفيل بلكونة من تنفيذ Skyline" loading="lazy" width="640" height="800"></figure>
      <div class="am-tag"><strong>2019</strong><span>سنة التأسيس</span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">خدماتنا</p><h2>حلول متكاملة لأبواب وشبابيك بيتك</h2><p>من الشباك العادي لتقفيل البلكونة والشيش الحصيرة والتصميمات الخاصة — كل نظام بنختاره على حسب المكان والاستخدام.</p></div>
    <div class="svc-cards">{services_full}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">ليه Skyline؟</p><h2>تفاصيل بتفرق معاك على المدى الطويل</h2><p>إحنا مش بنبيع شبابيك وبس — إحنا بنقدم راحة بال. ودي الحاجات اللي بنلتزم بيها في كل مشروع.</p></div>
    <div class="why-grid">{why}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">الرحلة</p><h2>من الاستشارة إلى التسليم.</h2></div>
    <ol class="journey">{steps}</ol>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">من أحدث الشغل</p><h2>مشاريع بالفيديو</h2><p>كل فيديو مكتوب تحته المكان اللي اتنفذ فيه.</p></div>
    <div class="featured" id="featured-grid" data-ids="1170529468969019,1024769387253886,1028796103526905,1605864494534502"></div>
    <p style="margin-top:28px" class="reveal"><a class="btn btn-ghost" href="projects.html">باقي الفيديوهات</a></p>
  </div>
</section>

<section class="section">
  <div class="container mat-split">
    <div class="reveal">
      <p class="eyebrow">الخامات</p>
      <h2 class="h2">مواصفات بنلتزم بيها في كل شغلانة</h2>
      <p class="muted">الجودة بتبدأ من الخامة وبتكمل في التفاصيل. دي المواصفات اللي بننفذ بيها شغلنا، سواء القطاع مصري أو تركي.</p>
    </div>
    <div class="mat-groups reveal reveal-d1">
      <div class="full"><ul class="check-list spec-list">
        <li>جميع القطاعات المصرية أو التركية مدعّمة بحديد مجلفن داير ميدور ضلفة وسلك.</li>
        <li>جميع الإكسسوارات المستخدمة للقطاعات المصرية أو التركية إكسسوارات تركية (<span dir="ltr">KALE</span> أو <span dir="ltr">VORNEX</span>).</li>
        <li>الزجاج المستخدم فرنسي (<span dir="ltr">SAINT GOBAIN</span>) سنجل 6 مم بأعلى سماكة.</li>
        <li>يتم التركيب باستخدام أعلى مواد العزل المستوردة، سواء الفوم أو السيليكون.</li>
        <li><strong>ضمان 10 سنوات على القطاع وضمان 5 سنوات على الإكسسوارات.</strong></li>
        <li>يتم استخدام عجل نحاس وليس فايبر.</li>
        <li>يتم استخدام مفصلات حديد صلب بديلة لمفصلات القطاع المصنوعة من حديد الزهر.</li>
      </ul></div>
      <div><h3>الألوان</h3><ul class="pill-list"><li>أبيض</li><li>أوف وايت</li><li>بيج</li><li>أرو</li><li>خشبي</li><li>رمادي</li><li>أسود</li></ul></div>
      <div><h3>الإكسسوارات</h3><ul class="pill-list"><li>عجل نحاس</li><li>مفصلات صلب</li><li>سبليونات إقفال كاملة</li><li>مقابض فاخرة</li></ul></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container faq-split" id="faq">
    <div class="reveal">
      <p class="eyebrow">أسئلة شائعة</p>
      <h2 class="h2">عندك سؤال؟</h2>
      <p class="muted">جمعنا أكتر الأسئلة اللي بتتكرر. لو سؤالك مش هنا، ابعتلنا على واتساب.</p>
      <div class="hero-actions" style="margin-top:20px"><a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{I["wa"]}اسألنا على واتساب</a></div>
    </div>
    <div class="faq reveal reveal-d1">{faq_short}</div>
  </div>
</section>

<section class="section section-tight">
  <div class="container contact-strip">
    <a class="cs-item cs-map reveal" href="{MAPS}" target="_blank" rel="noopener"><span class="card-icon">{I["pin"]}</span><div><strong>المعرض الرئيسي</strong><span>{ADDRESS}</span><em class="cs-cta cs-cta-map">افتح على خرائط جوجل ←</em></div></a>
    <div class="cs-item reveal reveal-d1"><span class="card-icon">{I["phone"]}</span><div><strong>للحجز والاستفسار</strong><span dir="ltr"><a href="tel:+201111934900">01111934900</a> · <a href="tel:+201080477077">01080477077</a></span></div></div>
    <a class="cs-item cs-wa reveal reveal-d2" href="{WA}" target="_blank" rel="noopener" aria-label="راسلنا على واتساب +20 11 11934900"><span class="card-icon">{I["wa"]}</span><div><strong>واتساب</strong><span dir="ltr">+20 11 11934900</span><em class="cs-cta">ابدأ المحادثة ←</em></div></a>
  </div>
</section>

''' + MODAL + footer('<script src="assets/vendor/three.min.js"></script>\n<script src="assets/js/hero3d.js?v=' + ASSET_V + '"></script>\n')


def page_about():
    return head("عن Skyline | أبواب وشبابيك uPVC", "معلومات عن شركة Skyline - For UPVC & Shutter كما هي منشورة على حساباتها الرسمية.") + header("about.html") + f'''
''' + phero("عن الشركة", "عن الشركة · Skyline", "Skyline - For UPVC &amp; Shutter.", "شركة متخصصة في توريد وتركيب أبواب وشبابيك uPVC والشيش الحصيرة، والمعرض الرئيسي في مدينة نصر.") + f'''
<section class="section" style="padding-top:24px">
  <div class="container two-col">
    <div class="reveal reveal-right">
      <span class="about-logo"><img class="logo-light" src="assets/logo-tagline.png" alt="شعار Skyline — الإختيار الراقي لمن يُقَدِّر التفاصيل" width="896" height="629"><img class="logo-dark" src="assets/logo-tagline-dark.png" alt="" aria-hidden="true" width="896" height="629"></span>
      <p class="quote">«الإختيار الراقي لمن يُقَدِّر التفاصيل» 💎</p>
      <p class="muted">ده الشعار اللي الشركة بتختم بيه منشوراتها. في المشاريع المنشورة، الشغل بيتأسس بنظام «الخدمة الشاقة»: تدعيم داخلي بحديد مجلفن (1.25 مم) بكامل القطاع، وعجل جرار نحاس، ومفصلات صلب، وتقفيل بالسيليكون والفوم.</p>
      <h3 style="margin-top:28px">مواصفاتنا — زي ما الشركة نشرتها</h3>
      <ul class="check-list"><li><strong>عجل نحاس أصلي</strong> — بيتحرك بسهولة وبيعيش سنين من غير صوت ولا تعطل.</li><li><strong>مفصلات صلب معالج</strong> — للفتح والقفل اليومي لسنين.</li><li><strong>حديد داعم سماكة عالية</strong> — للحلق والضلف وضلفة السلك.</li><li><strong>مقابض فاخرة</strong> من موردين مختارين.</li><li><strong>سبليونات إقفال كاملة</strong> — إقفال طولي بطول الضلفة.</li></ul>
      <p class="note">من منشور «ليه نوافذ وأبواب Skyline UPVC هي الاختيار الأفضل؟» — 19 يونيو 2025.</p>
      <h3 style="margin-top:28px">القطاعات المستخدمة في المشاريع المنشورة</h3>
      <ul class="pill-list"><li>كاترا Katra</li><li>كومبين Kompen</li><li>مايسترو Maestro</li><li>كرافت لاين Kraftline</li></ul>
      <h3 style="margin-top:24px">أنواع الزجاج</h3>
      <ul class="pill-list"><li>سنجل</li><li>دبل (فراغ 9 مم)</li><li>عاكس أبيض</li><li>عاكس بني</li><li>مصنفر</li><li>سان جوبان Saint-Gobain</li></ul>
      <h3 style="margin-top:24px">الألوان اللي ظهرت في الشغل</h3>
      <ul class="pill-list"><li>أبيض</li><li>أوف وايت</li><li>بيج</li><li>أرو</li><li>خشبي</li><li>رمادي</li><li>أسود</li></ul>
    </div>
    <div class="reveal reveal-left reveal-d1">
      <table class="fact-table">
        <tr><th>الاسم</th><td>Skyline - For UPVC &amp; Shutter</td></tr>
        <tr><th>النشاط</th><td>تركيب شبابيك (Window installation service)</td></tr>
        <tr><th>سنة التأسيس</th><td>2019</td></tr>
        <tr><th>المعرض الرئيسي</th><td>{ADDRESS}</td></tr>
        <tr><th>تليفون</th><td dir="ltr" style="text-align:right">010 80477077</td></tr>
        <tr><th>واتساب</th><td dir="ltr" style="text-align:right">+20 11 11934900</td></tr>
        <tr><th>اللغات</th><td>العربية والإنجليزية</td></tr>
        <tr><th>تقييم فيسبوك</th><td>100% بيرشحوا الشركة (48 تقييم)</td></tr>
      </table>
      <p class="note" style="margin-top:10px">بيانات التواصل والتقييم من صفحة «About» على فيسبوك، بتاريخ 10 أكتوبر 2026.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0"><div class="container"><div class="cta-band reveal"><div><h2>شوف الشغل بنفسك</h2><p>فيديوهات حقيقية من مواقع التنفيذ، ومكتوب تحت كل فيديو المكان.</p></div><a class="btn btn-primary" href="projects.html">{I["video"]}مشاريعنا</a></div></div></section>
''' + footer()


def page_projects():
    return head("مشاريع شبابيك وأبواب uPVC بالفيديو | Skyline سكاي لاين", "شوف فيديوهات مشاريع Skyline الحقيقية لشبابيك وأبواب uPVC وتقفيل البلكونات والشيش الحصيرة في مدينة نصر والتجمع ومدينتي وأكتوبر والشروق.") + header("projects.html") + f'''
''' + phero("مشاريعنا", "مشاريعنا · فيديو", "فيديوهات من مواقع التنفيذ.", "كل الفيديوهات المنشورة على صفحة Skyline في فيسبوك، ومكتوب تحت كل فيديو المكان. اضغط على الفيديو عشان تشغّله.") + f'''
<section class="section" style="padding-top:16px">
  <div class="container">
    <div class="filters reveal" id="filters" role="group" aria-label="تصفية المشاريع"></div>
    <div class="video-grid" id="video-grid"></div>
    <div class="more-box reveal">
      <p>ممكن تلاقي صور وفيديوهات تانية على الحسابات الرسمية.</p>
      <div class="hero-actions">
        <a class="btn btn-primary btn-sm" href="{FB}/videos" target="_blank" rel="noopener">{I["fb"]}كل الفيديوهات على فيسبوك</a>
        <a class="btn btn-ghost btn-sm" href="{IG}" target="_blank" rel="noopener">{I["ig"]}إنستجرام</a>
      </div>
    </div>
  </div>
</section>
''' + MODAL + footer()


FAQ = [
    ("فين معرضكم؟", f"<p>المعرض الرئيسي: <a href=\"{MAPS}\" target=\"_blank\" rel=\"noopener\">{ADDRESS}</a>.</p>"),
    ("إزاي أحجز معاينة أو أستفسر؟", "<p>للحجز والاستفسار وطلب المعاينات: <span dir=\"ltr\">01111934900</span> – <span dir=\"ltr\">01080477077</span>، أو على واتساب <span dir=\"ltr\">+20 11 11934900</span>.</p>"),
    ('بتشتغلوا في أنهي مناطق؟', '<p>في Skyline بنسعد بتقديم خدماتنا في جميع أنحاء القاهرة الكبرى والمدن الجديدة، ومستعدين للوصول إليك في كل محافظات الجمهورية.</p>'),
    ('أنهي قطاعات uPVC بتستخدموها؟', '<p>في Skyline، بنوفر مجموعة منتقاة من أفضل قطاعات الـ UPVC (الأوروبية، التركية، والمصرية) لتلبية كافة الاحتياجات والأذواق المعمارية والميزانيات، ومن أبرزها:</p><ul><li><strong>قطاع ديكونيك (Deceuninck) البلجيكي:</strong> قمة التكنولوجيا الأوروبية، خيار النخبة لمن يبحث عن أقصى درجات الفخامة، العزل الفائق، والعمر الافتراضي الطويل.</li><li><strong>قطاع كومبين (Kompen) التركي:</strong> فخامة القطاعات التركية المعتمدة وأعلاها متانة وقوة تحمل.</li><li><strong>قطاع كاترا (Katra):</strong> الصلابة المثالية والحل الأمثل للمساحات والفتحات الكبيرة.</li><li><strong>قطاعات كرافت لاين (Kraftline)، مايسترو (Maestro)، ووينتك (Wintech):</strong> خيارات متميزة جداً وعملية تجمع بين الجودة العالية والتكلفة الاقتصادية.</li></ul>'),
    ("إيه أنواع الزجاج المتاحة؟", "<p>في المشاريع المنشورة: زجاج سنجل، ودبل بفراغ 9 مم، وعاكس أبيض وبني، ومصنفر للحمامات والخصوصية، وزجاج سان جوبان (Saint-Gobain).</p>"),
    ("إيه أنظمة الفتح اللي بتنفذوها؟", "<p>جرار (2 و4 ضلفة)، مفصلي، منطبق، باندا، وتصميمات خاصة زي الشباك الدائري. ومعاها سلك متحرك أو بليسيه أو ثابت، وشيش حصيرة يدوي.</p>"),
    ('بتعملوا تقفيل بلكونات؟', '<p>بكل تأكيد! تقفيل البلكونات بالـ UPVC هو واحد من أهم تخصصاتنا والأكثر طلباً في Skyline.</p><p>إحنا بنعتبر تقفيل البلكونة مش مجرد تركيب شبابيك، ده استثمار ذكي لتحويل مساحة مهدرة أو معرضة للتراب والدوشة لـ "غرفة إضافية" نظيفة، هادية، ومريحة جداً للاستخدام طول السنة.</p><p><strong>ليه تقفل بلكونتك مع Skyline؟</strong></p><ul><li><strong>عزل تام للأتربة والضوضاء:</strong> بفضل التقفيل الهندسي المحكم واستخدام الزجاج الدبل (سان جوبان)، بنفصلك تماماً عن إزعاج الشارع.</li><li><strong>تأسيس يتحمل ضغط الهواء:</strong> لأن البلكونات (خاصة في الأدوار العالية) بتتعرض لتيارات هواء قوية، بندعم قطاعاتنا بحديد مجلفن (سمك 1.25 مم) لضمان أقصى درجات الصلابة والأمان.</li><li><strong>تصميمات تناسب مساحتك:</strong> بنوفر كل الحلول (أنظمة الجرار لتوفير المساحة، الشباك المنطبق "Folding" لفتح البلكونة بالكامل، والأنظمة الثابتة)، بالإضافة لتوفير "سلك متحرك أو بليسيه" للتهوية بدون حشرات.</li><li><strong>مقاومة العوامل الجوية:</strong> قطاعاتنا لا تتأثر بحرارة الشمس أو الأمطار، ولا تتعرض للصدأ أو التآكل.</li></ul>'),
    ("إزاي بيتأسس الشغل؟", "<p>حسب المنشورات: تدعيم داخلي بحديد مجلفن (1.25 مم) بكامل القطاع، عجل جرار نحاس، مفصلات صلب، وتقفيل بالسيليكون والفوم.</p>"),
    ('بتعملوا حاجة غير الشبابيك؟', '<p>بكل تأكيد! في Skyline نحن نقدم حلولاً متكاملة لتشطيب وتجهيز بيتك بأعلى معايير الجودة، ولا نقتصر على الشبابيك فقط. تشمل خدماتنا:</p><ul><li><strong>الأبواب (UPVC):</strong> نصمم وننفذ أبواب الغرف، الحمامات، والبلكونات. تتميز بعزلها التام للصوت والمياه، ولا تتأثر بالرطوبة أو الحشرات نهائياً مقارنة بالأبواب الخشبية التقليدية.</li><li><strong>مطابخ الألومنيوم والكلادينج:</strong> نصنع مطابخ تجمع بين المتانة الفائقة والشكل المودرن. نؤسس المطبخ بقوائم ألومنيوم صلبة للخدمة الشاقة، مع أرفف وأرضيات بسمك (4 مم) لتحمل الأوزان، وواجهات "كلادينج" عصرية مقاومة للحرارة والمياه وسهلة التنظيف.</li><li><strong>الشيش حصيرة (Shutters):</strong> نوفر أنظمة الشيش حصيرة (اليدوية والمزودة بموتور للتحكم عن بعد)، والتي تمنحك أماناً إضافياً، عزلاً حرارياً ممتازاً، وتحكماً كاملاً في درجة الإضاءة والخصوصية.</li><li><strong>تقفيل البلكونات والقواطع الداخلية:</strong> نحول البلكونات والمساحات المهدرة إلى غرف معزولة تماماً، وننفذ قواطع (Partitions) لتقسيم المساحات الواسعة في المنازل أو الشركات بشياكة وخصوصية.</li><li><strong>التصميمات المعمارية الخاصة:</strong> ننفذ أصعب الأشكال الهندسية مثل الدورانات، الأقواس، وأنظمة الفتح الكبيرة (المنطبق والباندا) للواجهات البانورامية.</li></ul>'),
    ("الأسعار ومدة الضمان كام؟", "<p>الضمان 10 سنوات على القطاع و5 سنوات على الإكسسوارات. السعر بيتحدد حسب المقاسات والقطاع والزجاج — <a href=\"quote.html\">اطلب عرض سعر</a>.</p>"),
]


def page_faq():
    items = "".join(f'<details class="reveal"><summary>{q}</summary><div class="answer">{a}</div></details>' for q, a in FAQ)
    return head("الأسئلة الشائعة | Skyline uPVC", "إجابات مبنية على المعلومات المنشورة رسمياً من Skyline.") + header("faq.html") + f'''
''' + phero("الأسئلة الشائعة", "الأسئلة الشائعة", "أسئلة بتتكرر.", "الإجابات هنا مبنية بس على المعلومات اللي الشركة نشرتها على حساباتها الرسمية.") + f'''
<section class="section" style="padding-top:24px"><div class="container"><div class="faq">{items}</div></div></section>
''' + footer()


def page_contact():
    from urllib.parse import quote
    q = quote(MAPQ)
    return head("تواصل مع Skyline لشبابيك uPVC — مدينة نصر، القاهرة", "اتصل بـ Skyline لشبابيك وأبواب uPVC: 01111934900 – 01080477077، واتساب، والمعرض في شارع حسن مأمون، مدينة نصر، القاهرة.") + header("contact.html") + f'''
''' + phero("تواصل", "تواصل · معاينة واستفسار", "اتواصل مع Skyline.", "للحجز والاستفسار وطلب المعاينات — بالتليفون أو واتساب أو زورنا في المعرض.") + f'''
<section class="section" style="padding-top:24px">
  <div class="container contact-grid">
    <div class="contact-side">
    <div class="card quote-cta reveal"><div><strong>محتاج عرض سعر؟</strong><span class="muted">ابعت المقاسات وصورة المكان من صفحة طلب عرض السعر.</span></div><a class="btn btn-primary btn-sm" href="quote.html">{I["doc"]}طلب عرض سعر</a></div>
    <div class="contact-list">
      <a class="card contact-item reveal" href="tel:+201111934900"><span class="card-icon">{I["phone"]}</span><div><strong>اتصال</strong><span>01111934900</span></div></a>
      <a class="card contact-item reveal reveal-d1" href="tel:+201080477077"><span class="card-icon">{I["phone"]}</span><div><strong>اتصال</strong><span>01080477077</span></div></a>
      <a class="card contact-item reveal reveal-d1" href="{WA}" target="_blank" rel="noopener"><span class="card-icon">{I["wa"]}</span><div><strong>واتساب</strong><span>+20 11 11934900</span></div></a>
      <a class="card contact-item reveal reveal-d2" href="{FB}" target="_blank" rel="noopener"><span class="card-icon">{I["fb"]}</span><div><strong>فيسبوك</strong><span>skylineupvcwindow</span></div></a>
      <a class="card contact-item reveal reveal-d3" href="{IG}" target="_blank" rel="noopener"><span class="card-icon">{I["ig"]}</span><div><strong>إنستجرام</strong><span>@skylinepvc</span></div></a>
    </div>
    <div class="card map-card reveal reveal-d1">
      <iframe title="خريطة المعرض الرئيسي" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP_EMBED}"></iframe>
      <div class="map-foot">
        <div><strong style="display:flex;gap:6px;align-items:center">{I["pin"].replace('<svg', '<svg width="18" height="18" style="color:var(--brand)"')}المعرض الرئيسي</strong><span class="muted">{ADDRESS}</span></div>
        <a class="btn btn-ghost btn-sm" href="{MAPS}" target="_blank" rel="noopener">{I["ext"]}افتح في خرائط جوجل</a>
      </div>
    </div>
    </div>
  </div>
  </section>
''' + footer()


QUOTE_FORM = f'''    <form class="card request-form reveal" id="wa-form" novalidate>
      <p class="eyebrow">نموذج طلب عرض سعر</p>
      <h2>ابعت بياناتك والمقاسات</h2>
      <div class="form-grid">
        <label>الاسم بالكامل *<input name="name" required autocomplete="name"></label>
        <label>رقم الموبايل *<input name="phone" required inputmode="tel" autocomplete="tel" dir="ltr"></label>
        <label>المنطقة<input name="area" placeholder="مثلاً: مدينة نصر"></label>
        <label>نوع القطاع<input name="profile" placeholder="مثلاً: كاترا، كومبين، أو سيبها لترشيحنا"></label>
        <label>اللون<input name="color" placeholder="أبيض، بيج، أرو، خشبي، رمادي، أسود…"></label>
        <div class="full upload-field">
          <span class="upload-label">صورة المقاسات</span>
          <label class="dropzone" id="dropzone">
            <input type="file" name="photo" id="photo" accept="image/*" capture="environment">
            <span class="dz-icon">{I["upload"]}</span>
            <span class="dz-text"><strong>ارفع صورة المقاسات</strong><span>اسحب الصورة هنا أو اضغط للاختيار — JPG / PNG لحد 10 ميجا</span></span>
          </label>
          <div class="upload-preview" id="upload-preview" hidden>
            <img alt="معاينة صورة المقاسات" id="preview-img">
            <div><strong id="preview-name"></strong><span class="muted" id="preview-size"></span></div>
            <button type="button" class="icon-btn" id="remove-photo" aria-label="إزالة الصورة">{I["x"]}</button>
          </div>
        </div>
        <label class="full">تفاصيل (اختياري)<textarea name="details" rows="4" placeholder="اكتب ملاحظاتك"></textarea></label>
      </div>
      <p class="form-error" id="wa-error" role="alert" hidden></p>
      <div class="form-success" id="wa-success" role="status" hidden></div>
      <div class="hero-actions"><button class="btn btn-primary" type="submit">{I["wa"]}ابعت الطلب على واتساب</button><a class="btn btn-ghost" href="tel:+201111934900">{I["phone"]}اتصل بدل كده</a></div>
      <p class="note">الطلب بيروح على رقم واتساب الشركة المنشور على فيسبوك <span dir="ltr">+20 11 11934900</span>. على الموبايل الصورة بتتبعت مع الرسالة مباشرة؛ على الكمبيوتر هتتفتح المحادثة وتلزق الصورة فيها. مفيش بيانات بتتخزن على الموقع.</p>
    </form>
'''


def page_quote():
    return head("اطلب عرض سعر شبابيك وأبواب uPVC | Skyline سكاي لاين", "اطلب عرض سعر لشبابيك وأبواب uPVC وتقفيل البلكونات والشيش الحصيرة من Skyline — ابعت المقاسات وصورة المكان على واتساب.") + header("quote.html") + phero("طلب عرض سعر", "عرض سعر · معاينة", "اطلب عرض سعر.", "املا البيانات وارفع صورة المقاسات، والطلب هيوصل لفريق Skyline على واتساب.") + f'''
<section class="section" style="padding-top:24px">
  <div class="container quote-grid">
{QUOTE_FORM}
    <aside class="quote-side">
      <div class="card reveal reveal-d1"><h3>إزاي تصوّر المقاسات؟</h3><ul class="steps-list"><li><span>1</span>اكتب العرض × الارتفاع بالسنتيمتر لكل فتحة على ورقة.</li><li><span>2</span>ارفع الصورة في النموذج وابعت الطلب.</li></ul></div>
      <div class="card reveal reveal-d2"><h3>أو كلّمنا مباشرة</h3><p class="muted" style="margin-bottom:12px">للحجز والاستفسار وطلب المعاينات:</p><div class="hero-actions"><a class="btn btn-ghost btn-sm" href="tel:+201111934900" dir="ltr">01111934900</a><a class="btn btn-ghost btn-sm" href="tel:+201080477077" dir="ltr">01080477077</a></div></div>
    </aside>
  </div>
</section>
''' + footer()


GALLERY = [("1160000315931806", "قبل وبعد — تركيب شباك uPVC في موقع عميل", "صورة منشورة على صفحة فيسبوك — 17 يونيو 2025", "")]


def page_gallery():
    fb = "".join(f'<figure class="gitem reveal {cls}"><button type="button" class="gbtn" data-full="assets/gallery/{i}.jpg" data-cap="{t}"><img src="assets/gallery/{i}.jpg" alt="{t}" loading="lazy"></button><figcaption><strong>{t}</strong><span>{d}</span><a href="https://www.facebook.com/photo.php?fbid={i}" target="_blank" rel="noopener">{I["ext"]}المنشور الأصلي</a></figcaption></figure>' for i, t, d, cls in GALLERY)
    return head("صور شبابيك uPVC وتقفيل بلكونات من مواقعنا | Skyline", "معرض صور حقيقية لشبابيك وأبواب uPVC من مواقع تنفيذ Skyline: شبابيك جرار، بانوراما، تقفيل بلكونات وشيش حصيرة.") + header("gallery.html") + phero("معرض الصور", "معرض الصور", "شبابيك وأبواب من شغلنا.", "لقطات من مواقع التنفيذ الحقيقية — مأخوذة من فيديوهات وصور صفحة Skyline على فيسبوك.") + f'''
<section class="section" style="padding-top:24px">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">من مواقع التنفيذ</p><h2>لقطات من المشاريع</h2><p>اضغط على أي صورة لتكبيرها. الفيديو الكامل لكل مشروع في <a href="projects.html">صفحة المشاريع</a>.</p></div>
    <div class="gallery-grid" id="gallery-grid"></div>
    <div class="section-head reveal" style="margin-top:56px"><p class="eyebrow">من صفحة فيسبوك</p><h2>قبل وبعد</h2></div>
    <div class="gallery-fb">{fb}</div>
    <div class="more-box reveal"><p>صور أكتر على الحسابات الرسمية.</p><div class="hero-actions"><a class="btn btn-primary btn-sm" href="{FB}/photos" target="_blank" rel="noopener">{I["fb"]}صور فيسبوك</a><a class="btn btn-ghost btn-sm" href="{IG}" target="_blank" rel="noopener">{I["ig"]}إنستجرام</a></div></div>
  </div>
</section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="عرض الصورة"><button class="icon-btn lb-close" type="button" aria-label="إغلاق">{I["x"]}</button><figure><img alt=""><figcaption></figcaption></figure></div>
''' + footer()


def page_reviews():
    return head("آراء العملاء في شبابيك وأبواب uPVC | Skyline سكاي لاين", "تقييمات وآراء عملاء Skyline الحقيقية من صفحة فيسبوك الرسمية — شبابيك وأبواب uPVC وتقفيل بلكونات وشيش حصيرة.") + header("reviews.html") + phero(
        "آراء العملاء", "آراء العملاء", "عملاؤنا بيقولوا إيه.", "تقييمات حقيقية كتبها عملاؤنا على صفحة Skyline الرسمية على فيسبوك، وبتتحدّث هنا تلقائياً.", extra='''
  <div class="rv-hero-badge reveal reveal-d3" aria-label="100% من العملاء بيرشحوا Skyline"><p class="rv-hero-pct"><strong id="rv-pct-hero">100%</strong><span>ترشيح</span></p><div class="rv-arc" aria-hidden="true"><i style="--i:0"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.85 6 6.55.78-4.84 4.5 1.28 6.52L12 17.18 6.16 20.4l1.28-6.52L2.6 9.38l6.55-.78z"/></svg></i><i style="--i:1"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.85 6 6.55.78-4.84 4.5 1.28 6.52L12 17.18 6.16 20.4l1.28-6.52L2.6 9.38l6.55-.78z"/></svg></i><i style="--i:2"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.85 6 6.55.78-4.84 4.5 1.28 6.52L12 17.18 6.16 20.4l1.28-6.52L2.6 9.38l6.55-.78z"/></svg></i><i style="--i:3"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.85 6 6.55.78-4.84 4.5 1.28 6.52L12 17.18 6.16 20.4l1.28-6.52L2.6 9.38l6.55-.78z"/></svg></i><i style="--i:4"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.85 6 6.55.78-4.84 4.5 1.28 6.52L12 17.18 6.16 20.4l1.28-6.52L2.6 9.38l6.55-.78z"/></svg></i></div></div>''') + f'''
<section class="section" style="padding-top:24px">
  <div class="container">
    <div class="rv-summary reveal" id="rv-summary" hidden>
      <div class="rv-count"><strong id="rv-count">—</strong><span>تقييم على فيسبوك</span></div>
      <a class="btn btn-ghost btn-sm" href="{FB}/reviews" target="_blank" rel="noopener">{I["fb"]}كل التقييمات على فيسبوك</a>
    </div>
    <div class="reviews-grid" id="reviews-grid" aria-live="polite"></div>
    <div class="rv-load" id="rv-load" hidden><button type="button" class="btn btn-ghost" id="rv-load-btn">عرض المزيد من التقييمات <span class="rv-load-n" id="rv-load-n"></span></button></div>
    <div class="rv-empty reveal" id="rv-empty" hidden>
      <span class="card-icon">{I["fb"]}</span>
      <h2>التقييمات على صفحتنا في فيسبوك</h2>
      <p>اقرأ آراء عملائنا مباشرةً على صفحة Skyline الرسمية.</p>
      <a class="btn btn-primary btn-sm" href="{FB}/reviews" target="_blank" rel="noopener">{I["fb"]}شوف التقييمات</a>
    </div>
    <div class="more-box reveal"><p>اتعاملت معانا؟ رأيك بيفرق معانا ومع اللي جايين بعدك.</p><div class="hero-actions"><a class="btn btn-primary btn-sm" href="{FB}/reviews" target="_blank" rel="noopener">{I["fb"]}اكتب تقييمك</a><a class="btn btn-ghost btn-sm" href="quote.html">{I["doc"]}اطلب عرض سعر</a></div></div>
  </div>
</section>
''' + footer()


REDIRECT = '''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>Skyline</title>
<meta name="robots" content="noindex, follow"><meta http-equiv="refresh" content="0; url=index.html#about"><link rel="canonical" href="index.html#about">
<script>location.replace("index.html#about")</script></head><body><a href="index.html#about">عن الشركة</a></body></html>
'''


def write_seo_files():
    import datetime
    today = datetime.date.today().isoformat()
    urls = [("", "1.0", "weekly"), ("projects.html", "0.8", "weekly"), ("gallery.html", "0.7", "monthly"),
            ("quote.html", "0.8", "monthly"), ("reviews.html", "0.7", "weekly"), ("contact.html", "0.7", "monthly")]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod><changefreq>{f}</changefreq><priority>{pr}</priority></url>\n" for u, pr, f in urls) + "</urlset>\n"
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")


def main():
    write_seo_files()
    import re
    data = (ROOT / "assets/js/projects-data.js").read_text(encoding="utf-8")
    n = len(re.findall(r'\bid: "', data))
    pages = {"quote.html": page_quote(), "gallery.html": page_gallery(), "index.html": page_index().replace("{n}", str(n)), "about.html": REDIRECT, "projects.html": page_projects(),
             "faq.html": REDIRECT.replace("#about", "#faq").replace("عن الشركة", "الأسئلة الشائعة"), "contact.html": page_contact(), "reviews.html": page_reviews()}
    for name, html in pages.items():
        canon = SITE if name == "index.html" else SITE + name
        html = html.replace("__CANON__", canon).replace("__LD__", jsonld() if name == "index.html" else "")
        (ROOT / name).write_text(html, encoding="utf-8")
        print("wrote", name)


if __name__ == "__main__":
    main()
