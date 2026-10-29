---
schema: qual/card@1
id: E-6XHXX
kind: problem
title: $\RR$ is separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that $\RR$ is separable.
:::

::: {.solution}

::: pf

::: pf-step

The subset $\QQ\subset\RR$ is countable.

::: pf-proof

The map
$$
\ZZ\times\ZZ_{>0}\longrightarrow\QQ,
\qquad (p,q)\longmapsto p/q,
$$
is surjective, and $\ZZ\times\ZZ_{>0}$ is countable.

:::

:::

::: pf-step

The subset $\QQ$ is dense in $\RR$.

::: pf-proof

Let $(a,b)$ be a nonempty open interval. Choose $q\in\ZZ_{>0}$ with
$q(b-a)>1$. Then there is an integer $p$ with
$$
qa<p<qb,
$$
so $p/q\in(a,b)\cap\QQ$. Hence every nonempty basic open set meets $\QQ$.

:::

:::

::: pf-step

Therefore $\RR$ has a countable dense subset and is separable.

:::

:::

:::
