import random
# Torn-paper edges as clip-paths. The tear runs along each edge at a fixed depth in px (not % of the
# element), so a tall print and a small card tear the same amount and captions can sit clear of it.
# python3 build/torn.py > build/torn.css
def torn(seed, n=22, amp=6.0):
    r = random.Random(seed)
    j = lambda: r.uniform(0, amp) * (1.8 if r.random() < .15 else 1)
    pts = []
    for i in range(n + 1): pts.append(f'{i*100/n:.1f}% {j():.1f}px')
    for i in range(1, n + 1): pts.append(f'calc(100% - {j():.1f}px) {i*100/n:.1f}%')
    for i in range(1, n + 1): pts.append(f'{100-i*100/n:.1f}% calc(100% - {j():.1f}px)')
    for i in range(1, n): pts.append(f'{j():.1f}px {100-i*100/n:.1f}%')
    return 'polygon(' + ','.join(pts) + ')'
print('\n'.join(f'.torn-{k+1}{{clip-path:{torn(s)}}}' for k, s in enumerate([3, 11, 29, 41])))
