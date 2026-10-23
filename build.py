#!/usr/bin/env python3
"""Static site generator for CatCalc. Run: python3 build.py  -> writes ./docs"""
import json, os, shutil, html, datetime, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from foods import FOODS
from names import NAMES

ROOT = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(ROOT, "config.json")))
OUT = os.path.join(ROOT, "docs")
URL = C["site_url"].rstrip("/")
NAME = C["site_name"]
TODAY = datetime.date.today().isoformat()
pages = []  # for sitemap
e = html.escape

def rel(path):  # absolute path within site
    from urllib.parse import urlparse
    base = urlparse(URL).path.rstrip("/")
    return base + path

VERD = {"no": ("No", "Toxic / avoid", "bad"), "caution": ("Caution", "Only rarely, tiny amounts", "warn"), "yes": ("Yes", "Safe in moderation", "good")}

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
    return '<div class="ad-slot" aria-hidden="true"></div>' if C.get("adsense_publisher_id") else ""

def layout(path, title, desc, body, schema=None):
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
    doc = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{e(canon)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website"><meta property="og:url" content="{e(canon)}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐱</text></svg>">
<link rel="stylesheet" href="{rel('/assets/style.css')}">
{head_extra}</head><body>
<header class="top"><div class="wrap"><a class="logo" href="{rel('/')}">🐱 {e(NAME)}</a>
<nav><a href="{rel('/cat-age-calculator/')}">Age</a><a href="{rel('/cat-calorie-calculator/')}">Calories</a><a href="{rel('/can-cats-eat/')}">Can cats eat…?</a><a href="{rel('/cat-name-generator/')}">Names</a></nav></div></header>
<main class="wrap">{body}{product_box()}</main>
<footer><div class="wrap"><p>{e(NAME)} provides general information only and is not a substitute for veterinary advice. If you think your cat ate something toxic, call your vet, the ASPCA Animal Poison Control Center (888-426-4435, fee may apply) or Pet Poison Helpline (855-764-7661).</p>
<p><a href="{rel('/about/')}">About</a> · <a href="{rel('/privacy/')}">Privacy</a>{social} · © {datetime.date.today().year} {e(NAME)}</p></div></footer>
</body></html>"""
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(doc)
    pages.append(canon)

def faq_schema(qas):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}

# ---------------- pages ----------------
def home():
    cards = [("/cat-age-calculator/", "🎂 Cat Age Calculator", "Convert your cat's age to human years using the AAHA/AAFP formula, plus life stage."),
             ("/cat-calorie-calculator/", "🍽️ Cat Calorie & Food Calculator", "How many calories and grams of food your cat needs per day."),
             ("/can-cats-eat/", "🥕 Can Cats Eat…?", f"Quick yes / no / caution answers for {len(FOODS)} common human foods."),
             ("/cat-name-generator/", "✨ Cat Name Generator", "Hundreds of name ideas: orange, black, Halloween, food and cute names.")]
    c = "".join(f'<a class="card" href="{rel(p)}"><h2>{t}</h2><p>{d}</p></a>' for p, t, d in cards)
    toxic = ", ".join(f'<a href="{rel("/can-cats-eat/"+s+"/")}">{e(n)}</a>' for s, n, v, *_ in FOODS if v == "no")
    body = f"""<section class="hero"><h1>Free, simple tools for cat owners</h1>
<p>Fast calculators and clear answers. No sign-up, nothing to install, works on your phone.</p></section>
<div class="grid">{c}</div>{ad_slot()}
<section class="box"><h2>Foods that are toxic to cats</h2><p>{toxic}.</p>
<p>Also dangerous: <strong>lilies</strong> (true lilies and daylilies). Even pollen or vase water can cause kidney failure in cats, so keep them out of homes with cats.</p></section>"""
    layout("/", f"{NAME}: Free Cat Age, Calorie & Food Safety Tools", "Free cat tools: cat age in human years, daily calorie and food calculator, can cats eat this food, and a cat name generator.", body,
           {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": URL + "/"})

def age():
    qas = [("How old is my cat in human years?", "By the AAHA/AAFP life stage guidelines, a 1-year-old cat is about 15 human years, a 2-year-old about 24, and each year after that adds about 4 human years."),
           ("What are the life stages of a cat?", "Kitten: birth to 1 year. Young adult: 1-6 years. Mature adult: 7-10 years. Senior: over 10 years (2021 AAHA/AAFP Feline Life Stage Guidelines)."),
           ("How long do indoor cats live?", "Many indoor cats live into their mid-teens, and some reach 20 or more. Regular vet checks become more important from the senior stage.")]
    rows = "".join(f"<tr><td>{y}</td><td>{15 if y==1 else 24+4*(y-2)}</td></tr>" for y in range(1, 21))
    faq = "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in qas)
    body = f"""<h1>Cat Age Calculator: Cat Years to Human Years</h1>
<p class="lead">Enter your cat's age to see the human equivalent and life stage.</p>
<div class="tool" id="age-tool">
<label>Years <input type="number" id="ay" min="0" max="35" value="3"></label>
<label>Months <input type="number" id="am" min="0" max="11" value="0"></label>
<button class="btn" id="ago">Calculate</button>
<div class="result" id="ares" aria-live="polite"></div></div>{ad_slot()}
<h2>How the calculation works</h2><p>Cats mature very fast: the first year equals about 15 human years and the second year adds about 9 more. After age 2, each cat year equals roughly 4 human years. Ages under 1 year are approximate and based on typical kitten development.</p>
<h2>Cat age chart</h2><table><thead><tr><th>Cat age (years)</th><th>Human age (years)</th></tr></thead><tbody>{rows}</tbody></table>
<h2>FAQ</h2>{faq}
<p class="small">Source: <a href="https://catvets.com/guidelines/practice-guidelines/life-stage-guidelines" rel="noopener" target="_blank">2021 AAHA/AAFP Feline Life Stage Guidelines</a>.</p>
{gear([("cat senior supplements", "Senior cat care"), ("cat birthday toy", "Cat birthday toys")])}
<script src="{rel('/assets/tools.js')}"></script>"""
    layout("/cat-age-calculator/", "Cat Age Calculator: Cat Years to Human Years (Chart)", "Convert cat years to human years with the vet-recommended AAHA/AAFP formula. Includes a 1-20 year chart and cat life stages.", body, faq_schema(qas))

def calories():
    qas = [("How many calories does a cat need per day?", "A typical 4.5 kg (10 lb) neutered indoor adult cat needs roughly 215-260 kcal per day (inactive to neutered-adult factor), but needs vary. The calculator uses RER = 70 x (weight in kg)^0.75 multiplied by a life-stage factor."),
           ("How much wet or dry food should I feed my cat?", "Divide your cat's daily calorie needs by the calories in the food (printed on the bag or can as kcal/kg, kcal/cup or kcal/can)."),
           ("How many treats can a cat have?", "A common veterinary rule of thumb is to keep treats under 10% of daily calories.")]
    faq = "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in qas)
    body = f"""<h1>Cat Calorie Calculator & Daily Food Amount</h1>
<p class="lead">Estimate how many calories your cat needs and how much of your food to serve.</p>
<div class="tool" id="cal-tool">
<label>Weight <input type="number" id="cw" min="0.3" max="15" step="0.1" value="4.5">
<select id="cu"><option value="kg">kg</option><option value="lb">lb</option></select></label>
<label>Cat type <select id="cf">
<option value="1.2">Neutered / spayed adult</option><option value="1.4">Intact adult</option>
<option value="1.0">Inactive indoor or weight-gain prone</option><option value="0.8">Weight loss (use ideal weight)</option>
<option value="2.5">Kitten (under 1 year)</option></select></label>
<label>Food calories (optional) <input type="number" id="ck" min="0" step="1" placeholder="e.g. 3800">
<select id="ckunit"><option value="kg">kcal per kg</option><option value="cup">kcal per cup</option><option value="can">kcal per can</option></select></label>
<button class="btn" id="cgo">Calculate</button>
<div class="result" id="cres" aria-live="polite"></div></div>{ad_slot()}
<h2>The formula</h2><p>Vets start from the <strong>Resting Energy Requirement</strong>: RER = 70 × (body weight in kg)<sup>0.75</sup>. This is multiplied by a factor for life stage and activity, for example 1.2 for a neutered adult or 0.8 for weight loss. These are starting points; adjust based on your cat's body condition and ask your vet, especially for weight loss, pregnancy or illness.</p>
<h2>FAQ</h2>{faq}
{gear([("kitchen scale grams", "Digital kitchen scale (weigh food accurately)"), ("slow feeder cat bowl", "Slow feeder bowls"), ("cat water fountain", "Cat water fountains")])}
<script src="{rel('/assets/tools.js')}"></script>"""
    layout("/cat-calorie-calculator/", "Cat Calorie Calculator: How Much Should I Feed My Cat?", "Free cat calorie calculator using the vet RER formula. Find daily kcal and grams or cups of wet or dry food for kittens, adults and weight loss.", body, faq_schema(qas))

def foods():
    groups = ""
    for v in ("no", "caution", "yes"):
        lab, sub, cls = VERD[v]
        items = "".join(f'<li><a href="{rel("/can-cats-eat/"+s+"/")}">{e(n)}</a></li>' for s, n, vv, *_ in FOODS if vv == v)
        groups += f'<section class="box"><h2><span class="tag {cls}">{lab}</span> {sub}</h2><ul class="cols">{items}</ul></section>'
    body = f"""<h1>Can Cats Eat…? Human Food Safety List</h1>
<p class="lead">Search {len(FOODS)} foods for a quick answer.</p>
<input type="search" id="fsearch" placeholder="Type a food, e.g. tuna" aria-label="Search foods">{groups}{ad_slot()}
<p>Cats are obligate carnivores: they need nutrients found in animal tissue. Treats, including human food, should stay under about 10% of daily calories.</p>
<script src="{rel('/assets/tools.js')}"></script>"""
    layout("/can-cats-eat/", "Can Cats Eat…? Safe & Toxic Human Foods for Cats", f"Which human foods are safe for cats? Quick yes, no or caution answers for {len(FOODS)} foods including chocolate, tuna, milk, eggs and fruit.", body)
    for s, n, v, why, todo in FOODS:
        lab, sub, cls = VERD[v]
        q = f"Can cats eat {n.lower()}?"
        short = {"no": f"No. {n} is not safe for cats.", "caution": f"Only with caution. {n} is not ideal for cats.", "yes": f"Yes, in moderation. {n} is generally safe for cats."}[v]
        related = [f for f in FOODS if f[2] == v and f[0] != s][:6]
        rl = "".join(f'<li><a href="{rel("/can-cats-eat/"+f[0]+"/")}">Can cats eat {e(f[1].lower())}?</a></li>' for f in related)
        g = gear([("cat treats", "Cat-safe treats")]) if v != "no" else ""
        body = f"""<p class="crumbs"><a href="{rel('/can-cats-eat/')}">Can cats eat…?</a> › {e(n)}</p>
<h1>{e(q[0].upper()+q[1:])}</h1>
<div class="verdict {cls}"><strong>{lab}</strong> · {sub}</div>
<p class="lead">{e(short)}</p>
<h2>Why</h2><p>{e(why)}</p>
<h2>{'What to do' if v=='no' else 'How to serve it'}</h2><p>{e(todo)}</p>{ad_slot()}
<p class="small">Always check with your vet if your cat has health conditions, and see the <a href="https://www.aspca.org/pet-care/animal-poison-control/people-foods-avoid-feeding-your-pets" rel="noopener" target="_blank">ASPCA list of people foods to avoid</a>.</p>
{g}<h2>Related</h2><ul>{rl}</ul>"""
        layout(f"/can-cats-eat/{s}/", f"Can Cats Eat {n}? ({lab}) Vet-Based Answer", f"{short} Learn why and what to do. Quick, vet-informed answer for cat owners."[:158], body,
               faq_schema([(q, short + " " + why)]))

def namesp():
    cats = "".join(f'<option value="{k}">{e(v["label"])}</option>' for k, v in NAMES.items())
    lists = "".join(f'<h3>{e(v["label"])}</h3><p>{", ".join(e(x) for x in v["names"][:30])}</p>' for v in NAMES.values())
    body = f"""<h1>Cat Name Generator</h1><p class="lead">Pick a style and get name ideas for your new cat or kitten.</p>
<div class="tool"><label>Style <select id="nstyle">{cats}</select></label><button class="btn" id="ngo">Generate names</button>
<ul class="result names" id="nres" aria-live="polite"></ul></div>{ad_slot()}
<h2>Popular cat names by style</h2>{lists}
{gear([("personalized cat collar", "Personalized cat collars and ID tags")])}
<script>window.CAT_NAMES={json.dumps({k: v["names"] for k, v in NAMES.items()})};</script>
<script src="{rel('/assets/tools.js')}"></script>"""
    layout("/cat-name-generator/", "Cat Name Generator: Cute, Orange, Black & Halloween Cat Names", "Free cat name generator with hundreds of cute, funny, orange, black, food and Halloween cat names for boys and girls.", body)

def about():
    em = f'<p>Contact: <a href="mailto:{e(C["contact_email"])}">{e(C["contact_email"])}</a></p>' if C.get("contact_email") else ""
    layout("/about/", f"About {NAME}", f"About {NAME}, a set of free tools for cat owners.",
           f"<h1>About {e(NAME)}</h1><p>{e(NAME)} is a small, independent site run by cat lovers who also make short cat videos. We build quick, free tools that answer everyday cat-care questions, based on published veterinary guidelines (AAHA/AAFP, ASPCA). We are not veterinarians, and nothing here replaces advice from your own vet.</p>{em}")

def privacy():
    ads = "<h2>Advertising</h2><p>We use Google AdSense to show ads. Google and its partners use cookies to serve ads based on your prior visits to this and other websites. You can opt out of personalized advertising at <a href=\"https://adssettings.google.com\" rel=\"noopener\">Google Ads Settings</a> or <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. See <a href=\"https://policies.google.com/technologies/partner-sites\" rel=\"noopener\">how Google uses data from partner sites</a>.</p>"
    aff = "<h2>Affiliate links</h2><p>Some links are affiliate links. As an Amazon Associate we earn from qualifying purchases, at no extra cost to you.</p>"
    layout("/privacy/", f"Privacy Policy | {NAME}", f"Privacy policy for {NAME}.",
           f"<h1>Privacy Policy</h1><p>Last updated: {TODAY}</p><p>All calculators run in your browser. We do not ask for accounts and do not store what you type into the tools.</p>{ads}{aff}<h2>Contact</h2><p>Questions about this policy can be sent to the contact address on the About page.</p>")

def assets():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    for f in ("style.css", "tools.js"):
        shutil.copy(os.path.join(ROOT, "src", f), os.path.join(OUT, "assets", f))

def seo_files():
    sm = "".join(f"<url><loc>{e(u)}</loc><lastmod>{TODAY}</lastmod></url>" for u in pages)
    open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {URL}/sitemap.xml\n")
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    pub = C.get("adsense_publisher_id", "")
    if pub:
        open(os.path.join(OUT, "ads.txt"), "w").write(f"google.com, {pub.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    open(os.path.join(OUT, "404.html"), "w").write(f'<!doctype html><meta charset="utf-8"><title>Not found</title><p style="font-family:sans-serif">Page not found. <a href="{rel("/")}">Go to {e(NAME)}</a></p>')

if __name__ == "__main__":
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    home(); age(); calories(); foods(); namesp(); about(); privacy(); assets(); seo_files()
    print(f"Built {len(pages)} pages into {OUT}")
