"""Generate one page per retreat into retreats/<slug>.html from the data below.

Every page is self-contained HTML (own doctype, inline CSS) so it works on any static host
and inside the artifact preview. Copy rule: only facts from the WC notes, Instagram captions
or Sam. No invented numbers, quotes or places.
"""
import html, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
from seo import SITE, script, breadcrumbs, event, sitemap, llms

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TORN = open(os.path.join(HERE, 'torn.css')).read()

RETREATS = [
    dict(
        slug='broughton-island',
        seo_title='Broughton Island Kayaking Weekend, Port Stephens',
        seo_desc='March 2025: a handful of mates sea-kayaked out to Broughton Island off Port Stephens, speared fish for dinner and camped in the rocks. Where Wildly Calm started.', name='Broughton Island', when='March 2025', where='Port Stephens, NSW',
        tag='Where it started',
        hook='A spontaneous weekend kayaking trip that turned into Wildly Calm.',
        hero='sunset-broughton.jpg', hero_pos='50% 70%', hero_pos_m='62% 70%',
        story=[
            "It wasn't meant to be the start of anything. A handful of mates loaded up sea kayaks and paddled out to Broughton Island, off Port Stephens, for the weekend.",
            "We speared fish for dinner, strung a tarp between the rocks for shade, and spent the nights on the sand with a gas stove and a string of fairy lights.",
            "We came back with one big lesson: we loved it. And we wanted to keep making spaces like that for other men.",
        ],
        did=['Sea kayaking out to the island', 'Spearfishing for dinner', 'Camping between the rocks', 'Sunsets on the sand'],
        quote=None,
        photos=[
            ('kayaks-broughton.jpg', 'Rafted up on the way out', 'A raft of sea kayaks on flat grey water, one man waving'),
            ('catch-broughton.jpg', 'Dinner sorted', 'Three men in wetsuits holding up the fish they speared'),
            ('spearfishers-broughton.jpg', 'Spears and kayaks', 'Two men in wetsuits with spearguns beside the kayaks'),
            ('tarp-camp-broughton.jpg', 'Camp in the rocks', 'A tarp strung between rocks over a sandy camp'),
            ('walk-fish-broughton.jpg', 'Walking the catch home', 'Two men walking along the beach carrying fish'),
            ('night-camp-broughton.jpg', 'Fairy lights and a gas stove', 'Four men laughing at camp at night under fairy lights'),
            ('two-kayak-broughton.jpg', 'Broughton Island - Men\'s Retreat', 'Two men standing by a yellow sea kayak on the beach'),
            ('rocks-camp-broughton.jpg', 'Kayaks pulled up in the gully', 'Men among the rocks with kayaks pulled up on the sand'),
        ],
    ),
    dict(
        slug='camp-bunya',
        seo_title="Camp Bunya Men's Retreat",
        seo_desc="October 2025, our first men's retreat: river days in kayaks, yoga on the grass and sleeping bags round the fire.", name='Camp Bunya', when='October 2025', where=None,
        tag='Our first retreat',
        hook='River days, yoga on the grass and sleeping bags round the fire.',
        hero='kayaks-bunya.jpg', hero_pos='50% 60%', hero_pos_m='38% 84%',
        story=[
            "Camp Bunya was the first time we ran it as a proper retreat. Days on the river in kayaks, yoga on the grass, and nights in sleeping bags round the fire.",
            "We learned a lot that weekend. The biggest lesson: go deeper, stay longer, get wilder. Everything we've run since has been built on it.",
        ],
        did=['Kayaking the river', 'Yoga on the grass', 'Sharing round the fire', 'Sleeping out under the stars'],
        quote=("A place to adventure in the wild but also to really look inwards and reflect. A safe space for you to express yourself and ask hard questions. Somewhere for you to show your weaknesses but also to celebrate your strengths.", 'Camp Bunya participant'),
        photos=[
            ('watermelon-bunya.jpg', 'Lunch stop', 'A man in a bucket hat biting into watermelon in a kayak'),
            ('yoga-bunya.jpg', 'Yoga on the grass', 'A group doing yoga on the grass in front of tall trees'),
            ('hug-bunya.jpg', 'Camp Bunya - Men\'s Retreat', 'Two men hugging, faces hidden under sun hats'),
            ('paddle-bridge-bunya.jpg', 'Under the bridge', 'A man paddling a yellow kayak below a suspension bridge'),
            ('fire-bunya.jpg', 'Where we slept', 'Sleeping bags and logs around a smoking campfire'),
            ('laughing-bunya.jpg', 'Between sessions', 'Three men laughing on the grass'),
            ('circle-talk-bunya.jpg', 'Talking it through', 'A man talking to the group on the grass'),
            ('embrace-bunya.jpg', 'Holding on', 'Two men embracing on a grassy clearing'),
        ],
    ),
    dict(
        slug='croajingalong',
        seo_title="Croajingalong Men's Retreat, East Gippsland",
        seo_desc='February 2026: a busload of Sydney men, three days of coastal hiking and off-grid camping in Croajingalong National Park, and deep listening round the fire.', name='Croajingalong', when='February 2026', where='East Gippsland, VIC',
        tag='Three days on a wild coast',
        hook='A busload of Sydney men, three days of wilderness hiking and off-grid camping.',
        hero='beach-circle-croajingalong.jpg', hero_pos='50% 55%', hero_pos_m='26% 62%',
        story=[
            "A busload of Sydney men headed down to Croajingalong National Park in East Gippsland for three days of hiking along the coast and camping off-grid.",
            "Between the walking there were workshops: deep listening, rock running, ecstatic dance, yoga, and one afternoon where everyone painted the man they want to be. Grown men, paintbrushes, a lot of laughing, then some very honest pictures.",
            "At night it was the fire, and the conversations that only happen when everyone's tired, a long way from home and has nowhere else to be.",
        ],
        did=['Three days of coastal hiking', 'Off-grid camping', 'Deep listening and sharing round the fire', 'Painting the man you want to be', 'Rock running, ecstatic dance, yoga'],
        quote=("I knew I was in a slump, a proper downturn mentally before this trip. It wasn't till I was on the drive home that it truly hit me how important this trip was to the trajectory of my year.", 'Croajingalong participant'),
        photos=[
            ('group-croajingalong.jpg', 'Croajingalong - Men\'s Retreat', 'Eleven men grinning on a beach, arms round each other'),
            ('creek-croajingalong.jpg', 'Following the creek', 'Three men with packs walking along a rainforest creek'),
            ('hikers-croajingalong.jpg', 'Break on the track', 'Hikers with packs resting in regrowth bush'),
            ('camp-croajingalong.jpg', 'Camp kitchen', 'Two men laughing at camp beside a cooking pot'),
            ('forest-circle-croajingalong.jpg', 'Circle in the clearing', 'A small group sitting in a circle under tall gums'),
            ('tarp-camp-croajingalong.jpg', 'Under the tarp', 'Men in sleeping bags under a tarp in the bush'),
            ('beach-sit-croajingalong.jpg', 'On the beach', 'Three men sitting on a beach below scrubby dunes'),
            ('forest-walk-croajingalong.jpg', 'Into the scrub', 'Two hikers deep in tall scrubby forest'),
        ],
    ),
    dict(
        slug='the-snowies',
        seo_title="Snowy Mountains Men's Retreat, Crackenback",
        seo_desc='September 2026: hiking in the snow near Thredbo, breathwork and yoga, show and tell by the fire, then a sauna and an ice bath.', name='The Snowies', when='September 2026', where='Crackenback, NSW',
        tag='Our first one in the snow',
        hook='A small group, a cottage near Thredbo, and snow on the ground.',
        hero='snow-tors-snowies.jpg', hero_pos='50% 60%', hero_pos_m='22% 60%',
        story=[
            "Our first retreat in the snow. A small group in a cottage at Crackenback, just down the road from Thredbo.",
            "We hiked out across the snow among the granite tors, cooked breakfast in the snow gums, and came back to a sauna and an ice bath.",
            "On the first night every man brought one thing he loves and talked about it by the fire for ten minutes. It sounds soft. Then you watch a quiet bloke light up about the thing he cares about.",
        ],
        did=['Hiking in the snow', 'Breathwork and yoga', 'Deep listening', 'Show and tell by the fire', 'Sauna and ice bath'],
        quote=None,
        photos=[
            ('tors-figures-snowies.jpg', 'Snowy Mountains - Men\'s Retreat', 'Two tiny figures crossing snow below granite tors'),
            ('lunch-snowgums-snowies.jpg', 'Breakfast in the snow gums', 'Four men in beanies eating breakfast from one pot'),
            ('fireside-drawing-snowies.jpg', 'Show and tell', 'A man drawing at a table beside a stone fireplace'),
            ('kitchen-snowies.jpg', 'The cottage', 'Men cooking together in a timber cottage kitchen'),
            ('map-snowies.jpg', 'Which way?', 'Two men checking a phone in the snow'),
            ('heath-snowies.jpg', 'Through the heath', 'Three men picking their way across alpine heath below snow'),
            ('bushwalk-snowies.jpg', 'Walking out', 'Hikers on a track through snow gums under blue sky'),
            ('landscape-snowies.jpg', 'Cloud on the tops', 'Cloud rolling over a snowy ridge'),
        ],
    ),
]

