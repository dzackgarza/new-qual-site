---
schema: qual/card@1
id: P-UPCWX
kind: problem
title: Uniform differentiability on $[a,b]$ is equivalent to continuity of $f'$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Continuity
  - Uniform Continuity
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source requires the difference-quotient bound whenever $\abs{x-y} < \delta$, which includes x = y where the quotient is undefined; the statement now requires $0 < \abs{x-y} < \delta$ with x, y in [a, b].'
---

::: {.problem}
Let $f$ be differentiable on $[a, b]$.
Say that $f$ is *uniformly differentiable* iff

$$
\forall \varepsilon > 0,\, \exists \delta > 0 \text{ such that } \quad x, y \in [a, b],\ 0 < \abs{x-y} < \delta \implies \abs{ {f(x) - f(y) \over x-y}  - f'(y)}  < \varepsilon.
$$

Prove that $f$ is uniformly differentiable on $[a, b] \iff f'$ is continuous on $[a, b]$.
:::

::: {.solution}
Write $Q(x, y) = \frac{f(x) - f(y)}{x - y}$ for $x \neq y$, and note $Q(x, y) = Q(y, x)$.

::: pf

::: pf-step

If $f$ is uniformly differentiable, then $f'$ is (uniformly) continuous on $[a, b]$.

::: pf-proof

Fix $\varepsilon > 0$ and take $\delta$ from the definition for $\varepsilon/2$. For $x, y \in [a, b]$ with $0 < \abs{x-y} < \delta$, applying the definition to the pairs $(x, y)$ and $(y, x)$ gives
$$
\abs{f'(x) - f'(y)} \leq \abs{f'(x) - Q(y, x)} + \abs{Q(x, y) - f'(y)} < \varepsilon.
$$

:::

:::

::: pf-step

If $f'$ is continuous on $[a, b]$, then $f$ is uniformly differentiable.

::: pf-proof

A continuous function on the compact interval $[a, b]$ is uniformly continuous, so given $\varepsilon > 0$ there is $\delta > 0$ with $\abs{f'(s) - f'(t)} < \varepsilon$ whenever $s, t \in [a, b]$ and $\abs{s - t} < \delta$. Let $x, y \in [a, b]$ with $0 < \abs{x - y} < \delta$. By the mean value theorem there is $\xi$ strictly between $x$ and $y$ with $Q(x, y) = f'(\xi)$. Since $\abs{\xi - y} < \abs{x - y} < \delta$,
$$
\abs{Q(x, y) - f'(y)} = \abs{f'(\xi) - f'(y)} < \varepsilon.
$$

:::

:::

:::

:::
