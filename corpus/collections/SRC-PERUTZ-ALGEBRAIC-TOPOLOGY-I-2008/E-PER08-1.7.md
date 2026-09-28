---
schema: qual/card@1
id: E-PER08-1.7
kind: problem
title: Direct proof that the 2-sphere is simply connected
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 1.7 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the piecewise-geodesic approximation rel basepoint, existence of a missed point, and contraction after stereographic projection.
---

::: {.problem}
Prove directly that the 2-sphere
\[
S^2=\{x\in\mathbb R^3:|x|=1\}
\]
is simply connected.
:::

::: {.solution}
We prove that $S^2$ is path-connected and that every based loop is null-homotopic.

<1>1. The sphere $S^2$ is path-connected.
::: {.proof}
If $x,y\in S^2$ are not antipodal, the normalized straight-line path
\[
\gamma(t)=\frac{(1-t)x+ty}{\lVert(1-t)x+ty\rVert}
\]
joins $x$ to $y$. If $y=-x$, choose $z\in S^2$ with $z\neq\pm x$ and concatenate a path from $x$ to $z$ with one from $z$ to $-x$.
:::

<1>2. Every loop in $S^2$ is based-homotopic to a finite piecewise-geodesic loop.
::: {.proof}
Let
\[
f:(I,\partial I)\to(S^2,x_0)
\]
be a loop. Cover $S^2$ by open spherical caps of angular radius strictly less than $\pi/2$. Each such cap is geodesically convex: any two of its points are joined by a unique short great-circle arc lying in the cap.

By compactness of $f(I)$ and the Lebesgue-number lemma applied to the pullback cover of $I$, there is a partition
\[
0=t_0<t_1<\cdots<t_m=1
\]
such that for each $j$, the image
\[
f([t_{j-1},t_j])
\]
lies in one geodesically convex cap $U_j$.

Inside $U_j$, replace the path $f|_{[t_{j-1},t_j]}$ by the unique short geodesic segment joining the same two endpoints. To see that this replacement is a homotopy rel endpoints, use central projection from the cap to a convex disk in the tangent plane: there the original path and the straight segment are joined by the ordinary linear homotopy, which fixes the endpoints; projecting back gives the desired homotopy in $U_j$.

The endpoint-fixing homotopies on adjacent subintervals agree at the subdivision points, so they glue to a based homotopy of $f$ to a loop $g$ which is a finite concatenation of great-circle arcs.
:::

<1>3. The piecewise-geodesic loop $g$ misses some point of $S^2$.
::: {.proof}
Each geodesic segment in $g(I)$ lies in a great circle, and each great circle is the intersection of $S^2$ with a two-dimensional linear subspace of $\mathbb R^3$. Since $g$ has only finitely many segments, there are finitely many proper linear subspaces
\[
P_1,\dots,P_m\subsetneq\mathbb R^3
\]
whose intersections with $S^2$ contain $g(I)$.

A finite union of proper linear subspaces cannot equal $\mathbb R^3$. Hence choose a nonzero vector
\[
v\notin P_1\cup\cdots\cup P_m
\]
and set
\[
q=\frac{v}{\lVert v\rVert}\in S^2.
\]
Then $q\notin g(I)$.
:::

<1>4. The loop $g$ is null-homotopic rel basepoint.
::: {.proof}
Stereographic projection from $q$ is a homeomorphism
\[
\sigma:S^2\setminus\{q\}\xrightarrow{\cong}\mathbb R^2.
\]
By <1>3, $g(I)\subset S^2\setminus\{q\}$. Let
\[
p=\sigma(x_0).
\]
The loop $\sigma\circ g$ contracts linearly to $p$ by
\[
H(t,s)=(1-t)\sigma(g(s))+tp.
\]
Because $g(0)=g(1)=x_0$, this homotopy fixes the loop basepoint:
\[
H(t,0)=H(t,1)=p.
\]
Composing with $\sigma^{-1}$ gives a based null-homotopy of $g$ in $S^2\setminus\{q\}$, hence in $S^2$.
:::

By <1>2, the original loop $f$ is based-homotopic to $g$, and by <1>4, $g$ is null-homotopic. Thus every element of $\pi_1(S^2,x_0)$ is trivial. Together with path-connectedness from <1>1,
\[
\pi_1(S^2,x_0)=0,
\]
so $S^2$ is simply connected.
:::
