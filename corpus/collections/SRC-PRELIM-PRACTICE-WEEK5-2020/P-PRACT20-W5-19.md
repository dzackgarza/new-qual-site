---
schema: qual/card@1
id: P-PRACT20-W5-19
kind: problem
title: The region $\abs{z-a}<\abs{z-b}$ in $\CC$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 19).
---

::: {.problem}
For $a, b \in \CC$, sketch the set of points $z \in \CC$ such that $\abs{\frac{z - a}{z - b}} < 1$.
:::

::: {.solution}

::: pf

::: pf-step

Suppose $a\ne b$. For every $z\ne b$,
$$
\abs{\frac{z-a}{z-b}}<1
\quad\Longleftrightarrow\quad
\abs{z-a}<\abs{z-b}.
$$


::: pf-proof

Since $z\ne b$, the positive number $\abs{z-b}$ may be multiplied across the
inequality.

:::

:::

::: pf-step

The boundary
$$
\abs{z-a}=\abs{z-b}
$$
is the perpendicular bisector of the line segment joining $a$ and $b$.


::: pf-proof

The equation says exactly that $z$ is equidistant from the two points $a$
and $b$. In the Euclidean plane, the locus of points equidistant from two
distinct points is their perpendicular bisector.

:::

:::

::: {.pf-step #s1-3}

For $a\ne b$, the desired region is the open half-plane bounded by
that perpendicular bisector and containing $a$:
$$
\boxed{\{z\in\CC:\abs{z-a}<\abs{z-b}\}}.
$$


::: pf-proof

The perpendicular bisector divides the plane into two open half-planes. On
one side points are closer to $a$, and on the other they are closer to $b$.
The point $a$ itself satisfies
$$
\abs{a-a}=0<\abs{a-b},
$$
so the desired side is the one containing $a$.

Equivalently, squaring and expanding gives the linear inequality
$$
\operatorname{Re}\!\bigl((\overline b-\overline a)z\bigr)
<
\frac{\abs{b}^2-\abs{a}^2}{2}.
$$

:::

:::

::: {.pf-step #s1-4}

If $a=b$, the solution set is empty.


::: pf-proof

For $z\ne a=b$,
$$
\abs{\frac{z-a}{z-b}}=1,
$$
so the strict inequality fails. At $z=b$ the quotient is undefined.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} describe the set in all cases and determine its sketch.

:::

:::

:::
