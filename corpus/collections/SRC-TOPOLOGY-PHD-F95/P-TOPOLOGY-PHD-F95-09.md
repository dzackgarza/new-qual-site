---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-09
kind: problem
title: Universal cover and fundamental group of a wedge with RP^2
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section II, problem 4 of the 23 September 1995 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Interpreted the source's isolated S^2 in part (c) as a typo for S^1,
    as required by the surrounding statement. Described the universal cover as
    the Bass--Serre tree of universal covers of the two wedge summands and
    checked both the covering map and simple connectivity.
---

::: {.problem}
(a) Define a covering space.

(b) State the main theorem about path lifting and covering spaces.

(c) Let $S^1\vee\mathbb{R}P^2$ be the one point union of the circle and two-dimensional real projective space, i.e. the quotient space obtained by taking the disjoint union of $S^2$ and $\mathbb{R}P^2$ and then identifying a single point $x\in S^2$ with a single point $y\in\mathbb{R}P^2$.
Describe the universal cover of $S^1\vee\mathbb{R}P^2$.

(d) Describe the fundamental group of $S^1\vee\mathbb{R}P^2$.
:::

::: remark
In part (c), the source says that the displayed one-point union $S^1\vee\mathbb{R}P^2$ is obtained from the disjoint union of $S^2$ and $\mathbb{R}P^2$.
The same sentence calls the first summand a circle, and both the beginning and end of the part display $S^1\vee\mathbb{R}P^2$.
Thus the occurrence of $S^2$ is a source typo; the solution uses the intended space $S^1\vee\mathbb{R}P^2$.
:::

::: {.solution}
Fix the wedge point $x_0\in X=S^1\vee\mathbb{R}P^2$.

<1>1. A covering space of a space $X$ is a space $\widetilde X$ together with a continuous surjection
\[
p:\widetilde X\longrightarrow X
\]
such that every $x\in X$ has an open neighborhood $U$ for which
\[
p^{-1}(U)=\coprod_{\alpha}V_\alpha
\]
is a disjoint union of open sets and every restriction
\[
p|_{V_\alpha}:V_\alpha\longrightarrow U
\]
is a homeomorphism.
::: {.proof}
This is the definition of an evenly covered neighborhood and of a covering projection.
:::

<1>2. The path-lifting theorem gives existence and uniqueness of a lift once its initial point is prescribed.
::: {.proof}
Let $p:\widetilde X\to X$ be a covering projection, let
\[
\gamma:[0,1]\longrightarrow X
\]
be a path, and choose $\widetilde x_0\in p^{-1}(\gamma(0))$.
Then there exists a unique path
\[
\widetilde\gamma:[0,1]\longrightarrow\widetilde X
\]
such that
\[
p\circ\widetilde\gamma=\gamma,
\qquad
\widetilde\gamma(0)=\widetilde x_0.
\]
:::

<1>3. The fundamental group of $X$ is
\[
G:=\pi_1(X,x_0)\cong \ZZ*(\ZZ/2)
\cong\langle a,b\mid b^2=1\rangle.
\]
::: {.proof}
Choose small open neighborhoods of the two wedge summands whose intersection deformation retracts to the wedge point.
The Seifert--van Kampen theorem gives
\[
\pi_1(S^1\vee\mathbb{R}P^2,x_0)
\cong
\pi_1(S^1,x_0)*\pi_1(\mathbb{R}P^2,x_0).
\]
Since
\[
\pi_1(S^1)\cong\ZZ,
\qquad
\pi_1(\mathbb{R}P^2)\cong\ZZ/2,
\]
the displayed presentation follows.
:::

<1>4. Construct a space $\widetilde X$ from copies of the universal covers of the two wedge summands.
::: {.proof}
Let
\[
A=\langle a\rangle\cong\ZZ,
\qquad
B=\langle b\rangle\cong\ZZ/2.
\]
Form the bipartite graph $T$ whose vertices are the left cosets
\[
G/A\quad\text{and}\quad G/B,
\]
and whose edges are indexed by $g\in G$, with the edge labelled $g$ joining
\[
gA\quad\text{to}\quad gB.
\]

