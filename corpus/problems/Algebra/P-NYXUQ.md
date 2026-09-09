---
schema: qual/card@1
id: P-NYXUQ
kind: problem
title: Conjugacy of stabilizers along an orbit
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
What group-theoretic construct relates the stabilizer of two points in the same orbit under a group action?
:::

::: solution
If $y=g\cdot x$, then
\[
G_y=gG_xg^{-1}.
\]
Indeed, for $h\in G_x$,
\[
(ghg^{-1})\cdot y=gh\cdot x=g\cdot x=y,
\]
so $gG_xg^{-1}\subseteq G_y$. Applying the same argument with $g^{-1}$ gives the reverse inclusion. Thus stabilizers of points in the same orbit are conjugate.
:::
