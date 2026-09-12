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

On any closed surface $\Sigma_g$ of genus $g \geq 1$, it is possible to find a pair of simple closed curves (submanifolds homeomorphic to $S^1$) meeting transversely once.
Use this fact together with intersection theory to show that any map $S^2 \to \Sigma_g$ has degree zero.

::: {.solution}
<1>1. Choose oriented simple closed curves $\alpha,\beta\subset\Sigma_g$ meeting transversely in exactly one point.
::: {.proof}
Such curves exist by the hypothesis supplied in the problem. After choosing orientations, their algebraic intersection number is $\pm1$.
:::

<1>2. Let $u,v\in H^1(\Sigma_g;\mathbb Z)$ be the Poincaré duals of $[\alpha]$ and $[\beta]$. Then
$$
\langle u\smile v,[\Sigma_g]\rangle=\pm1.
$$
:::
::: {.proof}
The cup-product pairing of the Poincaré dual classes evaluates on the fundamental class as the algebraic intersection number of the represented $1$-cycles.
:::

<1>3. Hence $u\smile v$ is a generator, up to sign, of
$$
H^2(\Sigma_g;\mathbb Z)\cong\mathbb Z.
$$
:::
::: {.proof}
Its evaluation on the fundamental class is $\pm1$ by <1>2.
:::

<1>4. For any continuous map $f:S^2\to\Sigma_g$, one has $f^*u=f^*v=0$.
::: {.proof}
The group $H^1(S^2;\mathbb Z)$ is zero.
:::

<1>5. Therefore
$$
f^*(u\smile v)=0.
$$
:::
::: {.proof}
Naturality of cup products gives
$$
f^*(u\smile v)=f^*u\smile f^*v=0.
$$
:::

<1>6. The degree of $f$ is zero.
::: {.proof}
By <1>3, $u\smile v$ is an orientation generator of $H^2(\Sigma_g)$. The induced map on top cohomology is multiplication by $\deg f$. Since <1>5 says it sends this generator to zero, one must have $\deg f=0$.
:::
:::

