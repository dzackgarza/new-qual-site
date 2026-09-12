---
schema: qual/card@1
id: P-RAF05B
kind: problem
title: Measurable planar sets with nonmeasurable Minkowski sum
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Measure
  - Measurable Sets
  - Sumsets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2005 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Find Lebesgue measurable sets $A, B \subset \mathbb{R}^2$ such that $A + B$ is not Lebesgue measurable.
:::

::: solution
<1>1. Choose a nonmeasurable subset of the real line.
::: proof
Let $V\subset\mathbb R$ be a non-Lebesgue-measurable set, for example a Vitali set. Define
\[
A:=V\times\{0\},
\qquad
B:=\{0\}\times\mathbb R.
\]
Both $A$ and $B$ are subsets of one-dimensional affine subspaces of $\mathbb R^2$, hence of planar Lebesgue-null sets. Since planar Lebesgue measure is complete, both $A$ and $B$ are Lebesgue measurable in $\mathbb R^2$.
:::

<1>2. Compute the Minkowski sum.
::: proof
Every element of $A+B$ has the form
\[
(v,0)+(0,t)=(v,t)
\]
with $v\in V$ and $t\in\mathbb R$. Thus
\[
A+B=V\times\mathbb R.
\]
:::

<1>3. Show that $V\times\mathbb R$ is not Lebesgue measurable.
::: proof
Suppose for contradiction that $V\times\mathbb R$ were Lebesgue measurable in $\mathbb R^2$. Then
\[
E:=(V\times\mathbb R)\cap(\mathbb R\times[0,1])
=V\times[0,1]
\]
would also be Lebesgue measurable.

For a Lebesgue measurable subset of $\mathbb R^2$, Fubini's theorem implies that its horizontal sections are Lebesgue measurable for almost every $y$. But for every $y\in[0,1]$,
\[
E_y:=\{x:(x,y)\in E\}=V.
\]
Hence $V$ would be Lebesgue measurable, contradicting its choice. Therefore
\[
\boxed{A+B=V\times\mathbb R\text{ is not Lebesgue measurable}.}
\]
:::
:::
