---
schema: qual/card@1
id: T-WYX24
kind: theorem
title: Generalized DCT
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

::: {.theorem title="Generalized DCT"}
If

- $f_n \in L^1$ with $f_n \to f$ almost everywhere,

- There exist $g_n\geq 0 \in L^1$ nonnegative with $\abs{f_n} \leq g_n$,

- $g_n\to g$ almost everywhere with $g\in L^1$, and

- $\lim \int g_n = \int g$,

then $f\in L^1$ and $\lim \int f_n = \int f < \infty$.

> Note that this is the DCT with $\abs{f_n} < \abs{g}$ relaxed to $\abs{f_n} < g_n \to g\in L^1$.
:::
