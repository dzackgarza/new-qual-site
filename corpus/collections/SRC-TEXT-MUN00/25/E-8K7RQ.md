---
schema: qual/card@1
id: E-8K7RQ
kind: problem
title: Components and continuous maps out of the lower limit line
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

What are the components and path components of $\RR_\ell$?
What are the continuous maps $f: \RR \to \RR_\ell$?
:::

::: {.solution}
::: pf

::: {.pf-step #components-are-points}
The components and path components of $\RR_\ell$ are the one-point sets.

::: pf-proof
For $a\in\RR$, the rays $(-\infty,a)=\bigcup_{n\ge1}[a-n,a)$ and $[a,\infty)=\bigcup_{n\ge0}[a+n,a+n+1)$ are open in $\RR_\ell$, disjoint, and cover $\RR$.
If $x<y$, choosing $a$ with $x<a\le y$ gives a separation of $\RR_\ell$ with $x$ and $y$ on different sides, so no connected set contains both.
Hence the components are points, and so are the path components, each of which lies in a component.
:::

:::

::: {.pf-step #maps-are-constant}
The continuous maps $f\colon\RR\to\RR_\ell$ are exactly the constant maps.

::: pf-proof
Constant maps are continuous.
If $f$ is continuous, $f(\RR)$ is connected because $\RR$ is, so by step [](#components-are-points){.pf-ref} it is a single point.
:::

:::

::: pf-qed
Steps [](#components-are-points){.pf-ref} and [](#maps-are-constant){.pf-ref} answer the two questions.
:::

:::

:::
