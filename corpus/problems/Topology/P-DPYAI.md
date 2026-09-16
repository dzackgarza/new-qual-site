---
schema: qual/card@1
id: P-DPYAI
kind: problem
title: $S^n$ minus $k$ points is a wedge of $k-1$ spheres
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
relations: []
review: draft
---

::: {.problem}
6. Lemma: $S^n - \theset{p_i}_{i=1}^k = \bigvee_{k-1}S^{n-1}$, i.e. $S^n$ minus $k$ points is equal to $k-1$ copies of of $S^{n-1}$.
   Proof: $S^n - \theset{p_1} \cong \RR^n$ by stereographic projection, so $S^n - \theset{p_1, p_2 \cdots p_k} \cong \RR^n - \theset{p_2, \cdots p_k}$.
   WLOG, suppose none of these points are zero (otherwise, take a translation away from zero.
   This is affine and continuous.)
   Then fix 0 as the base point, and form $k-1$ loops $\alpha_i$, where the $i$th loop encircles $p_i$.
   Then $\RR^n$ deformation retracts onto $\cup_{i=1}^{k-1} \alpha_i$, which is homeomorphic to $\bigvee_{i=1}^{k-1} S^1$.
:::

::: {.solution}
<1>1. For $k\ge1$, stereographic projection identifies $S^n$ minus one chosen point with $\mathbb R^n$, so removing $k$ points from $S^n$ reduces to removing $k-1$ points from $\mathbb R^n$.
::: {.proof}
Choose one of the removed points as the projection point.
:::

<1>2. If $n\ge2$, $\mathbb R^n$ minus $r$ points deformation retracts onto a wedge of $r$ copies of $S^{n-1}$.
::: {.proof}
Choose disjoint small balls around the removed points and connect their boundary spheres to a common basepoint by disjoint arcs forming a tree. The complement deformation retracts onto the union of these boundary spheres and arcs; collapsing the tree gives the wedge of the $r$ spheres.
:::

<1>3. Hence for $n\ge2$,
$$\boxed{S^n\setminus\{p_1,\dots,p_k\}\simeq\bigvee^{k-1}S^{n-1}.}$$
::: {.proof}
Apply <1>1--<1>2 with $r=k-1$.
:::
:::
