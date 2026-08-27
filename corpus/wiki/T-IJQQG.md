---
schema: qual/card@1
id: T-IJQQG
kind: theorem
title: Dominated Convergence
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
  - L¹
relations: []
review: draft
---

:::{.theorem}
If $f_n \in L^1$ and $f_n \to f$ almost everywhere with $\abs {f_n} \leq g$ for some $g\in L^1$, then $f\in L^1$ and
\[
\int \abs{f_n - f} \to 0
.\]

As a consequence,
\[
\lim \int f_n = \int \lim f_n = \int f \quad \text{i.e.}~~ \int f_n \to \int f < \infty
\]

> Positivity *not* needed.

:::
