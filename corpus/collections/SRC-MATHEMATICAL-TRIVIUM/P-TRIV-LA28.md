---
schema: qual/card@1
id: P-TRIV-LA28
kind: problem
title: Orthonormal basis adapted to two vectors in $\mathbb{R}^2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 28, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the vectors $\vec { a } _ { 1 }$ and $\vec { a } _ { 2 }$ in $\mathbb { R } ^ { 2 }$ with the lengths $| \vec { a } _ { 1 } | = 2 , | \vec { a } _ { 2 } | = 6$ and the angle between them $\phi = \frac { \pi } { 6 }$ . Construct the orthonormal basis $\vec { e } _ { 1 } , \vec { e } _ { 2 }$ such that $\vec { e } _ { 1 } | | \vec { a } _ { 1 }$ , and write the components of $\vec { a } _ { 1 } , \vec { a } _ { 2 }$ in this basis.
:::

::: {.solution}
<1>1. Define
$$
e_1=\frac{a_1}{\|a_1\|}
=
\frac{a_1}{2}.
$$
Then $e_1$ is a unit vector parallel to $a_1$.

::: {.proof}
Since $\|a_1\|=2$,
$$
\|e_1\|
=
\frac{\|a_1\|}{2}
=1.
$$
It is plainly a scalar multiple of $a_1$.
:::

<1>2. Choose a unit vector $e_2$ perpendicular to $e_1$ and oriented so that
$$
a_2\cdot e_2>0.
$$
Then
$$
\{e_1,e_2\}
$$
is an orthonormal basis of $\mathbb R^2$.

::: {.proof}
In $\mathbb R^2$, the orthogonal complement of the line spanned by $e_1$ is
one-dimensional and has exactly two unit vectors. Choose the sign for which
the $e_2$-component of $a_2$ is positive.
:::

<1>3. In this basis,
$$
\boxed{[a_1]_{(e_1,e_2)}=(2,0)}.
$$

::: {.proof}
By step <1>1,
$$
a_1=2e_1.
$$
:::

<1>4. The $e_1$-component of $a_2$ is
$$
a_2\cdot e_1
=
6\cos\frac\pi6
=
3\sqrt3.
$$

::: {.proof}
The angle between $a_2$ and $e_1$ equals the angle between $a_2$ and $a_1$,
namely $\pi/6$, because $e_1$ is parallel to $a_1$.
:::

<1>5. The $e_2$-component of $a_2$ is
$$
a_2\cdot e_2
=
6\sin\frac\pi6
=3.
$$

::: {.proof}
In the oriented orthonormal basis, the decomposition of a vector of length
$6$ making angle $\pi/6$ with $e_1$ is
$$
6\cos\frac\pi6\,e_1
+
6\sin\frac\pi6\,e_2.
$$
The sign convention in step <1>2 makes the second coefficient positive.
:::

<1>6. Therefore
$$
\boxed{[a_2]_{(e_1,e_2)}=(3\sqrt3,3)}.
$$

::: {.proof}
Combine steps <1>4 and <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 construct the orthonormal basis, and steps <1>3 and <1>6
give the requested coordinates.
:::
:::
