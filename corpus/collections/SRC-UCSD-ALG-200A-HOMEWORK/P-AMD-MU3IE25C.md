---
schema: qual/card@1
id: P-AMD-MU3IE25C
kind: problem
title: A group is not the union of two proper subgroups
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 2, Exercise 2(i).
    The source asks to prove that if G is the union of H_1 and H_2, then one
    of those subgroups is all of G.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Assuming both subgroups proper produces x in H_1\H_2 and y in H_2\H_1.
    The product xy can lie in neither subgroup: membership in either one forces
    the other factor into that subgroup by cancellation.
---

::: {.problem}
Let $H_1,H_2\leq G$ and suppose
\[
G=H_1\cup H_2.
\]

Show that $G=H_1$ or $G=H_2$.
:::

::: {.solution}
<1>1. If both $H_1$ and $H_2$ were proper, there would exist $x\in H_1\setminus H_2$ and $y\in H_2\setminus H_1$.
::: {.proof}
Assume for contradiction that $H_1\ne G$ and $H_2\ne G$.
Choose $y\in G\setminus H_1$.
Since $G=H_1\cup H_2$, necessarily $y\in H_2$, so
\[
y\in H_2\setminus H_1.
\]
Similarly, choose $x\in G\setminus H_2$.
Then $x\in H_1$, hence
\[
x\in H_1\setminus H_2.
\]
:::

<1>2. The element $xy$ lies in neither $H_1$ nor $H_2$.
::: {.proof}
If $xy\in H_1$, then $x\in H_1$ and closure under inverses and products gives
\[
y=x^{-1}(xy)\in H_1,
\]
contrary to <1>1.

If $xy\in H_2$, then $y\in H_2$ and
\[
x=(xy)y^{-1}\in H_2,
\]
again contrary to <1>1. Thus $xy\notin H_1\cup H_2$.
:::

<1>3. Therefore one of the two subgroups is all of $G$.
::: {.proof}
By hypothesis every element of $G$, including $xy$, belongs to $H_1\cup H_2$.
This contradicts <1>2, so the assumption in <1>1 that both subgroups are proper is impossible.
Hence
\[
G=H_1\qquad\text{or}\qquad G=H_2.
\]
:::
:::
