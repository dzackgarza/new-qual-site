---
schema: qual/card@1
id: T-O2PGN
kind: theorem
title: $\Aut_\CC(\HH)\cong\PSL_2(\RR)$
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Fractional Linear Transformations
relations:
- kind: variant-of
  target: T-VGDFW
review: draft
---

::: {.theorem}
Let $\HH\coloneqq\{z\in\CC : \operatorname{Im}z>0\}$ be the upper half-plane.
The group $\Aut_\CC(\HH)$ of [[D-TM4TE|biholomorphisms]] $\HH\to\HH$ is
$$
\Aut_\CC(\HH)=\Bigl\{z\mapsto\frac{az+b}{cz+d} : a,b,c,d\in\RR,\ ad-bc=1\Bigr\},
$$
and sending the matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\SL_2(\RR)$ to this map induces a group isomorphism $\PSL_2(\RR)\cong\Aut_\CC(\HH)$.
:::
