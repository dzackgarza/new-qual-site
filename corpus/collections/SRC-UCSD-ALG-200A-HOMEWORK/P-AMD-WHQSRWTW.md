---
schema: qual/card@1
id: P-AMD-WHQSRWTW
kind: problem
title: A group is abelian iff every triple contains a commuting pair
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 2, Exercise 1. The source
    asks for the equivalence; the prior card retained only the nontrivial
    implication, so the omitted converse has been restored.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    For the nontrivial direction, applied the hypothesis to x, y, xy. Commutation
    of either x or y with xy cancels to xy = yx, while commutation of x and y is
    already the desired conclusion. The converse is immediate for an abelian
    group.
---

::: {.problem}
Show that a group $G$ is abelian if and only if, in every triplet of elements of $G$, two of the elements commute.
:::

::: {.solution}
<1>1. If $G$ is abelian, then every triplet in $G$ contains two commuting elements.
::: {.proof}
If $G$ is abelian, every two elements of $G$ commute.
Hence every triplet has, in particular, a commuting pair.
:::

<1>2. Conversely, suppose every triplet in $G$ contains two commuting elements.
Then $G$ is abelian.
::: {.proof}
Let $x,y\in G$ be arbitrary and consider the triplet
\[
x,\qquad y,\qquad xy.
\]
By hypothesis, some pair among these three elements commutes.

If $x$ and $y$ commute, then $xy=yx$ immediately.

If $x$ and $xy$ commute, then
\[
x(xy)=(xy)x.
\]
Thus $x^2y=xyx$, and left cancellation by $x$ gives $xy=yx$.

If $y$ and $xy$ commute, then
\[
y(xy)=(xy)y.
\]
Thus $yxy=xy^2$, and right cancellation by $y$ gives $yx=xy$.

In every case, $x$ and $y$ commute.
Since $x$ and $y$ were arbitrary, $G$ is abelian.
:::

<1>3. Therefore the two conditions are equivalent.
::: {.proof}
This follows from <1>1 and <1>2.
:::
:::
