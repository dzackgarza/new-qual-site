---
schema: qual/card@1
id: E-GQMTN
kind: problem
title: There is no entire function with $\abs{f(z)}\ge\abs{z}+1$ for all $z$
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
$$
\abs{f(z)} \geq \abs{z} + 1 \qquad \forall z\in \CC
.$$
:::

::: {.solution}

::: pf

::: {.pf-step #reciprocal}
If $f$ satisfies the inequality, then $g\coloneqq1/f$ is entire with $\abs{g(z)}\le{1\over\abs z+1}$.

::: pf-proof
The inequality gives $\abs{f}\ge1$, so $f$ has no zeros and $1/f$ is entire.
:::

:::

::: pf-step
There are $\boxed{\text{no such functions}}$.

::: pf-proof
By step [](#reciprocal){.pf-ref}, $\abs g\le1$, so $g$ is a constant $c$ by Liouville's theorem.
Since $\abs{g(z)}\le1/(\abs z+1)\to0$ as $\abs z\to\infty$, $c=0$, which contradicts $g=1/f$.
:::

:::

:::

:::
