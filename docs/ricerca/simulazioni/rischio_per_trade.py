import numpy as np
rng=np.random.default_rng(7)
N=20000; T=2*250  # 2 trades/day, 1 year
scen={'edge_pos (p=0.35,W=2.2R)':(0.35,2.2),'zero_edge (p=0.33,W=2.0R)':(0.3333,2.0),'neg_edge (p=0.30,W=2.0R) + costs':(0.30,2.0)}
for name,(p,W) in scen.items():
    print(name, 'EV/trade R =', round(p*W-(1-p),3))
    for r in [0.01,0.02,0.03,0.05,0.10]:
        wins=rng.random((N,T))<p
        ret=np.where(wins,W*r,-r)
        eq=np.cumprod(1+ret,axis=1)
        peak=np.maximum.accumulate(np.concatenate([np.ones((N,1)),eq],axis=1),axis=1)[:,1:]
        dd=1-eq/peak
        mdd=dd.max(axis=1)
        # max losing streak effect & time
        out=[f"P(DD>={x:.0%})={np.mean(mdd>=x):.0%}" for x in (0.10,0.20,0.30,0.50)]
        print(f"  risk {r:.0%}: median final {np.median(eq[:,-1]):.2f}x | median maxDD {np.median(mdd):.0%} | "+" ".join(out))
# losing streak probability
p=0.35
for k in (5,8,10,12):
    # prob of at least one streak >=k in 500 trades via sim
    L=rng.random((N,500))>=p
    # compute longest run
    best=np.zeros(N,int); cur=np.zeros(N,int)
    for t in range(500):
        cur=np.where(L[:,t],cur+1,0); best=np.maximum(best,cur)
    print(f"win rate 35%: P(streak of >= {k} losses in 500 trades) = {np.mean(best>=k):.0%}")
