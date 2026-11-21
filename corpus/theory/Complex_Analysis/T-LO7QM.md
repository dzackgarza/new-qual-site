---
schema: qual/card@1
id: T-LO7QM
kind: theorem
title: Stokes' theorem
slogan: 'For a smooth $(n-1)$-form $\omega$ on a compact oriented $n$-manifold $M$ with boundary, $\int_{\bd M}\omega=\int_M d\omega$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $M$ be a compact oriented smooth $n$-manifold with boundary $\bd M$, carrying the induced orientation, and let $\omega$ be a smooth $(n-1)$-form on $M$.
Then
$$
\int_{\bd M}\omega=\int_M d\omega.
$$
In particular, let $\Omega\subseteq\CC$ be a bounded open set whose boundary consists of finitely many piecewise smooth closed curves, oriented positively with respect to $\Omega$, and let $f\in C^1(\overline{\Omega})$.
For $\omega=f(z)\dz$ one has $d\omega=\frac{\partial f}{\partial\overline z}\,d\overline z\wedge dz$ and $d\overline z\wedge dz=2i\,dx\wedge dy$, so
$$
\int_{\bd\Omega}f(z)\dz=2i\iint_\Omega\frac{\partial f}{\partial\overline z}\dA.
$$

This is [@Rud76, ch. 10, Theorem 10.33] in the Euclidean case, which states that $\int_\Psi d\omega=\int_{\partial\Psi}\omega$ for a $k$-chain $\Psi$ in an open set $V\subseteq\RR^m$ and a $(k-1)$-form $\omega$ of class $C'$ in $V$; the general manifold statement above is the chart-and-partition-of-unity reduction to it, and the second display is the case $k=m=2$ with $\omega=f\dz$.
:::
