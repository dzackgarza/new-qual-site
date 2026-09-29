---
schema: qual/card@1
id: P-BKF95-2
kind: problem
title: Boundary-length bound for neighborhoods of finite planar sets
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/Fall95_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Partitioned the r-neighborhood by Voronoi cells. Each exposed circle arc
    sweeps a radial sector inside its Voronoi piece, giving perimeter at most
    2/r times area; the whole neighborhood lies in the disk of radius 1+r.
---

::: {.problem}
Let $A$ be a finite subset of the unit disk in the plane, and let $N(A,r)$ be the set of points at distance at most $r$ from $A$, where $0<r<1$.
Show that the length of the boundary of $N(A,r)$ is at most
\[
\frac Cr
\]
for some constant $C$ independent of $A$.
:::

::: {.solution}
Write
$$
A=\{a_1,\ldots,a_m\}.
$$
For each $j$, let
$$
V_j
\coloneqq
\left\{
x\in\RR^2:
\norm{x-a_j}\leq\norm{x-a_\ell}
\text{ for every }\ell
\right\}
$$
be the Voronoi cell of $a_j$.

::: pf

::: {.pf-step #s1}

Each $V_j$ is convex and contains $a_j$.

::: pf-proof

For fixed $j$ and $\ell$, the inequality
$$
\norm{x-a_j}^2\leq\norm{x-a_\ell}^2
$$
expands to a linear inequality in $x$, so it defines a closed half-plane
containing $a_j$. The cell $V_j$ is the intersection of these half-planes.
Hence it is convex and contains $a_j$.

:::

:::

::: {.pf-step #s2}

Up to sets of planar area zero, the sets
$$
P_j\coloneqq V_j\cap\overline{B}(a_j,r)
$$
partition $N(A,r)$.

::: pf-proof

The Voronoi cells cover the plane, and the interiors of distinct cells are
disjoint; their overlaps lie in finitely many perpendicular-bisector lines,
which have planar area zero.

If $x\in N(A,r)$, choose a nearest point $a_j\in A$. Then
$$
x\in V_j
\qquad\text{and}\qquad
\norm{x-a_j}\leq r,
$$
so $x\in P_j$. Conversely, every point of $P_j$ is within distance $r$ of
$a_j$ and hence belongs to $N(A,r)$. Thus the $P_j$ partition
$N(A,r)$ up to their shared boundaries.

:::

:::

::: {.pf-step #s3}

Let
$$
\Gamma_j
\coloneqq
\partial B(a_j,r)\cap V_j.
$$
Then
$$
\operatorname{length}(\Gamma_j)
\leq
\frac{2}{r}\operatorname{area}(P_j).
$$

::: pf-proof

Let $S_j\subseteq[0,2\pi)$ be the set of angles $\theta$ for which
$$
a_j+r(\cos\theta,\sin\theta)\in V_j.
$$
Then
$$
\operatorname{length}(\Gamma_j)
=
r\,\operatorname{length}(S_j),
$$
where the second length is angular measure.

By step [](#s1){.pf-ref}, $V_j$ is convex and contains $a_j$. Hence whenever
$\theta\in S_j$, the entire radial segment
$$
\left\{
a_j+\rho(\cos\theta,\sin\theta):
0\leq\rho\leq r
\right\}
$$
lies in $V_j$. Therefore the sector
$$
Q_j
\coloneqq
\left\{
a_j+\rho(\cos\theta,\sin\theta):
\theta\in S_j,\ 0\leq\rho\leq r
\right\}
$$
is contained in $P_j$. Its area is
$$
\operatorname{area}(Q_j)
=
\frac{r^2}{2}\operatorname{length}(S_j)
=
\frac r2\operatorname{length}(\Gamma_j).
$$
Since $Q_j\subseteq P_j$, the claimed inequality follows.

:::

:::

::: {.pf-step #s4}

The boundary of $N(A,r)$ satisfies
$$
\operatorname{length}\partial N(A,r)
\leq
\sum_{j=1}^m\operatorname{length}(\Gamma_j).
$$

::: pf-proof

The set $N(A,r)$ is the finite union
$$
\bigcup_{j=1}^m\overline B(a_j,r).
$$
Every boundary point therefore lies on the boundary circle of at least one
disk. If $x\in\partial N(A,r)$ lies on
$\partial B(a_j,r)$, then no center is closer to $x$ than $a_j$; otherwise
$x$ would lie in the interior of another radius-$r$ disk and hence in the
interior of $N(A,r)$. Thus
$$
x\in V_j
$$
and so $x\in\Gamma_j$. Hence
$$
\partial N(A,r)
\subseteq
\bigcup_{j=1}^m\Gamma_j.
$$
Taking lengths gives the inequality.

:::

:::

::: {.pf-step #s5}

One has
$$
\operatorname{length}\partial N(A,r)
\leq
\frac{2}{r}\operatorname{area}N(A,r).
$$

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
$$
\operatorname{length}\partial N(A,r)
\leq
\frac2r
\sum_{j=1}^m\operatorname{area}(P_j).
$$
Step [](#s2){.pf-ref} gives
$$
\sum_{j=1}^m\operatorname{area}(P_j)
=
\operatorname{area}N(A,r).
$$
Combine the two formulas.

:::

:::

::: {.pf-step #s6}

The neighborhood $N(A,r)$ is contained in the disk of radius
$1+r<2$ centered at the origin.

::: pf-proof

Every $a\in A$ lies in the unit disk. If $x\in N(A,r)$, then for some
$a\in A$,
$$
\norm{x-a}\leq r.
$$
Thus
$$
\norm{x}
\leq
\norm{a}+\norm{x-a}
<
1+r
<
2.
$$

:::

:::

::: {.pf-step #s7}

One has
$$
\boxed{
\operatorname{length}\partial N(A,r)
\leq
\frac{8\pi}{r}
}.
$$

::: pf-proof

Step [](#s6){.pf-ref} gives
$$
\operatorname{area}N(A,r)
\leq
4\pi.
$$
Insert this in step [](#s5){.pf-ref}:
$$
\operatorname{length}\partial N(A,r)
\leq
\frac2r(4\pi)
=
\frac{8\pi}{r}.
$$
Thus one may take $C=8\pi$, independently of $A$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required uniform boundary-length bound.

:::

:::

:::
