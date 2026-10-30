---
schema: qual/card@1
id: P-L3LHW
kind: problem
title: $\lim_{x\to 2}\frac{1}{3+x}=\frac{1}{5}$
classification:
  areas:
  - prelim
  topics:
  - Limits
  - Continuity
relations: []
review: draft
---

::: {.problem}
Give an $\varepsilon$-$\delta$ proof that
$$
\lim_{x\to2}\frac1{3+x}=\frac15.
$$
:::

::: {.solution}
Let $\varepsilon>0$ and choose $\delta=\min\{1,20\varepsilon\}$.
If $\abs{x-2}<\delta$, then $1<x<3$, so $\abs{5(3+x)}>20$.
Therefore
$$
\abs{\frac1{3+x}-\frac15}
=\abs{\frac{2-x}{5(3+x)}}
<\frac1{20}\abs{x-2}
<\varepsilon.
$$
:::
