---
schema: qual/card@1
id: D-5KDNB
kind: theorem
title: Alexander duality
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Homology
  - Cohomology
  - Manifolds
relations: []
review: draft
---

::: {.theorem title="Alexander duality"}
Let $n\geq 1$ and let $K\subsetneq S^n$ be a nonempty, compact, locally contractible subspace.
Then for all $i$,
$$
\tilde H_i(S^n \sm K; \ZZ) \cong \tilde H^{n-i-1}(K;\ZZ)
.$$
:::

::: {.remark}
It follows, with $M = S^n$ and the long exact sequence of the pair $(S^n, S^n\sm K)$, from the duality $H_i(M, M\sm K;\ZZ)\cong H^{n-i}(K;\ZZ)$ for a compact, locally contractible subspace $K$ of a closed, orientable $n$-manifold $M$ [@Hat02].
:::

::: {.concept}
[@Hat02].
:::
