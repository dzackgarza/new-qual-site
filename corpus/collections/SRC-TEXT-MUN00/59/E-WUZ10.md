---
schema: qual/card@1
id: E-WUZ10
kind: problem
title: Two spheres touching at a point
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 59 Exercise 1, printed p. 370,
    with Theorem 59.1 or Corollary 59.2. The card cuts the wedge of two spheres along a point of each sphere, checks that the two open pieces and their intersection are simply connected and the intersection path connected, and concludes $\pi_1=1$. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §59 Exercise 1, his p. 24, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. The solution is that proof transcribed: the two open
    pieces cut off by the planes $x=-1$ and $x=1$, each deformation retracting onto the sphere it
    keeps, and Corollary 59.2 applied to their intersection. The source is correct and needed no
    repair. Checked against the book: the exercise and its bracket on printed p. 370, Theorem 59.1
    and Corollary 59.2 on printed p. 369, and Theorem 59.3 on printed p. 369 for the simple
    connectedness of $S^2$. The card states what the source leaves to the reader, that the
    intersection is path connected, by joining each of its points to the common point inside its own
    sphere. Not claimed: that the source proves the deformation retraction by an explicit formula
    -- it describes the collapse along the meridians, and the card does the same.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Step 2 corrected: it called the part of the first sphere in $U$ the *closed* right hemisphere
    $\{x\ge-1\}\cap S^2_-$, but $U=X\cap\{x>-1\}$, so the great circle $x=-1$ is not in $U$ and the
    part is the open hemisphere $\{x>-1\}\cap S^2_-$; the same card says so one step earlier, where
    $U\cap V$ is described as the open hemisphere together with $\mathbf 0$. With the open
    hemisphere the sliding is also justified: the segment from a point of the open hemisphere to
    $\mathbf 0$ stays in $x>-1$ and avoids the centre of $S^2_-$, so its projection to the sphere is
    a path in the hemisphere, continuous in the pair and collapsing to $\mathbf 0$ at the end. The
    conclusion is unchanged. Checked against the book: the exercise on printed p. 370, Corollary
    59.2 and Theorem 59.3 on printed p. 369.
---

::: {.exercise}

Let $X$ be the union of two copies of $S^2$ having a single point in common.
What is the fundamental group of $X$?
Prove that your answer is correct.
[Be careful! The union of two simply connected spaces having a point in common is not necessarily simply connected. See [S], p. 59.]
:::

::: {.solution}
The exercise is §59 Exercise 1, with the warning in its bracket
that a union of two simply connected spaces with a point in common need not be
simply connected. The proof is transcribed from Pearse, *Topology (2nd ed.) —
James R. Munkres*, solutions, Cornell 2005, §59 Exercise 1, his p. 24, read in
`tmp/sources/cornell-erin-munkres.md`: it exhibits $X$ as the union of two open
subspaces with simply connected parts and path connected intersection, so that
Corollary 59.2  applies. The bracket's warning is answered by the
openness and by the intersection being contractible, not merely a point.

Place the two spheres in $\RR^3$ as the spheres of radius $1$ about $(-1,0,0)$
and $(1,0,0)$, so that they meet in the single point $\mathbf 0$ and
$X\subseteq[-2,2]\times\RR^2$; put $x_0=\mathbf 0$ and
$$
U=X\cap\bigl((-1,\infty)\times\RR^2\bigr),\qquad
V=X\cap\bigl((-\infty,1)\times\RR^2\bigr).
$$

::: pf

::: {.pf-step #cover}
$U$ and $V$ are open in $X$, $U\cup V=X$, and $U\cap V$ is path connected and
contains $x_0=\mathbf 0$.

::: pf-proof
Each of $(-1,\infty)\times\RR^2$ and $(-\infty,1)\times\RR^2$ is open in
$\RR^3$, so $U$ and $V$ are open in $X$. Every point of $X$ has first coordinate
in $[-2,2]$, and for such a coordinate at least one of $x>-1$ and $x<1$ holds, so
$U\cup V=X$.

The points of $U\cap V$ are the points of $X$ with $-1<x<1$. On the first sphere
those are its open right hemisphere together with $\mathbf 0$, a path connected
set: the open hemisphere is path connected, and each of its meridian arcs from
$\mathbf 0$ to the circle $\theset{x=-1}$ has $\mathbf 0$ as an endpoint, so
$\mathbf 0$ can be joined to any of its points inside that set. On the second
sphere the points with $-1<x<1$ are its open left hemisphere together with
$\mathbf 0$, path connected for the same reason. The two sets meet in
$\mathbf 0$, so their union $U\cap V$ is path connected, and it contains $x_0$.
:::

:::

::: {.pf-step #parts}
$U$ and $V$ are simply connected.

::: pf-proof
Consider $U$. The part of the first sphere in $U$ is its open right hemisphere
$H_+=\{x>-1\}\cap S^2_{-}$, the part cut off by the plane $x=-1$: the great
circle $x=-1$ of $S^2_{-}$ is not in $U$, because $U$ is defined by $x>-1$. The
meridians of $S^2_{-}$ from $\mathbf 0$ to $(-2,0,0)$ sweep out $H_+$, and
sliding each point of $H_+$ along its meridian towards $\mathbf 0$ gives a
deformation retraction of $U$ onto the second sphere
$S^2_+$, which is fixed throughout: for $p\in H_+$ the straight segment from $p$
to $\mathbf 0$ lies in the half space $x>-1$ and misses the centre
$c_-=(-1,0,0)$ of $S^2_-$, so projecting that segment to $S^2_-$ from $c_-$
gives a path in $H_+$ from $p$ to $\mathbf 0$, continuous in $(p,t)$ and equal to
$\mathbf 0$ for $t=1$. So $\pi_1(U)\cong\pi_1(S^2_+)$, which is
trivial by Theorem 59.3  with $n=2$. The same argument with the
roles exchanged gives that $V$ deformation retracts onto $S^2_{-}$ and
$\pi_1(V)$ is trivial.
:::

:::

::: {.pf-step}
$\boxed{\pi_1(X,x_0)\ \text{is trivial}}$.

::: pf-proof
By steps [](#cover){.pf-ref} and [](#parts){.pf-ref} the space $X$ is the union
of the open sets $U$ and $V$, which are simply connected, and $U\cap V$ is
nonempty and path connected, so Corollary 59.2  says that $X$ is
simply connected. Hence the fundamental group of $X$ is trivial, and since it is
trivial it is the same at every base point.
:::

:::

:::
:::
