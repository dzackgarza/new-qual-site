---
schema: qual/card@1
id: E-2JGJL
kind: problem
title: $\int_\Gamma\Re(z)\,dz$ around the unit square
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source says only "the unit square"; the statement fixes Gamma as the positively oriented boundary of [0,1]^2, the curve the solution integrates over.
---

::: {.exercise}
Compute $\int_\Gamma \Re(z) \dz$ for $\Gamma$ the positively oriented boundary of the unit square $[0,1]\times[0,1]$.
:::

::: {.solution}
Write $\Gamma = \gamma_1+\gamma_2+\gamma_3+\gamma_4$, traversing $0$, $1$, $1+i$, $i$ in order, with $t\in[0,1]$ and
$$
\gamma_1(t)=t,\quad \gamma_2(t)=1+it,\quad \gamma_3(t)=(1-t)+i,\quad \gamma_4(t)=i(1-t).
$$

![](../../assets/Complex_Analysis/010_Basics/figures/2021-12-19_03-22-20.png)

::: pf

::: {.pf-step #pieces}
The four pieces contribute $1/2$, $i$, $-1/2$, and $0$.

::: pf-proof
On $\gamma_1$, $\Re z=t$ and $dz=dt$, giving $\int_0^1 t\dt = 1/2$.
On $\gamma_2$, $\Re z=1$ and $dz=i\dt$, giving $i$.
On $\gamma_3$, $\Re z=1-t$ and $dz=-\dt$, giving $-\int_0^1 (1-t)\dt = -1/2$.
On $\gamma_4$, $\Re z=0$, giving $0$.
:::

:::

::: pf-step
$\int_\Gamma \Re(z) \dz = \boxed{i}$.

::: pf-proof
Add the four contributions of step [](#pieces){.pf-ref}.
:::

:::

:::

:::
