---
schema: qual/card@1
id: E-HAT-1.2-20
kind: problem
title: Fundamental group of union of tangent circles equals that of infinite wedge, and spaces are homotopy equivalent but not homeomorphic
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Free Groups
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Built explicit homotopy-equivalence maps by uniformly collapsing a neighborhood of the common tangency point, then separated the spaces by first countability at the wedge point.
---

Let $X$ be the subspace of $\mathbb{R}^2$ that is the union of the circles $C_n$ of radius $n$ and center $(n, 0)$ for $n = 1, 2, \cdots$.
Show that $\pi_1(X)$ is the free group $*_n \pi_1(C_n)$, the same as for the infinite wedge sum $\bigvee_\infty S^1$.
Show that $X$ and $\bigvee_\infty S^1$ are in fact homotopy equivalent, but not homeomorphic.

::: {.solution}
Let $o=(0,0)$, the common tangency point of all the circles $C_n$, and let
\[
W=\bigvee_{n=1}^{\infty}S^1_n
\]
with the usual CW wedge topology.

<1>1. There is a continuous map
\[
f:W\to X
\]
whose restriction to $S^1_n$ is a homeomorphism onto $C_n$ taking the wedge point to $o$.
::: {.proof}
Choose such a based homeomorphism separately on each circle.
The CW wedge $W$ has the weak topology with respect to its circles, so a map out of $W$ is continuous when its restriction to every circle is continuous.
Thus the circlewise maps assemble to a continuous $f$.
:::

<1>2. There is a continuous map
\[
g:X\to W
\]
such that each restriction
\[
g|_{C_n}:C_n\to S^1_n
\]
has degree one.
::: {.proof}
Fix a small radius $\varepsilon>0$.
On each $C_n$, collapse the connected arc
\[
C_n\cap \overline{B_\varepsilon(o)}
\]
containing $o$ to the wedge point, and map the complementary arc monotonically once around $S^1_n$.
This gives a continuous based degree-one map on each $C_n$.

The definitions agree at the only common point $o$.
Moreover,
\[
g\bigl(X\cap B_\varepsilon(o)\bigr)
\]
is exactly the wedge point.
Hence $g$ is continuous at $o$, regardless of how small the prescribed neighborhoods of the wedge point are on the individual circles of $W$.

If $x\in X\setminus\{o\}$, then $x$ lies on a unique circle $C_n$ and has a sufficiently small Euclidean neighborhood in $X$ meeting no other $C_m$.
Thus continuity at such $x$ reduces to continuity of $g|_{C_n}$.
:::

<1>3. The composite
\[
g f:W\to W
\]
is homotopic to the identity on $W$.
::: {.proof}
On each circle $S^1_n$, the restriction $gf|_{S^1_n}$ is a based map of degree one.
Every based degree-one self-map of $S^1$ is based-homotopic to the identity.
Choose such a homotopy on each $S^1_n$, fixing the wedge point throughout.
Because $W$ has the CW weak topology, these circlewise homotopies assemble to a continuous homotopy on $W$.
:::

<1>4. The composite
\[
fg:X\to X
\]
is homotopic to the identity on $X$.
::: {.proof}
On each $C_n$, the map $fg$ is obtained by collapsing the short arc near $o$ and reparametrizing the remaining arc once around $C_n$.
Homotope this reparametrization linearly in arc-length coordinates back to the identity, fixing $o$.

Choose the parametrizations so that throughout the homotopy a point whose Euclidean distance from $o$ is at most $r<\varepsilon$ stays within distance at most $2r$ of $o$.
This is possible by performing the reparametrization only along the two short end-arcs and using Euclidean arc length there.
The resulting circlewise homotopies agree at $o$, and the displayed uniform estimate gives continuity at $o$ for the assembled homotopy.
Away from $o$, only one circle is locally present, so continuity is again circlewise.
Hence $fg\simeq\operatorname{id}_X$.
:::

<1>5. Therefore
\[
X\simeq W.
\]
::: {.proof}
The maps $f$ and $g$ are homotopy inverses by <1>3--<1>4.
:::

<1>6. Consequently
\[
\boxed{
\pi_1(X,o)
\cong
*_{n=1}^{\infty}\pi_1(C_n,o)
\cong
*_{n=1}^{\infty}\mathbb Z.
}
\]
::: {.proof}
Homotopy equivalence gives
\[
\pi_1(X,o)\cong\pi_1(W,*).
\]
The wedge-point neighborhoods in each circle deformation retract to the wedge point, so the wedge-sum form of van Kampen gives
\[
\pi_1(W,*)\cong *_{n\ge1}\pi_1(S^1_n,*).
\]
Each factor is infinite cyclic.
:::

<1>7. The space $X$ is first countable at $o$.
::: {.proof}
It is a subspace of the metric space $\mathbb R^2$.
Thus the sets
\[
X\cap B_{1/m}(o),\qquad m=1,2,\dots,
\]
form a countable neighborhood base at $o$.
:::

<1>8. The infinite CW wedge $W$ is not first countable at its wedge point.
::: {.proof}
Suppose $U_1,U_2,\dots$ were a countable neighborhood base at the wedge point $*$.
For each $n$, because $U_n\cap S^1_n$ is a neighborhood of $*$ in the $n$th circle, choose a point
\[
p_n\in U_n\cap(S^1_n\setminus\{*\}).
\]
On each circle choose an open arc $V_n$ about $*$ that omits $p_n$.
The union
\[
V=\bigcup_{n\ge1}V_n
\]
is a neighborhood of $*$ in the CW wedge topology, since its intersection with every circle is open.
But for every $n$,
\[
p_n\in U_n\setminus V,
\]
so $U_n\nsubseteq V$.
This contradicts the assumption that the $U_n$ form a neighborhood base.
:::

<1>9. Hence $X$ and $W$ are not homeomorphic.
::: {.proof}
First countability is invariant under homeomorphism.
By <1>7, $X$ is first countable at the common point, while by <1>8 the wedge point of $W$ is not.
:::
:::
