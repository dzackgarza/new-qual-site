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
Show that $H_k(M; \mathbb{Q}) = H_k(S^n; \mathbb{Q})$ for any $k \geq 0$.
:::

::: {.solution}
<1>1. A nonzero-degree map $f:S^n\to M$ induces an injection
$$f^*:H^k(M;\mathbb Q)\hookrightarrow H^k(S^n;\mathbb Q)$$
for every $k$.
::: {.proof}
If $0\ne\alpha\in H^k(M;\mathbb Q)$, Poincaré duality gives $\beta\in H^{n-k}(M;\mathbb Q)$ with $\langle\alpha\smile\beta,[M]\rangle\ne0$. Naturality yields
$$\langle f^*\alpha\smile f^*\beta,[S^n]\rangle
=\deg(f)\langle\alpha\smile\beta,[M]\rangle\ne0,$$
so $f^*\alpha\ne0$.
:::

<1>2. Since $H^k(S^n;\mathbb Q)=0$ for $0<k<n$, one has
$$H^k(M;\mathbb Q)=0\qquad(0<k<n).$$
::: {.proof}
An injective map into the zero vector space forces the source to vanish.
:::

<1>3. Connectedness and orientability give
$$H^0(M;\mathbb Q)\cong H^n(M;\mathbb Q)\cong\mathbb Q.$$
::: {.proof}
The degree-$0$ statement is connectedness; the top-degree statement is the rational fundamental class of a closed orientable manifold.
:::

<1>4. Therefore
$$\boxed{H_k(M;\mathbb Q)\cong H_k(S^n;\mathbb Q)\text{ for all }k.}$$
::: {.proof}
Over a field, homology and cohomology have the same Betti numbers, or equivalently use rational Poincaré duality together with <1>2--<1>3.
:::
:::
