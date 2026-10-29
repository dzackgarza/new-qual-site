---
schema: qual/card@1
id: C-HE5SL
kind: corollary
title: Burnside's lemma
slogan: Orbit count is the average fixed-point count.
prompts:
- State Burnside's orbit-counting formula.
classification:
  areas:
  - algebra
  topics:
  - Burnside's Lemma
  - Group Actions
  - Orbit-Stabilizer
relations: []
review: draft
---

::: {.corollary}
Let $G$ be a finite group [[D-WYC7C|acting]] on a finite set $X$.
Let $X/G$ be the set of orbits, and for $g\in G$ let $\Fix(g) = \theset{x\in X \st gx=x}$.
Then
$$
\size (X/G) = \frac{1}{\size G}\sum_{g\in G} \size \Fix(g).
$$
:::

::: {.proof}
Count the set $\theset{(g,x)\in G\times X \st gx=x}$ in two ways.
Summing over $g$ gives $\sum_{g\in G}\size \Fix(g)$.
Summing over $x$ gives $\sum_{x\in X}\size G_x=\sum_{x\in X}\size G/\size(Gx)$ by the orbit-stabilizer theorem, and the $\size(Gx)$ points of each orbit contribute $\size G$ in total, so this sum is $\size G\,\size(X/G)$.
:::

::: {.remark}
The number of orbits is the average over $G$ of the number of fixed points.
:::
