#!/usr/bin/env python3
"""Static site generator for CatCalc. Run: python3 build.py  -> writes ./docs"""
import json, os, shutil, html, datetime, sys
from pathlib import Path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from foods import FOODS, FOOD_GUIDANCE, FOOD_SOURCES, related_foods
from names import NAMES

ROOT = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(ROOT, "config.json")))
OUT = os.path.join(ROOT, "docs")
URL = C["site_url"].rstrip("/")
NAME = C["site_name"]
DATES = json.loads(Path(ROOT, "src", "content_dates.json").read_text(encoding="utf-8"))
PLANNER_STATUS = "Coming soon / not yet available"
pages = []  # for sitemap
e = html.escape

def rel(path):  # absolute path within site
    from urllib.parse import urlparse
    base = urlparse(URL).path.rstrip("/")
    return base + path

VERD = {"no": ("Avoid", "Do not feed · read the specific risk", "bad"), "caution": ("Caution", "Preparation and dietary limits apply", "warn"), "yes": ("Small treats", "Plain preparation and small portions", "good")}

def content_date(path):
    return DATES.get(path, DATES.get('/can-cats-eat/*/') if path.startswith('/can-cats-eat/') else None)

def illustration(name, alt, eager=False, hero=False):
    widths, height = ((600, 1200), 600) if name == "home-cat-tools" else ((480, 960), 540)
    base = rel('/assets/img/illustrations/' + name)
    size = "(max-width: 600px) 284px, 412px" if name == "home-cat-tools" else ("(max-width: 600px) 160px, 320px" if hero else "(max-width: 600px) 284px, 320px")
    return f'<picture class="illustration {"home-art" if name == "home-cat-tools" else "tool-art"} {"intro-art" if hero else ""}"><source type="image/webp" srcset="{base}-{widths[0]}.webp {widths[0]}w, {base}-{widths[1]}.webp {widths[1]}w" sizes="{size}"><img src="{base}-{widths[0]}.webp" width="{widths[1]}" height="{height}" loading="{"eager" if eager else "lazy"}" decoding="async" alt="{e(alt)}"></picture>'

def amazon(q, label):
    tag = C.get("amazon_associates_tag")
    if not tag: return ""
    from urllib.parse import quote_plus
    return f'<li><a rel="sponsored nofollow noopener" target="_blank" href="https://www.amazon.com/s?k={quote_plus(q)}&tag={e(tag)}">{e(label)}</a></li>'

def gear(items):
    lis = "".join(amazon(q, l) for q, l in items)
    if not lis: return ""
    return f'<aside class="box gear"><h3>Helpful gear</h3><ul>{lis}</ul><p class="small">As an Amazon Associate we earn from qualifying purchases.</p></aside>'

def product_box():
    u = C.get("digital_product_url")
    if not u: return ""
    return f'<aside class="box product"><h3>🐾 {e(C["digital_product_title"])}</h3><p>Track feeding, weight, vet visits and vaccines on one printable page.</p><a class="btn" href="{e(u)}" target="_blank" rel="noopener">Get it</a></aside>'

def ad_slot():
    # Auto ads are controlled by AdSense; empty manual-slot divs serve no purpose.
    return ""

