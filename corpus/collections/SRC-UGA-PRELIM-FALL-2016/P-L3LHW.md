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

::: problem
Give an $\varepsilon$-$\delta$ proof that
\[
\lim_{x\to2}\frac1{3+x}=\frac15.
\]
:::

::: solution
Let $\varepsilon>0$ and choose $\delta=\min\{1,20\varepsilon\}$. If $|x-2|<\delta$, then $1<x<3$, so $|5(3+x)|>20$. Therefore
\[
\left|\frac1{3+x}-\frac15\right|
=\left|\frac{2-x}{5(3+x)}\right|
<\frac1{20}|x-2|
<\varepsilon.
\]
:::
