---
schema: qual/card@1
id: E-W3QMS
kind: problem
title: Holomorphic functions with vanishing derivative are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Contour Integration
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source does not say where f is defined; the conclusion fails on a disconnected open set, so the statement takes f holomorphic on a region. The source's pointer "See S&S Corollary 3.4" is removed from the statement.
---

::: {.exercise}
Let $f$ be holomorphic on a region $\Omega$.
Show that $f'=0 \implies f$ is constant using integrals and *primitives* (i.e. antiderivatives).
:::

::: {.solution}
::: pf

::: pf-step
$f(b) = f(a)$ for all $a, b\in\Omega$.

::: pf-proof
A region is open and connected, so there is a piecewise $C^1$ path $\gamma$ in $\Omega$ from $a$ to $b$.
Since $f$ is a primitive of $f'$,
$$
f(b)-f(a)=\int_\gamma f'(z)\,dz=0.
$$
:::

:::

:::

:::
