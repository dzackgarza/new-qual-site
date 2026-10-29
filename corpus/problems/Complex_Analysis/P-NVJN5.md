---
schema: qual/card@1
id: P-NVJN5
kind: problem
title: Triangle integrals vanish if $f$ is bounded near an isolated singularity
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
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'Corrected the typo "bounded in near" to "bounded near".'
---

::: {.problem}
Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a point $z_0$ inside $\Omega$.

Show that if $f(z)$ is bounded near $z_0$, then $\displaystyle \int_\Delta f(z) dz = 0$ for all triangles $\Delta$ in $\Omega$.
:::

::: {.solution}
Here a triangle $\Delta$ in $\Omega$ is a closed solid triangle contained in $\Omega$, and $\int_\Delta$ is the integral over its boundary. Let $\abs{f}\le M$ on a punctured disk $0<\abs{z-z_0}<\rho$ contained in $\Omega$. The cases below use Goursat's theorem: the integral of a holomorphic function over the boundary of a triangle on whose closure it is holomorphic vanishes.

::: pf

::: {.pf-step #outside}
If $z_0\notin\Delta$, then $\int_\Delta f=0$.

::: pf-proof
$f$ is holomorphic on the open set $\Omega\setminus\theset{z_0}$, which contains $\Delta$; apply Goursat's theorem.
:::

:::

::: {.pf-step #vertex}
If $z_0$ is a vertex of $\Delta$, then $\int_\Delta f=0$.

::: pf-proof
Let $\Delta=[z_0,b,c]$ and $0<\varepsilon<\rho$. Choose $b'$ on $[z_0,b]$ and $c'$ on $[z_0,c]$ so that the triangle $T=[z_0,b',c']$ has perimeter less than $\varepsilon$. Then $\Delta$ is the union of $T$, $[b',b,c]$, and $[b',c,c']$, the boundary integrals over the common edges cancel, and the last two triangles do not contain $z_0$. By step [](#outside){.pf-ref},
$$
\abs{\int_\Delta f}=\abs{\int_{\partial T} f}\le M\varepsilon,
$$
since $\partial T\setminus\theset{z_0}$ lies in the punctured disk where $\abs{f}\le M$. Let $\varepsilon\to0$.
:::

:::

::: pf-step
If $z_0\in\Delta$, then $\int_\Delta f=0$.

::: pf-proof
If $\Delta=[a,b,c]$, then $\Delta$ is the union of the triangles $[z_0,a,b]$, $[z_0,b,c]$, $[z_0,c,a]$, some possibly degenerate, and the integrals over the edges through $z_0$ cancel. So $\int_\Delta f$ is the sum of the three integrals, each zero by step [](#vertex){.pf-ref}; the integral over a degenerate triangle is zero because its boundary traverses a segment once in each direction.
:::

:::

:::
:::