def layout(path, title, desc, body, schema=None, not_found=False):
    head_extra = ""
    if C.get("adsense_publisher_id"):
        head_extra += f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={e(C["adsense_publisher_id"])}" crossorigin="anonymous"></script>\n'
    if C.get("google_site_verification"):
        head_extra += f'<meta name="google-site-verification" content="{e(C["google_site_verification"])}">\n'
    if schema:
        head_extra += f'<script type="application/ld+json">{json.dumps(schema)}</script>\n'
    social = ""
    if C.get("tiktok_url"): social += f' · <a href="{e(C["tiktok_url"])}" rel="noopener" target="_blank">TikTok</a>'
    if C.get("douyin_url"): social += f' · <a href="{e(C["douyin_url"])}" rel="noopener" target="_blank">Douyin</a>'
    canon = URL + path
    navigation = ''.join(f'<a href="{rel(p)}"' + (' aria-current="page"' if path == p or (p == '/can-cats-eat/' and path.startswith(p)) else '') + f'>{label}</a>' for p, label in [("/cat-age-calculator/", "Age"), ("/cat-calorie-calculator/", "Calories"), ("/can-cats-eat/", "Can cats eat…?"), ("/cat-name-generator/", "Names"), ("/cat-care-planner/", "Shop")])
    canonical = '<meta name="robots" content="noindex">' if not_found else f'<link rel="canonical" href="{e(canon)}">'
    share_image = URL + '/assets/img/01-cover-coming-soon.jpg'
    doc = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{canonical}
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website"><meta property="og:url" content="{e(canon)}">
<meta property="og:image" content="{share_image}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="1200">
<meta property="og:image:alt" content="Cat Care Planner preview, coming soon">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{share_image}"><meta name="twitter:image:alt" content="Cat Care Planner preview, coming soon">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐱</text></svg>">
<link rel="stylesheet" href="{rel('/assets/style.css')}">
<script defer src="{rel('/assets/tools.js')}"></script>
{head_extra}</head><body><a class="skip" href="#content">Skip to content</a>
<header class="top"><div class="wrap"><a class="logo" href="{rel('/')}">🐱 {e(NAME)}</a>
<nav aria-label="Main">{navigation}</nav></div></header>
<main class="wrap" id="content">{body}{'' if not_found else product_box()}</main>
<footer><div class="wrap"><p>{e(NAME)} provides general information only and is not a substitute for veterinary advice. If you think your cat ate something toxic, call your vet, the ASPCA Animal Poison Control Center (888-426-4435, fee may apply) or Pet Poison Helpline (855-764-7661).</p>
<p><a href="{rel('/cat-care-planner/')}">Shop</a> · <a href="{rel('/about/')}">About</a> · <a href="{rel('/contact/')}">Contact</a> · <a href="{rel('/terms/')}">Terms</a> · <a href="{rel('/privacy/')}">Privacy</a> · <a href="{rel('/refund-policy/')}">Refund Policy</a>{social} · © {datetime.date.today().year} {e(NAME)}</p></div></footer>
</body></html>"""
    target = Path(OUT, "404.html") if not_found else Path(OUT, path.strip("/"), "index.html")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(doc, encoding="utf-8")
    if not not_found: pages.append((canon, content_date(path)))

def faq_schema(qas):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}

# ---------------- pages ----------------
def home():
    cards = [("/cat-age-calculator/", "🎂 Cat Age Calculator", "Estimate your cat's age in human years and find its life stage."),
             ("/cat-calorie-calculator/", "🍽️ Cat Calorie & Food Calculator", "How many calories and grams of food your cat needs per day."),
             ("/can-cats-eat/", "🥕 Can Cats Eat…?", f"Quick yes / no / caution answers for {len(FOODS)} common human foods."),
             ("/cat-name-generator/", "✨ Cat Name Generator", "Hundreds of name ideas: orange, black, Halloween, food and cute names."),
             ("/cat-care-planner/", "🎃 Printable Cat Care Planner", PLANNER_STATUS + ". Preview a planned 22-page care tracker.")]
    c = "".join(f'<a class="card" href="{rel(p)}"><h2>{t}</h2><p>{d}</p></a>' for p, t, d in cards)
    toxic = "".join(f'<li><a href="{rel("/can-cats-eat/"+s+"/")}">{e(n)}</a> · {e(FOOD_GUIDANCE[s][0])}: {e(FOOD_GUIDANCE[s][1])}</li>' for s, n, v, *_ in FOODS if v == "no" or s in ("raw-fish", "raw-eggs"))
    body = f"""<section class="hero"><h1>Free, simple tools for cat owners</h1>
