---
schema: qual/card@1
id: E-SRFW8
kind: problem
title: Subgroups need not be direct summands
classification:
  areas:
  - topology
  topics:
  - Free Abelian Groups
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

Show that if $G_1$ is a subgroup of $G$, there may be no subgroup $G_2$ of $G$ such that $G = G_1 \oplus G_2$.
[Hint: Set $G = \mathbb{Z}$ and $G_1 = 2\mathbb{Z}$.]
:::

::: {.solution}
Take
\[
G=\mathbb Z,\qquad G_1=2\mathbb Z.
\]
Suppose there were a subgroup \(G_2\le\mathbb Z\) with
\[
\mathbb Z=2\mathbb Z\oplus G_2.
\]
Every subgroup of \(\mathbb Z\) has the form \(m\mathbb Z\) for some \(m\ge0\). If \(m=0\), then \(2\mathbb Z+G_2=2\mathbb Z\ne\mathbb Z\). If \(m>0\), then
\[
2m\in2\mathbb Z\cap m\mathbb Z
\]
is nonzero, contradicting directness. Therefore \(2\mathbb Z\) is a subgroup of \(\mathbb Z\) that has no complementary subgroup.
:::