ORDER = [r['slug'] for r in RETREATS]

CSS = open(os.path.join(HERE, 'base.css')).read() + """
.hero{position:relative;color:var(--cream);isolation:isolate;background:var(--ink);min-height:clamp(480px,72vh,720px);display:grid;align-items:end}
.hero > .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--pos,50% 50%);z-index:-2}
.hero::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(18,18,14,.5) 0%,rgba(18,18,14,.15) 35%,rgba(18,18,14,.75) 100%)}
.on-photo .seg{white-space:nowrap}
.top nav{margin-left:auto}
.hero > .wrap{width:100%;display:grid;gap:var(--s-3);padding-block:128px clamp(32px,5vw,56px)}
.hero h1{font-weight:500;font-size:var(--fs-display);line-height:1.05;letter-spacing:.08em;text-transform:uppercase}
.hero .hook{max-width:52ch;font-size:var(--fs-lead);opacity:.95}

.story .wrap{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,4fr);gap:clamp(32px,5vw,64px);align-items:start}
.prose{display:grid;gap:1.1em;max-width:var(--measure)}
.did{background:var(--olive);color:var(--cream);box-shadow:inset 0 0 0 1.5px rgba(241,238,230,.45);padding:clamp(24px,3vw,32px);display:grid;gap:var(--s-3)}
.did h3{font-weight:600;font-size:var(--fs-small);letter-spacing:.16em;text-transform:uppercase}
.did ul{list-style:none;margin:0;padding:0;display:grid;gap:var(--s-2)}
.did li{font-family:var(--hand);font-weight:700;font-size:var(--fs-hand);line-height:1.2}
.did li::before{content:"~ ";color:var(--amber)}
.quote{margin-top:clamp(32px,4vw,48px);filter:drop-shadow(0 16px 24px rgba(0,0,0,.25))}
.quote .card{padding:clamp(24px,3vw,36px)}
.quote .card blockquote{font-size:var(--fs-lead)}

.gallery{background:var(--sand-deep)}
.gal{--gap:clamp(16px,2.4vw,28px);display:flex;flex-wrap:wrap;column-gap:var(--gap);margin-top:clamp(24px,3vw,36px)}
/* --a is the print's aspect ratio x10 (grow factors under 1 would leave a lone print short of the row) */
.gal .print{flex:var(--a) 1 16px;min-width:0;margin:0 0 var(--gap);transform:rotate(.5deg)}
.gal .print.tilt{transform:rotate(-.6deg)}
.gal .print img{width:100%;height:auto}
.gal .br{display:none;flex-basis:100%;height:0}
@media (min-width:901px){.gal .br-d{display:block}}
@media (min-width:561px) and (max-width:900px){.gal .br-t{display:block}}
/* phones: one print per row, full width, as the retreat pages always were */
@media (max-width:560px){.gal .print{flex-basis:100%}.gal .print,.gal .print.tilt{transform:none}}
/* the caption sits clear of the deepest tear on every side */
.gal figcaption{padding:10px 14px 18px}
""" + TORN + """
.others{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(16px,2vw,24px);margin-top:var(--s-5)}
.other{text-decoration:none;display:grid;gap:var(--s-2)}
.other .print{margin:0;transition:transform .3s}
.other b{font-weight:600;letter-spacing:.12em;text-transform:uppercase;font-size:var(--fs-small);margin-top:var(--s-1)}
.other span{font-family:var(--type);font-size:var(--fs-type);color:var(--ink)}
.other:hover .print,.other:focus-visible .print{transform:translateY(-4px)}
.other:hover b{text-decoration:underline;text-decoration-color:var(--rust);text-decoration-thickness:2px;text-underline-offset:4px}
.more-link a{display:inline-flex;align-items:center;min-height:44px;font-weight:600;text-decoration-color:var(--rust);text-decoration-thickness:2px;text-underline-offset:5px}
.more-link a:hover{text-decoration-color:var(--ink)}

/* next retreat: the paddlers in a photo strip, the words below it on olive */
.nextup{color:var(--cream);background:var(--olive);padding-block:0}
.nextup > .bg{display:block;width:100%;height:auto;aspect-ratio:21/8;object-fit:cover;object-position:50% 86%}
.nextup .wrap{display:grid;gap:var(--s-3);justify-items:start;padding-block:var(--s-7) var(--s-8)}
.nextup .btn{margin-top:var(--s-3)}
.nextup h2{color:var(--amber)}
.nextup .on-photo{text-shadow:none;color:var(--cream)}
footer{display:flex;flex-wrap:wrap;justify-content:space-between;gap:var(--s-5)}
/* at 900 and below the hero photo stands on its own, cropped to the people, and the words follow on ink */
@media (max-width:900px){
  .hero{min-height:0;display:block;background:var(--olive)}
  .hero > .bg{position:relative;inset:auto;height:auto;aspect-ratio:4/3;object-position:var(--pos-m,var(--pos,50% 50%))}
  .hero::before{bottom:auto;height:200px;background:linear-gradient(180deg,rgba(18,18,14,.7) 0%,rgba(18,18,14,0) 100%)}
  .hero > .wrap{padding-block:var(--s-6) var(--s-7)}
  .nextup > .bg{aspect-ratio:3/2}
  .hero .on-photo{text-shadow:none;color:var(--cream)}
}
@media (max-width:860px){.story .wrap{grid-template-columns:minmax(0,1fr)}.others{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){
  .top .wrap{flex-wrap:wrap;row-gap:0}
  .top nav{order:3;flex-basis:100%;margin-left:0}
  .hero > .bg{aspect-ratio:1/1}
  .hero h1{font-size:clamp(1.75rem,8.5vw,2.25rem);letter-spacing:.05em}
  .others{grid-template-columns:minmax(0,1fr)}
}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Courier+Prime&family=Gaegu:wght@400;700&family=Montserrat:wght@400;500;600;700&display=swap">'

def e(s): return html.escape(s, quote=True)

def head(title, desc, img, path, graph):
    url = SITE + path
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="Wildly Calm">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/img/{img}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#D7D2C6">
<link rel="icon" href="../img/wc-symbol-05.png">
<link rel="apple-touch-icon" href="../img/wc-symbol-05.png">
{FONTS}
{script(graph)}
<style>{CSS}</style>
</head>
<body>'''

def header():
    return '''<header class="top"><div class="wrap">
  <a class="home" href="../"><img src="../img/wc-logo-amber.png" alt="Wildly Calm home" width="519" height="163"></a>
  <nav aria-label="Site"><a href="../#proof">All retreats</a><a href="../#how">How it works</a><a href="../blog/">Blog</a></nav>
  <a class="btn" href="../#register">Tickets</a>
</div></header>'''

def nextup():
    return '''<section class="nextup">
  <img class="bg" src="../img/river-bunya-wide.jpg" alt="" width="2000" height="1333" loading="lazy">
  <div class="wrap">
    <p class="on-photo">Next retreat</p>
    <h2>Barrington River Men's Retreat</h2>
    <p class="on-photo"><span class="seg">Canoe | Connect | Express</span> <span class="seg">· December 4th - 6th</span></p>
    <a class="btn" href="barrington-river.html">See the details</a>
  </div>
</section>'''

def footer():
    return '''<footer class="wrap">
  <img src="../img/wc-logo-01.png" alt="Wildly Calm" width="519" height="163">
  <div><b>Need to talk to someone now?</b><br>Lifeline 13 11 14 · MensLine Australia 1300 78 99 78 · Emergency 000</div>
  <p class="small" style="flex-basis:100%">Wildly Calm · Sydney, NSW · <a href="https://www.instagram.com/wildlycalmretreats/" rel="noopener">@wildlycalmretreats</a></p>
</footer>
</body>
</html>
'''

def torn(i): return f'torn-{i % 4 + 1}'

def jpeg_size(path):
    """(width, height) from a JPEG's SOF marker; no image library needed."""
    with open(path, 'rb') as f:
        data = f.read()
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        m = data[i + 1]
        if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            return int.from_bytes(data[i + 7:i + 9], 'big'), int.from_bytes(data[i + 5:i + 7], 'big')
        i += 2 + int.from_bytes(data[i + 2:i + 4], 'big')
    raise ValueError(path)

