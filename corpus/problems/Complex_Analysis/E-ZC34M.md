---
schema: qual/card@1
id: E-ZC34M
kind: problem
title: A holomorphic function attaining a minimum of $\abs{f}$ vanishes there or is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source concluded "either f(a) = 0 or f is constant" with a undefined, and did not require Omega connected (on a disjoint union of two discs, f = 1 on one and 2 on the other is a counterexample); the statement now takes Omega a region and concludes f(z_0) = 0.'
---

::: {.exercise}
Let $\Omega$ be a region and let $f: \Omega\to \CC$ be holomorphic, and suppose there is a $z_0 \in \Omega$ with $\abs{f(z_0)}\leq \abs{f(z)}$ for all $z\in \Omega$.
Show that either $f(z_0) = 0$ or $f$ is constant.
:::

::: {.solution}

::: pf

::: pf-step
If $f(z_0)\neq0$, then $f$ is constant.

::: pf-proof
For all $z\in\Omega$, $\abs{f(z)}\ge\abs{f(z_0)}>0$, so $g\coloneqq1/f$ is holomorphic on $\Omega$ and $\abs{g(z)}\le\abs{g(z_0)}$.
So $\abs g$ attains its maximum at the interior point $z_0$ of the connected open set $\Omega$, and $g$ is constant by the maximum modulus principle; hence so is $f$.
:::

:::

:::

:::
