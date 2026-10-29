---
schema: qual/card@1
id: P-TOPS20E
kind: problem
title: "A manifold admitting a nonzero-degree map from S^n has the rational homology of S^n"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Degree
  - Poincaré Duality
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $M$ be a closed, orientable, connected manifold of dimension $n$.
Suppose there is a continuous map $f : S^n \to M$ with nonzero mapping degree.
Show that $H_k(M; \QQ) = H_k(S^n; \QQ)$ for any $k \geq 0$.
:::

::: {.solution}

::: pf

::: pf-step
A nonzero-degree map $f:S^n\to M$ induces an injection
$$f^*:H^k(M;\QQ)\hookrightarrow H^k(S^n;\QQ)$$
for every $k$.

::: pf-proof
If $0\ne\alpha\in H^k(M;\QQ)$, Poincaré duality gives $\beta\in H^{n-k}(M;\QQ)$ with $\langle\alpha\smile\beta,[M]\rangle\ne0$. Naturality yields
$$\langle f^*\alpha\smile f^*\beta,[S^n]\rangle
=\deg(f)\langle\alpha\smile\beta,[M]\rangle\ne0,$$
so $f^*\alpha\ne0$.
:::

:::

::: {.pf-step #vanishing-intermediate}
Since $H^k(S^n;\QQ)=0$ for $0<k<n$, one has
$$H^k(M;\QQ)=0\qquad(0<k<n).$$

::: pf-proof
An injective map into the zero vector space forces the source to vanish.
:::

:::

::: {.pf-step #top-and-bottom-cohomology}
Connectedness and orientability give
$$H^0(M;\QQ)\cong H^n(M;\QQ)\cong\QQ.$$

::: pf-proof
The degree-$0$ statement is connectedness; the top-degree statement is the rational fundamental class of a closed orientable manifold.
:::

:::

::: pf-step
Therefore
$$\boxed{H_k(M;\QQ)\cong H_k(S^n;\QQ)\text{ for all }k.}$$

::: pf-proof
Over a field, homology and cohomology have the same Betti numbers, or equivalently use rational Poincaré duality together with steps [](#vanishing-intermediate){.pf-ref} and [](#top-and-bottom-cohomology){.pf-ref}.
:::

:::

:::

:::