# Justified gallery: every print in a row shares one image height, so each row closes edge to edge
# with no cropping. Row breaks are chosen per layout width (desktop, tablet, phone) and written as
# empty break elements, so the photo order and the words never change.
# per layout: (content width, gap, target image height, min image height, max prints per row, min share
# of the row any one print may take). Phones show one print per row, so they need no breaks.
GAL_WIDTHS = {'d': (1060, 28, 340, 280, 3, .26), 't': (706, 18, 250, 180, 3, .26)}

def rows(aspects, width, gap, target, hmin, maxn, minshare):
    n = len(aspects)
    best = [0.0] + [float('inf')] * n
    cut = [0] * (n + 1)
    for j in range(1, n + 1):
        for k in range(max(0, j - maxn), j):
            group = aspects[k:j]
            h = (width - gap * (len(group) - 1) - 16 * len(group)) / sum(group)
            cost = (h - target) ** 2
            if len(group) > 1 and (h < hmin or min(group) / sum(group) < minshare):
                cost += 1e7
            if best[k] + cost < best[j]:
                best[j], cut[j] = best[k] + cost, k
    ends, j = [], n
    while j:
        ends.append(j)
        j = cut[j]
    return set(ends)

def gallery(items):
    """items: list of (print_html_without_wrapper_attrs, aspect). Returns the .gal block."""
    aspects = [a for _, a in items]
    ends = {key: rows(aspects, *spec) for key, spec in GAL_WIDTHS.items()}
    out = []
    for i, (inner, a) in enumerate(items, 1):
        cls = 'print' + (' tilt' if i % 2 else '')
        out.append(f'<div class="{cls}" style="--a:{a * 10:.2f}">{inner}</div>')
        brk = ' '.join(f'br-{k}' for k in GAL_WIDTHS if i in ends[k] and i < len(items))
        if brk:
            out.append(f'<i class="br {brk}"></i>')
    return '<div class="gal">' + ''.join(out) + '</div>'

