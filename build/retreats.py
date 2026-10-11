"""Generate one page per retreat into retreats/<slug>.html from the data below.

Every page is self-contained HTML (own doctype, inline CSS) so it works on any static host
and inside the artifact preview. Copy rule: only facts from the WC notes, Instagram captions
or Sam. No invented numbers, quotes or places.
"""
import html, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
from seo import SITE, script, breadcrumbs, event, sitemap

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
        hero='sunset-broughton.jpg', hero_pos='50% 70%',
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
        hero='kayaks-bunya.jpg', hero_pos='50% 60%',
        story=[
            "Camp Bunya was the first time we ran it as a proper retreat. Days on the river in kayaks, yoga on the grass, and nights in sleeping bags round the fire.",
            "We learned a lot that weekend. The biggest lesson: go deeper, stay longer, get wilder. Everything we've run since has been built on it.",
        ],
        did=['Kayaking the river', 'Yoga on the grass', 'Sharing round the fire', 'Sleeping out under the stars'],
        quote=None,
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
        hero='beach-circle-croajingalong.jpg', hero_pos='50% 55%',
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
        hero='snow-tors-snowies.jpg', hero_pos='50% 60%',
        story=[
            "Our first retreat in the snow. A small group in a cottage at Crackenback, just down the road from Thredbo.",
            "We hiked out across the snow among the granite tors, cooked lunch in the snow gums, and came back to a sauna and an ice bath.",
            "On the first night every man brought one thing he loves and talked about it by the fire for ten minutes. It sounds soft. Then you watch a quiet bloke light up about the thing he cares about.",
        ],
        did=['Hiking in the snow', 'Breathwork and yoga', 'Deep listening', 'Show and tell by the fire', 'Sauna and ice bath'],
        quote=None,
        photos=[
            ('tors-figures-snowies.jpg', 'Snowy Mountains - Men\'s Retreat', 'Two tiny figures crossing snow below granite tors'),
            ('lunch-snowgums-snowies.jpg', 'Lunch in the snow gums', 'Four men in beanies eating lunch from one pot'),
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

CSS = """
:root{--sand:#D7D2C6;--sand-deep:#CCC6B8;--paper:#FBFAF6;--ink:#1F1E1B;--olive:#5E604A;--olive-text:#55573F;--amber:#F7AD19;--cream:#F1EEE6;--rust:#A65E39;
--sans:"Montserrat",system-ui,-apple-system,"Segoe UI",sans-serif;--hand:"Gaegu","Bradley Hand","Comic Sans MS",cursive;--type:"Courier Prime","Courier New",ui-monospace,monospace;--gutter:clamp(16px,4vw,40px);color-scheme:light}
*{box-sizing:border-box}html{scroll-behavior:smooth}html,body{overflow-x:clip}
body{margin:0;background:var(--sand);color:var(--ink);font-family:var(--sans);font-size:1.0625rem;line-height:1.7;-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}a{color:inherit}p{margin:0}h1,h2,h3{margin:0;text-wrap:balance}
a:focus-visible,button:focus-visible{outline:3px solid var(--amber);outline-offset:2px}
.wrap{max-width:1140px;margin-inline:auto;padding-inline:var(--gutter)}
section{padding-block:clamp(56px,8vw,96px)}
h2{font-weight:600;font-size:clamp(1.4rem,2.8vw,2rem);line-height:1.18;letter-spacing:.07em;text-transform:uppercase}
.eyebrow{font-family:var(--hand);font-size:1.45rem;line-height:1;color:var(--rust);margin-bottom:12px}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:40;opacity:.14;mix-blend-mode:multiply;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.btn{appearance:none;border:0;cursor:pointer;display:inline-block;text-decoration:none;font:600 .74rem/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;padding:14px 18px;background:var(--amber);color:var(--ink)}
.btn:hover{background:var(--cream)}
.on-photo{font-family:var(--hand);color:var(--amber);font-size:clamp(1.25rem,2vw,1.5rem);line-height:1.3;text-shadow:0 1px 10px rgba(0,0,0,.35)}

.hero{position:relative;color:var(--cream);isolation:isolate;background:var(--ink);min-height:clamp(480px,72vh,720px);display:grid;align-items:end}
.hero > .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2}
.hero::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(18,18,14,.5) 0%,rgba(18,18,14,.15) 35%,rgba(18,18,14,.75) 100%)}
.top{position:absolute;inset:0 0 auto 0;z-index:5;padding-top:env(safe-area-inset-top,0px)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-block:20px}
.top .home img{width:118px}
.top nav{display:flex;align-items:center;gap:clamp(14px,3vw,28px);font-weight:600;font-size:.72rem;letter-spacing:.18em;text-transform:uppercase}
.top nav a:not(.btn){color:var(--cream);text-decoration:none;border-bottom:1px solid transparent;padding-block:4px}
.top nav a:not(.btn):hover{border-color:var(--amber)}
.top .btn{padding:11px 14px}
.hero > .wrap{width:100%;display:grid;gap:10px;padding-block:120px clamp(32px,5vw,56px)}
.hero h1{font-weight:500;font-size:clamp(2rem,5vw,3.6rem);line-height:1.05;letter-spacing:.08em;text-transform:uppercase}
.hero .hook{max-width:52ch;font-size:clamp(1.02rem,1.5vw,1.18rem);opacity:.95}

.story .wrap{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,4fr);gap:clamp(28px,5vw,64px);align-items:start}
.prose{display:grid;gap:1.1em;max-width:60ch;font-size:1.08rem}
.did{background:var(--olive);color:var(--cream);padding:clamp(22px,3vw,30px);display:grid;gap:12px}
.did h3{font-weight:600;font-size:.8rem;letter-spacing:.18em;text-transform:uppercase;color:var(--amber)}
.did ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.did li{font-family:var(--hand);font-size:1.3rem;line-height:1.2}
.did li::before{content:"~ ";color:var(--amber)}
.quote{margin-top:clamp(28px,4vw,40px);filter:drop-shadow(0 16px 24px rgba(0,0,0,.25))}
.card{background:var(--paper);padding:clamp(22px,3vw,34px);display:grid;gap:12px}
.card blockquote{margin:0;font-family:var(--type);font-size:clamp(1rem,1.7vw,1.15rem);line-height:1.55}
.card cite{font-style:normal;font-family:var(--hand);font-size:1.25rem;color:var(--rust)}

.gallery{background:var(--sand-deep)}
.grid{columns:3 280px;column-gap:clamp(16px,2.4vw,28px);margin-top:clamp(24px,3vw,36px)}
.print{break-inside:avoid;margin:0 0 clamp(18px,2.6vw,30px);filter:drop-shadow(0 12px 16px rgba(0,0,0,.35))}
.print figure{background:var(--paper);padding:8px;margin:0}
.print img{width:100%}
.print figcaption{font-family:var(--type);font-size:.78rem;line-height:1.25;padding:8px 2px 2px}
.grid .print:nth-child(3n+1){transform:rotate(-.8deg)}.grid .print:nth-child(3n+2){transform:rotate(.6deg)}
""" + TORN + """
.others{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,2vw,24px);margin-top:24px}
.other{text-decoration:none;display:grid;gap:8px}
.other .print{margin:0}
.other b{font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:.9rem}
.other span{font-size:.85rem;color:var(--olive-text)}
.other:hover b{color:var(--rust)}

.nextup{position:relative;color:var(--cream);isolation:isolate;background:var(--ink)}
.nextup > .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 92%;z-index:-2}
.nextup::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(100deg,rgba(16,16,12,.85) 0%,rgba(16,16,12,.55) 60%,rgba(16,16,12,.3) 100%)}
.nextup .wrap{display:grid;gap:14px;justify-items:start}
.nextup h2{color:var(--amber)}
.details{display:grid;grid-template-columns:auto minmax(0,1fr);gap:8px 20px;margin:10px 0 0}
.details dt{font-weight:600;font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;opacity:.75;padding-top:4px}
.details dd{margin:0}
.faq{margin-top:18px;display:grid;gap:14px;max-width:52ch}
.faq b{display:block;font-weight:600}
footer{padding-block:40px 56px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:20px;font-size:.85rem}
footer img{width:130px}
.small{font-size:.8rem;color:var(--olive-text)}
@media (max-width:860px){.story .wrap{grid-template-columns:minmax(0,1fr)}.others{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.top nav a:not(.btn){display:none}.others{grid-template-columns:minmax(0,1fr)}}
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
  <nav aria-label="Site"><a href="../#proof">All retreats</a><a href="../#how">How it works</a><a class="btn" href="../#register">Tickets</a></nav>
</div></header>'''

def nextup():
    return '''<section class="nextup">
  <img class="bg" src="../img/river-bunya-wide.jpg" alt="" width="2000" height="1333" loading="lazy">
  <div class="wrap">
    <p class="on-photo">Next retreat</p>
    <h2>Barrington River Men's Retreat</h2>
    <p class="on-photo">Canoe | Connect | Express · December 4th - 6th</p>
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

def page(r):
    meta = r['when'] + (f" · {r['where']}" if r['where'] else '')
    path = f"/retreats/{r['slug']}.html"
    out = [head(f"{r['seo_title']} · Wildly Calm", r['seo_desc'], r['hero'], path, [breadcrumbs(r['name'], path)])]
    out.append(f'''<div class="hero">
  <img class="bg" src="../img/{r['hero']}" alt="" width="1400" height="933" style="object-position:{r['hero_pos']}" fetchpriority="high">
  {header()}
  <div class="wrap">
    <p class="on-photo">{e(meta)} · {e(r['tag'])}</p>
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
    prints = ''.join(f'<div class="print"><figure class="{torn(i)}"><img src="../img/{f}" alt="{e(a)}" loading="lazy"><figcaption>{e(c)}</figcaption></figure></div>' for i, (f, c, a) in enumerate(r['photos']))
    out.append(f'''<section class="gallery"><div class="wrap">
  <p class="eyebrow">Photos</p><h2>{e(r['name'])} in pictures</h2>
  <div class="grid">{prints}</div>
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
    out.append(f'''<div class="hero">
  <img class="bg" src="../img/river-bunya-wide.jpg" alt="" width="2000" height="1333" style="object-position:50% 92%" fetchpriority="high">
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
  <aside class="did"><h3>Tickets</h3><p style="font-size:.98rem">Tickets and the price are on the way. Head to the booking section for the latest.</p><a class="btn" href="../#register" style="justify-self:start">Book or register</a></aside>
</div></section>''')
    cards = ''.join(f'<a class="other" href="{o["slug"]}.html"><div class="print"><figure class="{torn(i)}"><img src="../img/{o["photos"][0][0]}" alt="" loading="lazy"></figure></div><b>{e(o["name"])}</b><span>{e(o["when"])}</span></a>' for i, o in enumerate(RETREATS[:3]))
    out.append(f'''<section class="gallery"><div class="wrap"><p class="eyebrow">Before this one</p><h2>Past retreats</h2><div class="others">{cards}</div><p style="margin-top:18px"><a href="the-snowies.html">And the Snowies, September 2026</a></p></div></section>''')
    out.append(footer())
    return '\n'.join(out)

if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'retreats'), exist_ok=True)
    for r in RETREATS:
        open(os.path.join(ROOT, 'retreats', r['slug'] + '.html'), 'w').write(page(r))
    open(os.path.join(ROOT, 'retreats', 'barrington-river.html'), 'w').write(barrington())
    paths = ['/', '/retreats/barrington-river.html'] + [f"/retreats/{r['slug']}.html" for r in RETREATS]
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sitemap(paths))
    print('retreat pages:', len(RETREATS) + 1, '· sitemap:', len(paths), 'urls')
