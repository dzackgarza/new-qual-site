---
schema: qual/card@1
id: FF-IAUQG
kind: fact
title: Weierstrass $M$-test for uniform convergence
slogan: 'A summable uniform majorant forces absolute and uniform convergence of a function series.'
prompts:
- What is the Weierstrass $M$-test?
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
---

::: {.fact}
Let $A$ be a set and let $f_n\colon A\to\CC$ for $n\geq 0$.
Put $\norm{f_n}_{\infty, A}\coloneqq\sup_{x\in A}\abs{f_n(x)}$.
If $\sum_{n\geq 0}\norm{f_n}_{\infty, A} < \infty$, then for every $x\in A$ the series $\sum_{n\geq 0} f_n(x)$ converges absolutely, and its partial sums [[D-YZC3C|converge uniformly]] on $A$ to $\sum_{n\geq 0} f_n$.

Equivalently, the conclusion holds whenever there are real numbers $M_n$ with $\abs{f_n(x)} \leq M_n$ for all $x\in A$ and $n\geq 0$ and $\sum_{n\geq 0} M_n < \infty$.
:::

::: {.remark}
Conversely, if $\sum_n f_n$ converges uniformly on $A$, then $\sup_{x\in A}\abs{f_n(x)}\to0$; this necessary condition does not imply $\sum_n\sup_{x\in A}\abs{f_n(x)}<\infty$, as the constant functions $f_n\coloneqq(-1)^n/n$ show.
:::

::: {.remark title="Variations"}
If $A$ is a topological space and every $f_n$ is continuous, then $\sum_{n\geq0}f_n$ is continuous on $A$, by the uniform limit theorem.
:::
