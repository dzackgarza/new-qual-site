---
schema: qual/card@1
id: E-WNXIR
kind: problem
title: Holomorphic functions have discrete zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Identity Theorem
  - Power Series
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source does not require Omega connected; a function that vanishes on one component of a disconnected open set and not on another is a counterexample, so the statement takes Omega to be a region.
---

::: {.exercise}
If $f$ is holomorphic on a region $\Omega$ and not identically zero, then $\inverseof{f}(0) \intersect \Omega$ is discrete.

:::

::: {.solution}
::: pf

::: {.pf-step #open-closed}
For every $a\in\Omega$, some derivative $f^{(m)}(a)$ is nonzero.

::: pf-proof
Let $U = \theset{a\in\Omega \st f^{(k)}(a) = 0 \text{ for all } k\ge0}$.
$U$ is closed in $\Omega$ as an intersection of closed sets.
$U$ is open: if $a\in U$, the Taylor series of $f$ at $a$ is zero and represents $f$ on a disk about $a$, so $f$ vanishes on that disk, which then lies in $U$.
Since $\Omega$ is connected and $f\not\equiv0$, $U = \emptyset$.
:::

:::

::: pf-step
If $f(a) = 0$, then $f$ is nonzero on a punctured disk about $a$.

::: pf-proof
By step [](#open-closed){.pf-ref}, let $m\ge1$ be minimal with $c_m \definedas f^{(m)}(a)/m! \neq 0$.
On a disk $\abs{z-a}<r$ in $\Omega$,
$$
f(z) = \sum_{k\geq m} c_k (z-a)^k = (z-a)^m g(z), \qquad g(z) \definedas \sum_{k\ge m}c_k(z-a)^{k-m},
$$
with $g$ holomorphic and $g(a) = c_m\neq0$.
By continuity $g\neq0$ on a smaller disk about $a$, and there $f(z)\neq0$ for $z\neq a$.
:::

:::

:::

:::