<p>Fast calculators and clear answers. No sign-up, nothing to install, works on your phone.</p>{illustration('home-cat-tools', 'An orange tabby beside a calculator, food bowl and care calendar.', True)}</section>
<div class="grid">{c}</div>{ad_slot()}
<section class="box"><h2>Foods to avoid or prepare carefully</h2>{illustration('home-food-awareness', 'An orange cat kept away from chocolate, onions and grapes in a closed cupboard.')}<ul>{toxic}</ul>
<p>Also dangerous: <strong>lilies</strong> (true lilies and daylilies). Even pollen or vase water can cause kidney failure in cats, so keep them out of homes with cats.</p></section>"""
    layout("/", f"{NAME}: Free Cat Age, Calorie & Food Safety Tools", "Free cat tools: cat age in human years, daily calorie and food calculator, can cats eat this food, and a cat name generator.", body,
           {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": URL + "/"})

def age():
    qas = [("How old is my cat in human years?", "This informal approximation uses about 15 human years at age 1, 24 at age 2, then 4 more per cat year. It is not a clinical measurement or an endorsed AAHA/AAFP formula."),
           ("What are the life stages of a cat?", "Kitten: birth to 1 year. Young adult: 1-6 years. Mature adult: 7-10 years. Senior: over 10 years (2021 AAHA/AAFP Feline Life Stage Guidelines)."),
           ("How long do indoor cats live?", "Many indoor cats live into their mid-teens, and some reach 20 or more. Regular vet checks become more important from the senior stage.")]
    rows = "".join(f"<tr><td>{y}</td><td>{15 if y==1 else 24+4*(y-2)}</td></tr>" for y in range(1, 21))
    faq = "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in qas)
    body = f"""<h1>Cat Age Calculator: Cat Years to Human Years</h1>
<p class="lead">Enter your cat's age to see the human equivalent and life stage.</p>
{illustration('cat-age-hero', 'An orange tabby growing from kitten to adult beside a calendar.', True, True)}
<form class="tool" id="age-tool" novalidate>
<div class="fields"><div><label for="ay">Years</label><input type="number" id="ay" min="0" max="35" step="1" value="3" required aria-describedby="age-range"></div>
<div><label for="am">Months</label><input type="number" id="am" min="0" max="11" step="1" value="0" required aria-describedby="age-range"></div></div>
<p class="small" id="age-range">Whole numbers only: years 0–35, months 0–11. Approximation, not a clinical age assessment.</p>
<button type="submit" class="btn" id="ago">Calculate</button><p class="error" id="aerror" role="alert"></p>
<div class="result" id="ares" aria-live="polite"></div></form>{ad_slot()}
<h2>How the calculation works</h2><p>Cats mature very fast: the first year equals about 15 human years and the second year adds about 9 more. After age 2, each cat year equals roughly 4 human years. Ages under 1 year are approximate and based on typical kitten development.</p>
<h2>Cat age chart</h2><table><caption>Approximate human-year equivalents</caption><thead><tr><th scope="col">Cat age (years)</th><th scope="col">Human age (years)</th></tr></thead><tbody>{rows}</tbody></table>
{illustration('cat-life-stages', 'Four illustrations showing a cat at different life stages.')}<p class="small">Life stages: kitten, young adult, mature adult and senior.</p>
<h2>FAQ</h2>{faq}
<p class="small">Life stage definitions: <a href="https://www.aaha.org/resources/2021-aaha-aafp-feline-life-stage-guidelines/feline-life-stage-definitions/">2021 AAHA/AAFP guidelines</a>. These definitions are separate from the informal human-year estimate above.</p>
{gear([("cat senior supplements", "Senior cat care"), ("cat birthday toy", "Cat birthday toys")])}
"""
    layout("/cat-age-calculator/", "Cat Age Calculator: Cat Years to Human Years (Chart)", "Estimate cat years in human years with an informal approximation. Includes a 1-20 year chart and separately sourced cat life stage definitions.", body, faq_schema(qas))

def calories():
    qas = [("How many calories does a cat need per day?", "A typical 4.5 kg (10 lb) neutered indoor adult cat needs roughly 215-260 kcal per day (inactive to neutered-adult factor), but needs vary. The calculator uses RER = 70 x (weight in kg)^0.75 multiplied by a life-stage factor."),
           ("How much wet or dry food should I feed my cat?", "Divide your cat's daily calorie needs by the calories in the food (printed on the bag or can as kcal/kg, kcal/cup or kcal/can)."),
           ("How many treats can a cat have?", "Keep treats under about 10% of the total daily calorie budget. Subtract treat calories from the food allowance rather than adding them on top.")]
    faq = "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in qas)
    body = f"""<h1>Cat Calorie Calculator & Daily Food Amount</h1>
