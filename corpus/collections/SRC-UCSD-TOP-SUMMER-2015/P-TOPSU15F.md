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
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the reversed Alexander-duality isomorphism with the degree-two duality and UCT torsion obstruction.
---

::: {.problem}
Let $M$ be a compact $3$-manifold-with-boundary such that $H_1(M; \mathbb{Z})$ contains a torsion element (i.e. element of finite order).
Prove that $M$ cannot be embedded as a submanifold of $S^3$.
(Hint: if it could, we could decompose $S^3 = M \cup_\Sigma N$ as a union of two compact $3$-manifolds, glued along their common boundary surface $\Sigma$.)
:::

::: {.solution}

::: pf

::: {.pf-step #assume-embedding}
Suppose for contradiction that $M$ embeds as a compact submanifold of $S^3$.

::: pf-proof
Identify $M$ with its image in $S^3$.
Because a compact manifold has the homotopy type of a finite CW complex, its homology groups are finitely generated.
:::

:::

::: {.pf-step #h2-free-abelian}
Alexander duality implies that $H^2(M;\ZZ)$ is free abelian.

::: pf-proof
The embedded manifold $M$ is compact and locally contractible, so Alexander duality gives
\[
\widetilde H^2(M;\ZZ)
\cong
\widetilde H_0(S^3\setminus M;\ZZ).
\]
The group $\widetilde H_0$ of any space is free abelian, since it is free on the path components modulo one diagonal copy of $\ZZ$.
Hence $\widetilde H^2(M;\ZZ)$ is free abelian.
In degree $2>0$, reduced and unreduced cohomology agree, so $H^2(M;\ZZ)$ is free abelian.
:::

:::

::: {.pf-step #h1-torsion-implies-h2-torsion}
If $H_1(M;\ZZ)$ has nonzero torsion, then $H^2(M;\ZZ)$ has nonzero torsion.

::: pf-proof
The universal coefficient theorem for cohomology gives a natural short exact sequence
\[
0
\longrightarrow
\operatorname{Ext}(H_1(M;\ZZ),\ZZ)
\longrightarrow
H^2(M;\ZZ)
\longrightarrow
\operatorname{Hom}(H_2(M;\ZZ),\ZZ)
\longrightarrow
0.
\]
By step [](#assume-embedding){.pf-ref}, the finitely generated abelian group $H_1(M;\ZZ)$ decomposes as
\[
H_1(M;\ZZ)\cong \ZZ^r\oplus T
\]
with $T$ finite.
If $T\ne0$, then
\[
\operatorname{Ext}(H_1(M;\ZZ),\ZZ)
\cong
\operatorname{Ext}(T,\ZZ)
\cong T
\]
is nonzero torsion.
The left arrow in the UCT sequence is injective, so this torsion subgroup embeds in $H^2(M;\ZZ)$.
:::

:::

::: pf-step
Therefore $M$ cannot embed in $S^3$.

::: pf-proof
The hypothesis says that $H_1(M;\ZZ)$ has nonzero torsion.
By step [](#h1-torsion-implies-h2-torsion){.pf-ref}, $H^2(M;\ZZ)$ then has nonzero torsion, while step [](#h2-free-abelian){.pf-ref} says that $H^2(M;\ZZ)$ is free abelian.
This contradiction disproves the assumed embedding from step [](#assume-embedding){.pf-ref}.
:::

:::

:::

:::
