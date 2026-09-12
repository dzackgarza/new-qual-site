---
schema: qual/card@1
id: P-BKS03-2B
kind: problem
title: Products of solutions to constant-coefficient linear ODEs
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Suppose entire functions $f,g$ satisfy constant-coefficient linear differential equations of orders $n$ and $m$, respectively. Show that $F=fg$ satisfies a nontrivial constant-coefficient linear differential equation of order at most $mn$.
:::

::: {.solution}
By induction on k, the function $F ^ { ( k ) }$ is a linear combination of the mn functions $f ^ { ( i ) } g ^ { ( j ) }$ for $0 \leq i < n , 0 \leq j < m$ , with constant coefficients. Therefore the $m n + 1$ functions $F ^ { ( 0 ) } , \ldots , F ^ { ( m n ) }$ are linearly dependent over C.
:::
