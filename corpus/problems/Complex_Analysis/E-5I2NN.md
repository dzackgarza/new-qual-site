---
schema: qual/card@1
id: E-5I2NN
kind: problem
title: $\abs{f'(a)}\le1$ at a fixed point and $\abs{f(0)}^2+\abs{f'(0)}^2\le1$ by
  Schwarz--Pick
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Fixed Points
  - Blaschke Factors
relations: []
review: draft
---

::: {.exercise}
Let $f\in \Hol(\DD)$.
Show that if $f$ has a fixed point $a$ then $\abs{f'(a)} \leq 1$, and that 
\[
\abs{f(0)}^2 + \abs{f'(0)}^2 \leq 1
.\]

:::

::: {.solution}
Assume $f(\DD)\subseteq\DD$, which the Schwarz--Pick lemma requires.
Set $f(a) = a$ in Schwarz-Pick:
\[
\left|f^{\prime}(a)\right| \leq \frac{1-|f(a)|^{2}}{1-|a|^{2}} \implies 
\abs{f'(a)} \leq {1 - \abs{a}^2 \over 1 - \abs{a}^2} = 1
.\]
Set $a=0$:
\[
\left|f^{\prime}(0)\right| \leq \frac{1-|f(0)|^{2}}{1-|0|^{2}} = 1-\abs{f(0)}^2
.\]
Since the right side is at most $1$, $\abs{f'(0)}^2\le\abs{f'(0)}\le1-\abs{f(0)}^2$.
:::

::: {.remark}
Both bounds fail for holomorphic maps that do not send $\DD$ into $\DD$: $f(z)=2z$ fixes $0$ and has $f'(0)=2$.
:::
