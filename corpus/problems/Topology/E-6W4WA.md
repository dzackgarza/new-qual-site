---
schema: qual/card@1
id: E-6W4WA
kind: problem
title: Dense subspace
classification:
  areas:
  - topology
  topics:
  - Density
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
- What does it mean for $E\subseteq X$ to be a **dense** subspace?
:::

::: solution
A subset $E\subseteq X$ is **dense in $X$** if
$$
\overline E=X.
$$
Equivalently, every nonempty open subset of $X$ meets $E$.
::: proof
A point $x$ lies in $\overline E$ exactly when every open neighborhood of $x$ intersects $E$. Hence $\overline E=X$ exactly when every nonempty open set intersects $E$.
:::
:::
