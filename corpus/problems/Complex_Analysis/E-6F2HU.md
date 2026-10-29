---
schema: qual/card@1
id: E-6F2HU
kind: problem
title: Real-valued holomorphic functions are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source reads "Show that a real-valued holomorphic function is constant" with no domain; the statement takes the domain connected, since on a disconnected open set a locally constant function is a counterexample.
---

::: {.exercise}
Show that a real-valued holomorphic function on a connected open set is constant.
:::

::: {.solution}
Let $f$ be holomorphic and real-valued on a connected open set $\Omega$.

::: pf

::: pf-step
$f$ is constant.

::: pf-proof
If $f$ were nonconstant, the open mapping theorem would make $f(\Omega)$ a nonempty open subset of $\CC$.
But $f(\Omega)\subseteq\RR$, and $\RR$ contains no nonempty open subset of $\CC$.
:::

:::

:::

:::
