---
schema: qual/card@1
id: E-HAT-4.A-4
kind: problem
title: "Automorphisms of wedge sums of spheres"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

With the notation of the preceding problem, show that $\operatorname{Aut}(\bigvee_n S^k) \approx \operatorname{GL}_n(\mathbb{Z})$ for $k > 1$, where $\bigvee_n S^k$ denotes the wedge sum of $n$ copies of $S^k$ and $\operatorname{GL}_n(\mathbb{Z})$ is the group of $n \times n$ matrices with entries in $\mathbb{Z}$ having an inverse matrix of the same form.

::: {.solution}
<1>1. Compute $\pi_k(X)$ for $X = \bigvee_{j=1}^n S^k$ ($k > 1$): <2>1. Since $k > 1$, the space $X$ is $(k-1)$-connected: $\pi_1(X) = \cdots = \pi_{k-1}(X) = 0$.
::: {.proof}
Seifert–van Kampen theorem and cellular approximation for $k$-dimensional CW complexes.
:::
<2>2. By the Hurewicz Theorem:
\[
\pi_k(X) \cong H_k(X; \mathbb{Z}) \cong \bigoplus_{j=1}^n H_k(S^k; \mathbb{Z}) \cong \mathbb{Z}^n.
\]
::: {.proof}
Hurewicz isomorphism theorem for $(k-1)$-connected spaces and homology of wedge sums.
:::
<2>3. Let $\iota_j: S^k \hookrightarrow X$ denote the inclusion of the $j$-th sphere summand; their homotopy classes $\{[\iota_1], \dots, [\iota_n]\}$ form a standard $\mathbb{Z}$-basis for $\pi_k(X)$.
::: {.proof}
generators of the homology of the wedge sum.
:::

<1>2. Characterize the monoid of based homotopy classes $[X, X]_*$: <2>1. By the universal property of the wedge sum, a based map $f: X \to X$ is determined up to based homotopy by its restrictions $f \circ \iota_j: S^k \to X$ for $j = 1, \dots, n$.
::: {.proof}
$[A \vee B, X]_* \cong [A, X]_* \times [B, X]_*$.
:::
<2>2. Each restriction $[f \circ \iota_j] \in \pi_k(X) \cong \mathbb{Z}^n$.
::: {.proof}
definition of the $k$-th homotopy group.
:::
<2>3. Thus $[X, X]_* \cong \prod_{j=1}^n \pi_k(X) \cong M_n(\mathbb{Z})$, where $f$ corresponds to the matrix $M(f) \in M_n(\mathbb{Z})$ whose $j$-th column is the coordinate vector of $f_*([\iota_j])$ in the basis $\{[\iota_1], \dots, [\iota_n]\}$.
::: {.proof}
column-by-column representation of linear maps on $\mathbb{Z}^n$.
:::
<2>4. The assignment $f \mapsto M(f)$ preserves composition: $M(g \circ f) = M(g) M(f)$.
::: {.proof}
functoriality of induced maps on homotopy groups $(g \circ f)_* = g_* \circ f_*$.
:::

<1>3. Characterize homotopy equivalences via Whitehead’s Theorem: <2>1. $X$ is a finite CW complex of dimension $k$ with cells only in dimensions $0$ and $k$.
::: {.proof}
cellular structure of a wedge of spheres.
:::
<2>2. By Whitehead’s Theorem, a based map $f: X \to X$ between simply connected CW complexes of dimension $k$ is a homotopy equivalence if and only if $f_*: \pi_k(X) \to \pi_k(X)$ is an isomorphism of abelian groups.
::: {.proof}
Whitehead's Theorem for CW complexes.
:::
<2>3. The group homomorphism $f_*: \mathbb{Z}^n \to \mathbb{Z}^n$ is an isomorphism if and only if its representation matrix $M(f)$ is invertible over $\mathbb{Z}$, which means $M(f) \in \operatorname{GL}_n(\mathbb{Z})$ (i.e. $\det M(f) = \pm 1$).
::: {.proof}
invertible $\mathbb{Z}$-linear endomorphisms of $\mathbb{Z}^n$ form the group $\operatorname{GL}_n(\mathbb{Z})$.
:::

<1>4. Conclusion: The map $[f] \mapsto M(f)$ induces an isomorphism of groups:
\[
\operatorname{Aut}\left(\bigvee_{j=1}^n S^k\right) \cong \operatorname{GL}_n(\mathbb{Z}).
\]
::: {.proof}
<1>2 and <1>3.
:::
Q.E.D.
:::
