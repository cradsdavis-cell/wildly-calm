import re,sys,os
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(here)
s=open(f'{here}/page.html').read().replace('/*TORN*/',open(f'{here}/torn.css').read())
import json
cfg=json.load(open(f'{here}/config.json'))
t=cfg.get('tickets_url','').strip()
cta={'CTA_URL': t or 'https://www.instagram.com/wildlycalmretreats/',
     'CTA_LABEL': 'Get tickets' if t else 'Register interest',
     'CTA_SHORT': 'Tickets' if t else 'Register',
     'CTA_TITLE': 'Tickets' if t else 'Register your interest',
     'CTA_NOTE': 'Tickets are on Humanitix.' if t else "Tickets go on sale soon. Message us on Instagram and we'll send you the plan, the price and the ticket link as soon as it's live."}
for k,v in cta.items(): s=s.replace('{{'+k+'}}',v)
open(f'{root}/index.html','w').write(s)
if len(sys.argv)>1:  # artifact preview: strip the document skeleton
    t=s
    for pat in [r'<!doctype html>\s*',r'<html[^>]*>\s*',r'</html>\s*',r'<head>\s*',r'</head>\s*',r'<body>\s*',r'</body>\s*',r'<meta charset[^>]*>\s*',r'<meta name="viewport"[^>]*>\s*']:
        t=re.sub(pat,'',t,flags=re.I)
    open(sys.argv[1],'w').write(t)
print('built')
import subprocess
subprocess.run([sys.executable, os.path.join(here, 'retreats.py')], check=True)
