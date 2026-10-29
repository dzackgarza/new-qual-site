---
schema: qual/card@1
id: E-U2X4C
kind: problem
title: Entire functions with $|f(z)|>1$ are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is entire and $\abs{f(z)} > 1$ for all $z$, then $f$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #reciprocal}
$1/f$ is entire and $\abs{1/f}<1$ on $\CC$.

::: pf-proof
The inequality $\abs{f}>1$ shows $f$ has no zeros, so $1/f$ is entire, and $\abs{1/f} = 1/\abs{f} < 1$.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By step [](#reciprocal){.pf-ref} and Liouville's theorem, $1/f$ is a constant, which is nonzero, so $f$ is constant.
:::

:::

:::

:::
