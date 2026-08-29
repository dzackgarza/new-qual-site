---
schema: qual/card@1
id: S-4T6FK
kind: solution
title: Solution to P-JNFJW
classification:
  areas:
  - real-analysis
  topics:
  - Holomorphic Functions
  - Counterexamples
relations:
- kind: solves
  target: P-JNFJW
review: draft
---

:::{.solution}
(a) Let $a\ne b\in\Omega$. Let $\gamma$ be a straight line from $a$ to $b$, parameterized by $\gamma(t)=(1-t)b+ta$. By convexity, $\gamma$ lies in $\Omega$. So we can write $\int_\gamma f'(z)\,dz = f(b)-f(a)$. Write $f=u+iv$, then $f'=u_x+iv_x$. Examining the integral above, we have
$$f(b)-f(a) = \int_\gamma f'(z)\,dz = \int_0^1 (u_x(\gamma(t))+iv_x(\gamma(t)))(b-a)\,dt = (b-a)\int_0^1 (u_x(\gamma(t))+iv_x(\gamma(t)))\,dt.$$
Note that the integral on the right side has nonzero real part because $u_x$ is always positive. Thus the whole right side is just some nonzero complex number since $b-a$ is a nonzero constant, so $f(b)\ne f(a)$. $\square$

(b) [example not given in source]
:::
