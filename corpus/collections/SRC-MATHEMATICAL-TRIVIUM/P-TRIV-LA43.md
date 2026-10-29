---
schema: qual/card@1
id: P-TRIV-LA43
kind: problem
title: Relative position of two lines given as intersections of planes
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 43, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider two lines formed by intersection of the planes,

$$
l _ { 1 } = \left\{ \begin{array} { l } { 3 x + 2 y + 5 z - 1 = 0 } \\ { - x + 2 y + 3 z - 1 = 0 } \end{array} \right. , l _ { 2 } = \left\{ \begin{array} { l } { 4 x - 6 y + 7 z + 2 = 0 } \\ { 5 x + 3 y - 8 z - 3 = 0 . } \end{array} \right.\tag{10}
$$

Find out if these lines are

(a) parallel to each other,

(b) crossing each other at some point.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A direction vector for $l_1$ is the cross product of the normals of its
two defining planes:
$$
d_1
=
(3,2,5)\times(-1,2,3)
=
(-4,-14,8).
$$


::: pf-proof

The direction of the intersection line is perpendicular to both plane normals.
Computing the cross product gives the displayed vector.

:::

:::

::: {.pf-step #s1-2}

A direction vector for $l_2$ is
$$
d_2
=
(4,-6,7)\times(5,3,-8)
=
(27,67,42).
$$


::: pf-proof

As in step [](#s1-1){.pf-ref}, take the cross product of the two plane normals.

:::

:::

::: {.pf-step #s1-3}

The lines are not parallel.


::: pf-proof

The direction vectors from steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} are not scalar multiples. For
example,
$$
\frac{27}{-4}
\neq
\frac{67}{-14}.
$$
Hence the directions are distinct.

:::

:::

::: pf-step

A parametrization of $l_1$ is
$$
\boxed{
l_1(t)
=
\left(
-\frac t2,
\frac12-\frac{7t}{4},
t
\right),
\qquad
t\in\RR.
}
$$


::: pf-proof

Set $z=t$. The two equations for $l_1$ are
$$
3x+2y+5t=1,
$$
$$
-x+2y+3t=1.
$$
Subtracting gives
$$
4x+2t=0,
$$
so $x=-t/2$. Substituting back gives
$$
y=\frac12-\frac{7t}{4}.
$$

:::

:::

::: pf-step

A parametrization of $l_2$ is
$$
\boxed{
l_2(u)
=
\left(
\frac{9u}{14}+\frac27,
\frac{67u}{42}+\frac{11}{21},
u
\right),
\qquad
u\in\RR.
}
$$


::: pf-proof

Set $z=u$ and solve
$$
4x-6y+7u=-2,
$$
$$
5x+3y-8u=3.
$$
Elimination gives the displayed formulas for $x$ and $y$.

:::

:::

::: {.pf-step #s1-6}

If the two lines intersect, then their parameters must satisfy
$$
t=u.
$$


::: pf-proof

The third coordinate of $l_1(t)$ is $t$, while that of $l_2(u)$ is $u$.
Equality of the two points therefore forces $t=u$.

:::

:::

::: {.pf-step #s1-7}

Equality of the first coordinates then forces
$$
t=-\frac14.
$$


::: pf-proof

Using step [](#s1-6){.pf-ref}, solve
$$
-\frac t2
=
\frac{9t}{14}+\frac27.
$$
Multiplying by $14$ gives
$$
-7t=9t+4,
$$
so
$$
t=-\frac14.
$$

:::

:::

::: {.pf-step #s1-8}

At $t=u=-1/4$, the two $y$-coordinates are different:
$$
\frac12-\frac{7(-1/4)}4
=
\frac{15}{16},
$$
while
$$
\frac{67(-1/4)}{42}+\frac{11}{21}
=
\frac18.
$$


::: pf-proof

Direct substitution gives the two values.

:::

:::

::: {.pf-step #s1-9}

Therefore the two lines do not intersect.


::: pf-proof

Any intersection point would have to satisfy steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}, but step
[](#s1-8){.pf-ref} shows the resulting points are distinct.

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\text{$l_1$ and $l_2$ are neither parallel nor intersecting; they are skew.}
}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} rules out parallelism and step [](#s1-9){.pf-ref} rules out intersection.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} answers parts (a) and (b).

:::

:::

:::