For every $A$-vertex $gA$, take a copy
\[
L_{gA}\cong\mathbb{R}
\]
of the universal cover $\mathbb{R}\to S^1$.
Label its points over $x_0$ by the elements of the coset $gA$ so that consecutive points are labelled
\[
ga^n,\ ga^{n+1}.
\]
For every $B$-vertex $gB$, take a copy
\[
S_{gB}\cong S^2
\]
of the universal cover $S^2\to\mathbb{R}P^2$.
Its two points over $x_0$ are labelled by the two elements
\[
g,\ gb
\]
of the coset $gB$.

For each $h\in G$, identify the point labelled $h$ in the line $L_{hA}$ with the point labelled $h$ in the sphere $S_{hB}$.
The resulting connected space is $\widetilde X$.
:::

<1>5. The piecewise map
\[
p:\widetilde X\longrightarrow S^1\vee\mathbb{R}P^2
\]
obtained from $\mathbb{R}\to S^1$ on every line and $S^2\to\mathbb{R}P^2$ on every sphere is a covering projection.
::: {.proof}
Away from the wedge point this is immediate from the two standard universal covering maps.

Choose connected evenly covered neighborhoods $U_1\subset S^1$ and $U_2\subset\mathbb{R}P^2$ of the wedge point, each small enough to be simply connected, and put
\[
U=U_1\vee U_2.
\]
For every $h\in G$, the lift of $U_1$ through the point labelled $h$ in $L_{hA}$ and the lift of $U_2$ through the point labelled $h$ in $S_{hB}$ meet only at that labelled point.
Their union is an open neighborhood $\widetilde U_h$ mapped homeomorphically onto $U$.
Moreover,
\[
p^{-1}(U)=\coprod_{h\in G}\widetilde U_h.
\]
Hence the wedge point is evenly covered as well.
:::

<1>6. The incidence graph $T$ is a tree.
::: {.proof}
It is connected because every element of the free product $G=A*B$ has a reduced alternating word in nonidentity elements of $A$ and $B$, and the successive prefixes give an edge path from the identity cosets to the cosets incident to that element.

If $T$ contained a reduced cycle, reading its successive changes of coset would give a nonempty reduced alternating word
\[
a^{n_1}b\,a^{n_2}b\cdots a^{n_r}b
\]
with each $n_i\neq0$ that represents the identity in $A*B$.
The normal-form theorem for free products says that no nonempty reduced word represents the identity.
Thus $T$ has no cycle.
:::

<1>7. The covering space $\widetilde X$ is simply connected.
::: {.proof}
Each vertex space in the tree-of-spaces description is simply connected:
\[
L_{gA}\cong\mathbb{R},
\qquad
S_{gB}\cong S^2.
\]
Adjacent vertex spaces meet in exactly one point, and the pattern of intersections is the tree $T$ from <1>6.
Applying the Seifert--van Kampen theorem along finite subtrees gives trivial fundamental group for every finite connected union of vertex spaces.
Every loop in this CW complex has compact image and therefore lies in such a finite connected union.
Hence
\[
\pi_1(\widetilde X)=1.
\]
Thus $p$ is the universal covering projection.
:::

<1>8. Therefore the universal cover is a tree of copies of $\mathbb{R}$ and $S^2$, and
\[
\boxed{\pi_1(S^1\vee\mathbb{R}P^2)\cong\ZZ*(\ZZ/2)}.
\]
::: {.proof}
The copies of $\mathbb{R}$ are the lifts of the $S^1$ summand; the copies of $S^2$ are the lifts of the $\mathbb{R}P^2$ summand; and their attachment pattern is the tree $T$.
The group computation is <1>3.
:::
:::