def page(r):
    meta = r['when'] + (f" · {r['where']}" if r['where'] else '')
    # the eyebrow breaks only at the dots, never inside a segment
    parts = [r['when']] + ([r['where']] if r['where'] else []) + [r['tag']]
    segs = ' '.join(f'<span class="seg">{"· " if i else ""}{e(x)}</span>' for i, x in enumerate(parts))
    path = f"/retreats/{r['slug']}.html"
    out = [head(f"{r['seo_title']} · Wildly Calm", r['seo_desc'], r['hero'], path, [breadcrumbs(r['name'], path)])]
    out.append(f'''<div class="hero" style="--pos:{r['hero_pos']};--pos-m:{r['hero_pos_m']}">
  <img class="bg" src="../img/{r['hero']}" alt="" width="1400" height="933" fetchpriority="high">
  {header()}
  <div class="wrap">
    <p class="on-photo">{segs}</p>
    <h1>{e(r['name'])}</h1>
    <p class="hook">{e(r['hook'])}</p>
  </div>
</div>''')
    story = ''.join(f'<p>{e(p)}</p>' for p in r['story'])
    did = ''.join(f'<li>{e(d)}</li>' for d in r['did'])
    quote = ''
    if r['quote']:
        quote = f'<div class="quote"><div class="card torn-3"><blockquote>"{e(r["quote"][0])}"</blockquote><cite>{e(r["quote"][1])}</cite></div></div>'
    out.append(f'''<section class="story"><div class="wrap">
  <div><p class="eyebrow">What happened</p><div class="prose">{story}</div>{quote}</div>
  <aside class="did"><h3>What we did</h3><ul>{did}</ul></aside>
</div></section>''')
    items = []
    for i, (f, c, a) in enumerate(r['photos']):
        w, h = jpeg_size(os.path.join(ROOT, 'img', f))
        items.append((f'<figure class="{torn(i)}"><img src="../img/{f}" alt="{e(a)}" width="{w}" height="{h}" loading="lazy"><figcaption>{e(c)}</figcaption></figure>', w / h))
    prints = gallery(items)
    out.append(f'''<section class="gallery"><div class="wrap">
  <p class="eyebrow">Photos</p><h2>{e(r['name'])} in pictures</h2>
  {prints}
</div></section>''')
    others = [o for o in RETREATS if o['slug'] != r['slug']]
    cards = ''.join(f'<a class="other" href="{o["slug"]}.html"><div class="print"><figure class="{torn(i+1)}"><img src="../img/{o["photos"][0][0]}" alt="" loading="lazy"></figure></div><b>{e(o["name"])}</b><span>{e(o["when"])}</span></a>' for i, o in enumerate(others))
    out.append(f'''<section><div class="wrap"><p class="eyebrow">Other retreats</p><h2>Where else we've been</h2><div class="others">{cards}</div></div></section>''')
    out.append(nextup())
    out.append(footer())
    return '\n'.join(out)

