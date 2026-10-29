---
schema: qual/card@1
id: P-SGXRZ
kind: problem
title: Normal subgroups
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Homomorphisms
  - Geometry
relations: []
review: draft
---

::: {.problem}
What is a normal subgroup? What natural map does it determine? How does this relate to covering spaces?
:::

::: {.solution}

A subgroup $N\le G$ is normal, written $N\normal G$, if $gNg^{-1}=N$ for every $g\in G$; equivalently, every left coset $gN$ equals the right coset $Ng$.

::: pf

::: pf-step

A normal subgroup $N$ determines the quotient homomorphism $\pi\colon G\twoheadrightarrow G/N$, $g\mapsto gN$, with $\ker\pi=N$; the normal subgroups of $G$ are exactly the kernels of homomorphisms out of $G$.

::: pf-proof

Normality makes $(gN)(hN)=ghN$ well defined: if $gN=g'N$ and $hN=h'N$, then $g'h'=gn\,hn'=gh(h^{-1}nh)n'\in ghN$ for some $n,n'\in N$. With this product $G/N$ is a group and $\pi$ is a surjective homomorphism with kernel $N$. Conversely, if $\varphi\colon G\to G'$ is a homomorphism and $k\in\ker\varphi$, then $\varphi(gkg^{-1})=1$, so $\ker\varphi$ is normal.

:::

:::

::: pf-qed

Let $X$ be path connected, locally path connected, and semilocally simply connected, with $G=\pi_1(X,x_0)$. By the classification of covering spaces, conjugacy classes of subgroups $H\le G$ correspond to connected coverings $p\colon\widetilde X\to X$ up to isomorphism, with $p_*\pi_1(\widetilde X)=H$. The covering is regular (Galois) exactly when $H\normal G$, and then its deck transformation group is $G/H$. Thus $H\normal G\twoheadrightarrow G/H$ is the fundamental group of the covering, the fundamental group of the base, and the deck group of the regular covering.

:::

:::

:::
