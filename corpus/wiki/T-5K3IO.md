---
schema: qual/card@1
id: T-5K3IO
kind: theorem
title: Monotone Convergence
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

:::{.theorem title="Monotone Convergence"}
If $f_n: X\to [0, \infty) \in L^+$ and $f_n \nearrow f$ almost everywhere, then
$$
\lim \int f_n
= \int \lim f_n = \int f
\quad \text{i.e.}~~ \int f_n \to \int f
.$$
:::
