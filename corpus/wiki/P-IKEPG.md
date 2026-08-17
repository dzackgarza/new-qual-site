---
schema: qual/card@1
id: P-IKEPG
kind: problem
title: "1. Use the fact that $\\sum_{i=1}^n i = \\frac 1 2 n(n+1)$, so"
classification:
  areas:
  - prelim
  topics:
  - induction
  - series-of-numbers
relations: []
review: draft
solved: false
---

::: problem
1. Use the fact that $\sum_{i=1}^n i = \frac 1 2 n(n+1)$, so
$$\begin{align*}
\sum_{i=1}^{n+1} i^3 &= \sum_{i=1}^{n} i^3 + (n+1)^3 \\ 
&= \left( \sum_{i=1}^{n} i \right)^2 + (n+1)^3 \\
&= \left( \frac 1 2 n(n+1) \right)^2 + (n+1)^3 \\
&= \frac 1 4 n^2(n+1)^2 + (n+1)(n+1)^2 \\
&= \frac 1 4 (n+1)^2 (n^2 + 4(n+1)) \\
&= \frac 1 4 (n+1)^2(n+2)^2 \\ 
&= \left( \frac 1 2 (n+1)(n+2)\right)^2 \\
&= \left( \sum_{i=1}^{n+1} i \right)^2. \qed
\end{align*}$$
:::
