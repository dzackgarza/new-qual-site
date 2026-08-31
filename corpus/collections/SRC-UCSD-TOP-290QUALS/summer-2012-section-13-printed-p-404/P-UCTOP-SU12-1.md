---
schema: qual/card@1
id: P-UCTOP-SU12-1
kind: problem
title: Subgroup of finite index in free group is free
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Let $F_n$ be the free group of rank $n$, and let $H$ be a subgroup of $F_n$ with index $d$.
Show that $H$ is free, and find its rank.

::: {.solution}
<1>1. Topological realization of $F_n$ and the covering space for $H$:
<2>1. Realize the free group $F_n$ as the fundamental group of a bouquet of $n$ circles:
\[
X = \bigvee_{i=1}^n S^1.
\]
$X$ is a connected 1-dimensional CW complex (graph) with $V = 1$ vertex and $E = n$ edges.
Its Euler characteristic is $\chi(X) = V - E = 1 - n$, and $\pi_1(X, x_0) \cong F_n$.
<2>2. By the classification of covering spaces, the subgroup $H \le \pi_1(X, x_0)$ of index $d = [F_n : H]$ corresponds to a connected $d$-sheeted covering space $p: \widetilde{X} \to X$ with $p_*(\pi_1(\widetilde{X}, \tilde{x}_0)) = H \cong \pi_1(\widetilde{X})$.

<1>2. Proof that $H$ is free:
<2>1. The total space $\widetilde{X}$ is a connected graph with $V' = d \cdot 1 = d$ vertices and $E' = d \cdot n$ edges.
<2>2. Every connected graph contains a maximal spanning tree $T \subset \widetilde{X}$, which is contractible.
Collapsing $T$ to a point yields a homotopy equivalence $\widetilde{X} \simeq \widetilde{X}/T \cong \bigvee_{j=1}^k S^1$, where $k$ is the number of edges outside $T$.
Therefore the fundamental group $H \cong \pi_1(\widetilde{X}) \cong \pi_1(\bigvee_{j=1}^k S^1)$ is a free group of rank $k$ (Nielsen–Schreier Theorem).

<1>3. Computation of the rank of $H$:
<2>1. The Euler characteristic of the $d$-sheeted cover satisfies:
\[
\chi(\widetilde{X}) = d \cdot \chi(X) = d(1 - n).
\]
<2>2. On the other hand, since $\widetilde{X} \simeq \bigvee_{j=1}^k S^1$:
\[
\chi(\widetilde{X}) = \chi\left(\bigvee_{j=1}^k S^1\right) = 1 - k.
\]
<2>3. Equating the two expressions for $\chi(\widetilde{X})$:
\[
1 - k = d(1 - n) \implies k = d(n - 1) + 1.
\]
Thus the rank of $H$ is $d(n - 1) + 1$.

<1>4. Conclusion:
$H$ is a free group of rank $d(n - 1) + 1$. Q.E.D.
:::
