---
schema: qual/card@1
id: P-L52MJ
kind: problem
title: $\int_\Delta f=0$ for triangles when $f$ is holomorphic off one point and bounded
  nearby
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Morera
  - Contour Integration
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source read "if f(z) is bounded in near z_0" and "for all triangles Delta in Omega". The typo "in near" now reads "near", and a triangle in Omega is now a closed triangle that lies in Omega together with its interior; if only the boundary lies in Omega the claim fails. The earlier solution appealed to the maximum modulus principle for a bound it did not need and was replaced by a subdivision proof.'
---

::: {.problem}
Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a point $z_0$ inside $\Omega$.
Show that if $f(z)$ is bounded near $z_0$, then $\int_{\partial\Delta} f(z)\, dz = 0$ for all closed triangles $\Delta$ contained, together with their interiors, in $\Omega$.
:::

::: {.solution}
Let $\abs{f} \leq M$ on $D(z_0, r) \setminus \{z_0\}$ with $D(z_0,r) \subseteq \Omega$, and let $d$ and $p$ be the diameter and perimeter of $\Delta$.

::: pf

::: {.pf-step #subdivide}
For each $n$, $\int_{\partial\Delta} f\,dz$ is the sum of $\int_{\partial\Delta'} f\,dz$ over the $4^n$ congruent triangles $\Delta'$ obtained by subdividing $\Delta$ $n$ times through the midpoints of the sides.
Each $\Delta'$ has diameter $2^{-n}d$ and perimeter $2^{-n}p$, and at most six of them contain $z_0$.

::: pf-proof
The interior edges are traversed once in each direction and cancel.
The triangles form a triangulation of $\Delta$, and a point of it lies in at most six of its triangles.
:::

:::

::: {.pf-step #away}
If $z_0 \notin \Delta'$, then $\int_{\partial\Delta'} f\,dz = 0$.

::: pf-proof
$f$ is holomorphic on a neighbourhood of $\Delta'$, so Goursat's theorem applies.
:::

:::

::: pf-step
$\int_{\partial\Delta} f\,dz = 0$.

::: pf-proof
If $z_0 \notin \Delta$, this is step [](#away){.pf-ref} with $\Delta' = \Delta$.
Otherwise take $n$ with $2^{-n}d < r$; a triangle $\Delta'$ of step [](#subdivide){.pf-ref} that contains $z_0$ lies in $D(z_0, r)$, so $\abs{\int_{\partial\Delta'} f\,dz} \leq M\cdot 2^{-n}p$.
By steps [](#subdivide){.pf-ref} and [](#away){.pf-ref}, $\abs{\int_{\partial\Delta} f\,dz} \leq 6M\cdot 2^{-n}p$ for every large $n$.
:::

:::

:::
:::
