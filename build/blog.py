"""Generate the blog: blog/index.html (list of posts) and blog/<slug>.html (one page per post).

Reuses the retreat pages' head, header, footer and CSS, so the blog looks like the rest of
the site. Copy rule: a post is the author's own words, verbatim. Don't tidy their grammar or
punctuation; the only words we add are the title, byline, standfirst and photo captions they gave us.

Add a post: put its photos in img/, add a dict to POSTS (newest first), run build/build.py.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo import SITE, ORG_ID, script
from retreats import CSS, e, head, header, footer, torn

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

POSTS = [
    dict(
        slug='a-good-man',
        title='A Good Man',
        author='Kieran Maguire',
        role='Co-founder, Wildly Calm',
        date='2026-10-22', date_label='22 October 2026',
        kind='A poem',
        seo_desc="Kieran Maguire, one of Wildly Calm's co-founders, on the conversation with his dad that let him go to Ireland, and the poem he wrote on the flight out.",
        standfirst="On a hard conversation with his dad, his first trip to Ireland as an adult, and the poem he wrote on the flight out.",
        hero='kieran-carrauntoohil-hero.jpg', hero_1200='kieran-carrauntoohil-hero-1200.jpg', hero_pos='50% 55%',
        hero_alt='Looking down from Carrauntoohil over green valleys to a lake',
        intro=[
            "I wrote this poem when I left Ireland this year after traveling there for the first time in my adult life, which was a really pivotal experience for me. My dad is Irish, and historically I’ve had a pretty difficult relationship with him. I used to hold a lot of resentment towards him, and there were many negative feelings that I held inside my heart, which gets very heavy as the years go by.",
            "Thanks to many years of working on myself, and in a big part - my involvement in Wildly Calm, I was able to muster up the courage to have a conversation with him a few months before my trip, and I was able to share all of the things that I felt about him, and how his actions had affected my life. His response wasn’t amazing - but it didn’t really matter. The important part was getting it off of my chest.",
            "I had avoided Ireland in the past, but thanks to that conversation, I was able to go to the country where my roots were from, and connect with it in my own special way. Amongst a lot of tears on my flight out of Ireland, I wrote this little poem:",
        ],
        poem_title='A Good Man',
        poem=[
            "It’s so nice to feel it all; The love, the joy, the magic, and the pain - the moments of hurt that create the perspective to truly value all of the amazing other things that life has to offer.",
            "And then there is the freedom to feel; The freedom to laugh, and the freedom to cry! Because feelings are FEELINGS. They exist to be FELT.",
            "Remember that, and remember this: You are a special man, with a very kind, warm soul. You are all of the things that you aspired to be.",
            "You are.",
            "You look good. You feel good. But most importantly, you have no shame in screaming “I am not perfect and I never will be”",
        ],
        photos_title='Ireland, in pictures',
        # (file, Kieran's caption, alt text, width, height)
        photos=[
            ('kieran-surf-coumeenoole.jpg', 'My first surf in the Atlantic at Coumeenoole Beach', 'Kieran sitting on a stone wall above Coumeenoole Beach with a longboard', 1600, 1067),
            ('kieran-carrauntoohil.jpg', 'The view down from Carrauntoohil (highest mountain in Ireland)', 'Rocky green slopes falling away to a lake below Carrauntoohil', 1067, 1600),
            ('kieran-rewild-sunset.jpg', 'Watching the sunset with new friends that I met volunteering at Rewild Festival', 'Seven friends sitting on the grass at dusk, one playing guitar', 1600, 1200),
            ('kieran-rewild-sign.jpg', 'Celebrating putting up the main festival sign at Rewild', 'Two men below a hand-painted REWILD sign strung between poles', 899, 1599),
        ],
    ),
    dict(
        slug='the-other-half-of-the-room',
        title='The Other Half of the Room',
        author='Sam Davis',
        role='Co-founder, Wildly Calm',
        date='2026-09-25', date_label='September 2026',
        kind='An essay',
        seo_desc='Men and women are being sold stories about each other. The first AI most of us lived with was built to sell them. What should the next one be built for?',
        standfirst='Men and women are being sold stories about each other. The first AI most of us lived with was built to sell them. What should the next one be built for?',
        hero='ohr-campfire.jpg', hero_1200='ohr-campfire.jpg', hero_pos='50% 50%',
        hero_alt='A figure in a hooded jacket sitting alone on a log beside a campfire at night, sparks rising, a tent behind',
        card=('ohr-fire.jpg', 1600, 1067),
        # The essay body is HTML copied from the published page; see the note at the top of the file.
        body_file='the-other-half-of-the-room.html',
        canonical='https://crads-ai.com/writing/the-other-half-of-the-room',
        first_published='This essay first appeared on <a href="https://crads-ai.com/writing/the-other-half-of-the-room" rel="noopener">crads-ai.com</a> in September 2026.',
    ),
]

INDEX_HERO = ('kieran-carrauntoohil-hero.jpg', 'kieran-carrauntoohil-hero-1200.jpg', '50% 55%')

BLOG_CSS = """
.posts{display:grid;gap:clamp(28px,4vw,44px);margin-top:clamp(24px,3vw,36px)}
.post-card{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,6fr);gap:clamp(20px,4vw,48px);align-items:center;text-decoration:none}
.post-card .print{margin:0}
.post-card h2{margin:6px 0 10px}
.post-card:hover h2{color:var(--rust)}
.post-card .by{font-family:var(--type);font-size:.85rem;color:var(--olive-text)}
.post-card .read{display:inline-block;margin-top:14px;font-weight:600;font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;border-bottom:2px solid var(--amber);padding-bottom:2px}
.byline{font-family:var(--type);font-size:.9rem;opacity:.9}
.article .wrap{max-width:760px}
.article .prose{max-width:none}
.poem{margin:clamp(32px,5vw,48px) 0 0;filter:drop-shadow(0 16px 24px rgba(0,0,0,.25))}
.poem .card{gap:18px;padding:clamp(28px,5vw,52px)}
.poem h2{font-family:var(--hand);font-weight:700;text-transform:none;letter-spacing:0;font-size:clamp(1.9rem,4vw,2.5rem);color:var(--rust)}
.poem p{font-family:var(--type);font-size:clamp(1.02rem,1.8vw,1.15rem);line-height:1.7}
.poem cite{font-style:normal;font-family:var(--hand);font-size:1.3rem;color:var(--rust)}
.grid.two{columns:auto;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(18px,2.6vw,30px) clamp(16px,2.4vw,28px);align-items:start}
.grid.two .print{margin:0}
.grid.two img.tall{aspect-ratio:4/5;object-fit:cover}
.grid.two figcaption{padding-bottom:22px}
.essay h2{margin-top:1.4em;font-size:clamp(1.1rem,2.2vw,1.4rem)}
.essay a{color:var(--rust);text-underline-offset:3px}
.essay em{font-style:italic}
.essay-figure{margin:clamp(12px,2vw,20px) 0;background:var(--paper);padding:8px;filter:drop-shadow(0 12px 16px rgba(0,0,0,.3))}
.essay-figure:nth-of-type(odd){transform:rotate(-.6deg)}.essay-figure:nth-of-type(even){transform:rotate(.5deg)}
.essay-figure img{width:100%;max-height:80vh;object-fit:cover}
.essay-figure figcaption{font-family:var(--type);font-size:.78rem;line-height:1.3;padding:8px 2px 4px}
.essay-figure .credit{color:var(--olive-text)}
.essay-refs{margin-top:1.5em;font-size:.88rem}
.essay-refs summary{cursor:pointer;font-weight:600;letter-spacing:.12em;text-transform:uppercase;font-size:.78rem}
.essay-refs h3{font-weight:600;font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;margin:1.2em 0 .4em;color:var(--olive-text)}
.essay-refs ul{margin:0;padding-left:1.1em;display:grid;gap:.5em;overflow-wrap:anywhere}
.first-pub{margin-top:1.4em;font-size:.88rem;color:var(--olive-text)}
@media (max-width:760px){.post-card,.grid.two{grid-template-columns:minmax(0,1fr)}}
"""


def blog_head(title, desc, img, path, graph, og_type='website', canonical=None):
    h = head(title, desc, img, path, graph).replace('<style>' + CSS, '<style>' + CSS + BLOG_CSS)
    if canonical:  # cross-posted: point search engines at the original
        h = h.replace(f'<link rel="canonical" href="{SITE}{path}">', f'<link rel="canonical" href="{canonical}">')
    return h.replace('<meta property="og:type" content="website">', f'<meta property="og:type" content="{og_type}">')


def crumbs(*items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + p} for i, (n, p) in enumerate(items)]}


def hero(img, img_1200, pos, alt, kicker, title, hook):
    srcset = f' srcset="../img/{img_1200} 1200w, ../img/{img} 2000w" sizes="100vw"' if img_1200 != img else ''
    return f'''<div class="hero">
  <img class="bg" src="../img/{img}"{srcset} alt="{e(alt)}" width="2000" height="1333" style="object-position:{pos}" fetchpriority="high">
  {header()}
  <div class="wrap">
    <p class="on-photo">{kicker}</p>
    <h1>{e(title)}</h1>
    <p class="hook">{hook}</p>
  </div>
</div>'''


def post_page(p):
    path = f"/blog/{p['slug']}.html"
    graph = [crumbs(('Wildly Calm', '/'), ('Blog', '/blog/'), (p['title'], path)), {
        '@type': 'BlogPosting', 'headline': p['title'], 'description': p['seo_desc'],
        'datePublished': p['date'], 'image': SITE + '/img/' + p['hero'], 'url': SITE + path,
        'author': {'@type': 'Person', 'name': p['author']}, 'publisher': {'@id': ORG_ID},
        'inLanguage': 'en-AU'}]
    if p.get('canonical'):
        graph[1]['mainEntityOfPage'] = p['canonical']
    out = [blog_head(f"{p['title']}, by {p['author']} · Wildly Calm", p['seo_desc'], p['hero'], path, graph, 'article', p.get('canonical'))]
    out.append(hero(p['hero'], p['hero_1200'], p['hero_pos'], p['hero_alt'],
                    f"Blog · {e(p['kind'])}", p['title'],
                    f"{e(p['standfirst'])}<br><span class=\"byline\">{e(p['author'])} · {e(p['date_label'])}</span>"))
    if p.get('body_file'):
        body = open(os.path.join(HERE, 'posts', p['body_file'])).read()
        out.append(f'''<section class="article"><div class="wrap">
  <p class="eyebrow">{e(p['author'])}, {e(p['role'].split(',')[0].lower())}</p>
  <div class="prose essay">{body}</div>
  <p class="first-pub">{p['first_published']}</p>
</div></section>''')
        return '\n'.join(out + [more(), footer()])
    intro = ''.join(f'<p>{e(x)}</p>' for x in p['intro'])
    poem = ''.join(f'<p>{e(x)}</p>' for x in p['poem'])
    out.append(f'''<section class="article"><div class="wrap">
  <p class="eyebrow">{e(p['author'])}, {e(p['role'].split(',')[0].lower())}</p>
  <div class="prose">{intro}</div>
  <div class="poem"><div class="card torn-3"><h2>{e(p['poem_title'])}</h2>{poem}<cite>{e(p['author'])}</cite></div></div>
</div></section>''')
    prints = ''.join(f'<div class="print"><figure class="{torn(i)}"><img src="../img/{f}"{' class="tall"' if h > w else ''} alt="{e(a)}" width="{w}" height="{h}" loading="lazy"><figcaption>{e(c)}</figcaption></figure></div>'
                     for i, (f, c, a, w, h) in enumerate(p['photos']))
    out.append(f'''<section class="gallery"><div class="wrap">
  <p class="eyebrow">Photos by {e(p['author'].split()[0])}</p><h2>{e(p['photos_title'])}</h2>
  <div class="grid two">{prints}</div>
</div></section>''')
    out.append(more())
    out.append(footer())
    return '\n'.join(out)


def more():
    return '''<section><div class="wrap"><p class="eyebrow">More</p><h2>Back to the blog</h2>
  <p style="margin-top:14px"><a class="btn" href="./">All posts</a> <a class="btn" href="../retreats/barrington-river.html" style="background:var(--cream)">Next retreat</a></p>
</div></section>'''


def card(p):
    if p.get('card'):
        return p['card']
    f, _, _, w, h = p['photos'][0]
    return f, w, h


def index_page():
    path = '/blog/'
    graph = [crumbs(('Wildly Calm', '/'), ('Blog', path)),
             {'@type': 'Blog', 'name': 'Wildly Calm blog', 'url': SITE + path, 'publisher': {'@id': ORG_ID}, 'inLanguage': 'en-AU',
              'blogPost': [{'@type': 'BlogPosting', 'headline': p['title'], 'url': f"{SITE}/blog/{p['slug']}.html", 'datePublished': p['date']} for p in POSTS]}]
    out = [blog_head('Blog · Wildly Calm', 'Writing from the people behind Wildly Calm: poems, stories and what we learn out there.', INDEX_HERO[0], path, graph)]
    out.append(hero(*INDEX_HERO, '', 'Wildly Calm', 'Blog',
                    'Writing from the people behind Wildly Calm.'))
    cards = ''.join(f'''<a class="post-card" href="{p['slug']}.html">
  <div class="print"><figure class="{torn(i + 1)}"><img src="../img/{card(p)[0]}" alt="" width="{card(p)[1]}" height="{card(p)[2]}" loading="lazy"></figure></div>
  <div><p class="eyebrow">{e(p['kind'])}</p><h2>{e(p['title'])}</h2><p>{e(p['standfirst'])}</p><p class="by" style="margin-top:10px">{e(p['author'])} · {e(p['date_label'])}</p><span class="read">Read it</span></div>
</a>''' for i, p in enumerate(POSTS))
    out.append(f'<section><div class="wrap"><p class="eyebrow">Latest</p><div class="posts">{cards}</div></div></section>')
    out.append(footer())
    return '\n'.join(out)


def paths():
    # cross-posts with a canonical elsewhere stay out of the sitemap
    return ['/blog/'] + [f"/blog/{p['slug']}.html" for p in POSTS if not p.get('canonical')]


if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'blog'), exist_ok=True)
    for p in POSTS:
        open(os.path.join(ROOT, 'blog', p['slug'] + '.html'), 'w').write(post_page(p))
    open(os.path.join(ROOT, 'blog', 'index.html'), 'w').write(index_page())
    print('blog pages:', len(POSTS) + 1)
