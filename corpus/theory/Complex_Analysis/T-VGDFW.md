---
schema: qual/card@1
id: T-VGDFW
kind: theorem
title: Automorphisms of the upper half-plane
slogan: 'The upper half-plane automorphism group is $\PSL_2(\RR)$ acting by real Möbius transformations.'
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

This is C. McMullen, *Advanced Complex Analysis*, Corollary 2.18, which identifies $\Aut(\HH)$ with the subgroup $\SL_2(\RR)\subseteq\SL_2(\CC)$; his Theorem 2.21 states that every such map is an isometry of the hyperbolic metric.
:::

::: {.remark}
The subgroup $\SL_2(\RR)$ acts on $\HH$ by Möbius transformations, and the two matrices $\pm\begin{pmatrix}a&b\\c&d\end{pmatrix}$ induce the same map, which is why the group is $\PSL_2(\RR)$ and not $\SL_2(\RR)$ (C. McMullen, *Advanced Complex Analysis*, Corollary 2.18).
:::

::: {.remark}
See [@SS03, ch. 8, §2.2] for the same computation in the disc model.
:::
