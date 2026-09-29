---
schema: qual/card@1
id: E-HAT-3.3-2
kind: problem
title: Deleting a point does not affect orientability
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that deleting a point from a manifold of dimension greater than 1 does not affect orientability of the manifold.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Characterization of orientability via the orientation double cover:

::: pf-proof

::: pf-step

An $n$-manifold $M$ is orientable if and only if its 2-sheeted orientation covering space $p: \widetilde{M} \to M$ is trivial (i.e. $\widetilde{M}$ is disconnected into two homeomorphic copies of $M$).

::: pf-proof

Hatcher Section 3.3 (The Orientation Double Cover).

:::

:::

::: pf-step

For any point $x_0 \in M$, let $M' = M \setminus \{x_0\}$. The orientation double cover of $M'$ is the restriction:
\[
\widetilde{M'} = p^{-1}(M') = \widetilde{M} \setminus p^{-1}(x_0).
\]

::: pf-proof

naturality of covering space constructions under restriction to open subsets.

:::

:::

::: pf-step

Since $p: \widetilde{M} \to M$ is a 2-to-1 covering, $p^{-1}(x_0)$ consists of exactly two points $\{y_1, y_2\} \subset \widetilde{M}$.

::: pf-proof

covering degree 2.

:::

:::

:::

:::

::: {.pf-step #s2}

Connectedness and point removal in dimension $n \ge 2$:

::: pf-proof

::: {.pf-step #s2-1}

Removing a finite set of points from a connected $n$-dimensional manifold with $n \ge 2$ preserves connectedness:
Let $N$ be any connected $n$-manifold with $n \ge 2$. For any two points $y_1, y_2 \in N$, $N \setminus \{y_1, y_2\}$ is connected.

::: pf-proof

in a Euclidean chart $\mathbb{R}^n$ ($n \ge 2$), $\mathbb{R}^n \setminus \{0\}$ is connected, and any path between points in $N \setminus \{y_1, y_2\}$ can be perturbed around isolated points.

:::

:::

::: pf-step

**If $M$ is orientable:**
$\widetilde{M} = M_1 \amalg M_2$ is a disjoint union of two connected components homeomorphic to $M$.
Since $n \ge 2$, removing $y_1$ from $M_1$ and $y_2$ from $M_2$ leaves each component connected:
\[
\widetilde{M'} = (M_1 \setminus \{y_1\}) \amalg (M_2 \setminus \{y_2\}).
\]
Thus $\widetilde{M'}$ is disconnected, so $M'$ is orientable.

::: pf-proof

Step [](#s2-1){.pf-ref} applied to each component.

:::

:::

::: pf-step

**If $M$ is non-orientable:**
$\widetilde{M}$ is connected.
Since $n \ge 2$, by step [](#s2-1){.pf-ref} removing the two points $\{y_1, y_2\}$ leaves $\widetilde{M'} = \widetilde{M} \setminus \{y_1, y_2\}$ connected.
Since its orientation cover is connected, $M'$ is non-orientable.

::: pf-proof

Step [](#s2-1){.pf-ref} applied to the connected cover $\widetilde{M}$.

:::

:::

:::

:::

::: pf-step

Conclusion:
$M \setminus \{x_0\}$ is orientable if and only if $M$ is orientable for all $n \ge 2$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
