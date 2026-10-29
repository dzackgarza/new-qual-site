---
schema: qual/card@1
id: E-ELZ3Z
kind: problem
title: A function with bounded derivative is uniformly continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Calculus
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "Show that $f''$ bounded implies $f$ is uniformly continuous." with no domain. On a disconnected domain the claim fails (a locally constant function on $\bigcup_n [1/(2n+1),1/(2n)]$ taking alternate values $0$ and $1$); the statement now takes $f$ real-valued and differentiable on an interval.'
---

::: {.problem}
Let $I\subseteq\RR$ be an interval and let $f:I\to\RR$ be differentiable.
Show that $f'$ bounded implies $f$ is uniformly continuous.
:::

::: {.solution}
Let $\abs{f'}\le M$ on $I$.

::: pf

::: {.pf-step #lipschitz}
For all $x,y\in I$, $\abs{f(x)-f(y)}\le M\abs{x-y}$.

::: pf-proof
The mean value theorem gives $\xi$ between $x$ and $y$, hence in $I$, with
$$
\abs{f(x) - f(y)} = \abs{f'(\xi)} \abs{x-y} \le M\abs{x-y}.
$$
:::

:::

::: pf-step
$f$ is uniformly continuous.

::: pf-proof
Let $\varepsilon>0$. Take $\delta=\varepsilon/M$ if $M>0$, and any $\delta>0$ if $M=0$.
By step [](#lipschitz){.pf-ref}, $\abs{x-y}<\delta$ implies $\abs{f(x)-f(y)}<\varepsilon$ for all $x,y\in I$.
:::

:::

:::

:::
