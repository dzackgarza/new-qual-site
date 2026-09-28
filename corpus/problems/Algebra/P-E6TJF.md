---
schema: qual/card@1
id: P-E6TJF
kind: problem
title: Stabilizers of points in the same orbit are conjugate
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Conjugacy
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that if $x, y$ are in the same orbit, then their stabilizers are conjugate.
:::

::: {.solution}
Let $G$ act on $X$, and suppose $y=g\cdot x$. Then
\[
G_y=gG_xg^{-1}.
\]
Indeed, if $h\in G_x$, then
\[
(ghg^{-1})\cdot y
=ghg^{-1}g\cdot x
=g(h\cdot x)
=g\cdot x
=y,
\]
so $gG_xg^{-1}\subseteq G_y$.

Conversely, if $k\in G_y$, then
\[
(g^{-1}kg)\cdot x
=g^{-1}k\cdot(gx)
=g^{-1}(k\cdot y)
=g^{-1}y
=x,
\]
so $g^{-1}kg\in G_x$, hence $k\in gG_xg^{-1}$. Therefore
\[
G_y=gG_xg^{-1}.
\]
:::
