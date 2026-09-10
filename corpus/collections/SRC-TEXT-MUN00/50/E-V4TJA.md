---
schema: qual/card@1
id: E-V4TJA
kind: problem
title: Five points in general position and K5 in space
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Show that the points $\mathbf{0}, \epsilon_1, \epsilon_2, \epsilon_3$, and $(1, 1, 1)$ are in general position in $\mathbb{R}^3$.
Sketch the corresponding imbedding into $\mathbb{R}^3$ of the complete graph on five vertices.
:::

::: {.solution}
Let
\[
p_0=0,\quad p_1=e_1,\quad p_2=e_2,\quad p_3=e_3,\quad p_4=(1,1,1).
\]
In \(\mathbb R^3\), general position for five points means that every four are affinely independent and no three are collinear. It suffices to check the four-point condition.

The set \(\{p_0,p_1,p_2,p_3\}\) is affinely independent because \(e_1,e_2,e_3\) are linearly independent. If \(p_0\) and \(p_4\) occur and one of the \(e_i\)'s is omitted, the three difference vectors are the two remaining basis vectors together with \((1,1,1)\); the corresponding determinant is \(\pm1\). Finally, for \(\{p_1,p_2,p_3,p_4\}\), subtracting \(p_1\) gives
\[
p_2-p_1=(-1,1,0),\quad p_3-p_1=(-1,0,1),\quad p_4-p_1=(0,1,1),
\]
whose determinant is \(2\ne0\). Hence every four points are affinely independent, so the five points are in general position.

The required embedding of \(K_5\) sends its five vertices to these points and each edge to the straight line segment joining the corresponding pair. If two edges without a common endpoint met, their four endpoints would lie in one affine plane, contradicting affine independence. Thus distinct edges meet only at common endpoints, and these ten segments form an embedded linear copy of \(K_5\) in \(\mathbb R^3\).
:::
