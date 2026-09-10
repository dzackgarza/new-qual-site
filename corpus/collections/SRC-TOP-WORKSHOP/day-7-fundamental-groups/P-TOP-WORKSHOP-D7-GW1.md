---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-GW1
kind: problem
title: Realize a presented group as a fundamental group (workshop warm-up)
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Cell Complexes
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $G=\langle x,y\mid x^2yxy=1\rangle$.
Describe a space $X$ that has $\pi_1(X)=G$.
:::

::: {.solution}
Start with the wedge of two oriented circles
\[
R=S^1_x\vee S^1_y,
\]
whose fundamental group is the free group \(F(x,y)\). Attach one \(2\)-cell to \(R\) by a map \(S^1\to R\) representing the word
\[
x^2yxy.
\]
If \(X\) denotes the resulting CW complex, Seifert--van Kampen gives
\[
\pi_1(X)\cong F(x,y)/\langle\!\langle x^2yxy\rangle\!\rangle
\cong\langle x,y\mid x^2yxy=1\rangle=G.
\]
Thus a two-petal rose with one \(2\)-cell attached along the indicated word realizes the presentation.
:::
