---
schema: qual/card@1
id: P-TOPF24F
kind: problem
title: Reduced homology of spheres via Mayer–Vietoris
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: problem
Use Mayer-Vietoris to show that the reduced homology of $S^n$ is $\mathbb{Z}$ in dimension $n$ and zero otherwise, for all $n \geq 0$.
:::

::: {.solution}
<1>1. For $n=0$, $S^0$ consists of two points, so
$$\widetilde H_k(S^0;\mathbb Z)\cong\begin{cases}\mathbb Z,&k=0,\\0,&k\ne0.\end{cases}$$
::: {.proof}
Reduced $H_0$ of a space with two path components is free of rank one.
:::

<1>2. For $n\ge1$, cover $S^n$ by two open sets $U,V$ obtained by slightly enlarging the northern and southern hemispheres. Then $U$ and $V$ are contractible and
$$U\cap V\simeq S^{n-1}.$$
::: {.proof}
Each enlarged hemisphere deformation retracts to a point, while their overlap is an equatorial band that deformation retracts onto the equator $S^{n-1}$.
:::

<1>3. The reduced Mayer--Vietoris sequence gives isomorphisms
$$\widetilde H_k(S^n;\mathbb Z)\cong\widetilde H_{k-1}(S^{n-1};\mathbb Z)$$
for all $k$.
::: {.proof}
In the reduced Mayer--Vietoris sequence, all reduced homology groups of $U$ and $V$ vanish, so exactness identifies the middle term with the preceding shifted homology of $U\cap V$.
:::

<1>4. Induction on $n$ therefore yields
$$\boxed{\widetilde H_k(S^n;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=n,\\
0,&k\ne n.
\end{cases}}$$
for every $n\ge0$.
::: {.proof}
Iterating <1>3 reduces the computation to <1>1.
:::
:::
