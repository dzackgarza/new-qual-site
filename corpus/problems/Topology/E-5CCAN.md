---
schema: qual/card@1
id: E-5CCAN
kind: problem
title: $\mathbb{R}$ is not homeomorphic to $[0,\infty)$
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Connectedness
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
Show that $\RR$ is not homeomorphic to $[0, \infty)$.
:::

::: {.solution}

::: pf

::: pf-step

Suppose that a homeomorphism
$$
f:[0,\infty)\longrightarrow\mathbb R
$$
exists, and set $y=f(0)$.

:::

::: pf-step

Restricting $f$ gives a homeomorphism
$$
(0,\infty)=[0,\infty)\setminus\{0\}
\longrightarrow
\mathbb R\setminus\{y\}.
$$

:::

::: pf-step

The space $(0,\infty)$ is connected, whereas
$$
\mathbb R\setminus\{y\}=(-\infty,y)\sqcup(y,\infty)
$$
is disconnected.

:::

::: pf-step

This contradicts invariance of connectedness under homeomorphism. Therefore $\mathbb R$ is not homeomorphic to $[0,\infty)$.

:::

:::

:::
