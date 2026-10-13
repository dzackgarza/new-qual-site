---
schema: qual/card@1
id: PR-CRVDEGBD
kind: proposition
title: The degree thresholds $2g$ and $2g+1$
slogan: 'On a genus-$g$ curve, positive degree is ample, degree $2g$ frees base points, and degree $2g+1$ is very ample.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Very Ample Divisors
  - Ample Divisors
  - Linear Systems
relations:
- kind: uses
  target: T-MWDVL
- kind: uses
  target: D-CRVSPEC
review: draft
prompts:
- When is a divisor on a curve ample?
- When is a divisor on a curve base-point free?
- What degree guarantees a divisor on a curve is very ample?
---

::: {.proposition}
Let $D$ be a divisor on a smooth projective curve $C$ of genus $g$ over an algebraically closed field.

- $D$ is ample if and only if $\deg D > 0$.

- $\abs{D}$ is base-point free if $\deg D \geq 2g$.

- $D$ is very ample if $\deg D \geq 2g+1$.

:::

::: {.remark}
If $\deg D\geq2g$ and $p\in C$, then both $D$ and $D-p$ have degree greater than $2g-2$. Riemann--Roch therefore gives
$$
\ell(D)-\ell(D-p)=1,
$$
so $\abs D$ has no base point at $p$.

If $\deg D\geq2g+1$ and $E$ is any effective divisor of degree $2$, then $D-E$ has degree greater than $2g-2$, and
$$
\ell(D)-\ell(D-E)=2.
$$
Thus global sections separate every pair of points and every tangent direction, so $D$ is very ample.

If $\deg D>0$, then $\deg(nD)\geq2g+1$ for all sufficiently large $n$, so some positive multiple of $D$ is very ample and $D$ is ample. Conversely, if $D$ is ample, some positive multiple $nD$ is very ample and therefore has positive degree; hence $\deg D>0$.

The degree bounds for base-point freeness and very ampleness are sufficient rather than necessary. For a smooth plane quartic, $g=3$ and the canonical divisor has degree $4<2g+1=7$, but the canonical map is the given plane embedding.
On $\PP^1$, a divisor is ample or very ample exactly when its degree is positive. On an elliptic curve, a divisor is very ample exactly when its degree is at least $3$; degree $3$ gives the plane cubic embedding. On a genus-$2$ curve, every divisor of degree at least $5$ is very ample, and a degree-$5$ divisor embeds the curve as a quintic in $\PP^3$.
If $D$ is very ample and $\varphi$ is the resulting embedding, then $\deg \varphi(C) = \deg D$.
:::
