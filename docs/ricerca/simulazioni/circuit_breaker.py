import numpy as np
rng=np.random.default_rng(11)
N=20000; T=500
def run(p,W,base,tiers,stop):
    eq=np.ones(N); peak=np.ones(N); stopped=np.zeros(N,bool); t_stop=np.full(N,-1)
    for t in range(T):
        dd=1-eq/peak
        r=np.full(N,base)
        for lvl,rr in tiers:
            r=np.where(dd>=lvl,np.minimum(r,rr),r)
        newstop=(dd>=stop)&~stopped
        t_stop[newstop]=t; stopped|=newstop
        win=rng.random(N)<p
        ret=np.where(win,W*r,-r)
        eq=np.where(stopped,eq,eq*(1+ret)); peak=np.maximum(peak,eq)
    return stopped.mean(), np.median(eq), np.median(t_stop[t_stop>=0]) if stopped.any() else None
scen={'edge +0.12R':(0.35,2.2),'edge 0':(0.3333,2.0),'edge -0.10R':(0.30,2.0)}
for base in (0.02,0.015):
  for stop in (0.20,0.25):
    tiers=[(0.10,0.01),(0.15,0.005)]
    print(f"base risk {base:.1%}, tiers -10%->1%, -15%->0.5%, STOP at -{stop:.0%}")
    for n,(p,W) in scen.items():
        s,m,ts=run(p,W,base,tiers,stop)
        print(f"   {n:12s}: P(stop in 500 trades)={s:.0%}  median final equity={m:.2f}x  median trade# of stop={ts}")
print("----")
for base in (0.02,):
  for tiers,stop in [([(0.10,0.01)],0.25),([(0.10,0.01),(0.18,0.005)],0.25),([(0.10,0.01)],0.30),([(0.12,0.01),(0.20,0.005)],0.30)]:
    print(f"base {base:.0%} tiers {tiers} STOP -{stop:.0%}")
    for n,(p,W) in scen.items():
        s,m,ts=run(p,W,base,tiers,stop)
        print(f"   {n:12s}: P(stop)={s:.0%}  median final={m:.2f}x  median trade# stop={ts}")
