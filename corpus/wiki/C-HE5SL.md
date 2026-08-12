---
schema: qual/card@1
id: C-HE5SL
kind: corollary
title: "Burnside's Lemma"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.corollary title="Burnside's Lemma"}
For $G$ a finite group acting on $X$, 
\[
\size  {X/G} = \frac{1}{\size  G }\sum_{g\in G} \size  \Fix(g)
,\]
where $X/G = \ts{\Orb(x_1), \cdots, \Orb(x_n)}$ is the set or orbits and $\Fix(g) = \ts{x\in X \st gx=x}$ are the fixed points under $g$.

> Slogan: the number of orbits is equal to the average number of fixed points.

:::
