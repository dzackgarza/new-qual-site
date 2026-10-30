---
schema: qual/card@1
id: P-CASP09D
kind: problem
title: "Derivative estimate for an analytic function at the origin"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Suppose $f(z)$ is analytic at $z = 0$.
Prove that there is an integer $n > 0$ such that $\abs{f^{(n)}(0)} < n^n \cdot n!$.
:::

::: {.solution}
::: pf

::: {.pf-step #cauchy}
There are $r>0$ and $M<\infty$ with $\abs{f^{(n)}(0)}\le n!\,M/r^n$ for every $n\ge1$.

::: pf-proof
$f$ is analytic on some disk $B(0,R)$ with $R>0$. Take $0<r<R$ and $M=\max_{\abs{z}=r}\abs{f(z)}$. Cauchy's estimate gives the bound.
:::

:::

::: {.pf-step #large}
$M<(nr)^n$ for all sufficiently large $n$.

::: pf-proof
For $n>2/r$ we have $nr>2$, so $(nr)^n>2^n$, and $2^n>M$ for large $n$.
:::

:::

::: pf-qed
For $n$ as in step [](#large){.pf-ref}, step [](#cauchy){.pf-ref} gives $\abs{f^{(n)}(0)}\le n!\,M/r^n<n!\,n^n$.
:::

:::
:::
