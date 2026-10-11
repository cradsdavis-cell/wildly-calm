"""Structured data (schema.org JSON-LD) and the sitemap, shared by build.py and retreats.py.

Facts only: everything here also appears in the visible page copy. Leave the Event's
offers out until there is a real ticket link (tickets_url in config.json).
"""
import json

SITE = 'https://wildlycalm.org'
INSTAGRAM = 'https://www.instagram.com/wildlycalmretreats/'
ORG_ID = SITE + '/#org'

ORG = {
    '@type': 'NGO',
    '@id': ORG_ID,
    'name': 'Wildly Calm',
    'url': SITE + '/',
    'logo': SITE + '/img/wc-logo-01.png',
    'image': SITE + '/img/hero-beach-croajingalong.jpg',
    'slogan': 'Nurture the man. Strengthen the boy.',
    'description': "Small outdoor retreats for men in their twenties and thirties: three days somewhere wild, something hard to do together, and honest conversation. A NSW not-for-profit incorporated association.",
    'email': 'wildlycalmretreats@gmail.com',
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Sydney', 'addressRegion': 'NSW', 'addressCountry': 'AU'},
    'areaServed': {'@type': 'State', 'name': 'New South Wales'},
    'foundingDate': '2025',
    'founder': [{'@type': 'Person', 'name': n} for n in ('Lockie Ranson', 'Kieran Maguire', 'Sam Davis')],
    'taxID': '11 518 768 964',
    'sameAs': [INSTAGRAM],
}

NEXT_EVENT = {
    '@type': 'Event',
    '@id': SITE + '/retreats/barrington-river.html#event',
    'name': "Barrington River Men's Retreat",
    'description': 'Three days canoeing the Barrington River, NSW: paddling, camping by the water, fire at night and the circle. For men in their twenties and thirties. Small group, on purpose.',
    'startDate': '2026-12-04',
    'endDate': '2026-12-06',
    'eventStatus': 'https://schema.org/EventScheduled',
    'eventAttendanceMode': 'https://schema.org/OfflineEventAttendanceMode',
    'location': {'@type': 'Place', 'name': 'Barrington River',
                 'address': {'@type': 'PostalAddress', 'addressRegion': 'NSW', 'addressCountry': 'AU'}},
    'image': [SITE + '/img/river-bunya-wide.jpg'],
    'url': SITE + '/retreats/barrington-river.html',
    'organizer': {'@id': ORG_ID, '@type': 'Organization', 'name': 'Wildly Calm', 'url': SITE + '/'},
}


def event(tickets_url=''):
    ev = dict(NEXT_EVENT)
    if tickets_url:
        ev['offers'] = {'@type': 'Offer', 'url': tickets_url, 'availability': 'https://schema.org/InStock'}
    return ev


def script(graph):
    data = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=1)
    return '<script type="application/ld+json">\n' + data.replace('</', '<\\/') + '\n</script>'


def home_jsonld(tickets_url=''):
    site = {'@type': 'WebSite', '@id': SITE + '/#website', 'name': 'Wildly Calm', 'url': SITE + '/',
            'inLanguage': 'en-AU', 'publisher': {'@id': ORG_ID}}
    return script([ORG, site, event(tickets_url)])


def breadcrumbs(name, path):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Wildly Calm', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Retreats', 'item': SITE + '/#proof'},
        {'@type': 'ListItem', 'position': 3, 'name': name, 'item': SITE + path},
    ]}


def sitemap(paths):
    urls = ''.join(f'  <url><loc>{SITE}{p}</loc></url>\n' for p in paths)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
