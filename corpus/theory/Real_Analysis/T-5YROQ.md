---
schema: qual/card@1
id: T-5YROQ
kind: theorem
title: Small tails in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Small Tails
  - L¹
relations: []
review: draft
---

::: {.theorem}
Let $f\in L^1(\RR^n)$.
For every $\varepsilon>0$ there exists $R>0$ such that
$$
\int_{\theset{x\in\RR^n\suchthat\abs{x}\geq R}} \abs{f} < \varepsilon .
$$
:::

::: {.proof}
The functions $\abs{f}\chi_{\theset{\abs{x}\geq k}}$, $k\in\NN$, are dominated by $\abs{f}\in L^1$ and tend to $0$ pointwise as $k\to\infty$, so their integrals tend to $0$ by the dominated convergence theorem [[T-IJQQG]].
:::
