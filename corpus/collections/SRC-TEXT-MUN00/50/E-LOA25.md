---
schema: qual/card@1
id: E-LOA25
kind: problem
title: Metrizability equals paracompact Hausdorff for locally euclidean spaces
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Paracompactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be a space that is locally $m$-euclidean.
Show that $X$ is metrizable if and only if $X$ is paracompact Hausdorff.
:::

::: {.solution}
<1>1. If $X$ is metrizable, then $X$ is paracompact Hausdorff.

::: {.proof}
Distinct points of a metric space have disjoint open balls around them, so $X$ is Hausdorff. Every metrizable space is paracompact by Stone's theorem.
:::

<1>2. If $X$ is paracompact Hausdorff, then $X$ is metrizable.

::: {.proof}
Every point of $X$ has a neighborhood homeomorphic to $\RR^m$, which is metrizable, so $X$ is locally metrizable. By the Smirnov metrization theorem, a paracompact Hausdorff space that is locally metrizable is metrizable.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give the two implications.
:::
:::
