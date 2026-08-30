---
schema: qual/card@1
id: E-HAT-3.3-2
kind: exercise
title: "Deleting a point does not affect orientability"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Show that deleting a point from a manifold of dimension greater than 1 does not affect orientability of the manifold.

::: {.solution}
<1>1. Characterization of orientability via the orientation double cover:
<2>1. An $n$-manifold $M$ is orientable if and only if its 2-sheeted orientation covering space $p: \widetilde{M} \to M$ is trivial (i.e. $\widetilde{M}$ is disconnected into two homeomorphic copies of $M$).
Proof: Hatcher Section 3.3 (The Orientation Double Cover).
<2>2. For any point $x_0 \in M$, let $M' = M \setminus \{x_0\}$. The orientation double cover of $M'$ is the restriction:
\[
\widetilde{M'} = p^{-1}(M') = \widetilde{M} \setminus p^{-1}(x_0).
\]
Proof: naturality of covering space constructions under restriction to open subsets.
<2>3. Since $p: \widetilde{M} \to M$ is a 2-to-1 covering, $p^{-1}(x_0)$ consists of exactly two points $\{y_1, y_2\} \subset \widetilde{M}$.
Proof: covering degree 2.

<1>2. Connectedness and point removal in dimension $n \ge 2$:
<2>1. Removing a finite set of points from a connected $n$-dimensional manifold with $n \ge 2$ preserves connectedness:
Let $N$ be any connected $n$-manifold with $n \ge 2$. For any two points $y_1, y_2 \in N$, $N \setminus \{y_1, y_2\}$ is connected.
Proof: in a Euclidean chart $\mathbb{R}^n$ ($n \ge 2$), $\mathbb{R}^n \setminus \{0\}$ is connected, and any path between points in $N \setminus \{y_1, y_2\}$ can be perturbed around isolated points.
<2>2. **If $M$ is orientable:**
$\widetilde{M} = M_1 \amalg M_2$ is a disjoint union of two connected components homeomorphic to $M$.
Since $n \ge 2$, removing $y_1$ from $M_1$ and $y_2$ from $M_2$ leaves each component connected:
\[
\widetilde{M'} = (M_1 \setminus \{y_1\}) \amalg (M_2 \setminus \{y_2\}).
\]
Thus $\widetilde{M'}$ is disconnected, so $M'$ is orientable.
Proof: <2>1 applied to each component.
<2>3. **If $M$ is non-orientable:**
$\widetilde{M}$ is connected.
Since $n \ge 2$, by <2>1 removing the two points $\{y_1, y_2\}$ leaves $\widetilde{M'} = \widetilde{M} \setminus \{y_1, y_2\}$ connected.
Since its orientation cover is connected, $M'$ is non-orientable.
Proof: <2>1 applied to the connected cover $\widetilde{M}$.

<1>3. Conclusion:
$M \setminus \{x_0\}$ is orientable if and only if $M$ is orientable for all $n \ge 2$. Q.E.D.
Proof: <1>1 and <1>2.
:::
