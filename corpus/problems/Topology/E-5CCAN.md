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

::: exercise
Show that $\RR$ is not homeomorphic to $[0, \infty)$.
:::

::: solution
<1>1. Suppose that a homeomorphism
$$
f:[0,\infty)\longrightarrow\mathbb R
$$
exists, and set $y=f(0)$.

<1>2. Restricting $f$ gives a homeomorphism
$$
(0,\infty)=[0,\infty)\setminus\{0\}
\longrightarrow
\mathbb R\setminus\{y\}.
$$

<1>3. The space $(0,\infty)$ is connected, whereas
$$
\mathbb R\setminus\{y\}=(-\infty,y)\sqcup(y,\infty)
$$
is disconnected.

<1>4. This contradicts invariance of connectedness under homeomorphism. Therefore $\mathbb R$ is not homeomorphic to $[0,\infty)$.
:::
