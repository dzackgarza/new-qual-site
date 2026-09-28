---
schema: qual/card@1
id: P-JHUFA02CAD
kind: problem
title: Unique nearest-point projection onto a closed convex subset of a Hilbert space
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Convex Sets
  - Orthogonal Projection
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 4 of the Fall 2002 JHU real-analysis qualifying exam in the preserved compiled source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
4. Let K be a closed convex subset of a Hilbert space H. Show that for each $x \in H$ , there is a unique $y \in K$ such that

$$
| | x - y | | = i n f _ { z \in K } | | x - z | |
$$
:::

::: {.solution}
Let $d=\inf_{z\in K}\norm{x-z}$. For $u,v\in K$ the parallelogram law and $\frac{u+v}2\in K$ give
$$\norm{u-v}^2=2\norm{u-x}^2+2\norm{v-x}^2-4\norm{\tfrac{u+v}2-x}^2\le2\norm{u-x}^2+2\norm{v-x}^2-4d^2.\tag{$*$}$$

<1>1. Some $y\in K$ has $\norm{x-y}=d$.

::: {.proof}
Choose $z_n\in K$ with $\norm{x-z_n}\to d$. By $(*)$, $\norm{z_n-z_m}^2\to2d^2+2d^2-4d^2=0$, so $(z_n)$ is Cauchy and converges to some $y\in H$, since $H$ is complete. Then $y\in K$ because $K$ is closed, and $\norm{x-y}=d$ by continuity of the norm.
:::

<1>2. Two such points are equal.

::: {.proof}
If $\norm{x-y_1}=\norm{x-y_2}=d$ with $y_1,y_2\in K$, then $(*)$ gives $\norm{y_1-y_2}^2\le0$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give existence and uniqueness.
:::
:::
