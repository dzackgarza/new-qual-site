---
schema: qual/card@1
id: P-KNLBB
kind: problem
title: $z^2$ is uniformly continuous on $\abs{z}<R$ but not on $\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-reviewed
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The card body carried the source label "Tie, Fall 2009" above the statement; it was removed from the public card. The earlier solution bounded on the wrong disc and mixed w = z + delta/2 with w = z + delta; it was rewritten.'
---

::: {.problem}
Show that $f(z) = z^2$ is uniformly continuous in any open disk $\abs{z} < R$, where $R>0$ is fixed, but it is not uniformly continuous on $\CC$.
:::

::: {.solution}
::: pf

::: pf-step
$f$ is uniformly continuous on $\abs{z} < R$.

::: pf-proof
Let $\varepsilon > 0$ and $\delta = \frac{\varepsilon}{2R}$.
For $\abs{z}, \abs{w} < R$ with $\abs{z - w} < \delta$,
$$
\abs{z^2-w^2} = \abs{z-w}\abs{z+w} < \delta \cdot 2R = \varepsilon.
$$
:::

:::

::: pf-step
$f$ is not uniformly continuous on $\CC$.

::: pf-proof
Take $\varepsilon = 1$ and any $\delta > 0$.
For real $x > 0$ let $z = x + \delta/2$ and $w = x$, so $\abs{z - w} < \delta$ and
$$
\abs{z^2 - w^2} = \frac{\delta}{2}\left(2x + \frac{\delta}{2}\right) \geq \delta x,
$$
which exceeds $1$ once $x > 1/\delta$.
So no $\delta$ works for $\varepsilon = 1$.
:::

:::

:::
:::

::: {.remark}
The failure on $\CC$ also follows from sequences: $z_n=n$ and $w_n=n+\frac1n$ satisfy $\abs{z_n-w_n}\to0$, but $\abs{w_n^2-z_n^2}=2+\frac1{n^2}\to2$.
:::
