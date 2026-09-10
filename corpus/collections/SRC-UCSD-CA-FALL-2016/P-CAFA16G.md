---
schema: qual/card@1
id: P-CAFA16G
kind: problem
title: "Analytic continuation of the logarithm along a path is always a branch of the logarithm"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $\gamma: [0, 1] \to \mathbb{C}$ be a path such that $\gamma(0) = 1$ and $\gamma(t) \neq 0$ for every $t \in [0, 1]$.
Assume that $(f_t, D_t)_{0 \leq t \leq 1}$ is an analytic continuation of $f_0(z) = \log z$ along $\gamma$.
Prove that $f_t$ is a branch of the logarithm for every $t \in [0, 1]$.
:::

::: solution
For the initial germ,
\[
e^{f_0(z)}=z.
\]
We show that this identity propagates along the analytic continuation.

Whenever two consecutive continuation domains overlap, the corresponding functions agree on a nonempty open subset of the overlap. If $e^{f_s(z)}=z$ on the earlier domain, then on the overlap
\[
e^{f_t(z)}=e^{f_s(z)}=z.
\]
By the identity theorem, the holomorphic functions $e^{f_t(z)}$ and $z$ agree on all of the connected domain $D_t$.

Proceeding along the chain of overlapping continuation neighborhoods gives, for every $t$,
\[
e^{f_t(z)}=z\qquad(z\in D_t).
\]
In particular $0\notin D_t$, and $f_t$ is a holomorphic logarithm of the identity function on $D_t$. Thus each $f_t$ is a branch of the logarithm.
:::
