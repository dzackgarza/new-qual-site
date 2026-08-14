---
schema: qual/card@1
id: T-QNYSB
kind: theorem
title: "Lefschetz Duality"
classification:
  areas:
  - topology
  topics:
  - poincare-duality
  - manifolds
  - cohomology
relations: []
review: draft
---

::: {.theorem title="Lefschetz Duality"}
Let $M$ be a compact $R\dash$orientable $n\dash$manifold whose boundary is decomposed as $\del M = A \union B$ with $A, B$ compact $(n-1)\dash$manifolds meeting in $\del A = \del B = A \intersect B$.
Then cap product with a fundamental class $[M]\in H_n(M, \del M; R)$ gives isomorphisms
\[
D_M: H^k(M, A; R) \mapsvia{\sim} H_{n-k}(M, B; R)
\]
for all $k$.
The cases $A = \emptyset$ and $B = \emptyset$ are what is usually called Lefschetz duality:
\[
H^k(M, \del M; R) \cong H_{n-k}(M; R), \qquad H^k(M; R)\cong H_{n-k}(M, \del M; R)
.\]
:::

::: {.concept}
See Hatcher, §3.3, Theorem 3.43, p. 254.
:::
