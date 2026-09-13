---
schema: qual/card@1
id: E-PER08-1.5
kind: problem
title: Complements of finitely many points as wedge sums of spheres
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 1.5 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the one-dimensional component count and the higher-dimensional punctured-ball spine construction.
---

::: {.problem}
Let $\{X_\alpha\}_{\alpha\in A}$ be spaces with chosen basepoints $x_\alpha\in X_\alpha$.
Define the wedge sum $\bigvee_{\alpha\in A}X_\alpha$ as the quotient of the disjoint union $\coprod_\alpha X_\alpha$ by the relation $x_\alpha\sim x_\beta$ for all $\alpha,\beta\in A$.

Show carefully that, for $n\ge 1$, the complement of $p$ distinct points in $\mathbb R^n$ is homotopy equivalent to the wedge sum of $p$ copies of $S^{n-1}$.
:::

::: {.solution}
Let
\[
A=\{a_1,\dots,a_p\}\subset\mathbb R^n,
\qquad
X=\mathbb R^n\setminus A.
\]

<1>1. The assertion holds for $n=1$.
::: {.proof}
After ordering the punctures as
\[
a_1<a_2<\cdots<a_p,
\]
the complement $\mathbb R\setminus A$ is the disjoint union of the $p+1$ open intervals and rays
\[
(-\infty,a_1),\ (a_1,a_2),\dots,\ (a_{p-1},a_p),\ (a_p,\infty).
\]
Each component is contractible, so $X$ is homotopy equivalent to a discrete space of $p+1$ points.

Now $S^0$ is a two-point space. Wedge together $p$ copies of $S^0$ by identifying one chosen point from each copy. The result consists of the common basepoint together with one remaining point from each copy, hence exactly $p+1$ discrete points. Therefore
\[
\mathbb R\setminus A\simeq\bigvee_{i=1}^p S^0.
\]
:::

Assume henceforth that $n\ge2$.

<1>2. Replace the punctures by small spherical boundary components and truncate infinity.
::: {.proof}
Choose pairwise disjoint closed balls
\[
B_i=\overline B(a_i,\varepsilon_i),
\qquad 1\le i\le p,
\]
and choose a large closed ball $B_0$ whose interior contains all the $B_i$.
Set
\[
M=B_0\setminus\bigcup_{i=1}^p\operatorname{int}(B_i).
\]

There is a strong deformation retraction $X\to M$. On each punctured ball
\[
B_i\setminus\{a_i\}
\]
push points radially away from $a_i$ onto $\partial B_i$. Outside $B_0$, push points radially inward onto $\partial B_0$. Fix every point of $M$. Since these regions are disjoint and each radial homotopy fixes the relevant boundary sphere, the homotopies glue continuously. Hence
\[
X\simeq M.
\]
:::

<1>3. The punctured ball $M$ has a spine consisting of the inner spheres joined by a tree.
::: {.proof}
Choose points $q_i\in\partial B_i$. Because $n\ge2$ and $M$ is connected, one can choose embedded arcs in $M$ joining the $q_i$ so that their union is a finite tree $T$ and
\[
T\cap\partial B_i=\{q_i\}
\]
for every $i$. In dimension $2$ choose noncrossing arcs successively; in dimensions at least $3$, small perturbations make finitely many arcs disjoint except at prescribed endpoints.

Let
\[
K=T\cup\bigcup_{i=1}^p\partial B_i.
\]
A closed ball with finitely many disjoint open balls removed is a regular neighborhood of this spine: thicken each sphere $\partial B_i$ by a collar and thicken the edges of $T$ by mutually disjoint tubes; the remaining complementary pieces are collars of the resulting outer boundary and collapse onto the tube-and-sphere neighborhood. Collapsing each collar in its normal interval and each tube in its normal disk gives a deformation retraction
\[
M\simeq K.
\]
Equivalently, this is the usual spine of an $n$-ball with $p$ holes.
:::

<1>4. The spine $K$ is homotopy equivalent to a wedge of $p$ copies of $S^{n-1}$.
::: {.proof}
The tree $T$ is a contractible subcomplex of the finite CW complex $K$. Collapsing a contractible subcomplex that is included as a CW subcomplex is a homotopy equivalence: collapse the edges of the tree one at a time, starting with terminal edges, using the homotopy extension property for the adjacent cells.

After all of $T$ is collapsed to one point, each sphere $\partial B_i\cong S^{n-1}$ meets all the others only at that common point. Thus
\[
K/T\cong\bigvee_{i=1}^p S^{n-1},
\]
and hence
\[
K\simeq\bigvee_{i=1}^p S^{n-1}.
\]
:::

Combining <1>2--<1>4 gives, for $n\ge2$,
\[
\mathbb R^n\setminus\{a_1,\dots,a_p\}
\simeq M
\simeq K
\simeq\bigvee_{i=1}^p S^{n-1}.
\]
Together with <1>1, this proves the result for every $n\ge1$.
:::
