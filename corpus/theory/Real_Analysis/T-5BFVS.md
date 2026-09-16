---
schema: qual/card@1
id: T-5BFVS
kind: theorem
title: Duals of $L^p$ spaces
prompts:
- State the Riesz representation theorem for $L^p(X)\dual$.
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Lp Spaces
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $1\leq p<\infty$, and let $q\in(1,\infty]$ satisfy $\frac1p+\frac1q=1$.
If $p=1$, assume that $\mu$ is [[D-BXAUS|$\sigma$-finite]].
Then the map
$$
L^q(X,\mu)\to L^p(X,\mu)\dual,\qquad g\mapsto\qty{f\mapsto\int_X fg\dmu},
$$
is an isometric isomorphism onto the space $L^p(X,\mu)\dual$ of continuous linear functionals on $L^p(X,\mu)$ with the [[D-T4LOC|dual norm]] [@Fol13].
:::
