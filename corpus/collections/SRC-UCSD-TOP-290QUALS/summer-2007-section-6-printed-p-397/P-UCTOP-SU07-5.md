---
schema: qual/card@1
id: P-UCTOP-SU07-5
kind: problem
title: Any map from S^2 to surface of genus g has degree zero
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
---

::: {.problem}
On any closed surface $\Sigma_g$ of genus $g \geq 1$, it is possible to find a pair of simple closed curves (submanifolds homeomorphic to $S^1$) meeting transversely once.
Use this fact together with intersection theory to show that any map $S^2 \to \Sigma_g$ has degree zero.
:::

::: {.solution}

::: pf

::: pf-step
Choose oriented simple closed curves $\alpha,\beta\subset\Sigma_g$ meeting transversely in exactly one point.

::: pf-proof
Such curves exist by the hypothesis supplied in the problem. After choosing orientations, their algebraic intersection number is $\pm1$.
:::

:::

::: {.pf-step #cup-product-intersection}
Let $u,v\in H^1(\Sigma_g;\mathbb Z)$ be the Poincaré duals of $[\alpha]$ and $[\beta]$. Then
$$
\langle u\smile v,[\Sigma_g]\rangle=\pm1.
$$

::: pf-proof
The cup-product pairing of the Poincaré dual classes evaluates on the fundamental class as the algebraic intersection number of the represented $1$-cycles.
:::

:::

::: {.pf-step #cup-product-generator}
Hence $u\smile v$ is a generator, up to sign, of
$$
H^2(\Sigma_g;\mathbb Z)\cong\mathbb Z.
$$

::: pf-proof
Its evaluation on the fundamental class is $\pm1$ by step [](#cup-product-intersection){.pf-ref}.
:::

:::

::: pf-step
For any continuous map $f:S^2\to\Sigma_g$, one has $f^*u=f^*v=0$.

::: pf-proof
The group $H^1(S^2;\mathbb Z)$ is zero.
:::

:::

::: {.pf-step #pullback-cup-product-zero}
Therefore
$$
f^*(u\smile v)=0.
$$

::: pf-proof
Naturality of cup products gives
$$
f^*(u\smile v)=f^*u\smile f^*v=0.
$$
:::

:::

::: pf-step
The degree of $f$ is zero.

::: pf-proof
By step [](#cup-product-generator){.pf-ref}, $u\smile v$ is an orientation generator of $H^2(\Sigma_g)$. The induced map on top cohomology is multiplication by $\deg f$. Since step [](#pullback-cup-product-zero){.pf-ref} says it sends this generator to zero, one must have $\deg f=0$.
:::

:::

:::

:::

