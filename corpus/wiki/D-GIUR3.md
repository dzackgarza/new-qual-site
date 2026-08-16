---
schema: qual/card@1
id: D-GIUR3
kind: definition
title: "Lefschetz duality"
classification:
  areas:
  - topology
  topics:
  - homology
  - duality
  - manifolds
relations:
- kind: related-to
  target: T-QNYSB
review: draft
---

::: {.definition title="Lefschetz duality"}
For $M$ a compact $R\dash$orientable $n\dash$manifold with boundary, the **Lefschetz duality map** is cap product with a fundamental class $[M] \in H_n(M, \del M; R)$,
\[
D_M: H^k(M, \del M; R) \to H_{n-k}(M; R), \qquad D_M: H^k(M; R) \to H_{n-k}(M, \del M; R)
,\]
and Lefschetz duality is the statement that both are isomorphisms for every $k$.
Taking $\del M = \emptyset$ recovers Poincaré duality.
:::

::: {.concept}
See Hatcher, §3.3, Theorem 3.43, stated there in the more general form that decomposes $\del M$ as a union of two compact $(n-1)$-manifolds; the related theorem card gives that version.
:::
