---
schema: qual/card@1
id: P-AMD-Q626TCVB
kind: problem
title: Groups of exponent $2$ are abelian
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked the card against the source-audited UCSD Math 200A Fall 2016 Homework 1 collection occurrence. The live provenance PDF endpoint timed out during this review, so no claim is made of a fresh PDF comparison. Independently corroborated the standard theorem that groups of exponent 2 are abelian in published group-theory literature.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used x^2=e to identify every element with its inverse, then compared the inverse of xy in the two ways (xy)^(-1)=xy and (xy)^(-1)=y^(-1)x^(-1)=yx.
---

::: {.problem}
Given: $\forall x \in G, x^2 = e$

Show: $G \in \mathbf{Ab}$
:::

::: {.solution}
<1>1. Every element of $G$ is its own inverse.
::: {.proof}
Let $x\in G$.
By hypothesis,
\[
x^2=e.
\]
Thus
\[
xx=e,
\]
so uniqueness of inverses gives
\[
x^{-1}=x.
\]
:::

<1>2. Any two elements of $G$ commute.
::: {.proof}
Let $x,y\in G$.
By <1>1, applied to the element $xy$, one has
\[
(xy)^{-1}=xy.
\]
On the other hand, the inverse-of-a-product formula and <1>1 give
\[
(xy)^{-1}=y^{-1}x^{-1}=yx.
\]
Therefore
\[
xy=yx.
\]
Since $x$ and $y$ were arbitrary, $G$ is abelian.
:::
:::
