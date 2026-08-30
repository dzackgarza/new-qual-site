---
schema: qual/card@1
id: P-TOPSU15F
kind: problem
title: "A 3-manifold with torsion in H_1 cannot embed in S^3"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Embeddings
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $M$ be a compact $3$-manifold-with-boundary such that $H_1(M; \mathbb{Z})$ contains a torsion element (i.e. element of finite order).
Prove that $M$ cannot be embedded as a submanifold of $S^3$.
(Hint: if it could, we could decompose $S^3 = M \cup_\Sigma N$ as a union of two compact $3$-manifolds, glued along their common boundary surface $\Sigma$.)
:::

::: {.solution}
<1>1. Decomposition of $S^3$:
<2>1. Suppose for contradiction that $M$ embeds as a compact 3-submanifold of $S^3$.
Let $N = \overline{S^3 \setminus M}$ be the closure of the complement.
Then $N$ is a compact 3-manifold with boundary $\partial N = \partial M = \Sigma$, and:
\[
S^3 = M \cup_\Sigma N, \qquad M \cap N = \Sigma.
\]
Proof: decomposition of $S^3$ along the common boundary surface $\Sigma$.

<1>2. Application of Alexander Duality:
<2>1. By Alexander Duality for the compact subset $M \subset S^3$:
\[
\widetilde{H}_1(M; \mathbb{Z}) \cong \widetilde{H}^{3 - 1 - 1}(S^3 \setminus M; \mathbb{Z}) = \widetilde{H}^1(S^3 \setminus M; \mathbb{Z}).
\]
Proof: Alexander Duality Theorem $\widetilde{H}_i(X) \cong \widetilde{H}^{n - i - 1}(S^n \setminus X)$.
<2>2. Since $N$ deformation retracts onto $S^3 \setminus M$ (by collar neighborhoods of the boundary $\Sigma$):
\[
H^1(S^3 \setminus M; \mathbb{Z}) \cong H^1(N; \mathbb{Z}).
\]
Thus $H_1(M; \mathbb{Z}) \cong H^1(N; \mathbb{Z})$ (for the reduced/unreduced positive degree groups).
Proof: collar neighborhood theorem for manifold boundaries.

<1>3. Torsion-free property of first cohomology via UCT:
<2>1. By the Universal Coefficient Theorem for Cohomology:
\[
H^1(N; \mathbb{Z}) \cong \operatorname{Hom}(H_1(N; \mathbb{Z}), \mathbb{Z}) \oplus \operatorname{Ext}(H_0(N; \mathbb{Z}), \mathbb{Z}).
\]
Proof: Universal Coefficient Theorem for Cohomology.
<2>2. Because $H_0(N; \mathbb{Z})$ is a free abelian group, $\operatorname{Ext}(H_0(N; \mathbb{Z}), \mathbb{Z}) = 0$.
Proof: Ext vanishes when the first argument is free.
<2>3. For any abelian group $G$, the group $\operatorname{Hom}(G, \mathbb{Z})$ is a subgroup of a direct product of copies of $\mathbb{Z}$, hence contains no non-zero elements of finite order (it is torsion-free).
Thus $H^1(N; \mathbb{Z}) \cong \operatorname{Hom}(H_1(N; \mathbb{Z}), \mathbb{Z})$ is torsion-free.
Proof: $\mathbb{Z}$ is torsion-free.

<1>4. Contradiction and conclusion:
<2>1. By <1>2 and <1>3, $H_1(M; \mathbb{Z}) \cong H^1(N; \mathbb{Z})$ must be torsion-free.
This contradicts the hypothesis that $H_1(M; \mathbb{Z})$ contains a torsion element.
Proof: contradiction.
<2>2. Therefore $M$ cannot be embedded as a submanifold of $S^3$.
Proof: proof by contradiction.

<1>5. Conclusion:
$M$ cannot embed in $S^3$. Q.E.D.
Proof: <1>1 through <1>4.
:::
