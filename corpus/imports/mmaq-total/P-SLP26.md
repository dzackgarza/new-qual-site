---
schema: qual/card@1
id: P-SLP26
kind: problem
title: Assume that $K$ is a cyclic group, $H$ is an arbitrary group, and…
classification:
  areas:
  - algebra
  topics:
  - classification
  - groups
relations: []
review: draft
---

::: problem
Assume that $K$ is a cyclic group, $H$ is an arbitrary group, and $\varphi_1$
and $\varphi_2$ are homomorphisms from $K$ into $\Aut(H)$ such that
$\varphi_1(K)$ and $\varphi_2(K)$ are conjugate subgroups
of $\Aut(H)$.

Prove by constructing an explicit isomorphism that
$H\rtimes_{\varphi_1}K\cong H\rtimes_{\varphi_2} K$.

> Suppose $\sigma_{\varphi_1}(K)\sigma\inv=\varphi_2(K)$
> so that for some $a\in\mathbb Z$ we have $\sigma\varphi_1(k)\sigma\inv
> =\varphi_2(k)^a$ for all $k\in K$. Show that the map $\psi:H
> \rtimes_{\varphi_1}K\rightarrow H\rtimes_{\varphi_2}K$
> defined by $\psi((h,k))=(\sigma(h),k^a)$ is a homomorphism.
> Show $\psi$ is bijective by construcing a 2-sided inverse.
:::
