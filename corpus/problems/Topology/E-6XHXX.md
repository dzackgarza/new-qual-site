---
schema: qual/card@1
id: E-6XHXX
kind: problem
title: $\mathbb{R}$ is separable
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

::: exercise
Show that $\RR$ is separable.
:::

::: solution
<1>1. The subset $\mathbb Q\subset\mathbb R$ is countable.
::: proof
The map
$$
\mathbb Z\times\mathbb Z_{>0}\longrightarrow\mathbb Q,
\qquad (p,q)\longmapsto p/q,
$$
is surjective, and $\mathbb Z\times\mathbb Z_{>0}$ is countable.
:::

<1>2. The subset $\mathbb Q$ is dense in $\mathbb R$.
::: proof
Let $(a,b)$ be a nonempty open interval. Choose $q\in\mathbb Z_{>0}$ with
$q(b-a)>1$. Then there is an integer $p$ with
$$
qa<p<qb,
$$
so $p/q\in(a,b)\cap\mathbb Q$. Hence every nonempty basic open set meets $\mathbb Q$.
:::

<1>3. Therefore $\mathbb R$ has a countable dense subset and is separable.
:::
