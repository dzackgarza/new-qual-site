---
schema: qual/card@1
id: E-HEJJK
kind: problem
title: An entire function whose image misses a disk is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Removable Singularities
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is entire and there exists a disc $\DD_r(a)$ not intersecting $f(\CC)$, then $f$ must be constant.
:::

::: {.solution}

::: pf

::: {.pf-step #bounded}
$G(z)\coloneqq{1\over f(z)-a}$ is entire with $\abs{G}\le1/r$.

::: pf-proof
Since $f(\CC)$ misses $\DD_r(a)$, $\abs{f(z)-a}\ge r>0$ for all $z\in\CC$.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By step [](#bounded){.pf-ref} and Liouville's theorem, $G$ is constant, hence so is $f=a+1/G$.
:::

:::

:::

:::