<p class="lead">Estimate how many calories your cat needs and how much of your food to serve.</p>
{illustration('cat-calorie-hero', 'An orange cat beside a pet scale and a kitchen scale for food.', True, True)}
<form class="tool" id="cal-tool" novalidate>
<label for="cw">Weight</label><div class="input-unit"><input type="number" id="cw" min="0.3" max="15" step="any" value="4.5" required aria-describedby="weight-range">
<select id="cu" aria-label="Weight unit"><option value="kg">kg</option><option value="lb">lb</option></select></div>
<p class="small" id="weight-range">Supported range: 0.3–15 kg. Ask your vet about weights outside this calculator's range.</p>
<label for="cf">Cat type</label><select id="cf">
<option value="1.2">Neutered / spayed</option><option value="1.4">Intact adult</option>
<option value="1.0">Inactive adult</option><option value="0.8">Weight loss</option>
<option value="2.5">Kitten under 1 year</option></select>
<p class="small">For weight loss, use ideal weight with your vet's guidance.</p>
<label for="ck">Food calories (optional)</label><div class="input-unit"><input type="number" id="ck" min="1" max="10000" step="1" placeholder="e.g. 3800" aria-describedby="food-range">
<select id="ckunit" aria-label="Food calorie unit"><option value="kg">kcal/kg</option><option value="cup">kcal/cup</option><option value="can">kcal/can</option></select></div>
<p class="small" id="food-range">Copy the label: 1–10000 kcal/kg, whole numbers. Leave blank to skip food conversion.</p>
<button type="submit" class="btn" id="cgo">Calculate</button><p class="error" id="cerror" role="alert"></p>
<div class="result" id="cres" aria-live="polite"></div></form>{ad_slot()}
<h2>The formula</h2><p>Vets start from the <strong>Resting Energy Requirement</strong>: RER = 70 × (body weight in kg)<sup>0.75</sup>. This is multiplied by a factor for life stage and activity, for example 1.2 for a neutered adult or 0.8 for weight loss. These are starting points; adjust based on your cat's body condition and ask your vet, especially for weight loss, pregnancy or illness.</p>
<p class="small">Source: <a href="https://www.aaha.org/resources/2021-aaha-nutrition-and-weight-management-guidelines/">AAHA nutrition and weight management guidelines</a>. The estimate is a starting point, not an individual feeding prescription. Treats are part of the total budget.</p>
{illustration('cat-food-measurements', 'A kitchen scale, measuring cup and wet food can used to measure cat food.')}
<h2>FAQ</h2>{faq}
{gear([("kitchen scale grams", "Digital kitchen scale (weigh food accurately)"), ("slow feeder cat bowl", "Slow feeder bowls"), ("cat water fountain", "Cat water fountains")])}
"""
    layout("/cat-calorie-calculator/", "Cat Calorie Calculator: How Much Should I Feed My Cat?", "Estimate daily cat calories with RER and a life-stage factor. Convert food-label calories to a starting food allowance and include treats in the total.", body, faq_schema(qas))

def foods():
    groups = ""
    for v in ("no", "caution", "yes"):
        lab, sub, cls = VERD[v]
        items = "".join(f'<li><a href="{rel("/can-cats-eat/"+s+"/")}">{e(n)}</a> <span class="small">{e(FOOD_GUIDANCE[s][0])} · {e(FOOD_GUIDANCE[s][1])}</span></li>' for s, n, vv, *_ in FOODS if vv == v)
        groups += f'<section class="box food-group"><h2><span class="tag {cls}">{lab}</span> {sub}</h2><ul class="cols">{items}</ul></section>'
    body = f"""<h1>Can Cats Eat…? Human Food Safety List</h1>
