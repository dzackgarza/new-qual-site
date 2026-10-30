---
schema: qual/card@1
id: T-D8TUX
kind: theorem
title: When the canonical divisor is very ample
slogan: 'The canonical map embeds exactly the non-hyperelliptic curves of genus at least $3$; a degree-two pencil is the obstruction.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Canonical Divisor
  - Very Ample Divisors
  - Hyperelliptic Curves
relations:
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- When is a canonical divisor very ample?
- When is a divisor on a curve very ample?
---

::: {.theorem}
Let $C$ be a smooth projective curve of genus $g$ over an algebraically closed field $k$.
The canonical divisor $K$ is very ample exactly when $g \geq 3$ and $C$ is not hyperelliptic.
:::

::: {.proposition title="Very-ampleness criterion"}
For every divisor $D$ and point $p\in C(k)$,
$$
\ell(D)-1\leq\ell(D-p)\leq\ell(D).
$$
A divisor $D$ on $C$ is very ample if and only if
$$
\ell(D - p - q) = \ell(D) - 2 \quad \text{for all points } p, q ,
$$
including $p = q$.
It is base-point free if and only if $\ell(D - p) = \ell(D) - 1$ for all $p$.
Any $D$ with $\deg D \geq 2g+1$ is very ample.
[@Har10a, Proposition IV.3.1, Corollary IV.3.2]
:::

::: {.remark}
The inequalities follow from
$$
0\to\OO_C(D-p)\to\OO_C(D)\to\OO_C(D)\restrict_p\to0,
$$
because $H^0(p,\OO_C(D)\restrict_p)$ is one-dimensional over $k$.
The very-ampleness criterion is equivalent to separation of pairs of points and tangent vectors, with the case $p=q$ testing tangent vectors.
Applied to $K$ and using Riemann--Roch,
$$
\ell(K-p-q)=g-3+\ell(p+q).
$$
Hence $K$ fails to be very ample exactly when some divisor $p+q$ moves in a pencil, equivalently when $C$ has a $g^1_2$ and is hyperelliptic.

For $g = 0$, $\deg K < 0$. For $g = 1$, $K \sim 0$. For $g = 2$, every curve is hyperelliptic and the canonical map has degree $2$ onto $\PP^1$.
For $g \geq 3$ non-hyperelliptic, $K$ embeds $C$ as a curve of degree $2g-2$ in $\PP^{g-1}$. In genus $3$ the canonical curve is a smooth plane quartic, and in genus $4$ it has degree $6$ in $\PP^3$.
:::
