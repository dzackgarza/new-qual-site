---
schema: qual/card@1
id: E-LOA25
kind: exercise
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
<1>1. ($\Rightarrow$) If $X$ is metrizable, then $X$ is paracompact Hausdorff.
<2>1. Every metric space is Hausdorff.
::: {.proof}
distinct points are separated by disjoint open balls.
:::
<2>2. Every metric space is paracompact.
::: {.proof}
Stone's theorem (metric spaces are paracompact).
:::
<2>3. Hence metrizable $\Rightarrow$ paracompact Hausdorff.
::: {.proof}
<2>1 and <2>2.
:::

<1>2. ($\Leftarrow$) If $X$ is paracompact Hausdorff and locally $m$-euclidean, then $X$ is metrizable.
<2>1. $X$ is locally metrizable.
::: {.proof}
$X$ is locally homeomorphic to $\RR^m$, which is metrizable.
:::
<2>2. A paracompact Hausdorff space that is locally metrizable is metrizable.
::: {.proof}
Smirnov metrization theorem.
:::
<2>3. Hence $X$ is metrizable.
::: {.proof}
<2>1 and <2>2.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