<p class="lead">Search {len(FOODS)} foods for a quick answer.</p>
<input type="search" id="fsearch" placeholder="Type a food, e.g. tuna" aria-label="Search foods"><p id="fstatus" role="status">{len(FOODS)} foods</p>{groups}{ad_slot()}
{illustration('cat-food-guide', 'An orange cat beside plain prepared food and separately stored seasonings.')}
<p>Cats are obligate carnivores: they need nutrients found in animal tissue. Treats, including human food, should stay under about 10% of daily calories.</p>
"""
    layout("/can-cats-eat/", "Can Cats Eat…? Food Risks & Preparation Guide", f"Check {len(FOODS)} human foods for cats: what to avoid, what needs cooking, small-treat preparation, dietary limits and evidence uncertainties.", body)
    for s, n, v, why, todo in FOODS:
        _, _, cls = VERD[v]
        lab, short, heading, _ = FOOD_GUIDANCE[s]
        q = f"Can cats eat {n.lower()}?"
        related = related_foods(s)
        rl = "".join(f'<li><a href="{rel("/can-cats-eat/"+f[0]+"/")}">Can cats eat {e(f[1].lower())}?</a></li>' for f in related)
        sources = FOOD_SOURCES.get(s, [])
        source_links = ''.join(f'<li><a href="{e(url)}">{e(label)}</a></li>' for label, url in sources)
        urgent = '<p class="box">If eaten, contact your veterinarian for advice. In the US: <a href="tel:+18884264435">ASPCA Poison Control: 888-426-4435</a> (fee may apply). Elsewhere, contact a local veterinary emergency service.</p>' if v == 'no' else ''
        g = gear([("cat treats", "Cat-safe treats")]) if v != "no" else ""
        body = f"""<p class="crumbs"><a href="{rel('/can-cats-eat/')}">Can cats eat…?</a> › {e(n)}</p>
<h1>{e(q[0].upper()+q[1:])}</h1>
<div class="verdict {cls}"><strong>{e(lab)}</strong></div>
<p class="lead">{e(short)}</p>{urgent}
<h2>Why</h2><p>{e(why)}</p>
<h2>{e(heading)}</h2><p>{e(todo)}</p>{ad_slot()}
<h2>Sources and limits</h2><ul><li><a href="https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets">ASPCA general food hazard guidance</a> (covers multiple species; cat-specific limits are noted above).</li>{source_links}</ul>
<p class="small">General information, not veterinary review or individual advice. Ask your vet about health conditions. Content revised: {content_date('/can-cats-eat/'+s+'/')}.</p>
<p>Keep any treats within the total <a href="{rel('/cat-calorie-calculator/')}">daily calorie budget</a>; human food is not a complete cat diet.</p>
{g}<h2>Related</h2><ul>{rl}</ul>"""
        layout(f"/can-cats-eat/{s}/", f"Can Cats Eat {n}? {lab}", short, body,
               faq_schema([(q, short + " " + why + " " + todo)]))

def namesp():
    cats = "".join(f'<option value="{k}">{e(v["label"])}</option>' for k, v in NAMES.items())
    lists = "".join(f'<h3>{e(v["label"])}</h3><ul class="name-list">' + ''.join(f'<li>{e(x)}</li>' for x in v['names'][:30]) + '</ul>' for v in NAMES.values())
    body = f"""<h1>Cat Name Generator</h1><p class="lead">Pick a style and get name ideas for your new cat or kitten.</p>
{illustration('cat-name-ideas', 'An orange tabby, a black cat and a cream cat with blank name tags.', True, True)}
<div class="tool"><label for="nstyle">Style</label><select id="nstyle">{cats}</select><button type="button" class="btn" id="ngo">Generate names</button>
<ul class="result names" id="nres" aria-live="polite"></ul></div>{ad_slot()}
<h2>Popular cat names by style</h2>{lists}
{gear([("personalized cat collar", "Personalized cat collars and ID tags")])}
<script>window.CAT_NAMES={json.dumps({k: v["names"] for k, v in NAMES.items()})};</script>
"""
    layout("/cat-name-generator/", "Cat Name Generator: Cute, Orange, Black & Halloween Cat Names", "Free cat name generator with hundreds of cute, funny, orange, black, food and Halloween cat names for boys and girls.", body)

SELLER = "an independent creator based in China"
def contact_p():
    m = C["contact_email"]
    return f'<a href="mailto:{e(m)}">{e(m)}</a>'

def about():
    layout("/about/", f"About {NAME}", f"About {NAME}, free tools and printables for cat owners.",
           f"""<h1>About {e(NAME)}</h1><p>{e(NAME)} is a small website run by {SELLER} who loves cats and makes short cat videos (the "Pumpkin Cat" series). It offers free, quick tools that answer everyday cat-care questions, based on published veterinary guidelines (AAHA/AAFP, ASPCA).</p>
