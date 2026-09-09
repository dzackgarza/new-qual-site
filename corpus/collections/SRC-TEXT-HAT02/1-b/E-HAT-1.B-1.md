---
schema: qual/card@1
id: E-HAT-1.B-1
kind: problem
title: "Free simplicial actions are covering space actions"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.B, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the barycentric-coordinate metric to show every orbit is uniformly separated at each point, then chose a small translate-disjoint neighborhood.
---

Suppose a group $G$ acts simplicially on a complex $X$, where "simplicially" means that each element of $G$ takes each simplex of $X$ onto another simplex by a linear homeomorphism.
If the action is free, show it is a covering space action.


::: {.solution}
Realize $X$ in barycentric coordinates. Thus every point has the form
\[
x=\sum_{v\in S}\lambda_v v,
\qquad
\lambda_v>0,
\qquad
\sum_{v\in S}\lambda_v=1,
\]
with finite support $S$, and use the standard $\ell^1$ metric
\[
d(x,y)=\sum_v|x_v-y_v|.
\]
A simplicial automorphism permutes vertices, hence preserves this metric.

<1>1. For every $x\in X$ there is a number $\delta_x>0$ such that
\[
d(x,gx)\ge\delta_x
\qquad
\text{for all }g\ne1.
\]
::: {.proof}
Let $S$ be the finite support of $x$ and put
\[
m=\min_{v\in S}\lambda_v>0.
\]
If $gS\ne S$, choose $v\in S$ such that either $gv\notin S$ or, equivalently after replacing $g$ by $g^{-1}$ if needed, some positive coordinate of $x$ is moved outside $S$.
Then
\[
d(x,gx)\ge m.
\]

It remains to consider elements with $gS=S$.
Their restrictions to $S$ are permutations of the finite set $S$, so only finitely many points $gx$ can arise.
The action is free, hence none of these points equals $x$ when $g\ne1$.
The finite set of positive distances
\[
\{d(x,gx):gS=S,\ g\ne1\}
\]
therefore has a positive minimum when nonempty.
Taking the minimum of this number and $m$ gives the required $\delta_x$.
:::

<1>2. If
\[
U=B(x,\delta_x/3),
\]
then
\[
gU\cap U=\varnothing
\qquad
(g\ne1).
\]
::: {.proof}
Suppose $y\in U\cap gU$.
Then $y=gz$ for some $z\in U$.
Since $g$ is an isometry,
\[
d(gx,y)=d(x,z)<\delta_x/3.
\]
Also $d(x,y)<\delta_x/3$, so
\[
d(x,gx)
\le d(x,y)+d(y,gx)
<2\delta_x/3,
\]
contradicting <1>1.
:::

<1>3. The quotient map
\[
q:X\to X/G
\]
is evenly covered over $q(U)$.
::: {.proof}
The saturation of $U$ is the disjoint union
\[
q^{-1}(q(U))=\coprod_{g\in G}gU
\]
by <1>2.
For each $g$, the restriction
\[
q:gU\to q(U)
\]
is bijective, since two points of one translate cannot lie in the same orbit unless some nontrivial translate of $U$ meets $U$.
The quotient map is open, so each restriction is a homeomorphism.
Hence $q(U)$ is evenly covered.
:::

<1>4. Therefore a free simplicial action is a covering space action.
::: {.proof}
Every point $x$ has a neighborhood $U$ satisfying <1>2, and <1>3 gives the covering-space condition for the orbit map.
:::
:::
