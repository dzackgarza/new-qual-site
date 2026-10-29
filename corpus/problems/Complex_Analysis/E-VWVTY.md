---
schema: qual/card@1
id: E-VWVTY
kind: problem
title: Annulus of convergence of $\sum_{k\in\ZZ}2^{-\abs{k}}z^k$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Convergence Tests
  - Power Series
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source asks for the radius of convergence; a series indexed by Z converges on an annulus, so the statement asks for the region of convergence.
---

::: {.exercise}
Find the region of convergence for
$$
f(z) \definedas \sum_{k\in \ZZ} 2^{-\abs{k}}z^k.
$$

:::

::: {.solution}
Split $f = f_1 + f_2$ with
$$
f_1(z) \definedas \sum_{k\geq 1} (2z)^{-k}, \qquad f_2(z) \definedas \sum_{k\geq 0} (z/2)^k.
$$
The series $f$ converges exactly where both $f_1$ and $f_2$ converge.

::: pf

::: {.pf-step #f1}
$f_1(z)$ converges if and only if $\abs{z} > \frac12$.

::: pf-proof
It is a geometric series in $(2z)^{-1}$, which converges if and only if $\abs{(2z)^{-1}} < 1$.
:::

:::

::: {.pf-step #f2}
$f_2(z)$ converges if and only if $\abs{z} < 2$.

::: pf-proof
It is a geometric series in $z/2$, which converges if and only if $\abs{z/2} < 1$.
:::

:::

::: pf-step
$f$ converges exactly on the annulus $\boxed{\frac12 < \abs{z} < 2}$.

::: pf-proof
Intersect the regions of steps [](#f1){.pf-ref} and [](#f2){.pf-ref}.
:::

:::

:::

:::