<p>The <a href="{rel('/cat-care-planner/')}">printable Cat Care Planner</a> is a preview: {PLANNER_STATUS}. There are no physical products and nothing is shipped.</p>
<p>We are not veterinarians. Nothing on this site replaces advice from your own vet.</p>
<p>Contact: {contact_p()}</p>""")

def contact():
    layout("/contact/", f"Contact | {NAME}", f"How to contact {NAME}.",
           f"""<h1>Contact</h1><p>For questions about the site, the Cat Care Planner, an order, or a refund, email {contact_p()}.</p>
<p>Please include your order number if your question is about a purchase. We usually reply within 2 business days. The site is run by one person in China (UTC+8), so replies may arrive outside US business hours.</p>""")

def terms():
    layout("/terms/", f"Terms of Service | {NAME}", f"Terms of service for {NAME} and its digital products.",
           f"""<h1>Terms of Service</h1><p>Last updated: {DATES['/terms/']}</p>
<p>These terms apply to {e(NAME)} ({e(URL)}) and to digital products sold through it. The site is operated by {SELLER}. Contact: {contact_p()}.</p>
<h2>Free tools and information</h2><p>The calculators and articles are free and provided for general information only. They are not veterinary advice. Always ask your veterinarian about your cat's health, and contact a vet or pet poison hotline in an emergency.</p>
<h2>Digital products</h2><p>The Cat Care Planner is {PLANNER_STATUS}. No orders or pre-orders are currently accepted. Any future sale will identify the payment provider and delivery terms before checkout. No physical item is shipped.</p>
<h2>License</h2><p>When you buy a product you get a personal, non-transferable license to download, print and use it for your own household as many times as you like. You may not resell, share, redistribute or claim the files as your own.</p>
<h2>Refunds</h2><p>See our <a href="{rel('/refund-policy/')}">Refund Policy</a>.</p>
<h2>Liability</h2><p>The site and products are provided "as is". To the extent permitted by law, we are not liable for indirect or consequential losses arising from using the site or products. Nothing in these terms limits rights you have under consumer protection laws that apply to you.</p>
<h2>Changes</h2><p>We may update these terms. The date above shows the latest version.</p>""")

def refund():
    layout("/refund-policy/", f"Refund Policy | {NAME}", f"Refund policy for {NAME} digital products.",
           f"""<h1>Refund Policy</h1><p>Last updated: {DATES['/refund-policy/']}</p><p>Cat Care Planner: {PLANNER_STATUS}. The terms below describe the intended policy for future sales; no orders are currently accepted.</p>
