---
schema: qual/card@1
id: E-HAT-3.3-34
kind: problem
title: Poincaré duality diagram for manifolds with boundary
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 34; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
For a compact manifold $M$ verify that the following diagram relating Poincaré duality for $M$ and $\partial M$ is commutative, up to sign at least:

$$
\begin{array}{ccccccc}
H^{k-1}(\partial M;R)&\longrightarrow&H^k(M,\partial M;R)&\longrightarrow&H^k(M;R)&\longrightarrow&H^k(\partial M;R)\\
\downarrow { [\partial M]\frown - }&&\downarrow { [M,\partial M]\frown - }&&\downarrow { [M,\partial M]\frown - }&&\downarrow { [\partial M]\frown - }\\
H_{n-k}(\partial M;R)&\longrightarrow&H_{n-k}(M;R)&\longrightarrow&H_{n-k}(M,\partial M;R)&\longrightarrow&H_{n-k-1}(\partial M;R)
\end{array}
$$
:::

::: {.solution}
The top row is the cohomology long exact sequence of the pair $(M,\partial M)$,
$$
H^{k-1}(\partial M;R)\to H^k(M,\partial M;R)
\to H^k(M;R)\to H^k(\partial M;R),
$$
and the bottom row is the corresponding homology sequence
$$
H_{n-k}(\partial M;R)\to H_{n-k}(M;R)
\to H_{n-k}(M,\partial M;R)\to H_{n-k-1}(\partial M;R).
$$
The middle square commutes by naturality of cap product under the map from relative to absolute cochains and from absolute to relative chains.

For the outer squares, use the chain-level cap-product boundary identity
$$
\partial(c\frown\varphi)
=(\partial c)\frown\varphi\ \pm\ c\frown\delta\varphi
$$
together with Exercise 31,
$$
\partial[M,\partial M]=[\partial M].
$$
For an absolute cocycle $\varphi$, the identity says that the boundary of $[M,\partial M]\frown\varphi$ is $[\partial M]\frown(\varphi\restrict_{\partial M})$, proving the right square. For a cocycle on $\partial M$, extend it to a cochain on $M$; its coboundary represents the cohomology connecting class. The same identity, now applied to that extension, says that its cap product with $[M,\partial M]$ is the inclusion of the boundary cap product, proving the left square. The signs are those in the chosen cap and connecting-map conventions.
:::
