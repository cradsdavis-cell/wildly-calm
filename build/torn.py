import random
def torn(seed,n=22,amp=2.6):
    r=random.Random(seed); pts=[]
    j=lambda: r.uniform(0,amp)*(1.8 if r.random()<.15 else 1)
    for i in range(n+1): pts.append((i*100/n, j()))
    for i in range(1,n+1): pts.append((100-j(), i*100/n))
    for i in range(1,n+1): pts.append((100-i*100/n, 100-j()))
    for i in range(1,n): pts.append((j(), 100-i*100/n))
    return 'polygon('+','.join(f'{x:.1f}% {y:.1f}%' for x,y in pts)+')'
print('\n'.join(f'.torn-{k+1}{{clip-path:{torn(s)}}}' for k,s in enumerate([3,11,29,41])))
