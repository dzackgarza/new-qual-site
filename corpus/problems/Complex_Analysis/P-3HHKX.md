---
schema: qual/card@1
id: P-3HHKX
kind: problem
title: Reverse triangle inequality $|z+w|\ge\bigl||z|-|w|\bigr|$
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Prove the following inequality, and explain when equality holds:
$$
\abs{z+w} \geq \abs{ \abs{z} - \abs{w} }
.$$
:::

::: {.solution}

::: pf

::: {.pf-step #squares}
$\abs{z+w}^2-\qty(\abs{z}-\abs{w})^2 = 2\qty(\Re(z\bar w)+\abs{z\bar w})$.

::: pf-proof
Expand $\abs{z+w}^2=(z+w)(\bar z+\bar w)=\abs{z}^2+\abs{w}^2+2\Re(z\bar w)$ and $\qty(\abs{z}-\abs{w})^2=\abs{z}^2+\abs{w}^2-2\abs{z\bar w}$.
:::

:::

::: pf-step
$\abs{z+w}\geq\abs{\abs{z}-\abs{w}}$, with equality if and only if $z\bar w$ is a real number $\leq 0$, that is, $w=0$ or $z=-\mu w$ for some real $\mu\geq0$.

::: pf-proof
Both sides of the inequality are nonnegative, so it is equivalent to the inequality between their squares.
By step [](#squares){.pf-ref}, that is $\Re(z\bar w)\geq-\abs{z\bar w}$, which holds for every complex number, with equality exactly when $z\bar w\in(-\infty,0]$.
If $w\neq0$, then $z\bar w=-\mu\abs{w}^2$ with $\mu\geq0$ is the same as $z=-\mu w$.
:::

:::

:::

:::
