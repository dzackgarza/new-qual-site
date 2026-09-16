---
schema: qual/card@1
id: T-VGDFW
kind: theorem
title: Automorphisms of the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.theorem}
Let $\HH\coloneqq\{z\in\CC : \operatorname{Im}z>0\}$ be the upper half-plane.
The group $\Aut_\CC(\HH)$ of [[D-TM4TE|biholomorphisms]] $\HH\to\HH$ is
$$
\Aut_\CC(\HH)=\Bigl\{z\mapsto\frac{az+b}{cz+d} : a,b,c,d\in\RR,\ ad-bc=1\Bigr\},
$$
and sending $\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\SL_2(\RR)$ to this map induces a group isomorphism $\PSL_2(\RR)\cong\Aut_\CC(\HH)$.
:::

::: {.remark}
See [@SS03, Chapter 8, Theorem 2.4].
:::
