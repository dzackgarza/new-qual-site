---
schema: qual/card@1
id: D-8WMFK
kind: definition
title: Riemann surface
prompts:
- What is a Riemann surface?
- What makes a map between Riemann surfaces holomorphic?
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Surfaces
relations: []
review: draft
---

::: {.definition}
A \dfn{Riemann surface} is a connected Hausdorff topological space $S$ equipped with a family of charts $(\phi_\alpha, U_\alpha)_{\alpha\in A}$, where the $U_\alpha$ are open sets covering $S$ and each $\phi_\alpha\colon U_\alpha\to V_\alpha$ is a homeomorphism onto an open set $V_\alpha\subseteq\CC$, such that every transition map
$$
\phi_\beta\circ\phi_\alpha^{-1}\colon \phi_\alpha(U_\alpha\cap U_\beta)\to\phi_\beta(U_\alpha\cap U_\beta)
$$
is [[D-E7A5W|holomorphic]].
A continuous function $f\colon S\to\CC$ is \dfn{holomorphic} if $f\circ\phi_\alpha^{-1}$ is holomorphic on $V_\alpha$ for every chart, and a continuous map $S\to S'$ of Riemann surfaces is holomorphic if it is holomorphic in charts on both sides.
:::

::: {.example title="The plane, the disc, and the sphere"}
$\CC$ and every domain in $\CC$ are Riemann surfaces in the single chart $z$.
The [[D-3QTVR|Riemann sphere]] is one in the two charts $z$ on $\CP^1\sm\theset{\infty}$ and $w = 1/z$ on $\CP^1\sm\theset{0}$, whose transition map is holomorphic on $\CC\sm\theset{0}$.
A quotient of a Riemann surface by a group acting freely and properly discontinuously by biholomorphisms inherits the structure, which produces the compact examples: the complex torus $\CC/\Lambda$ for a lattice $\Lambda$, and the quotient of $\HH$ by a Fuchsian group acting cocompactly.
:::