<p>Our products are digital downloads, so we can't take them back once they are delivered. We still want you to be happy with your purchase.</p>
<h2>When you can get a refund</h2><p>Within <strong>14 days</strong> of purchase, you can ask for a full refund if:</p>
<ul><li>the file is defective, such as corrupted, won't open or is missing pages, and we can't fix it by sending you a working copy; or</li><li>the product is materially not as described on its product page.</li></ul>
<h2>How to request one</h2><p>Email {contact_p()} with your order number and a short description of the problem, plus a screenshot if you can. We usually reply within 2 business days. Approved refunds go back to your original payment method through our payment provider.</p>
<h2>Other cases</h2><p>Because files can't be returned, we don't normally refund a change of mind after download. Your statutory consumer rights are not affected.</p>""")

def privacy():
    ads = "<h2>Advertising</h2><p>We use Google AdSense to show ads. Google and its partners use cookies to serve ads based on your prior visits to this and other websites. You can opt out of personalized advertising at <a href=\"https://adssettings.google.com\" rel=\"noopener\">Google Ads Settings</a> or <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. See <a href=\"https://policies.google.com/technologies/partner-sites\" rel=\"noopener\">how Google uses data from partner sites</a>.</p>" if C.get("adsense_publisher_id") else ""
    aff = "<h2>Affiliate links</h2><p>Some links are affiliate links. As an Amazon Associate we earn from qualifying purchases, at no extra cost to you.</p>" if C.get("amazon_associates_tag") else ""
    layout("/privacy/", f"Privacy Policy | {NAME}", f"Privacy policy for {NAME}.",
           f"""<h1>Privacy Policy</h1><p>Last updated: {DATES['/privacy/']}</p><p>This site is operated by {SELLER}.</p>
<h2>Tools</h2><p>All calculators run in your browser. We do not ask for accounts and do not store what you type into the tools.</p>
<h2>Hosting</h2><p>The site is hosted on GitHub Pages, which may log basic technical data such as IP addresses for security. See <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub's privacy statement</a>.</p>
<h2>Purchases</h2><p>The Cat Care Planner is {PLANNER_STATUS}; this site currently accepts no orders. Payment-provider and purchase-data details will be supplied before any future sale.</p>
<h2>Emails</h2><p>If you email us, we use your address only to reply.</p>{ads}{aff}
<h2>Your choices</h2><p>You can ask us to access or delete the personal data we hold about you by emailing {contact_p()}.</p>""")

PLANNER = ["Cat Profile: microchip, breed, food, likes and quirks, with a photo spot", "Emergency Contacts, with the US pet poison hotline numbers already printed",
  "Vet Visit Log, plus a Vaccination & Flea/Worm Prevention Record", "Weight Tracker, plus a 12-month Weight Chart grid",
  "Weekly Daily Feeding Log and Water & Litter Box Log", "Undated Monthly Calendar", "Medication Tracker", "Daily Health Check (14 quick checks, Mon–Sun)",
  '"When to Call the Vet" warning-signs page', "Grooming & Dental Log", "New Food & Treat Trial Log", "Monthly Expenses Tracker and Yearly Budget Summary",
  "Draft food-risk reference (wording must be checked before release)", "Plants & Household Hazards (lilies, medicines, essential oils and more)",
  "Pet Sitter Info Sheet", "Dotted Notes page"]

def planner():
    imgs = ""
    for i, (stem, alt) in enumerate([
        ("01-cover-coming-soon", "Cat Care Planner cover and cat profile page, coming soon"),
        ("02-inside", "Planner pages for vet visits, weight tracking, feeding and a calendar"),
        ("03-toxic-foods", "Draft planner reference pages about foods and household hazards for cats")]):
        base = rel('/assets/img/' + stem)
        if i == 2:
            imgs += f'<aside class="box preview-warning"><strong>Outdated draft reference — not feeding advice.</strong><p>Cooked bones: do not feed. Raw fish and eggs: cook first. Cat-specific evidence for grapes, raisins and xylitol is limited. Use the <a href="{rel("/can-cats-eat/")}">updated food guide</a> for the current conclusions. This original preview has not been rewritten as a new PDF page.</p></aside>'
        imgs += f'<a href="{base}.jpg" aria-label="View full-size preview: {e(alt)}"><picture><source type="image/webp" srcset="{base}-480.webp 480w, {base}-800.webp 800w, {base}-1200.webp 1200w" sizes="(max-width: 760px) calc(100vw - 36px), 436px"><img src="{base}.jpg" alt="{e(alt)}" width="1200" height="1200" loading="{"eager" if i == 0 else "lazy"}" decoding="async"></picture></a>'
    lis = "".join(f"<li>{e(x)}</li>" for x in PLANNER)
    schema = {"@context": "https://schema.org", "@type": "WebPage", "url": URL + "/cat-care-planner/", "name": "Cat Care Planner – Printable PDF (Pumpkin Cat Edition)",
              "image": [URL + "/assets/img/01-cover-coming-soon.jpg"], "description": PLANNER_STATUS + ". Preview of a planned 22-page printable care tracker."}
    body = f"""<p class="crumbs"><a href="{rel('/')}">Home</a> › Shop</p>
