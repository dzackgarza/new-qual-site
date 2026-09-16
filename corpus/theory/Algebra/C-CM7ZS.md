---
schema: qual/card@1
id: C-CM7ZS
kind: corollary
title: Burnside's lemma
classification:
  areas:
  - algebra
  topics:
  - Burnside's Lemma
  - Group Actions
  - Orbit-Stabilizer
relations:
- kind: variant-of
  target: C-HE5SL
review: draft
---

::: {.corollary}
Let $G$ be a finite group [[D-WYC7C|acting]] on a finite set $X$.
Let $X/G$ be the set of orbits, and for $g\in G$ let $\Fix(g) = \theset{x\in X \st gx=x}$.
Then
$$
\# (X/G) = \frac{1}{\# G}\sum_{g\in G} \# \Fix(g).
$$
:::

::: {.remark}
The number of orbits is the average over $G$ of the number of fixed points.
:::
