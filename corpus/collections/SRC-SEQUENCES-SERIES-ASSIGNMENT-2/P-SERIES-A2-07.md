---
schema: qual/card@1
id: P-SERIES-A2-07
kind: problem
title: Convergence of ratios of consecutive Fibonacci numbers
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
The Fibonacci numbers $\{f_n\}$ are defined by
\[
f_0=f_1=1,\qquad f_{n+1}=f_n+f_{n-1}\quad(n\ge1),
\]
and for $n\ge1$ define $r_n=f_{n+1}/f_n$.

(a) Find a formula for $r_{n+1}$ in terms of $r_n$.

(b) Show that $f_n\ge n$ for all $n\ge2$.

(c) Show that
\[
f_{n+1}f_{n-1}-f_n^2=(-1)^{n+1}.
\]

(d) Hence show that, for $n\ge2$,
\[
|r_{n+1}-r_n|\le \frac1{(n-1)^2}.
\]

(e) Hence show that $\{r_n\}$ converges and compute its limit.
:::
