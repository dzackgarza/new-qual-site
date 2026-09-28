---
schema: qual/card@1
id: E-GQMTN
kind: problem
title: There is no entire function with $|f(z)|\ge|z|+1$ for all $z$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Counterexamples
relations: []
review: draft
---

::: {.exercise}
Find all entire functions $f$ satisfying
\[
\abs{f(z)} \geq \abs{z} + 1 &&\forall z\in \CC
.\]

:::

::: {.solution}
The inequality implies $f$ has no zeros, so $g(z) \da 1/f(z)$ is entire.
Moreover it is bounded on $\CC$, since
\[
\abs{g(z)} \leq {1\over \abs{z} + 1} \leq 1
,\]
so $g\equiv c$ is constant by Liouville.
Since $\abs{g(z)}\le 1/(\abs z+1)\to0$ as $\abs z\to\infty$, $c=0$, which contradicts $g=1/f$ having no zeros. So there are no such entire functions.
:::

