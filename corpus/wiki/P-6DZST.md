---
schema: qual/card@1
id: P-6DZST
kind: problem
title: "5. WLOG, assume $p_0, p_1$ are the north and south poles of $S^2$. We\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
5. WLOG, assume $p_0, p_1$ are the north and south poles of $S^2$. We can then form a deformation retract of $X$ onto the equator of $S^2$, which is equal to $S^1$. To do so, just move every point $x$ along the unique great circle connecting $x, p_0, p_1$, and proceed at linear speed towards the equator. This is well defined at every point on $S^2$ *except* the poles, which are not included in $X$, and the equator is fixed at every instant. So this forms a deformation retract.
Alternatively, use the fact that $\RR^n -\pt \cong S^{n-1} \cross \RR$ via polar coordinates, and $S^n - \pt \cong \RR^n$ by stereographic projection. So $S^2 - \theset{p_0, p_1} \cong \RR^2 - \theset{p_1} \cong S^{1} \cross \RR$. But since $\RR$ is contractible, the last one is homotopic to $S^1 \cross \theset {0} \cong S^1$.
**Alternatively**: use the lemma, then $k=2$ and so $S^2 - \theset{p_1, p_2} \homotopic \bigvee_{i=1}^{1}S^1 = S^1$.

