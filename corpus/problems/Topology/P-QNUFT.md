---
schema: qual/card@1
id: P-QNUFT
kind: problem
title: Paths with common endpoints in a simply connected space are homotopic
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source problem block held a worked answer opening 'Main idea: just algebraic manipulations using the pi_1 functor'; the statement now poses the claim that answer proves, and the solution carries the argument."
---

::: {.problem}
Let $X$ be a path-connected, simply connected space.
Show that any two paths in $X$ with the same initial point and the same terminal point are homotopic relative to their endpoints.
:::

::: {.solution}
Let $\gamma, \alpha\colon I \to X$ be paths with $\gamma(0) = \alpha(0) = x$ and $\gamma(1) = \alpha(1) = y$.
Write $\simeq$ for homotopy relative to endpoints, $*$ for concatenation, $\bar\alpha(t) = \alpha(1-t)$ for the reverse path, and $c_x$ for the constant path at $x$.

::: pf

::: {.pf-step #null}
$\gamma * \bar\alpha \simeq c_x$.

::: pf-proof
The path $\gamma * \bar\alpha$ is a loop at $x$, and $\pi_1(X, x) = 0$ because $X$ is simply connected.
:::

:::

::: pf-step
$\gamma \simeq \alpha$.

::: pf-proof
Concatenation is well defined on classes rel endpoints, associative up to $\simeq$, has constant paths as units, and satisfies $\bar\alpha * \alpha \simeq c_y$.
With step [](#null){.pf-ref},
$$
\gamma \simeq \gamma * c_y \simeq \gamma * (\bar\alpha * \alpha) \simeq (\gamma * \bar\alpha) * \alpha \simeq c_x * \alpha \simeq \alpha.
$$
:::

:::

:::

:::
