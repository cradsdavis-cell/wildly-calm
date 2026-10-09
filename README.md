# Wildly Calm website

Static site for Wildly Calm (men's outdoor retreats, NSW not-for-profit). Hosted on GitHub Pages; every push to `main` goes live.

## Editing
- Main page source: `build/page.html`. Retreat pages: data + template in `build/retreats.py`.
- Ticket link: set `tickets_url` in `build/config.json` (Humanitix event link). Empty = buttons go to Instagram.
- Rebuild: `python3 build/build.py`, then commit and push. Never edit `index.html` or `retreats/*.html` by hand; they are generated.
- Brand notes: `docs/brand-notes.md`. No phone numbers on the site.
