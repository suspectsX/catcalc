"""Create simple geometric placeholders and responsive exports with Pillow.

Run only when intentionally updating image assets, not on every site build.
"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "src/img"
ART = IMG / "illustrations"
ART.mkdir(exist_ok=True)
BG, ORANGE, INK, CREAM, BLUE = '#fffaf3', '#e8772e', '#4a3428', '#f7c99b', '#dce7eb'


def cat(draw, x, y, scale=1, color=ORANGE):
    def box(coords):
        return tuple(round((x if i % 2 == 0 else y) + v * scale) for i, v in enumerate(coords))
    def ellipse(coords, fill):
        draw.ellipse(box(coords), fill=fill, outline=INK, width=max(2, round(4*scale)))
    draw.arc(box((65, 30, 150, 145)), 280, 120, fill=color, width=max(4, round(15*scale)))
    ellipse((-48, 15, 65, 150), color)
    draw.polygon([box((-65,-15)), box((-55,-85)), box((-13,-49))], fill=color, outline=INK)
    draw.polygon([box((65,-15)), box((55,-85)), box((13,-49))], fill=color, outline=INK)
    ellipse((-70, -65, 70, 60), color)
    ellipse((-27, 1, 27, 40), CREAM)
    for eye in (-27, 27): ellipse((eye-5,-15,eye+5,-5), INK)
    draw.polygon([box((-7,5)),box((7,5)),box((0,13))], fill=INK)
    for stripe in (-23, 0, 23):
        draw.line([box((stripe,-57)),box((stripe-4,-36))], fill=INK, width=max(2,round(4*scale)))


SRC_ART = Path(__file__).resolve().parent / 'assets' / 'illustrations'


def final_art(name):
    """Export final illustration from scripts/assets/illustrations/<name>.jpg if present."""
    src = SRC_ART / f'{name}.jpg'
    if not src.exists():
        return False
    widths = (600, 1200) if name == 'home-cat-tools' else (480, 960)
    ratio = 2 if name == 'home-cat-tools' else 16 / 9
    with Image.open(src) as im:
        im = im.convert('RGB')
        w, h = im.size
        if w / h < ratio:
            nh = round(w / ratio); top = (h - nh) // 2
            im = im.crop((0, top, w, top + nh))
        else:
            nw = round(h * ratio); left = (w - nw) // 2
            im = im.crop((left, 0, left + nw, h))
        for width in widths:
            im.resize((width, round(width / ratio)), Image.Resampling.LANCZOS).save(ART / f'{name}-{width}.webp', quality=86, method=6)
    return True


def placeholder(name):
    size = (1200, 600) if name == 'home-cat-tools' else (960, 540)
    canvas = Image.new('RGB', size, BG)
    d = ImageDraw.Draw(canvas)
    def rect(bounds, fill=BLUE):
        d.rounded_rectangle(bounds, radius=14, fill=fill, outline=INK, width=5)
    if name == 'cat-life-stages':
        for x, scale in zip((150, 360, 580, 800), (.6,.85,1,1)):
            cat(d,x,230,scale)
    elif name == 'cat-name-ideas':
        for x, color in ((170,ORANGE),(470,'#514b47'),(770,CREAM)):
            cat(d,x,220,.85,color)
            rect((x-45,385,x+45,435),'#fff')
    elif name == 'cat-age-hero':
        for x, scale in ((130,.5),(350,.8),(590,1)):
            cat(d,x,240,scale)
        rect((745,160,890,320))
        d.line((745,200,890,200),fill=INK,width=6)
    elif name == 'home-food-awareness':
        cat(d,180,235,.9)
        rect((390,85,870,440),'#f7e5d0')
        rect((435,170,535,270),'#715349')  # stored chocolate
        d.ellipse((610,210,685,295),fill=CREAM,outline=INK,width=5)
        for x,y in ((750,190),(790,190),(770,230),(750,230),(790,230),(770,270)):
            d.ellipse((x-17,y-17,x+17,y+17),fill='#9b709b',outline=INK,width=3)
        d.line((570,85,570,440),fill=INK,width=6)  # closed glass cupboard
    else:
        cat(d,180,240,.95)
        if name == 'home-cat-tools':
            rect((410,180,555,395))
            rect((430,200,535,240),'#fff')
            for x in (440,475,510):
                for y in (280,325,365): d.ellipse((x-8,y-8,x+8,y+8),fill=INK)
            rect((810,180,1020,390),'#fff')
            d.line((810,225,1020,225),fill=INK,width=5)
            d.pieslice((615,295,755,415),0,180,fill=BLUE,outline=INK,width=5)
        elif name in ('cat-calorie-hero','cat-food-measurements'):
            rect((380,300,535,395))
            rect((410,330,500,360),'#fff')
            d.ellipse((365,240,550,310),fill=BLUE,outline=INK,width=5)
            rect((605,240,720,385),'#fff')
            for y in (270,300,330): d.line((605,y,645,y),fill=INK,width=4)
            rect((790,270,890,385),'#8ba58a')
            d.ellipse((790,250,890,285),fill=BLUE,outline=INK,width=5)
        elif name == 'cat-food-guide':
            rect((380,190,740,390),'#fff')
            d.ellipse((430,240,515,310),fill=CREAM,outline=INK,width=5)
            d.ellipse((580,240,660,310),fill=ORANGE,outline=INK,width=5)
            rect((790,150,900,340),'#8ba58a')  # closed seasoning storage
    widths = (600,1200) if name == 'home-cat-tools' else (480,960)
    for width in widths:
        canvas.resize((width,round(size[1]*width/size[0])),Image.Resampling.LANCZOS).save(ART/f'{name}-{width}.webp',quality=82)


def export_products():
    # Keep the actual page-preview pixels from the original JPG. Retain only
    # imagegen's edited sales badge, never its re-rendered PDF page content.
    with Image.open(IMG/'01-cover.jpg') as original:
        cover = original.convert('RGB')
        with Image.open(ROOT/'scripts/assets/cover-status-label.png') as badge:
            cover.paste(badge, (760,1045))
        cover.save(IMG/'01-cover-coming-soon.jpg',quality=95)
    for stem in ('01-cover-coming-soon','02-inside','03-toxic-foods'):
        with Image.open(IMG/f'{stem}.jpg') as image:
            for width in (480,800,1200):
                image.resize((width,width),Image.Resampling.LANCZOS).save(IMG/f'{stem}-{width}.webp',quality=90,method=6)


if __name__ == '__main__':
    for name in ('home-cat-tools','home-food-awareness','cat-age-hero','cat-life-stages',
                 'cat-calorie-hero','cat-food-measurements','cat-name-ideas','cat-food-guide'):
        if not final_art(name):
            placeholder(name)
    export_products()
    print('Prepared 8 illustrations (final art where available) and 9 product WebP sources.')
