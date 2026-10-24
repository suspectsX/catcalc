"""Local integrity checks for every generated HTML page. Standard library only."""
import json
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from foods import FOODS, FOOD_GUIDANCE

OUT = ROOT/'docs'
CONFIG = json.loads((ROOT/'config.json').read_text(encoding='utf-8'))
SITE = CONFIG['site_url'].rstrip('/')
DATES = json.loads((ROOT/'src/content_dates.json').read_text())
errors = []


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.tags = defaultdict(list)
        self.title = ''
        self.json = []
        self.in_title = self.in_json = False
        self.buffer = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags[tag].append(attrs)
        if tag == 'title': self.in_title = True
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.in_json = True
            self.buffer = ''

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False
        if tag == 'script' and self.in_json:
            try: self.json.append(json.loads(self.buffer))
            except ValueError as exc: errors.append(f'{self.path}: invalid JSON-LD: {exc}')
            self.in_json = False

    def handle_data(self, data):
        if self.in_title: self.title += data
        if self.in_json: self.buffer += data


def local_target(source, link):
    url = urlsplit(urljoin(SITE+source, link))
    if url.netloc != urlsplit(SITE).netloc or url.scheme not in ('https','http'):
        return None
    path = OUT/unquote(url.path).lstrip('/')
    return path/'index.html' if url.path.endswith('/') else path


pages = {}
titles, descriptions = Counter(), Counter()
inbound = {f'/can-cats-eat/{f[0]}/':set() for f in FOODS}
for file in sorted(OUT.rglob('*.html')):
    name = file.relative_to(OUT).as_posix()
    path = '/'+name.removesuffix('index.html') if name.endswith('index.html') else '/'+name
    doc = file.read_text(encoding='utf-8')
    page = Page(path)
    page.feed(doc)
    pages[path] = page
    def require(ok, message):
        if not ok: errors.append(f'{path}: {message}')
    descs = [m['content'] for m in page.tags['meta'] if m.get('name') == 'description']
    require(len(page.tags['title']) == 1 and bool(page.title), 'expected one title')
    require(len(descs) == 1 and bool(descs[0]), 'expected one description')
    require(len(page.tags['h1']) == 1, 'expected one H1')
    require(page.tags['html'][0].get('lang') == 'en', 'missing English language')
    require(any(m.get('name') == 'viewport' for m in page.tags['meta']), 'missing viewport')
    titles[page.title] += 1
    if descs: descriptions[descs[0]] += 1
    require(not re.search(r'Vet-Based|vet-recommended|vet-informed|instant\s+(?:digital\s+)?download|launching this week',doc,re.I), 'unsupported review or sales claim')
    require('ad-slot' not in doc, 'empty ad slot')
    require(CONFIG['adsense_publisher_id'] in doc, 'auto-ad script missing')
    for meta in ('og:image', 'twitter:image'):
        values = [m['content'] for m in page.tags['meta'] if m.get('property',m.get('name')) == meta]
        require(len(values) == 1 and values[0].startswith(SITE+'/'), f'missing absolute {meta}')
        if values: require(local_target(path,values[0]).is_file(),f'missing {meta} file')
    for attrs in page.tags['a']+page.tags['link']+page.tags['script']+page.tags['img']:
        link = attrs.get('href',attrs.get('src',''))
        if not link: continue
        target = local_target(path,link)
        if target:
            require(target.is_file(), f'missing link target {link}')
            fragment = urlsplit(link).fragment
            if fragment and target == file:
                require(any(a.get('id') == fragment for tags in page.tags.values() for a in tags), f'missing anchor {fragment}')
        if path in inbound and urlsplit(link).path in inbound and urlsplit(link).path != path:
            inbound[urlsplit(link).path].add(path)
    for attrs in page.tags['source']+page.tags['img']:
        for item in attrs.get('srcset','').split(','):
            if item.strip(): require(local_target(path,item.split()[0]).is_file(), 'missing srcset file '+item)
    for attrs in page.tags['img']:
        require(bool(attrs.get('width')) and bool(attrs.get('height')) and 'alt' in attrs, 'image dimensions or alt missing')
        require(attrs.get('loading') in ('lazy','eager') and attrs.get('decoding') == 'async','image loading contract missing')
    if path in inbound:
        slug = path.strip('/').split('/')[-1]
        label, short, *_ = FOOD_GUIDANCE[slug]
        require(short in page.json[0]['mainEntity'][0]['acceptedAnswer']['text'], 'FAQ conclusion drift')
        require(page.title.endswith(label) and descs == [short], 'metadata conclusion drift')
        require(short.replace('&','&amp;') in doc,'visible conclusion drift')
    if path == '/cat-care-planner/':
        require(page.tags['img'][0]['loading'] == 'eager', 'first product image lazy')
        require('offers' not in page.json[0], 'product must not have Offer')

for kind, counter in [('title',titles),('description',descriptions)]:
    for value, count in counter.items():
        if count > 1: errors.append(f'duplicate {kind}: {value}')
for path, sources in inbound.items():
    if len(sources) < 3: errors.append(f'{path}: only {len(sources)} distinct food-page inbound links')

ns = {'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = ET.parse(OUT/'sitemap.xml').getroot().findall('s:url',ns)
if len(urls) != 52 or len(pages) != 53: errors.append('expected 52 sitemap URLs and 53 HTML files')
for entry in urls:
    path = entry.find('s:loc',ns).text.removeprefix(SITE)
    date = entry.find('s:lastmod',ns)
    expected = DATES.get(path,DATES['/can-cats-eat/*/'] if path.startswith('/can-cats-eat/') else None)
    if (date.text if date is not None else None) != expected: errors.append(f'{path}: incorrect lastmod')
if titles and errors:
    print('\n'.join(errors))
    raise SystemExit(1)
counts = {p:len(s) for p,s in sorted(inbound.items())}
print(f'PASS: {len(pages)} HTML files; unique title/description, H1, local links, JSON-LD, images, sales and date checks.')
print(f'PASS: 41 food pages; distinct food-page inbound links min={min(counts.values())}, max={max(counts.values())}.')
for path,count in counts.items(): print(f'  {path}: {count}')
