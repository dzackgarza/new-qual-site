---
schema: qual/card@1
id: P-XPDMQ
kind: problem
title: "Main Idea: Exact same idea as 1, just a more complicated\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
2. **Main Idea**: Exact same idea as 1, just a more complicated check.

Take $H(x, t) = P(tf(x) + (1-t)g(x))$.
This is well defined; the only case to check is when the denominator is zero. But $\norm{x} = 0$ iff $x =0$, which would imply $tf(x) +(1-t)g(x) = 0$ and so $tf(x) = -(1-t)g(x)$.

Taking norms and observing that since $f,g \in S^n \implies \norm{f} = \norm{g} = 1$, this forces $t = 1-t$ and thus $t=1/2$. But this would force $(1/2)f(x) = (-1/2)g(x)$ and thus $f(x) = -g(x)$, which we assumed was not the case.

