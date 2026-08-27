---
schema: qual/card@1
id: PR-NKZBT
kind: proposition
title: Commuting Sums with Integrals
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Series of Functions
  - L¹
relations: []
review: draft
---

:::{.proposition}
\[
f_n \geq 0 \text{ and } \sum_n \int \abs{f_n} = \sum_n \norm{f_n}_{L^1} < \infty \implies \sum_n \int f_n = \int \sum_n f_n
.\]
If the $f_n$ are *not* necessarily non-negative, we still have
\[  
\ts{f_n} \subseteq L^1 \text { and }\qty{\sum\int\abs{f_n} < \infty \text { or } \int \sum \abs{f_n} < \infty }
\implies
\int\sum_n f_n = \sum_n \int f_n
.\]

:::
