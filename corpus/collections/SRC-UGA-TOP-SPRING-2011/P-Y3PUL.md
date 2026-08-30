---
schema: qual/card@1
id: P-Y3PUL
kind: problem
title: $\RP^2\vee S^1$ is not homotopy equivalent to a compact surface
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Surfaces
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Show that $\RP^2 \lor S^1$ is *not* homotopy equivalent to a compact surface (possibly with boundary).
:::

::: {.solution}
<1>1. Algebraic topological invariants of $X = \mathbb{RP}^2 \vee S^1$:
<2>1. By the Seifert–van Kampen Theorem:
\[
\pi_1(X) \cong \pi_1(\mathbb{RP}^2) * \pi_1(S^1) \cong \mathbb{Z}_2 * \mathbb{Z}.
\]
Proof: Seifert–van Kampen Theorem for wedge sums.
<2>2. The group $\pi_1(X) \cong \mathbb{Z}_2 * \mathbb{Z}$ contains non-trivial torsion elements (e.g. the generator of order 2).
Proof: Kurosh subgroup theorem / torsion in free products.
<2>3. Abelianizing $\pi_1(X)$ gives the first homology group:
\[
H_1(X; \mathbb{Z}) \cong \mathbb{Z}_2 \oplus \mathbb{Z}.
\]
Proof: abelianization of free product is direct sum of abelianizations.

<1>2. Surfaces with non-empty boundary:
<2>1. If $S$ is a compact connected 2-manifold with non-empty boundary ($\partial S \neq \emptyset$), then $S$ deformation retracts onto a 1-dimensional graph (a wedge of circles).
Proof: standard classification of surfaces with boundary.
<2>2. Thus $\pi_1(S)$ is a free group $F_r$, which is completely torsion-free.
Since $\pi_1(X)$ has 2-torsion, $S$ cannot have non-empty boundary.
Proof: free groups contain no non-trivial elements of finite order.

<1>3. Closed surfaces without boundary:
<2>1. If $S$ is a closed connected orientable surface of genus $g \ge 1$, $\pi_1(S)$ is a surface group, which is torsion-free (acting cocompactly on $\mathbb{R}^2$ or $\mathbb{H}^2$).
Proof: universal cover is $\mathbb{R}^2$ or $\mathbb{H}^2$, which is contractible, so $\pi_1(S)$ is torsion-free.
<2>2. If $S$ is a closed connected non-orientable surface of genus $k \ge 2$, its orientable double cover is a closed surface of genus $k-1 \ge 1$, so its universal cover is contractible ($\mathbb{R}^2$ or $\mathbb{H}^2$), and $\pi_1(S)$ is torsion-free.
Proof: deck group acting freely on contractible universal cover.
<2>3. The only closed surfaces with non-trivial fundamental group torsion are:
- $S^2$ (with $\pi_1(S^2) = 0$ and $H_1(S^2) = 0$),
- $\mathbb{RP}^2$ (with $\pi_1(\mathbb{RP}^2) \cong \mathbb{Z}_2$ and $H_1(\mathbb{RP}^2) \cong \mathbb{Z}_2$).
Neither matches $H_1(X) \cong \mathbb{Z}_2 \oplus \mathbb{Z}$.
Proof: comparison of homology groups.

<1>4. Conclusion:
No compact surface (with or without boundary) is homotopy equivalent to $\mathbb{RP}^2 \vee S^1$. Q.E.D.
Proof: <1>2 and <1>3.
:::
