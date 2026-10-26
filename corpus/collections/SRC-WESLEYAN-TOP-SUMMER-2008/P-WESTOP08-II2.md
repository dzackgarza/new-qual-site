---
schema: qual/card@1
id: P-WESTOP08-II2
kind: problem
title: Fundamental groups, universal covers, and simplicial homology of standard spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Determine the fundamental group of each space:
   - $S^1$;
   - the torus;
   - the infinite cylinder $S^1\times\mathbb R$;
   - $S^1\cup(\mathbb R\times\{0\})\subset\mathbb R^2$;
   - $\mathbb R^2\setminus(\mathbb R\times\{0\})$.
2. Find the universal covering space of each:
   - $S^1$;
   - $S^2$;
   - $\mathbb{RP}^2$;
   - the torus.
3. Compute the simplicial homology groups of each:
   - $S^1$;
   - $S^2$;
   - $\mathbb{RP}^2$.
:::

All homology groups below have integral coefficients.

::: pf

::: pf-step

One has
\[
\boxed{
\pi_1(S^1)\cong\mathbb Z.
}
\]


::: pf-proof

The exponential covering
\[
p:\mathbb R\to S^1,
\qquad
p(t)=e^{2\pi i t},
\]
has simply connected total space and deck group
\[
t\mapsto t+n,
\qquad
n\in\mathbb Z.
\]
Hence
\[
\pi_1(S^1)\cong\mathbb Z.
\]

:::

:::

::: pf-step

For the torus
\[
T^2=S^1\times S^1,
\]
\[
\boxed{
\pi_1(T^2)\cong\mathbb Z^2.
}
\]


::: pf-proof

The fundamental group preserves products:
\[
\pi_1(S^1\times S^1)
\cong
\pi_1(S^1)\times\pi_1(S^1)
\cong
\mathbb Z\times\mathbb Z.
\]

:::

:::

::: pf-step

For the infinite cylinder
\[
S^1\times\mathbb R,
\]
\[
\boxed{
\pi_1(S^1\times\mathbb R)
\cong
\mathbb Z.
}
\]


::: pf-proof

The factor
\[
\mathbb R
\]
is contractible, so projection onto the first factor is a homotopy
equivalence
\[
S^1\times\mathbb R
\simeq
S^1.
\]
Apply step <1>1.

:::

:::

::: pf-step

Let
\[
X
\coloneqq
S^1\cup(\mathbb R\times\{0\})
\subseteq
\mathbb R^2,
\]
where $S^1$ is the unit circle.
Then
\[
\boxed{
\pi_1(X)\cong F_2.
}
\]


::: pf-proof

The $x$-axis meets the unit circle at
\[
(-1,0)
\qquad\text{and}\qquad
(1,0).
\]
The two unbounded rays
\[
(-\infty,-1]
\quad\text{and}\quad
[1,\infty)
\]
are contractible trees attached at single points, so collapsing them gives
a deformation retract onto the graph consisting of:

- the line segment from $(-1,0)$ to $(1,0)$;
- the upper semicircle;
- the lower semicircle.

This is the theta graph: two vertices joined by three edges.
A connected finite graph has free fundamental group of rank
\[
E-V+1.
\]
Here
\[
E=3,
\qquad
V=2,
\]
so the rank is
\[
3-2+1=2.
\]
Hence
\[
\pi_1(X)\cong F_2.
\]

:::

:::

::: pf-step

The space
\[
\mathbb R^2\setminus(\mathbb R\times\{0\})
\]
has two path components, and the fundamental group of either component is
trivial.


::: pf-proof

The complement of the $x$-axis is
\[
\{(x,y):y>0\}
\sqcup
\{(x,y):y<0\}.
\]
Each component is an open half-plane and is convex, hence contractible.
Therefore, for a basepoint chosen in either component,
\[
\boxed{
\pi_1=0.
}
\]
The whole space is disconnected, so there is no single basepoint-independent
fundamental group for the union.

:::

:::

::: pf-step

A universal covering of $S^1$ is
\[
\boxed{
\mathbb R\xrightarrow{,t\mapsto e^{2\pi i t},}S^1.
}
\]


::: pf-proof

The map is a covering and
\[
\mathbb R
\]
is simply connected.

:::

:::

::: pf-step

A universal covering of $S^2$ is the identity covering
\[
\boxed{
S^2\xrightarrow{\operatorname{id}}S^2.
}
\]


::: pf-proof

The sphere
\[
S^2
\]
is simply connected, so it is already its own universal covering space.

:::

:::

::: pf-step

A universal covering of
\[
\mathbb{RP}^2
\]
is
\[
\boxed{
S^2\longrightarrow\mathbb{RP}^2,
\qquad
x\longmapsto[x].
}
\]


::: pf-proof

The quotient identifies antipodal points
\[
x\sim -x.
\]
This gives a two-sheeted covering.
Since
\[
S^2
\]
is simply connected, the covering is universal.

:::

:::

::: pf-step

A universal covering of the torus is
\[
\boxed{
\mathbb R^2
\longrightarrow
T^2,
\qquad
(s,t)
\longmapsto
\bigl(
e^{2\pi i s},
e^{2\pi i t}
\bigr).
}
\]


::: pf-proof

This is the product of the universal covering
\[
\mathbb R\to S^1
\]
with itself.
The space
\[
\mathbb R^2
\]
is simply connected.

:::

:::

::: pf-step

The simplicial homology of the circle is
\[
\boxed{
H_k(S^1)
\cong
\begin{cases}
\mathbb Z,&k=0,1,\\
0,&\text{otherwise}.
\end{cases}
}
\]


::: pf-proof

Using a simplicial triangulation of $S^1$, its simplicial homology agrees
with its cellular homology.
The standard CW model has one $0$-cell and one $1$-cell with zero boundary,
so the chain complex is
\[
0
\to
\mathbb Z
\xrightarrow{0}
\mathbb Z
\to
0.
\]
The displayed groups follow.

:::

:::

::: pf-step

The simplicial homology of the sphere is
\[
\boxed{
H_k(S^2)
\cong
\begin{cases}
\mathbb Z,&k=0,2,\\
0,&\text{otherwise}.
\end{cases}
}
\]


::: pf-proof

Any triangulation of $S^2$ computes the same homology as the standard CW
structure with one $0$-cell and one $2$-cell.
The cellular differential is zero, giving one copy of
\[
\mathbb Z
\]
in degrees $0$ and $2$ and zero elsewhere.

:::

:::

::: pf-step

The simplicial homology of the projective plane is
\[
\boxed{
H_k(\mathbb{RP}^2)
\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z/2,&k=1,\\
0,&k\ge2.
\end{cases}
}
\]


::: pf-proof

The standard CW structure on
\[
\mathbb{RP}^2
\]
has one cell in each dimension
\[
0,1,2.
\]
Its cellular chain complex is
\[
0
\longrightarrow
\mathbb Z
\xrightarrow{\times2}
\mathbb Z
\xrightarrow{0}
\mathbb Z
\longrightarrow
0.
\]
Hence
\[
H_2=0,
\]
\[
H_1
=
\mathbb Z/2,
\]
and
\[
H_0
=
\mathbb Z.
\]

Since simplicial and cellular homology agree with singular homology for
triangulable spaces, these are also the simplicial homology groups.

:::

:::

::: pf-qed

Steps <1>1--<1>5 compute the requested fundamental groups,
steps <1>6--<1>9 identify the universal covers, and
steps <1>10--<1>12 compute the simplicial homology groups.

:::

:::
