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
---

::: problem
Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a point $z_0$ inside $\Omega$.

Show that if $f(z)$ is bounded in near $z_0$, then $\displaystyle \int_\Delta f(z) dz = 0$ for all triangles $\Delta$ in $\Omega$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $f$ is analytic on $\Omega \setminus \theset{z_0}$ and bounded near $z_0$, show $\int_\Delta f = 0$ for every triangle $\Delta \subseteq \Omega$.

<1>1. $z_0$ is a removable singularity of $f$.
Proof: $f$ is bounded in a punctured neighborhood of $z_0$, so by Riemann's theorem on removable singularities $f$ extends holomorphically across $z_0$; call the extension $\tilde f$, which is holomorphic on all of $\Omega$.

<1>2. For every triangle $\Delta \subseteq \Omega$, $\int_\Delta \tilde f = 0$.
Proof: $\tilde f$ is holomorphic on the open set $\Omega$, so the Cauchy–Goursat theorem gives vanishing integrals over all closed triangles.

<1>3. $\int_\Delta f = 0$ for every triangle $\Delta \subseteq \Omega$.
Proof: By <1>1, $f$ and $\tilde f$ agree on $\Omega \setminus \theset{z_0}$; the boundary of a triangle is a finite union of segments not containing $z_0$ (if $z_0$ is a vertex or lies on an edge, perturb the triangle slightly or note the integral over the triangle equals the integral over a nearby one avoiding $z_0$, by continuity of the holomorphic extension — standard reduction: subdivide $\Delta$ so no sub-triangle has $z_0$ in its interior and let the ones containing $z_0$ shrink to zero measure), so $\int_\Delta f = \int_\Delta \tilde f = 0$ by <1>2.

<1>4. Q.E.D. Proof: <1>3 is the claim.
:::
