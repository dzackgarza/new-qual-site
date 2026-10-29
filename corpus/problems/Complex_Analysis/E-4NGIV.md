---
schema: qual/card@1
id: E-4NGIV
kind: problem
title: Entire doubly periodic functions are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that an entire doubly periodic function is constant.
:::

::: {.solution}
Let $\omega_1,\omega_2$ be two $\RR$-linearly independent periods of the entire function $f$, and let
$$
P=\{t_1\omega_1+t_2\omega_2:0\le t_1,t_2\le1\}
$$
be the closed fundamental parallelogram.

::: pf

::: {.pf-step #bounded-on-P}
$M\coloneqq\max_{z\in P}\abs{f(z)}<\infty$.

::: pf-proof
$P$ is compact and $f$ is continuous.
:::

:::

::: {.pf-step #bounded}
$\abs{f(z)}\le M$ for all $z\in\CC$.

::: pf-proof
Since $\omega_1,\omega_2$ form an $\RR$-basis of $\CC$, write $z=s_1\omega_1+s_2\omega_2$ and let $m=\lfloor s_1\rfloor$, $n=\lfloor s_2\rfloor$; then $z_0\coloneqq z-m\omega_1-n\omega_2\in P$.
By periodicity $f(z)=f(z_0)$, and step [](#bounded-on-P){.pf-ref} bounds $\abs{f(z_0)}$ by $M$.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By step [](#bounded){.pf-ref}, $f$ is a bounded entire function, so Liouville's theorem applies.
:::

:::

:::

:::
