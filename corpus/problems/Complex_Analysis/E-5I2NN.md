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
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source reads "Let f in Hol(D)"; both bounds fail without f(D) contained in D (f(z)=2z), so the statement adds that hypothesis.
---

::: {.exercise}
Let $f\in \Hol(\DD)$ with $f(\DD)\subseteq\DD$.
Show that if $f$ has a fixed point $a$ then $\abs{f'(a)} \leq 1$, and that
$$
\abs{f(0)}^2 + \abs{f'(0)}^2 \leq 1.
$$

:::

::: {.solution}
The Schwarz--Pick lemma gives, for every $z\in\DD$,
$$
\abs{f'(z)} \leq \frac{1-\abs{f(z)}^{2}}{1-\abs{z}^{2}}.
$$

::: pf

::: pf-step
If $f(a)=a$, then $\abs{f'(a)}\le1$.

::: pf-proof
Take $z=a$ in the Schwarz--Pick inequality: $\abs{f'(a)} \leq \frac{1 - \abs{a}^2}{1 - \abs{a}^2} = 1$.
:::

:::

::: pf-step
$\abs{f(0)}^2 + \abs{f'(0)}^2 \leq 1$.

::: pf-proof
Take $z=0$: $\abs{f'(0)} \leq 1-\abs{f(0)}^2\le1$.
Hence $\abs{f'(0)}^2\le\abs{f'(0)}\le1-\abs{f(0)}^2$.
:::

:::

:::

:::

::: {.remark}
Both bounds fail for holomorphic maps that do not send $\DD$ into $\DD$: $f(z)=2z$ fixes $0$ and has $f'(0)=2$.
:::
