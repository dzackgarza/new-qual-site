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

What are the components and path components of $\mathbb{R}_\ell$?
What are the continuous maps $f: \mathbb{R} \to \mathbb{R}_\ell$?
:::

::: {.solution}
<1>1. The components and path components of $\mathbb R_\ell$ are the one-point sets.

::: {.proof}
For $a\in\mathbb R$, the rays $(-\infty,a)=\bigcup_{n\ge1}[a-n,a)$ and $[a,\infty)=\bigcup_{n\ge0}[a+n,a+n+1)$ are open in $\mathbb R_\ell$, disjoint, and cover $\mathbb R$.
If $x<y$, choosing $a$ with $x<a\le y$ gives a separation of $\mathbb R_\ell$ with $x$ and $y$ on different sides, so no connected set contains both.
Hence the components are points, and so are the path components, each of which lies in a component.
:::

<1>2. The continuous maps $f\colon\mathbb R\to\mathbb R_\ell$ are exactly the constant maps.

::: {.proof}
Constant maps are continuous.
If $f$ is continuous, $f(\mathbb R)$ is connected because $\mathbb R$ is, so by step <1>1 it is a single point.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 answer the two questions.
:::
:::
