---
schema: qual/card@1
id: E-HAT-3.3-34
kind: problem
title: "Poincaré duality diagram for manifolds with boundary"
classification:
  areas:
  - topology
  topics:
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

$$\begin{array}{cc} H^{k-1}(\partial M; R) \to H^k(M, \partial M; R) \to H^k(M; R) \to H^k(M; R) \to H^k(\partial M; R) \\ \downarrow [\partial M] \frown \quad \downarrow [M] \frown \quad \downarrow [\partial M] \frown \\ H_{n-k}(\partial M; R) \to H_{n-k}(M; R) \to H_{n-k}(M, \partial M; R) \to H_{n-k-1}(\partial M; R) \end{array}$$
:::

::: {.solution}
The top row is the cohomology long exact sequence of the pair $(M,\partial M)$,
\[
H^{k-1}(\partial M;R)\to H^k(M,\partial M;R)
\to H^k(M;R)\to H^k(\partial M;R),
\]
and the bottom row is the corresponding homology sequence
\[
H_{n-k}(\partial M;R)\to H_{n-k}(M;R)
\to H_{n-k}(M,\partial M;R)\to H_{n-k-1}(\partial M;R).
\]
The vertical maps are cap product with $[\partial M]$ or $[M,\partial M]$ as indicated.

For the two middle squares, commutativity is the naturality of cap product with respect to the inclusion and quotient maps of pairs. Explicitly, if $j:\partial M\hookrightarrow M$, then
\[
j_*([\partial M]\frown j^*\alpha)
\]
agrees, up to the conventional sign, with the image of $[M,\partial M]\frown\alpha$ under the appropriate boundary/inclusion map.

For the two squares involving connecting homomorphisms, use the cap-product boundary identity
\[
\partial(c\frown\varphi)
=(\partial c)\frown\varphi\ \pm\ c\frown\delta\varphi
\]
together with Exercise 31,
\[
\partial[M,\partial M]=[\partial M].
\]
If $\varphi$ is a cocycle, the second term disappears; if one is tracing a connecting cohomology class, the same identity gives the other square with the standard degree sign. Hence every square in the diagram commutes up to the unavoidable sign convention for connecting maps.

Therefore the displayed Poincaré-duality diagram is commutative up to sign.
:::
