---
schema: qual/card@1
id: PR-W4ICW
kind: proposition
title: Jensen's inequality
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Integrals
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]] with $\mu(X)=1$, let $-\infty\leq a<b\leq\infty$, and let $\phi\colon(a,b)\to\RR$ be convex, that is,
$$
\phi(tx + (1-t)y) \leq t\phi(x) + (1-t)\phi(y) \quad\text{for all } x,y\in(a,b) \text{ and } t\in[0,1].
$$
If $f\in L^1(\mu)$ is real-valued with $a<f(x)<b$ for all $x\in X$, then
$$
\phi\Big(\int_X f\dmu\Big)\leq\int_X\phi\circ f\dmu .
$$
:::
