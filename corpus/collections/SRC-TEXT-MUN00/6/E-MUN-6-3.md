---
schema: qual/card@1
id: E-MUN-6-3
kind: problem
title: Cantor's theorem for $X^{\omega}$
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $X$ be the two-element set $\{0,1\}$ . Find a bijective correspondence between $X^{\omega}$ and a proper subset of itself.
:::

::: {.solution}
Let
\[
P=\{(y_1,y_2,\dots)\in X^\omega:y_1=0\}.
\]
This is a proper subset of \(X^\omega\), since for example \((1,0,0,\dots)\notin P\).

Define
\[
F:X^\omega\longrightarrow P,
\qquad
F(x_1,x_2,x_3,\dots)=(0,x_1,x_2,x_3,\dots).
\]
The inverse map is the left shift
\[
G(0,y_2,y_3,\dots)=(y_2,y_3,\dots).
\]
Then \(GF=\mathrm{id}_{X^\omega}\) and \(FG=\mathrm{id}_P\). Thus \(F\) is a bijection of \(X^\omega\) with the proper subset \(P\).
:::
