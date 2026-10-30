---
schema: qual/card@1
id: P-5RZWO
kind: problem
title: Composition of injective maps is injective
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Suppose $f$ and $g$ are injective maps of a set $S$ into itself.
Show that the composite function $f\circ g$ is also injective.
:::

::: {.solution}

::: pf

::: {.pf-step #fg-eq}

Let $x, y \in S$ with $(f\circ g)(x) = (f\circ g)(y)$. Then $g(x) = g(y)$.

::: pf-proof

By definition of composition, $f(g(x)) = f(g(y))$, and $f$ is injective.

:::

:::

::: pf-step

For all $x, y \in S$, $(f\circ g)(x) = (f\circ g)(y)$ implies $x = y$, so $f\circ g$ is injective.

::: pf-proof

By step [](#fg-eq){.pf-ref}, $g(x) = g(y)$, and $g$ is injective, so $x = y$.

:::

:::

:::

:::