<div class="prod"><div class="gallery">{imgs}</div><div class="buy">
<h1>Cat Care Planner – Printable Cat Health, Vet &amp; Feeding Tracker</h1>
<p class="lead">Keep vet visits, vaccines, weight, meds and expenses for your cat in one cute, organized place.</p>
<p class="price">Coming soon</p><p><strong>{PLANNER_STATUS}</strong>. Preview only; no purchase or pre-order is available.</p>
<button class="btn" disabled aria-disabled="true">Coming soon</button>
<p class="small">22 pages · US Letter (8.5 × 11 in) + A4 · undated · personal-use license · no physical item ships</p></div></div>
<h2>About this planner</h2><p>Your cat can't tell you when something's off, but a written record can. The Cat Care Planner (Pumpkin Cat Edition) is a 22-page printable PDF that keeps all of your cat's health and care information in one place, so vet visits are easier and small changes don't slip by.</p>
<p>The planned formats are US Letter and A4 for home printing. Preview pages are drafts, not a delivered product. Food-risk wording in the PDF previews still needs checking against the revised website before release.</p>
<h2>What's inside</h2><ul>{lis}</ul>
<h2>Details</h2><ul><li>Status: {PLANNER_STATUS}</li><li>Planned format: ZIP file with 2 PDFs (US Letter and A4)</li><li>Delivery: not yet available; no orders accepted</li><li>Intended license: personal use</li><li>Future sales policy: <a href="{rel('/refund-policy/')}">Refund Policy</a></li><li>Questions: {contact_p()}</li></ul>
<p class="small">This planner is an organizing tool, not veterinary advice.</p>"""
    layout("/cat-care-planner/", "Cat Care Planner Preview – Coming Soon", "Coming soon / not yet available. Preview the planned Cat Care Planner PDF for feeding, weight and care records. No purchases or pre-orders accepted.", body, schema)

def assets():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    for f in ("style.css", "tools.js"):
        shutil.copy(os.path.join(ROOT, "src", f), os.path.join(OUT, "assets", f))
    shutil.copytree(os.path.join(ROOT, "src", "img"), os.path.join(OUT, "assets", "img"), ignore=shutil.ignore_patterns('01-cover.jpg', '*.md'))

def seo_files():
    sm = "".join(f"<url><loc>{e(u)}</loc>" + (f"<lastmod>{date}</lastmod>" if date else "") + "</url>" for u, date in pages)
    open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {URL}/sitemap.xml\n")
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    if C.get("custom_domain"):
        open(os.path.join(OUT, "CNAME"), "w").write(C["custom_domain"] + "\n")
    pub = C.get("adsense_publisher_id", "")
    if pub:
        open(os.path.join(OUT, "ads.txt"), "w").write(f"google.com, {pub.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    layout('/404.html', 'Page Not Found | CatCalc', 'This page could not be found. Return to CatCalc tools or the cat food guide.',
           f'<h1>Page not found</h1><p>The address may be incorrect or the page may have moved.</p><p><a href="{rel("/")}">Return to home</a> · <a href="{rel("/can-cats-eat/")}">Browse the food guide</a> · <a href="{rel("/cat-age-calculator/")}">Cat age calculator</a></p>', not_found=True)

if __name__ == "__main__":
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    home(); age(); calories(); foods(); namesp(); about(); contact(); terms(); refund(); privacy(); planner(); assets(); seo_files()
    print(f"Built {len(pages)} pages into {OUT}")
