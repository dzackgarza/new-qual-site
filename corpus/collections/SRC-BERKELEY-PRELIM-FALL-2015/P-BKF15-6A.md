---
schema: qual/card@1
id: P-BKF15-6A
kind: problem
title: Hyperplane sections of the ellipsoid $2x^2+3y^2+4z^2+5u^2=1$ that are spheres
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: every
    3-plane meets both coordinate 2-planes nontrivially, producing section
    points on opposite sides of the radius 1/2 threshold.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the dimension estimates, the norm bounds on both coordinate
    ellipses, and that a centrally symmetric sphere in a subspace must be
    centered at the origin.
---

::: {.problem}
In the Euclidean space $\mathbb { R } ^ { 4 }$ , consider the “hyper-ellipsoid” $2 x ^ { 2 } + 3 y ^ { 2 } + 4 z ^ { 2 } + 5 u ^ { 2 } = 1$ . Does there exist a 3-dimensional subspace passing through the origin which intersects the ellipsoid in a sphere?
:::

::: {.solution}
Let
$$
E\coloneqq
\left\{
(x,y,z,u)\in\RR^4:
2x^2+3y^2+4z^2+5u^2=1
\right\}.
$$
Let $W\subset\RR^4$ be any $3$-dimensional linear subspace.

::: pf

::: {.pf-step #s1}

The intersection
$$
W\cap\{x=y=0\}
$$
contains a nonzero vector.

::: pf-proof

The coordinate plane
$$
H_+\coloneqq\{(0,0,z,u):z,u\in\RR\}
$$
has dimension $2$. Therefore
$$
\dim(W\cap H_+)
\ge
\dim W+\dim H_+-4
=
3+2-4
=
1.
$$
Hence the intersection contains a nonzero vector.

:::

:::

::: {.pf-step #s2}

There is a point
$$
p\in E\cap W\cap\{x=y=0\}
$$
with
$$
\norm{p}\le\frac12.
$$

::: pf-proof

Choose a nonzero vector in the intersection from step [](#s1){.pf-ref} and scale it
by a positive real number until
$$
4z^2+5u^2=1.
$$
This produces a point $p\in E\cap W$ with $x=y=0$. For such a point,
$$
1
=
4z^2+5u^2
\ge
4(z^2+u^2)
=
4\norm{p}^2.
$$
Thus $\norm{p}\le1/2$.

:::

:::

::: {.pf-step #s3}

The intersection
$$
W\cap\{z=u=0\}
$$
contains a nonzero vector.

::: pf-proof

The coordinate plane
$$
H_-\coloneqq\{(x,y,0,0):x,y\in\RR\}
$$
also has dimension $2$. As in step [](#s1){.pf-ref},
$$
\dim(W\cap H_-)
\ge
3+2-4
=
1.
$$

:::

:::

::: {.pf-step #s4}

There is a point
$$
q\in E\cap W\cap\{z=u=0\}
$$
with
$$
\norm{q}\ge\frac1{\sqrt3}>\frac12.
$$

::: pf-proof

Choose a nonzero vector in the intersection from step [](#s3){.pf-ref} and scale it
to satisfy
$$
2x^2+3y^2=1.
$$
Then $q=(x,y,0,0)$ lies in $E\cap W$. Moreover,
$$
1
=
2x^2+3y^2
\le
3(x^2+y^2)
=
3\norm{q}^2.
$$
Hence
$$
\norm{q}\ge\frac1{\sqrt3}>\frac12.
$$

:::

:::

::: {.pf-step #s5}

If $E\cap W$ were a sphere in $W$, that sphere would be centered
at the origin.

::: pf-proof

The set $E\cap W$ is centrally symmetric:
$$
v\in E\cap W
\quad\Longrightarrow\quad
-v\in E\cap W,
$$
because both $E$ and the linear subspace $W$ are invariant under
$v\mapsto-v$.

If a sphere with center $c\in W$ is invariant under $v\mapsto-v$, then
its image under this map is the same sphere but with center $-c$.
A Euclidean sphere has a unique center, so $c=-c$, hence $c=0$.

:::

:::

::: {.pf-step #s6}

No $3$-dimensional subspace through the origin cuts $E$ in a
sphere.

::: pf-proof

If $E\cap W$ were a sphere, step [](#s5){.pf-ref} would make it a sphere centered
at $0$, so every point of the section would have the same Euclidean
norm. But steps [](#s2){.pf-ref} and [](#s4){.pf-ref} give points $p,q\in E\cap W$ with
$$
\norm{p}\le\frac12
<
\frac1{\sqrt3}
\le
\norm{q}.
$$
Thus the section contains points at different distances from the
origin, a contradiction.

:::

:::

::: {.pf-step #s7}

Therefore the answer is
$$
\boxed{\text{no}}.
$$

::: pf-proof

The subspace $W$ was arbitrary, and step [](#s6){.pf-ref} excludes every
$3$-dimensional linear subspace.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} answers the question.

:::

:::

:::
