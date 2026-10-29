---
schema: qual/card@1
id: P-5S2DR
kind: problem
title: Unique solution of $\alpha ze^z=1$ in the unit disc when $\abs{\alpha}>e$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
---

::: {.exercise}
Show that $\alpha z e^z = 1$ where $\abs{\alpha} > e$ has exactly one solution in $\DD$.
:::

::: {.solution}
Since $e^z\neq0$, the equation $\alpha ze^z=1$ is equivalent to $h(z)\coloneqq \alpha z - e^{-z} = 0$.
Set $f(z) = \alpha z$ and $g(z) = e^{-z}$, so $h = f - g$.

::: pf

::: {.pf-step #estimate}
On $\abs{z}=1$, $\abs{g(z)} < \abs{f(z)}$.

::: pf-proof
For $\abs{z}=1$, $\abs{g(z)} = e^{-\Re z} \le e^{1} < \abs{\alpha} = \abs{f(z)}$.
:::

:::

::: pf-step
$h$ has exactly one zero in $\DD$, so $\alpha ze^z=1$ has exactly one solution in $\DD$.

::: pf-proof
By step [](#estimate){.pf-ref} and Rouché's theorem, $h = f-g$ and $f$ have the same number of zeros in $\DD$, counted with multiplicity.
The function $f$ has exactly one zero there, the simple zero $z=0$.
:::

:::

:::

:::
