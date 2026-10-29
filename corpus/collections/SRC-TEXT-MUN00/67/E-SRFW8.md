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
[Hint: Set $G = \ZZ$ and $G_1 = 2\ZZ$.]
:::

::: {.solution}
Take
\[
G=\ZZ,\qquad G_1=2\ZZ.
\]
Suppose there were a subgroup \(G_2\le\ZZ\) with
\[
\ZZ=2\ZZ\oplus G_2.
\]
Every subgroup of \(\ZZ\) has the form \(m\ZZ\) for some \(m\ge0\). If \(m=0\), then \(2\ZZ+G_2=2\ZZ\ne\ZZ\). If \(m>0\), then
\[
2m\in2\ZZ\cap m\ZZ
\]
is nonzero, contradicting directness. Therefore \(2\ZZ\) is a subgroup of \(\ZZ\) that has no complementary subgroup.
:::