def barrington():
    path = '/retreats/barrington-river.html'
    tickets = json.load(open(os.path.join(HERE, 'config.json'))).get('tickets_url', '').strip()
    out = [head("Barrington River Men's Retreat, 4 to 6 Dec 2026 · Wildly Calm",
                'Three days canoeing the Barrington River, NSW, Friday 4 to Sunday 6 December 2026. Camping, fire and the circle. Men in their 20s and 30s, small group.',
                'river-bunya-wide.jpg', path, [breadcrumbs("Barrington River Men's Retreat", path), event(tickets)])]
    out.append(f'''<div class="hero" style="--pos:50% 92%;--pos-m:44% 84%">
  <img class="bg" src="../img/river-bunya-wide.jpg" alt="" width="2000" height="1333" fetchpriority="high">
  {header()}
  <div class="wrap">
    <p class="on-photo">Next retreat · Canoe | Connect | Express</p>
    <h1>Barrington River</h1>
    <p class="hook">Three days canoeing the Barrington River. Friday 4 to Sunday 6 December 2026.</p>
  </div>
</div>''')
    out.append('''<section class="story"><div class="wrap">
  <div>
    <p class="eyebrow">The plan</p>
    <div class="prose">
      <p>Three days on the Barrington River in canoes: paddling, camping by the water, fire at night and the circle.</p>
      <p>Same shape as every Wildly Calm weekend. Something hard first, a space everyone builds together, and then the conversations that usually never happen.</p>
    </div>
    <dl class="details" style="margin-top:24px">
      <dt>When</dt><dd>Friday 4 to Sunday 6 December 2026</dd>
      <dt>Where</dt><dd>Barrington River, NSW</dd>
      <dt>What</dt><dd>Canoeing, camping, fire and circle</dd>
      <dt>Who</dt><dd>Men in their twenties and thirties. Small group, on purpose.</dd>
    </dl>
    <div class="faq">
      <div><b>Do I need to be fit or outdoorsy?</b><p>No. You don't need to be good at talking about feelings either. You just need to turn up.</p></div>
      <div><b>Is this therapy?</b><p>No. It's peers, not counsellors. If you need more support, we'll help you find it.</p></div>
    </div>
  </div>
  ''' + (f'<aside class="did"><h3>Tickets</h3><p>Tickets are on sale now on Humanitix.</p><a class="btn" href="{e(tickets)}" rel="noopener" style="justify-self:start">Get tickets</a></aside>' if tickets else
         '<aside class="did"><h3>Tickets</h3><p>Tickets and the price are on the way. Head to the booking section for the latest.</p><a class="btn" href="../#register" style="justify-self:start">Book or register</a></aside>') + '''
</div></section>''')
    cards = ''.join(f'<a class="other" href="{o["slug"]}.html"><div class="print"><figure class="{torn(i)}"><img src="../img/{o["photos"][0][0]}" alt="" loading="lazy"></figure></div><b>{e(o["name"])}</b><span>{e(o["when"])}</span></a>' for i, o in enumerate(RETREATS[:3]))
    out.append(f'''<section class="gallery"><div class="wrap"><p class="eyebrow">Before this one</p><h2>Past retreats</h2><div class="others">{cards}</div><p class="more-link" style="margin-top:18px"><a href="the-snowies.html">And the Snowies, September 2026</a></p></div></section>''')
    out.append(footer())
    return '\n'.join(out)

if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'retreats'), exist_ok=True)
    for r in RETREATS:
        open(os.path.join(ROOT, 'retreats', r['slug'] + '.html'), 'w').write(page(r))
    open(os.path.join(ROOT, 'retreats', 'barrington-river.html'), 'w').write(barrington())
    paths = ['/', '/retreats/barrington-river.html'] + [f"/retreats/{r['slug']}.html" for r in RETREATS]
    import blog
    paths += blog.paths()
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sitemap(paths))
    open(os.path.join(ROOT, 'llms.txt'), 'w').write(llms(RETREATS, blog.POSTS))
    print('retreat pages:', len(RETREATS) + 1, '· sitemap:', len(paths), 'urls')
