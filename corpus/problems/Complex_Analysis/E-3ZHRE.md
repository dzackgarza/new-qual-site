---
schema: qual/card@1
id: E-3ZHRE
kind: problem
title: Entire functions with $\abs{f(z)}\ge e^{\abs z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Casorati-Weierstrass
  - Counterexamples
relations: []
review: draft
---

::: {.exercise}
Find all entire functions $f$ that satisfy
$$
\abs{f(z)} \geq e^{\abs{z}} \qquad \forall z\in \CC.
$$

:::

::: {.solution}

::: pf

::: {.pf-step #reciprocal}
If $f$ satisfies the inequality, then $1/f$ is entire and constant.

::: pf-proof
The inequality gives $\abs{f(z)}\ge1>0$, so $f$ has no zeros and $1/f$ is entire with $\abs{1/f}\le1$.
By Liouville's theorem $1/f$ is constant.
:::

:::

::: pf-step
$\boxed{\text{No entire function satisfies the inequality.}}$

::: pf-proof
By step [](#reciprocal){.pf-ref}, such an $f$ would be a constant $c$, but $e^{\abs z}\to\infty$ as $\abs z\to\infty$, so $\abs c\ge e^{\abs z}$ fails for large $\abs z$.
:::

:::

:::

:::
