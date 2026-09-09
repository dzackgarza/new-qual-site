---
schema: qual/card@1
id: P-TOPS00F
kind: problem
title: "Degree-one map from S^n to M^n forces vanishing intermediate homology"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Degree
  - Manifolds
relations: []
review: draft
---

::: problem
Let $M^n$ be a connected closed oriented manifold and assume that there is a degree one map $f : S^n \to M^n$.
Show that $H_i(M; \mathbb{F}) = 0$ for all $0 < i < n$ and any field $\mathbb{F}$.
:::

::: {.solution}
<1>1. Let $0<i<n$ and suppose $0\ne\alpha\in H^i(M;\mathbb F)$.
::: {.proof}
We show this leads to a contradiction.
:::

<1>2. By Poincaré duality over the field $\mathbb F$, there exists
$$
\beta\in H^{n-i}(M;\mathbb F)
$$
such that
$$
\langle\alpha\smile\beta,[M]_{\mathbb F}\rangle\ne0.
$$
::: {.proof}
The cup-product pairing in complementary degrees is nondegenerate for a closed connected oriented manifold over any field.
:::

<1>3. Since $H^i(S^n;\mathbb F)=0$ for $0<i<n$, one has $f^*\alpha=0$.
::: {.proof}
The sphere has cohomology only in degrees $0$ and $n$.
:::

<1>4. But naturality and the degree-one hypothesis give
$$
0
=\langle f^*(\alpha\smile\beta),[S^n]_{\mathbb F}\rangle
=\langle\alpha\smile\beta,f_*[S^n]_{\mathbb F}\rangle
=\langle\alpha\smile\beta,[M]_{\mathbb F}\rangle,
$$
contradicting <1>2.
::: {.proof}
The first equality uses $f^*\alpha=0$. A degree-one map sends the fundamental class of $S^n$ to that of $M$, and this remains true over every coefficient field.
:::

<1>5. Hence $H^i(M;\mathbb F)=0$ for all $0<i<n$, and therefore
$$
\boxed{H_i(M;\mathbb F)=0\qquad(0<i<n).}
$$
::: {.proof}
The argument above applies in each intermediate degree. Over a field, the universal coefficient theorem identifies $H^i(M;\mathbb F)$ with the dual vector space of $H_i(M;\mathbb F)$, so one vanishes exactly when the other does.
:::
:::
