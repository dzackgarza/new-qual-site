---
schema: qual/card@1
id: C-CM7ZS
kind: corollary
title: Burnside's Lemma
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

:::{.corollary title="Burnside's Lemma"}
For $G$ a finite group acting on $X$,
\[
\# {X/G} = \frac{1}{\# G }\sum_{g\in G} \# \Fix(g)
,\]
where $X/G = \ts{\Orb(x_1), \cdots, \Orb(x_n)}$ is the set or orbits and $\Fix(g) = \ts{x\in X \st gx=x}$ are the fixed points under $g$.

> Slogan: the number of orbits is equal to the average number of fixed points.

:::
