---
schema: qual/card@1
id: T-D8TUX
kind: theorem
title: When the canonical divisor is very ample
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
Let $C$ be a smooth projective curve of genus $g$ over $k = \bar{k}$.
The canonical divisor $K$ is very ample exactly when $g \geq 3$ and $C$ is not hyperelliptic.
:::

::: {.proposition title="The criterion it comes from"}
For every divisor $D$ and closed point $p$ on $C$, $\ell(D) - 1 \leq \ell(D - p) \leq \ell(D)$.
A divisor $D$ on $C$ is very ample if and only if
\[
\ell(D - p - q) = \ell(D) - 2 \quad \text{for all points } p, q ,
\]
including $p = q$.
It is base-point free if and only if $\ell(D - p) = \ell(D) - 1$ for all $p$.
Any $D$ with $\deg D \geq 2g+1$ is very ample.
[@Har10a, Proposition IV.3.1, Corollary IV.3.2]
:::

::: {.remark}
The criterion says the linear system separates points and tangent vectors, which is exactly what an embedding must do.
Applied to $K$ and using duality, $\ell(K-p-q) = \ell(K) - 2$ fails precisely when $\ell(p+q) = 2$, that is, when there is a degree-two map to $\PP^1$ — the definition of hyperelliptic.

The excluded cases are genuinely excluded: for $g = 0$, $\deg K < 0$; for $g = 1$, $K = 0$; for $g = 2$, every curve is hyperelliptic and $K$ gives the degree-two map rather than an embedding.
For $g \geq 3$ non-hyperelliptic, $K$ embeds $C$ as a curve of degree $2g-2$ in $\PP^{g-1}$, the canonical curve, which for $g = 3$ is a smooth plane quartic and for $g = 4$ a curve of degree $6$ in $\PP^3$.
:::
