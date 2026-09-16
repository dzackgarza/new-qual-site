---
schema: qual/card@1
id: T-4BDE3
kind: theorem
title: Bessel's inequality
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
relations: []
review: draft
---

::: {.theorem}
Let $\mch$ be a [[D-7QQUO|Hilbert space]], let $(u_n)_{n\geq1}$ be an [[D-4IXAO|orthonormal]] sequence in $\mch$, and let $x\in\mch$.
For every $N\geq1$,
$$
\norm{x-\sum_{n=1}^{N}\inner{x}{u_n}u_n}^{2}=\norm{x}^{2}-\sum_{n=1}^{N}\abs{\inner{x}{u_n}}^{2},
$$
and consequently
$$
\sum_{n=1}^{\infty}\abs{\inner{x}{u_n}}^{2} \leq\norm{x}^{2}.
$$
:::
