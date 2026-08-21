---
schema: qual/card@1
id: E-OEEU4
kind: exercise
title: Rudin 10.4
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
solved: true
---

:::{.exercise title="Rudin 10.4"}
Let $f$ be entire and suppose that for $\abs{z} \geq M$,
\[
\abs{f} \leq A + B\abs{z}^k
\]
for some constants $A, B$ and $k$.
Show that $f$ is a polynomial of degree at most $k$.

:::

:::{.solution}
Apply a Cauchy estimate over a contour of radius $R> M$ to obtain
\[
\abs{f^{(n)}(0)} \leq n!{A+B R^k \over R^n} \asymptotic 1/R^{n-k}
,\]
and if $n>k$ then this goes to zero in $R$ and $c_n = 0$ for all $n>k$.
:::

