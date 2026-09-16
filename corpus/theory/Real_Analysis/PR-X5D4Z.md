---
schema: qual/card@1
id: PR-X5D4Z
kind: proposition
title: Cauchy--Schwarz inequality
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - L²
  - Inner Product Spaces
relations: []
review: draft
---

::: {.proposition}
Let $H$ be an inner product space over $\CC$ with inner product $\inner{\cdot}{\cdot}$ and norm $\norm{x}\coloneqq\inner{x}{x}^{1/2}$.
For all $f,g\in H$,
$$
\abs{\inner{f}{g}} \leq \norm{f}\norm{g},
$$
with equality if and only if $f$ and $g$ are linearly dependent.
In particular, for a [[D-QYLPH|measure space]] $(X,\mcm,\mu)$ and $f,g\in L^2(\mu)$, $\abs{\int_X f\overline g\dmu}\leq\norm{f}_2\norm{g}_2$.
:::
