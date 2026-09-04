---
schema: qual/card@1
id: E-CLSFF
kind: problem
title: Meromorphic functions on $\mathbb{CP}^1$
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Principal Parts
  - Poles
  - Liouville's Theorem
  - Riemann Surfaces
relations: []
review: draft
---

::: {.exercise}
Show that the only meromorphic functions on $\CP^1$ are rational functions.
:::

::: {.solution}
Compactness of $\CP^1$ implies that $f$ has only finitely many poles.
Let $a_1,\ldots,a_n\in\CC$ be the finite poles, and let $P_j$ be the principal part of $f$ at $a_j$.
Then
\[
g(z)\da f(z)-\sum_{j=1}^nP_j(z)
\]
is entire on $\CC$.

The function $g$ is also meromorphic at $\infty$, because both $f$ and each rational principal part $P_j$ are meromorphic on $\CP^1$.
Hence $g(1/w)$ has at most a pole at $w=0$, so its Laurent series has only finitely many negative powers:
\[
g(1/w)=\sum_{k=-m}^{\infty}c_kw^k.
\]
Equivalently,
\[
g(z)=\sum_{k=1}^m c_{-k}z^k+h(z),
\]
where $h$ is entire and has a removable singularity at $\infty$.
Thus $h$ extends holomorphically to the compact sphere, so it is constant.
Therefore $g$ is a polynomial, and
\[
f(z)=g(z)+\sum_{j=1}^nP_j(z)
\]
is rational.
:::
