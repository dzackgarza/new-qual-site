---
schema: qual/card@1
id: PR-DIVAMPCURVE
kind: proposition
title: Ampleness of a divisor on a curve
slogan: 'On a smooth projective curve, positive degree is ample, degree $2g$ kills base points, and degree $2g+1$ is very ample.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ample Divisors
  - Curves
  - Degree
relations:
- kind: uses
  target: D-DIVAMPLE
- kind: uses
  target: PR-Y5S7V
- kind: related-to
  target: PR-CRVDEGBD
- kind: related-to
  target: T-D8TUX
review: draft
prompts:
- When is a divisor on a curve ample?
- What degree makes a divisor on a curve base-point free? Very ample?
---

::: {.proposition}
Let $D$ be a divisor on a smooth projective curve $X$ of genus $g$ over an algebraically closed field $k$.

- $D$ is ample if and only if $\deg D > 0$.

- $\deg D \geq 2g$ implies $\abs{D}$ is base-point free.

- $\deg D \geq 2g+1$ implies $D$ is very ample.
:::

::: {.remark}
If $\deg D\geq2g$, then for every $p\in X(k)$, Riemann--Roch gives
$$
\ell(D)-\ell(D-p)=1,
$$
so $\abs D$ is base-point free.
If $\deg D\geq2g+1$, then for every effective divisor $E$ of degree $2$,
$$
\ell(D)-\ell(D-E)=2,
$$
so sections separate points and tangent directions and $D$ is very ample.

If $\deg D>0$, then $nD$ has degree at least $2g+1$ for all sufficiently large $n$, so $D$ is ample. Conversely, if $D$ is ample, some $nD$ is very ample and therefore has positive degree.

For an elliptic curve, degree $2$ is base-point free but not very ample, while every divisor of degree $3$ is very ample. Thus the two sufficient bounds are attained in genus $1$.
:::
