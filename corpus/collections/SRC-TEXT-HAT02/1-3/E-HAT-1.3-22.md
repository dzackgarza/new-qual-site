---
schema: qual/card@1
id: E-HAT-1.3-22
kind: problem
title: "Product of covering space actions"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 22; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used products of evenly covered neighborhoods and the universal property of orbit quotients.
---

Given covering space actions of groups $G_1$ on $X_1$ and $G_2$ on $X_2$, show that the action of $G_1 \times G_2$ on $X_1 \times X_2$ defined by $(g_1, g_2)(x_1, x_2) = (g_1(x_1), g_2(x_2))$ is a covering space action, and that $(X_1 \times X_2)/(G_1 \times G_2)$ is homeomorphic to $X_1/G_1 \times X_2/G_2$.


::: {.solution}
<1>1. The product action of $G_1\times G_2$ on $X_1\times X_2$ is free.
::: {.proof}
Suppose
\[
(g_1,g_2)(x_1,x_2)=(x_1,x_2).
\]
Then
\[
g_1x_1=x_1,\qquad g_2x_2=x_2.
\]
Since each $G_i$ acts as a covering space action, in particular freely, we obtain
\[
g_1=e_1,\qquad g_2=e_2.
\]
:::

<1>2. The product action is a covering space action.
::: {.proof}
Fix $(x_1,x_2)\in X_1\times X_2$.
Since the action of $G_i$ is a covering space action, choose an open neighborhood $U_i$ of $x_i$ such that
\[
g_iU_i\cap U_i=\varnothing
\qquad(g_i\ne e_i).
\]
Set
\[
U=U_1\times U_2.
\]
If
\[
(g_1,g_2)U\cap U\ne\varnothing,
\]
then necessarily
\[
g_1U_1\cap U_1\ne\varnothing,
\qquad
g_2U_2\cap U_2\ne\varnothing.
\]
Hence $g_1=e_1$ and $g_2=e_2$.
Thus distinct translates of $U$ are disjoint, which is exactly the local condition for a covering space action.
:::

<1>3. Let
\[
q:X_1\times X_2\to (X_1\times X_2)/(G_1\times G_2)
\]
and
\[
q_i:X_i\to X_i/G_i
\]
be the quotient maps.
The map
\[
q_1\times q_2:X_1\times X_2\to (X_1/G_1)\times(X_2/G_2)
\]
is constant on $(G_1\times G_2)$-orbits.
::: {.proof}
For every $(g_1,g_2)$,
\[
(q_1\times q_2)(g_1x_1,g_2x_2)
=(q_1x_1,q_2x_2),
\]
since each $q_i$ is constant on $G_i$-orbits.
:::

<1>4. Hence there is a unique continuous map
\[
\Phi:(X_1\times X_2)/(G_1\times G_2)
\to
(X_1/G_1)\times(X_2/G_2)
\]
with
\[
\Phi([(x_1,x_2)])=([x_1],[x_2]).
\]
It is bijective.
::: {.proof}
Existence and continuity follow from the quotient property of $q$ and <1>3.
Surjectivity is immediate.
For injectivity, suppose
\[
([x_1],[x_2])=([y_1],[y_2]).
\]
Then there exist $g_i\in G_i$ with
\[
y_i=g_ix_i.
\]
Therefore
\[
(y_1,y_2)=(g_1,g_2)(x_1,x_2),
\]
so the two points lie in the same $(G_1\times G_2)$-orbit.
:::

<1>5. The map $\Phi$ is a homeomorphism.
::: {.proof}
Each quotient map $q_i$ is open, since for an open set $V_i\subseteq X_i$,
\[
q_i^{-1}(q_i(V_i))=\bigcup_{g_i\in G_i}g_iV_i
\]
is open.
Hence $q_1\times q_2$ is open on the basis of product-open sets and therefore open.
Since
\[
q_1\times q_2=\Phi\circ q
\]
and $q$ is a quotient map, this implies that $\Phi$ is open.
A continuous bijective open map is a homeomorphism.
Thus
\[
\boxed{(X_1\times X_2)/(G_1\times G_2)\cong X_1/G_1\times X_2/G_2.}
\]
:::
:::
