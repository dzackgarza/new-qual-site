---
schema: qual/card@1
id: E-AHBVF
kind: problem
title: Taylor expansion of $z^2\cos(z/3)$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Expand $f(z) = z^2\cos\qty{z\over 3}$ about $z=0$.
:::

::: {.solution}

::: pf

::: {.pf-step #cos}
$\cos\qty{\frac z3}=\sum_{k=0}^\infty(-1)^k\frac{(z/3)^{2k}}{(2k)!}$ for all $z\in\CC$.

::: pf-proof
Substitute $z/3$ into the Taylor series of $\cos$, which converges on all of $\CC$.
:::

:::

::: pf-step
$$
z^2\cos\qty{\frac z3}
=\boxed{\sum_{k=0}^\infty(-1)^k\frac{z^{2k+2}}{3^{2k}(2k)!}
=z^2-\frac{z^4}{2!\,3^2}+\frac{z^6}{4!\,3^4}-\cdots}
$$
for all $z\in\CC$.

::: pf-proof
Multiply the series of step [](#cos){.pf-ref} by $z^2$.
:::

:::

:::

:::
